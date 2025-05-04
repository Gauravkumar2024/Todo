from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    sr_number=models.AutoField(primary_key=True,auto_created=True)
    Tittle=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)