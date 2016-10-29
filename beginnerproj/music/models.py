from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#this is a structure of database
#any change to this file, you have to migrate and restart server.
#python manage.py makemigrations app_name
#python manage.py migrate


class Album(models.Model):
	#migrated as column
	artist = models.CharField(max_length = 250)
	album_title = models.CharField(max_length = 500)
	genre = models.CharField(max_length = 100)
	album_logo = models.FileField()

	#This function redirects after clicking the submit button
	def get_absolute_url(self):
		return reverse('music:detail', kwargs = {'pk': self.pk})


	def __str__(self):
		return self.album_title + ' - ' + self.artist

class Song(models.Model):
	album  = models.ForeignKey(Album, on_delete = models.CASCADE)   #Connects with album
	FILE_TYPE = models.CharField(max_length = 10)
	song_title = models.CharField(max_length = 250)
	is_favourite = models.BooleanField(default = False)
	song_upload = models.CharField(max_length = 500)

	def get_absolute_url(self):
		return reverse('music:song-index')

	def __str__(self):
		return self.song_title 
