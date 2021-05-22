from django.urls import path

from core import views

urlpatterns = [
    path('', views.dashboard_view),
    path('login', views.login_view),
]
