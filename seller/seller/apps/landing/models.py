from django.db import models
import os
from stdimage import StdImageField, JPEGField


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class New(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.TextField(max_length=200)
    date = models.CharField('Date', max_length=20, null=True)
    text = models.TextField(max_length=300, help_text="Сама новость")
    pic = StdImageField(upload_to=get_image_path, blank=True, null=True, variations={'thumbnail': {'width': 298, 'height': 298}})
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class FlatRodonit(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    flat_name = models.CharField(max_length=300)
    price = models.CharField('Цена', max_length=20, null=True)
    pic = StdImageField(upload_to=get_image_path, blank=True, null=True, variations={'large': {'width': 1000, 'height': 500}})
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.flat_name

class FlatAqvarel(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    flat_name = models.CharField(max_length=300)
    price = models.CharField('Цена', max_length=20, null=True)
    pic = StdImageField(upload_to=get_image_path, blank=True, null=True, variations={'large': {'width': 1000, 'height': 500}})
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.flat_name


class InfoText(models.Model):
    h1_content = models.CharField(max_length=2000, blank = True)
    h1_font_size = models.IntegerField(default=18, blank = True)
    h1_text_align = models.CharField(default='center', max_length=15, blank = True)
    h1_text_color = models.CharField(default='black', max_length=50,blank = True)
    text_content = models.TextField(max_length=5000, blank = True)
    text_font_size = models.IntegerField(default=18, blank = True)
    text_align = models.CharField(default='center', max_length=15, blank = True)
    text_color = models.CharField(default='black', max_length=50, blank = True)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.text_content[0:50]