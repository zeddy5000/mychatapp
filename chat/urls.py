from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    # path("<str:room_name>/", views.room, name="room"),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='chat/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]