from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("table_list", views.table_list, name='table_list'),
]
