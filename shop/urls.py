from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:subcategory_slug>/<slug:item_slug>/', views.item_view, name='item_view'),
    path('<slug:category_slug>/<slug:subcategory_slug>/', views.main_view, name='subcategory_view'),
    path('<slug:category_slug>/', views.main_view, name='category_view'),
    path('', views.main_view, name='order_view'),

]