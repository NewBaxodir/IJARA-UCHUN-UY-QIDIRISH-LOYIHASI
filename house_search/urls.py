"""house_search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from administrator import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cscss/', TemplateView.as_view(template_name="login/index.html")),
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('social_django.urls', namespace='social')),
    path('', include('home.urls')),

    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # START LOGIN - HISOB ***********************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up.as_view(), name='sign_up'),
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # START LOGIN - HISOB ***********************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕


    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # START ACCOUNT - HISOB ***********************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

    path('account/', views.account_home, name='account'),
    path('settings/', views.settings, name='settings'),
    path('account_update/<int:pk>/', views.account_update, name='account_update'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),
    path('liked/', views.like_unlike_post, name='like-post-view'),
    path('add/<int:pk>/', views.add_post, name='add_post'),
    path('announcement_like/', views.announcement_like, name='announcement_like'),

    path('search/', views.search, name='search'),


    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name="password_reset_complete"),


    # path('like/<int:pk>/', LikeView, name='like_post'),
    # path('like/<str:slug>/', views.PostLikeRedirect.as_view(), name='like'),

    
    path('logout/',views.logout_view, name='logout'),

    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # END ACCOUNT - HISOB ***********************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕



    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # START ANNOUNCEMENTS - E'LONLAR **************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

    path('announcements/', views.announcement, name='announcement'),
    path('create/', views.create, name='create'),
    path('announcement_update/<int:pk>/', views.announcement_updates, name='announcement_updates'),
    path('announcement_delete/<int:pk>/', views.announcement_delete, name='announcement_delete'),
    path('images_update/<int:pk>/', views.images_update, name='images_update'),

    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # END ANNOUNCEMENTS - E'LONLAR ***************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕


    
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # START ADMINISTRATOR - ADMIN *****************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

    path('administrator', views.administrator, name='administrator'),
    
    # ANNOUNCERS ************************************************************************
    path('admin-announcers/', views.admin_announcers, name='admin_announcers'),
    path('admin-announcers-update/<int:pk>/', views.admin_announcers_update, name='admin_announcers_update'),
    path('admin-announcers-delete/<int:pk>/', views.admin_announcers_delete, name='admin_announcers_delete'),
    # ANNOUNCERS ************************************************************************

    # ANNOUNCEMENTS *********************************************************************
    path('admin-announcements/', views.admin_announcements, name='admin_announcements'),
    path('admin-announcements-update/<int:pk>/', views.admin_announcements_update, name='admin_announcements_update'),
    path('admin-announcements-update-image/<announcements_id>/', views.admin_announcements_update_image, name='admin_announcements_update_image'),
    path('admin-announcements-delete/<int:pk>/', views.admin_announcements_delete, name='admin_announcements_delete'),
    # ***********************************************************************************

    
    
    # MODERATORS *************************************************************************
    path('moderators/', views.moderators, name='moderators'),
    path('moderator-create/', views.moderator_create.as_view(), name='moderator_create'),
    path('moderator-update/<int:pk>/', views.moderator_update, name='moderator_update'),
    path('moderator-delete/<int:pk>/', views.moderator_delete, name='moderator_delete'),
    # MODERATORS *************************************************************************



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



