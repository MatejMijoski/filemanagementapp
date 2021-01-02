from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name="index"),
    url('login', views.login_view, name='login'),
    url('logout', views.logout_view, name='logout'),
    path('usertags/<slug:slug>/', views.tagged, name="tagged"),
    url('^', include('django.contrib.auth.urls')),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^delete/(?P<pk>\d+)/$', views.FileDelete.as_view(), name="delete_file"),
    url('view/', views.auth_file_check, name="auth_file_check"),
    path('file-comment/<int:pk>/comment/', views.add_comment_to_file, name='add_comment_to_file'),
    path('change/<int:pk>', views.change_tags, name='change_tags')
]


