from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name = "login_page"),
    path('register/', register, name = "register"),
    path('logout/', logout_page, name = "logout"),
    path('', Home, name = "home"),
]