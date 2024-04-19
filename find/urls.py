from django.urls import path
from . import views

urlpatterns = [
    path("",views.admins,name="signin"),
    path("home",views.home,name="home"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path("search",views.searching,name="search"),
    path("homelist",views.home_list,name="homelist"),
    path("delete/<id>",views.deleting,name="delete"),
    path("editing/<id>",views.editing,name="edit"),
]
