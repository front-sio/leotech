from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('contact/success/', views.contact_success, name='contact_success'),
]
