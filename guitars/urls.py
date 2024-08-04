from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'guitars'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('add_client/', views.add_client, name="add_client")
]
