from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    query = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['last_name','first_name']

class RegisterUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)

    def set_password(self,raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self,raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username, self.email
