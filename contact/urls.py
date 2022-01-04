from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.addContact, name='add-contact'),
    path('profile/<str:pk>', views.contactProfile, name='profile'),
    path('edit-contact/<str:pk>', views.editContact, name='edit-contact'),
    path('delete/<str:pk>', views.deleteContact, name='delete'),
    path('accounts/', include('django.contrib.auth.urls'))
]