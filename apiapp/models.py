from unittest.util import _MAX_LENGTH
from django.db import models

class APIData(models.Model):

    vid_id = models.CharField(max_length=50, primary_key=True )
    vid_title = models.CharField(max_length=500)
    vid_publishDate = models.CharField(max_length=50)
    vid_description = models.CharField(max_length=5000)
    logo_url = models.CharField(max_length=50)
    