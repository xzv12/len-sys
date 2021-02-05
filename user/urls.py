
from django.urls import path
from .views import *


urlpatterns = [
    
    path('register/',CreateUserView.as_view(),name='register'),
    path('login/',CreateTokenView.as_view(),name='login'),
    path('edit-profile/',ManageUserView.as_view(),name='edit-profile')   

]



