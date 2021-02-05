
from rest_framework import generics
from.serializers import *
from .models import *
from rest_framework import authentication ,permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class create_request_view(APIView):
    serializer_class        = request_serializer
    authentication_classes  = (authentication.TokenAuthentication,)
    permission_classes      = (permissions.IsAuthenticated,)

    def post(self, request):
        user        = request.user
        loan_req    = loan_request(user=user)
        serializer  = self.serializer_class(loan_req,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        


class list_requests_view(APIView):
    serializer_class        = request_serializer
    authentication_classes  = (authentication.TokenAuthentication,)
    permission_classes      = (permissions.IsAuthenticated,)


    def get(self, request):

        serializer_context = {
            'request': request,
        }

        reqs = loan_request.objects.all().exclude(user = request.user)
        data = request_serializer(reqs,context=serializer_context, many=True).data
        return Response(data)
    

class list_myrequests_view(APIView):
    serializer_class        = request_serializer
    authentication_classes  = (authentication.TokenAuthentication,)
    permission_classes      = (permissions.IsAuthenticated,)


    def get(self, request):

        serializer_context = {
            'request': request,
        }
        reqs = loan_request.objects.filter(user = request.user)
        data = request_serializer(reqs,context=serializer_context, many=True).data
        return Response(data)
    

class request_view(APIView):
    serializer_class        = offer_create_serializer
    authentication_classes  = (authentication.TokenAuthentication,)
    permission_classes      = (permissions.IsAuthenticated,)


    def get(self, request,pk):

        serializer_context = {
            'request': request,
        }
        reqs    = loan_request.objects.get(id = pk)
        offers  = offer.objects.filter(request = reqs)
        data    = self.serializer_class(offers,context=serializer_context, many=True).data
        return Response(data)

    def post(self, request,pk):
        user  = request.user

        serializer_context = {
            'request': request,
        }    

        if loan_request.objects.get(id=pk).user == user:
            raise ValueError("you can't make offer on your requests" )
        
        else:
            reqs        = loan_request.objects.get(id = pk)
            off         = offer(user=user,request=reqs)
            serializer  = self.serializer_class(off,context=serializer_context,data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print(serializer.errors)


class offer_view(APIView):
    serializer_class        = offer_manage_serializer
    authentication_classes  = (authentication.TokenAuthentication,)
    permission_classes      = (permissions.IsAuthenticated,)

    def post(self,request,pk):
        ofr   = offer.objects.get(id=pk)
        
        lenme_fee = 3

        if request.user == ofr.request.user:

            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                
                if serializer.validated_data.get('accepted') == True and ofr.accepted==False:

                    if ofr.user.balance >= (ofr.request.amount+lenme_fee):
                        
                        ofr.user.balance         = ofr.user.balance -(ofr.request.amount+lenme_fee)
                        ofr.request.user.balance = ofr.request.user.balance+ofr.request.amount
                        ofr.request.Funded       = True
                        ofr.accepted             = True

                        ofr.user.save()
                        ofr.request.user.save()
                        ofr.request.save()
                        ofr.save()            
                else:
                    raise ValueError('no changes')

            else:
                raise ValueError(serializer.errors)


        else:
            raise ValueError('only request owner can accept offers')
