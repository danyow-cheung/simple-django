from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("register/",views.registerPage,name="register"),
    # 将默认主页定向到定制的主页
    path("",views.home,name="home"),

    # path("room/<str:pk>/",views.room,name="room"),
    path("room/<int:pk>/",views.room,name="room"),
    path("profile/<str:pk>",views.userProfile,name="user-profile"),

    path("create-room/",views.create_room,name="create-room"),
    # path("update-room/<str:pk>/",views.update_room,name="update-room"),
    path("update-room/<int:pk>/",views.update_room,name="update-room"),
    path("delete-room/<int:pk>/",views.delete_room,name="delete-room"),
    path('delete-message/<int:pk>/', views.deleteMessage, name="delete-message"),

]
