from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food_blog(models.Model):
    username    = models.ForeignKey(User,on_delete=models.CASCADE)
    Tfood       = models.CharField(max_length=100,primary_key=True)
    Cost        = models.IntegerField()
    Image       = models.ImageField(upload_to = 'sai')
    Description = models.TextField()
    Ingredients = models.TextField()
    Famous      = models.TextField()

    
    def __str__(self):
        return self.Tfood































