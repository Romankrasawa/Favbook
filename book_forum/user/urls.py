from django.urls import path

from .views import *

urlpatterns = [
    path('log_in/', log_in, name="log_in"),
    path('log_out/', log_out, name="log_out"),
    path('register/', register, name="register"),
    path('settings/', settings, name="settings"),
    path('<user_id>/', profile , name="profile"),
    path('', account, name="account"),
]