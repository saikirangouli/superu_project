from django.urls import path
from .views import *
urlpatterns = [

   path('user-profile/',UserProfileView.as_view(),name='user-profile'),
   path('user-profile/<int:pk>/',UserProfileView.as_view(),name='user-profile')
]