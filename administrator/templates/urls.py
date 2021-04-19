from django.conf.urls import url
from django.urls import path, include
from administrator import views

# from administrator.views import  AnnouncementListView

# LikeView

urlpatterns = [
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # START HOME - BOSH SAHIFA ********************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

    path('', views.home, name='home'),

    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # END HOME - BOSH SAHIFA ********************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    



    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # START ACCOUNT - HISOB ***********************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕

    path('account/', views.account_home, name='account'),
    path('settings/', views.settings, name='settings'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up.as_view(), name='sign_up'),
    path('account_update/<int:pk>/', views.account_update, name='account_update'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),
    path('liked/', views.like_unlike_post, name='like-post-view'),

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
    # END ANNOUNCEMENTS - E'LONLAR **************************************
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



    # API
    # path('annser/', views.announcemenserializ, name='annser'),
    # path('announ/', views.AnnouncementListView.as_view(), name='announ'),
    
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
    # END ADMINISTRATOR - ADMIN *****************************************
    # ↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕
   
]
