
from django.urls import path

from idcard import views

app_name = "idcard"

urlpatterns = [
    path('', views.home, name="home"),
    path('convert/', views.convert, name="convert"),
]