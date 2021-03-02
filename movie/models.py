from django.db import models

# Create your models here.

class MovieModel(models.Model):

  title = models.CharField(max_length = 150)
  url = models.TextField()
  description = models.TextField(blank=True, null=True)
  message = models.TextField(blank=True, null=True)
  uploaded_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title