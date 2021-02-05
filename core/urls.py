
from django.urls import  path
from .views import *


urlpatterns = [
    path('create-request',create_request_view.as_view(),name='create_request'),
    path('list-requests',list_requests_view.as_view(),name='list_requests'),
    path('list-my-requests',list_myrequests_view.as_view(),name='list_my_requests'),
    path('request/<int:pk>',request_view.as_view(),name='request_view'),
    path('offer/<int:pk>',offer_view.as_view(),name='offer_view'),
    


]




