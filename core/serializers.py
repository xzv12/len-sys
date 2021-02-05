
from rest_framework import serializers

from .models import *
from core.models import *

class request_serializer(serializers.ModelSerializer):

    url=serializers.HyperlinkedIdentityField(
        view_name       = 'request_view',
        lookup_field    = 'pk'
    )
    
    class Meta:
        model               = loan_request
        fields              = ('url','id','user','amount','period')
        read_only_fields    = ('id','user')

 


class offer_create_serializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name       = 'offer_view',
        lookup_field    = 'pk'

    )
    class Meta:
        model               = offer
        fields              = ('url','id','request','user','rate','accepted')
        read_only_fields    = ('id','request','user','accepted')
        

class offer_manage_serializer(serializers.ModelSerializer):

    class Meta:
        model               = offer
        fields              = ('id','request','user','rate','accepted')
        read_only_fields    = ('id','request','user','rate')
        
