from rest_framework import  serializers
from django.contrib.auth import get_user_model,authenticate



class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model           = get_user_model()
        fields          = ('phone','password','name','email','balance')
        extra_kwargs    = {'password':{'write_only':True,'min_length':5}}
     
    
    def create(self,validated_data):
        return get_user_model().objects.create_user(**validated_data)
      
    def update(self, instance, validated_data): 
        password        = validated_data.pop('password',None)
        user            = super().update(instance,validated_data)
        
        if password:
            user.set_password(password)
            user.save()

        return user     


class AuthTokenSerializer(serializers.Serializer):
    """ note this extend base serializer notice the differnt from model serialzer apove """
   
    email       = serializers.CharField()
    password    = serializers.CharField (
        style           = {'input_type':'password'},
        trim_whitespace = False           
        )
    

    def validate (self,attrs):
        """validate input data """

        email     = attrs.get('email')
        password  = attrs.get('password')
        user      = authenticate(
                request   = self.context.get('request'),
                username  = email,
                password  = password
        )

        if not user:
            msg=( " there isn't user with this values ")            
            raise serializers.ValidationError(msg,code='authentcation')
            
        attrs['user']  = user
        return attrs        

