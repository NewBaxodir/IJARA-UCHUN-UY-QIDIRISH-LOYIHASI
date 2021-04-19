from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, View
from django.db import transaction
from django.dispatch import receiver
from django.forms import CheckboxSelectMultiple
from multiselectfield import MultiSelectField
from .models import User, Useradminpage, Householder
from search.models import Announcement, Photo, Rooms, Floor





# from multiselectfield import MultiSelectField

class UseradminpageSignUpForm(UserCreationForm):

    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Familya'}
        ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Ism'}
        ))
    father_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Otasini ismi'}
        ))     
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Elektron pochtangiz'}
        ))
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': '+99(893) xxx-xx-xx'}
        ))
    admin_image = forms.ImageField(required=True)
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Login'}
        ))
    password1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password','class':'form-control', 'placeholder': 'Parol'}
        ))
    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password','class':'form-control', 'placeholder': 'Parolni qaytadan kiriting'}
        ))


    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.is_employee = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        if commit:
            user.save()
            group = Group.objects.get(name="admin")
            user.groups.add(group)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.username = self.cleaned_data.get('username')
        user.password1 = self.cleaned_data.get('password1')
        user.password2 = self.cleaned_data.get('password2')
        user.save()

        useradminpage = Useradminpage.objects.create(user=user)
        useradminpage.father_name=self.cleaned_data.get('father_name')
        useradminpage.phone_numer=self.cleaned_data.get('phone_numer')
        useradminpage.admin_image = self.cleaned_data.get('admin_image') 
        
        useradminpage.save()
        return user
   
          



class UserhouseholderSignUpForm(UserCreationForm):
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Familya'}
        ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Ism'}
        ))   
    # email = forms.CharField(required=True, widget=forms.TextInput(
    #     attrs = {'class':'form-control', 'placeholder': 'Elektron pochtangiz'}
    #     ))
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'number','class':'form-control', 'placeholder': '(893) xxx-xx-xx'}
        ))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'autocomplete':'username', 'placeholder': 'Login'}
        ))
    password1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password', 'class':'form-control', 'autocomplete':'current-password', 'placeholder': 'Parol'}
        ))
    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'type': 'password','class':'form-control', 'autocomplete':'current-password', 'placeholder': 'Parolni qaytadan kiriting'}
        ))
 
    
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        
        if commit:
            user.save()
            group = Group.objects.get(name="householder")
            user.groups.add(group)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        # user.email = self.cleaned_data.get('email')
        user.save()
        useradminpage = Householder.objects.create(user=user)
        useradminpage.father_name=self.cleaned_data.get('father_name')
        useradminpage.phone_numer=self.cleaned_data.get('phone_numer')
        useradminpage.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Login'}) 
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Parol'}) 
        self.fields['password2'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Parolni qaytadan kiriting'}) 
    



# Change OneToOne form 
class UserForm(forms.ModelForm):
    last_name = forms.CharField(required=True, label="Familya", widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Familya'}
        ))
    first_name = forms.CharField(required=True, label="Ism", widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Ism'}
        ))   
    email = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Elektron pochtangiz'}
        ))


    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email')




class UseradminpageForm(forms.ModelForm):
    father_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Otasini ismi'}
        ))
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Telefon nomber'}
        ))
    class Meta:
        model = Useradminpage
        fields = ('father_name', 'phone_numer', 'admin_image')




class HouseholderForm(forms.ModelForm):
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Telefon nomber'}
        ))
    class Meta:
        model = Householder
        fields = ('phone_numer', 'householder_image',)





































MODE = (
        ('kunlik ijara', "kunlik ijara"),
        ('oylik ijara', "oylik ijara"),
        ('yillik ijara', "yillik ijara"),
    )
KIMLAR = (
        ("erkak", "erkak"),
        ("ayol", "ayol"),
        ("oila", "oila"),
    )


# */****************************************
KISHI_SONI = (
        ('1 kishilik', "1 kishilik"),
        ('2 kishilik', "2 kishilik"),
        ('3 kishilik', "3 kishilik"),
        ('4 kishilik', "4 kishilik"),
        ('5 kishilik', "5 kishilik"),
        ('6 kishilik', "6 kishilik"),
        ('7 kishilik', "7 kishilik"),
        ('oilalilar', "oilalilar"),
    )
TOPSHIRILGAN = (
        ("uy bo'sh", "uy bo'sh"),
        ("uy band", "uy band"),
    )

MONEYC = (
        ('USD', "USD"),
        ('RUB', "RUB"),
        ("UZS", "UZS"),
    )

SOVUQ_SUV = (
        ('sovuq suv bor KT.bilan', "sovuq suv bor KT.bilan"),
        ('sovuq suv bor KT.tashqari', "sovuq suv bor KT.tashqari"),
        ('sovuq suv yoq', "sovuq suv yoq"),
    )
ISSIQ_SUV = (
        ('issiq suv bor KT.bilan', "issiq suv bor KT.bilan"),
        ('issiq suv bor KT.tashqari', "issiq suv bor KT.tashqari"),
        ('issiq suv yoq', "issiq suv yoq"),
    )
SVET = (
        ('elektr bor KT.bilan', "elektr bor KT.bilan"),
        ('elektr bor KT.tashqari', "elektr bor KT.tashqari"),
        ('elektr yoq', "elektr yoq"),
    )
GAZ = (
        ('gaz bor KT.bilan', "gaz bor KT.bilan"),
        ('gaz bor KT.tashqari', "gaz bor KT.tashqari"),
        ('gaz yoq', "gaz yoq"),
    )
WIFI = (
        ('wifi bor KT.bilan', "wifi bor KT.bilan"),
        ('wifi bor KT.tashqari', "wifi bor KT.tashqari"),
        ('wifi yoq', "wifi yoq"),
    )
SOVUTGICH = (
        ('sovutgich bor KT.bilan', "sovutgich bor KT.bilan"),
        ('sovutgich bor KT.tashqari', "sovutgich bor KT.tashqari"),
        ('sovutgich yoq', "sovutgich yoq"),
    )
KONDISIONER = (
        ('kondisioner bor KT.bilan', "kondisioner bor KT.bilan"),
        ('kondisioner bor KT.tashqari', "kondisioner bor KT.tashqari"),
        ('kondisioner yoq', "kondisioner yoq"),
    )
HAMMOM = (
        ('hammom bor KT.bilan', "hammom bor KT.bilan"),
        ("hammom bor KT.tashqari", "hammom bor KT.tashqari"),
        ("hammom yo'q", "hammom yo'q"),
    )
HOJAT = (
        ('hojat bor', "hojat bor"),
        ("hojat yo'q", "hojat yo'q"),
    )

XAVSIZ = (
        ('xavsizlik E.tizimi bor', "xavsizlik E.tizimi bor"),
        ("xavsizlik E.tizimi yo'q", "xavsizlik E.tizimi yo'q"),
    )


FLOOR = (
        ('hovli joy', "hovli joy"),
        ("ko'p qavatli", "ko'p qavatli"),
    )

FLOORMANY = (
        ('', ""),
        ('1 - qavatda', "1 - qavatda"),
        ('2 - qavatda', "2 - qavatda"),
        ('3 - qavatda', "3 - qavatda"),
        ('4 - qavatda', "4 - qavatda"),
        ('5 - qavatda', "5 - qavatda"),
        ('6 - qavatda', "6 - qavatda"),
        ('7 - qavatda', "7 - qavatda"),
        ('8 - qavatda', "8 - qavatda"),
        ('9 - qavatda', "9 - qavatda"),
        ('10 - qavatda', "10 - qavatda"),
        ('11 - qavatda', "11 - qavatda"),
        ('12 - qavatda', "12 - qavatda"),
       
    )

ROOMS = (
        ('1 hona', "1 hona"),
        ('2 hona', "2 hona"),
        ('3 hona', "3 hona"),
        ('4 hona', "4 hona"),
        ('5 hona', "5 hona"),
        ('6 hona', "6 hona"),
        ('7 hona', "7 hona"),
        ('8 hona', "8 hona"),
        ('9 hona', "9 hona"),
        ('10 hona', "10 hona"),
     
       
    )

REGIONN = (
        ("Samarqand shahri", "Samarqand shahri"),
        ("Samarqand tumani", "Samarqand tumani"),
        ("Toyloq tumani", "Toyloq tumani"),        
        ("Bulungʻur tumani", "Bulungʻur tumani"),
        ("Jomboy tumani", "Jomboy tumani"),
        ("Urgut tumani", "Urgut tumani"),        
        ("Pastdargʻom tumani", "Pastdargʻom tuman"),
        ("Payariq tumani", "Payariq tumani"),
        ("Oqdaryo tumani", "Oqdaryo tumani"),        
        ("Ishtixon tumani", "Ishtixon tumani"),
        ("Qoʻshrabot tumani", "Qoʻshrabot tumani"),
        ("Kattaqoʻrgʻon tumani", "Kattaqoʻrgʻon tumani"),        
        ("Nurobod tumani", "Nurobod tumani"),
        ("Narpay tumani", "Narpay tumani"),
        ("Paxtachi tumani", "Paxtachi tumani"),
    )

class AnnouncementUpdate(forms.ModelForm):
    region = forms.ChoiceField(required=False, choices = REGIONN)

    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Uy manzili'}
        ))
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Telefon nomer'}
        ))
    mode = forms.ChoiceField(required=False, choices = MODE) 
    kimlar = forms.ChoiceField(required=False, choices=KIMLAR) 
    kishilar = forms.ChoiceField(required=False, choices=KISHI_SONI) 
    topshirilgan = forms.ChoiceField(required=False, choices=TOPSHIRILGAN) 
    moneyc = forms.ChoiceField(required=False, choices=MONEYC) 
    money = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Miqdorni kiriting'}
        ))
    floor = forms.ChoiceField(required=False, choices = FLOOR)
    floormany = forms.ChoiceField(required=False, choices = FLOORMANY)
    rooms = forms.ChoiceField(required=False, choices = ROOMS)

    tartiblar = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text', 'style':'height: 100px',  'placeholder': ""}
        ))
    requiredbuild = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': ""}
        ))
    ish = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text', 'style':'height: 100px', 'placeholder': ""}
        ))


    sovuq_suv = forms.ChoiceField(required=False, choices=SOVUQ_SUV) 
    issiq_suv = forms.ChoiceField(required=False, choices=ISSIQ_SUV) 
    svet = forms.ChoiceField(required=False, choices=SVET) 
    gaz = forms.ChoiceField(required=False, choices=GAZ)
    additional2 = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text', 'style':'height: 100px',  'placeholder': ""}
        ))

    wifi = forms.ChoiceField(required=False, choices=WIFI) 
    sovutgich = forms.ChoiceField(required=False, choices=SOVUTGICH) 
    kondisioner = forms.ChoiceField(required=False, choices=KONDISIONER) 
    additional3 = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text', 'style':'height: 100px',  'placeholder': ""}
        ))

    hojat = forms.ChoiceField(required=False, choices=HOJAT) 
    hammom = forms.ChoiceField(required=False, choices=HAMMOM) 
    additional4 = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text', 'style':'height: 100px', 'placeholder': ""}
        ))
    xafsiz = forms.ChoiceField(required=False, choices=XAVSIZ) 
    additional5 = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text', 'style':'height: 100px', 'placeholder': ""}
        ))
    geolocaion = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'Geo-joylashuv'}
        ))
           
    


    class Meta:
        model = Announcement
        fields = (

             'region', 'address', 'phone_numer', 'floormany', 'rooms', 'mode', 'kimlar', 'kishilar',
            'topshirilgan', 'moneyc', 'money', 'floor', 'tartiblar', 'ish',            
            'sovuq_suv', 'issiq_suv', 'svet', 'gaz', 'additional2',
            'wifi', 'sovutgich', 'kondisioner', 'additional3',
            'hammom', 'additional4',
            'xafsiz', 'additional5', 'geolocaion'

            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mode'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['kimlar'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['kishilar'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['topshirilgan'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['moneyc'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['floor'].widget.attrs.update({'class':'form-control'}) 
        
        self.fields['sovuq_suv'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['issiq_suv'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['svet'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['gaz'].widget.attrs.update({'class': 'form-control'}) 

        self.fields['wifi'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['sovutgich'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['kondisioner'].widget.attrs.update({'class': 'form-control'}) 
        
        self.fields['hojat'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['hammom'].widget.attrs.update({'class': 'form-control'}) 
        
        self.fields['xafsiz'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['floormany'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['rooms'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['region'].widget.attrs.update({'class': 'form-control'}) 





class PhotoUpdate(forms.ModelForm):

    image = forms.ImageField(label='Uy surati')

    class Meta:
        model = Photo
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'input-group-text', 'type':'file'})
  
 



# floormany
# rooms
