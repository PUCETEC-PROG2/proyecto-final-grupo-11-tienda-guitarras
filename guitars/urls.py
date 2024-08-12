from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'guitars'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('add_client/', views.add_client, name="add_client"),
    path('client/', views.client_list, name="client_list"),
    path('create_product/', views.create_product, name="create_product"),
    path('product/', views.product_list, name="product_list"),
    path('client/edit_client/<int:id>', views.edit_client, name="edit_client"),
    path('client/delete_client/<int:id>', views.delete_client, name="delete_client"),
    path('product/edit_product/<int:id>', views.edit_product, name="edit_product"),
    path('product/delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    path('category/<str:category_name>/product/<int:id>/', views.product, name='category_product'),
    path('category/<str:category_name>/edit_product/<int:id>/', views.edit_product, name='edit_category_product'),
    path('category/<str:category_name>/delete_product/<int:id>/', views.delete_product, name='delete_category_product'),
    path('categories/', views.category_list, name='category_list'),

    
]

