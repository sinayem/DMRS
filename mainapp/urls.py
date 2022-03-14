from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.home,name='homepage'),
    path("logout", views.logout_request, name="logout"),
    path("log_in/",views.reg_sign_in, name = 'signin_name'),
    path("reg_home/", views.reg_home, name="reg_home_name"),
    path("detail/<str:pk>", views.detail, name="detail"),
    path("reg_marriage/", views.reg_mar, name="reg_marriage"),
    path("searchbar/", views.searchbar, name="searchbar"),
    path("sorry_page/", views.sorry, name="sorry_name"),
    path('pdf/<int:pk>',views.c_pdf,name='pdf'),

]
