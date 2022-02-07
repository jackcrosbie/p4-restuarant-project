from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('user_account/<user_id>', views.user_account, name='user_account'),
]