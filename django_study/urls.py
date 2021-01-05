from django.urls import path

from . import views

app_name = 'django_study'
urlpatterns = [
    path('templates/insert', views.insert_template, name='insert_template'),
    path('templates/table', views.table_template, name='table_template'),
    path('templates/', views.index_template, name='index_template'),
    path('', views.IndexView.as_view(), name="index"),
]