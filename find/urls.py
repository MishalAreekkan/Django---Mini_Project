from django.urls import path
from . import views

urlpatterns = [
    path("",views.admins,name="signin"),
    path("home",views.home,name="home"),
    path('login',views.user_login,name="login")
]
