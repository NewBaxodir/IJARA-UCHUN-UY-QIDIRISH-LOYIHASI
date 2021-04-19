from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from administrator.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import authenticate, login as dj_login
from administrator.forms import UserhouseholderSignUpForm, UserChangeForm, UserForm, UseradminpageForm, HouseholderForm
from django.views.generic import CreateView, ListView, View
from django.db import transaction, IntegrityError
from django.core import serializers
from search.models import Streets, Photo, Announcement, Rooms, Floor
from administrator.forms import UseradminpageSignUpForm, UserhouseholderSignUpForm, AnnouncementUpdate, PhotoUpdate
from datetime import datetime
import json
from .models import User, Useradminpage, Householder
from django.forms import modelformset_factory, inlineformset_factory
from .filters import AnnouncementFilter


from django.db import transaction, IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from dataclasses import dataclass, field
from django.forms import formset_factory
from django.urls import reverse_lazy, reverse

# Create your views here.







# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START ACCOUNT - HISOB ***********************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
from administrator.models import User
from django.contrib.auth.hashers import check_password

# account page - hisob bosh sahifa
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['householder'])
def account_home(request):
    photo = Photo.objects.all()
    street = Streets.objects.all()
    filter = AnnouncementFilter(request.GET, queryset=Announcement.objects.all())
    object_list = filter.qs
    paginator = Paginator(object_list, 20)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)
    context = {"object_list": object_list, "filter": filter, "photo": photo, "street": street}
    return render(request, 'account/account_home.html', context)




# setting page - sozlamalar 
def settings(request):
    return render(request, 'account/settings.html')


# sign_in page - hisobga kirishni tasdiqlash 
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('administrator')

        else:
            messages.info(request, 'Login yoki Parolingiz xato.')
            
    context = {}
    return render(request, 'account/sign_in.html',context)


# sign_up page - ro'yxatdan o'tish
class sign_up(CreateView):
    model = User
    form_class = UserhouseholderSignUpForm
    template_name = 'account/sign_up.html'

    
    def form_valid(self, form):
        user = form.save()
        # dj_login(self.request, user)
        return redirect('sign_in')




# account_update page - account malumotlarini o'zgartirish

def account_update(request, pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = HouseholderForm(request.POST,request.FILES, instance=request.user.householder)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Wrong username or password.')
            return redirect('settings')
        else:
            messages.info(request, 'Wrong username or password.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = HouseholderForm(instance=request.user.householder)
    return render(request, 'account/account_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def delete_account(request, pk):
    account = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        account.delete()
        # if form.is_valid():
        return redirect('sign_in')
    context = {"account": account}
    return render(request, 'account/delete_account.html', context)


def search(request):
    street = Streets.objects.all()
    photo = Photo.objects.all()
    filter = AnnouncementFilter(request.GET, queryset=Announcement.objects.all())
    object_list = filter.qs
    paginator = Paginator(object_list, 20)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)
    context = {"object_list": object_list, "filter": filter, "street": street, "photo": photo}
    return render(request, 'search/search.html', context)



def like_unlike_post(request):
    user = request.user
    post = get_object_or_404(Announcement, id=request.POST.get('announcement_id'))
    print(post)
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('account')



def add_post(request, pk):
    user = request.user
    post = Announcement.objects.get(id=pk)
    if post in user.addd.all():
        user.addd.remove(post)
    else:
        user.addd.add(post)
    return redirect('account')




def announcement_like(request):
    photo = Photo.objects.all()
    user = request.user.id
    us = User.objects.all()
    context = {"us": us, "photo": photo}
    return render(request, 'account/announcement_like.html', context)



# logout - logindan chiqish
def logout_view(request):
    logout(request)
    return redirect('sign_in')

# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# END ACCOUNT - HISOB *************************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕













# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START ANNOUNCEMENTS - E'LONLAR **************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕


# announcement page - e'lonlar
def announcement(request):
    photo = Photo.objects.all()
    my_announcement = Announcement.objects.filter(user__user=request.user)
    context = {'my_announcement' : my_announcement, "photo": photo}
    return render(request, 'announcements/announcement.html', context)





# announcement create page - e'lon yaratish 
def create(request):
    room = Rooms.objects.all()
    floors = Floor.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['address'] != '':
            announcements, created = Announcement.objects.get_or_create(user=request.user.householder, 
                region=data['region'], address=data['address'], phone_numer=data['phone_numer'], mode=data['mode'],
                kimlar=data['kimlar'], kishilar=data['kishilar'], topshirilgan=data['topshirilgan'],
                moneyc=data['moneyc'], floor=data['floor'], floormany=data['floormany'], rooms=data['rooms'],
                money=data['money'], tartiblar=data['tartiblar'], ish=data['ish'], 

                sovuq_suv=data['sovuq_suv'], issiq_suv=data['issiq_suv'], svet=data['svet'],
                gaz=data['gaz'], additional2=data['additional2'],

                wifi=data['wifi'], sovutgich=data['sovutgich'], kondisioner=data['kondisioner'],
                additional3=data['additional3'],

                hammom=data['hammom'], additional4=data['additional4'], xafsiz=data['xafsiz'],
                additional5=data['additional5'])
        
        else:
            announcements = None

        for image in images:
            photo = Photo.objects.create(
                announcements=announcements,  image=image,
            )

        return redirect('announcement')

    context = {'room': room, "floors": floors}
    return render(request, 'announcements/create.html', context)





# def announcement_update(request, pk, template_name='announcements/announcement_update.html'):
#     category = get_object_or_404(Category, pk=pk)
#     form = CategoryUpdate(request.POST or None, instance=category)
#     if form.is_valid():
#         form.save()
#         return redirect('announcement')
#     return render(request, template_name, {'form':form})


def announcement_updates(request, pk):
    announcements = get_object_or_404(Announcement, pk=pk)
    form = AnnouncementUpdate(request.POST or None, instance=announcements)
    if form.is_valid():
        form.save()
        return redirect('announcement')
    context = {"form": form}
    return render(request, 'announcements/announcement_update.html', context)





def announcement_delete(request, pk):
    obj = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        obj.delete()
        # if form.is_valid():
        return redirect('announcement')
    context = {"obj": obj}
    return render(request, 'announcements/announcement_delete.html', context)




def images_update(request, pk):
    user = Announcement.objects.get(pk=pk)
    PhotoFormset = inlineformset_factory(Announcement, Photo, form=PhotoUpdate, extra=3)
    if request.method == 'POST':
        formset = PhotoFormset(request.POST, request.FILES, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect('announcement')
    formset = PhotoFormset(instance=user)
    context = {"formset": formset}
    return render(request, 'announcements/images_update.html', context)


# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# END ANNOUNCEMENTS - E'LONLAR **************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

















# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# START ADMINISTRATOR - ADMIN *****************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

# administrator page - admin sahifai
@login_required(login_url='login')
@admin_only
def administrator(request):
    return render(request, 'administrator/administrator.html')



# ANNOUNCEMENTS ******************************************************************************
def admin_announcements(request):
    photo = Photo.objects.all()
    street = Streets.objects.all()
    filter = AnnouncementFilter(request.GET, queryset=Announcement.objects.all())
    object_list = filter.qs
    context = {"object_list": object_list, "filter": filter, "photo": photo, "street": street}
    return render(request, 'administrator/admin_announcements.html', context)



def admin_announcements_update(request, pk):
    room = Rooms.objects.all()
    floors = Floor.objects.all()
    announcements = get_object_or_404(Announcement, pk=pk)
    form = AnnouncementUpdate(request.POST or None, instance=announcements)
    if form.is_valid():
        form.save()
        return redirect('admin_announcements')
    context = {"form": form, "room": room, "floors": floors}
    return render(request, 'administrator/admin_announcements_update.html', context)



def admin_announcements_update_image(request, announcements_id):
    user = Announcement.objects.get(pk=announcements_id)
    PhotoFormset = inlineformset_factory(Announcement, Photo, form=PhotoUpdate, extra=3)
    if request.method == 'POST':
        formset = PhotoFormset(request.POST, request.FILES, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect('admin_announcements')
    formset = PhotoFormset(instance=user)
    context = {"formset": formset}
    return render(request, 'administrator/admin_announcements_update_image.html', context)




def admin_announcements_delete(request, pk):
    obj = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        obj.delete()
        # if form.is_valid():
        return redirect('admin_announcements')
    context = {"obj": obj}
    return render(request, 'administrator/admin_announcements_delete.html', context)


# ANNOUNCEMENTS ******************************************************************************





# ANNOUNCERS  /**************************
def admin_announcers(request):
    householder = Householder.objects.all()
    context = {"householder": householder}
    return render(request, 'administrator/admin_announcers.html', context)



def admin_announcers_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = HouseholderForm(request.POST,request.FILES, instance=user.householder)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Login yoki Parol xato')
            return redirect('admin_announcers')
        else:
            messages.info(request, 'Login yoki Parol xato')
    else:
        user_form = UserForm(instance=user)
        profile_form = HouseholderForm(instance=user.householder)
    return render(request, 'administrator/admin_announcers_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




def admin_announcers_delete(request, pk):
    announcers = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        announcers.delete()
        # if form.is_valid():
        return redirect('admin_announcers')
    context = {"announcers": announcers}
    return render(request, 'administrator/admin_announcers_delete.html', context)
# ANNOUNCERS  /**************************





# MODERATORS  /**************************
def moderators(request):
    useradminpage = Useradminpage.objects.all()
    context = {"useradminpage": useradminpage}
    return render(request, 'administrator/moderators.html', context)



# sign_up page - ro'yxatdan o'tish
class moderator_create(CreateView):
    model = User
    form_class = UseradminpageSignUpForm
    template_name = 'administrator/moderator_create.html'

    
    def form_valid(self, form):
        user = form.save()
        # dj_login(self.request, user)
        return redirect('moderators')




def moderator_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UseradminpageForm(request.POST,request.FILES, instance=user.useradminpage)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Wrong username or password.')
            return redirect('moderators')
        else:
            messages.info(request, 'Wrong username or password.')
    else:
        user_form = UserForm(instance=user)
        profile_form = UseradminpageForm(instance=user.useradminpage)
    return render(request, 'administrator/moderator_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




def moderator_delete(request, pk):
    moderator = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        moderator.delete()
        # if form.is_valid():
        return redirect('moderators')
    context = {"moderator": moderator}
    return render(request, 'administrator/moderator_delete.html', context)
# /*******************************************************



# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
# END ADMINISTRATOR - ADMIN *****************************************
# ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕


