from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



class loan_request (models.Model):

    amount      = models.DecimalField(max_digits=50,decimal_places=2)
    period      = models.DecimalField(max_digits=3,decimal_places=1)
    user        = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add=True)
    Funded      = models.BooleanField(default=False)
    Completed   = models.BooleanField(default=False)

    def __str__ (self):
        return  self.user.email

    class Meta:
        ordering = ['created']


class offer (models.Model):
    user        = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    request     = models.ForeignKey(loan_request,on_delete=models.CASCADE)
    rate        = models.DecimalField(max_digits=4,decimal_places=2)
    created     = models.DateTimeField(auto_now_add=True)
    accepted    = models.BooleanField(default=False)


    class Meta:
        ordering = ['created']

