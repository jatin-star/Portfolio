from django.urls import path
from . import views

urlpatterns = [
    path('Hello/', views.Hello, name='Hello'),
    path('', views.portfolio_page, name='Portfolio'),
    path('mail/', views.contact_view, name='Mail')
]
