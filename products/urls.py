from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.retrieve_products,name='retrieve_products'),
    path('products/create/',views.create_product,name='create_product'),
    path('products/modify/<int:pk>/',views.update_products,name='update_products'),
]