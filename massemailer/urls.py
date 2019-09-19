from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendmail/<int:id>', views.massemail, name='sendmail'),
]