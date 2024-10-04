from django.db import models

# Create your models here.

class AddTeachers(models.Model):
    username = models.CharField(max_length=50)
    
    full_name = models.TextField()
    
    contact_no = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username