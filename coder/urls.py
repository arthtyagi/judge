from django.urls import path
from .import views
app_name = 'coder'

urlpatterns = [
    path('', views.home, name='home'),]
