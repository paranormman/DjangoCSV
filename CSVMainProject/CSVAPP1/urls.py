from django.conf.urls import  include, url
from .import views
from django.urls import path


urlpatterns = [ path('index/', views.index, name = 'index'),
url(r'^upload/', views.upload_csv, name='upload_csv'),
]