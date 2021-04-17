from django.urls import path
from . import views


urlpatterns =[
    path('', views.Home.as_view(), name = "Home"),
    path('index/', views.index, name = "Index"),
    path('upload/', views.upload_csv, name = "Upload"),
]

