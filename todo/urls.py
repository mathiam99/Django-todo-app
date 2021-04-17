from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('detail/<str:pk>', views.detail, name="detail"),
    path('delete/<str:pk>', views.delete, name="delete"),
    path('edit/<str:pk>', views.edit, name="edit")
]
