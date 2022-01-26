from django.db import models

# Create your models here.

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "pics")

class HomePageFormModel(models.Model):
    email    = models.EmailField()
    message  = models.TextField()

    def __str__(self):
        return self.email