from django.db import models

class UserModel(models.Model):

    email = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=40)
    
    def __str__(self):
        return self.username
    
     