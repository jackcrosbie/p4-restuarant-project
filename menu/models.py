from django.db import models

# Create your models here.

class Menu(models.Model):
    img_one = models.ImageField(upload_to='images/menu_page-0001.jpg')
    img_two = models.ImageField(upload_to='images/')
    img_three = models.ImageField(upload_to='images/')
    img_four = models.ImageField(upload_to='images/')