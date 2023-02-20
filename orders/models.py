from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User=get_user_model

class Order(models.Model):
    

    SIZES=(

       ('SMALl','small'),
       ('MEDIUM','medium'),
       ('LARGE','large'),
        ('EXTRA_LARGE','extra_large'),   

    )

    ORDER_STATUS=(

         ('PENDING','pending'),
         ('IN_TRANSIT','intransit'),
         ('DELIVERED','delivered'),



    )
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    size=models.CharField(max_length=20,choices=SIZES,default=SIZES[0][0])
    order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    quantity=models.IntegerField()