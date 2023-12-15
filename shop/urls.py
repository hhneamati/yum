from django.urls import path, include
from . import views


app_name = 'shop'
urlpatterns = [
	path('', views.Home.as_view(), name='home'),
]