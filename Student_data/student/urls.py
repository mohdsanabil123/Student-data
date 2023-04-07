from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert, name='insert'),
    path('insert', views.insertData, name='insertData'),
    path('show', views.show, name='show'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.destroy, name='delete'),
]