from django.urls import path
from .views import home,redirect_url,shorturl_details,delete_shorturl

urlpatterns = [
    path('',home, name="home"),
    path('<str:code>/',redirect_url, name="redirect"),
    path('details/<int:pk>/',shorturl_details, name="shorturl_details"),
    path('shorturl/delete/<int:pk>/', delete_shorturl, name='delete_shorturl'),
] 
