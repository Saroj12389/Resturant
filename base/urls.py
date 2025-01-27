from django.urls import path

from .views import HomeView, ItemsDetailView


urlpatterns = [

path('', HomeView.as_view(), name='home'),
path('item/detail/<int:pk>/', ItemsDetailView.as_view(), name='item_detail')

    
] 