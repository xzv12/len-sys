

from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField



class UserManager(BaseUserManager):
    """ this class extend user manager class create by django to manage 
    user model class you should override create_user and create_superuser functions"""

    def create_user(self,email,password,**extra_fields):
        """ this function take all arg you defind in custom user model and create new user """
        
        if not email:
            raise ValueError("user must have email")

        user=self.model(email= self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,password):
        user                = self.create_user(email,password)
        user.is_staff       = True
        user.is_superuser   = True

        user.save(using = self._db)
        return user

    
class User (AbstractBaseUser,PermissionsMixin):
    """ here is user model extend  usermodel created with django ,
     you can add any new fields you want                   """
    
    
    name            = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100,unique=True,blank=False,null=False)
    phone           = models.CharField(max_length=50)
    balance         = models.DecimalField(max_digits=50,decimal_places=2,default=0)
    

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email' 
    REQUIRED_FIELD  = []     
    
    objects         = UserManager() 

    def __str__(self):
       return str(self.email)