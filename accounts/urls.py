from django.urls import URLPattern, path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegister.as_view()),
 
 
 ]