from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View 
from .models import Album, Song
from .forms import UserForm



class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'
	def get_queryset(self):
		return Album.objects.all()


class SongIndexView(generic.ListView):
	template_name = 'music/song-index.html'
	context_object_name = 'all_songs'
	def get_queryset(self):
		return Song.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'
	
class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']
		
	
class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']
		
class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

class SongCreate(CreateView):
	model = Song
	fields = ['album','FILE_TYPE','song_title','is_favourite','song_upload']

# class SongUpdate(UpdateView):
# 	model = Song
# 	fields = ['album','FILE_TYPE','song_title','is_favourite','song_upload']

# class SongDelete(DeleteView):
# 	model = Album
# 	success_url = reverse_lazy('music:song-index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)
			# cleaned normalised data 
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct
			user = authenticate(username = username, password = password)  # checks in database

			if user is not None:

				if user.is_active:

					login(request, user)
					return redirect('music:index')    #redirects logged in user to homepage

		return render(request, self.template_name, {'form': form})



# class LandingView(View):
# 	template_name = 'landing.html'
# 	context_object_name = 'all_albums'
# 	def get_queryset(self):
# 		return Album.objects.all()























# # from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader  #for html templates
# from .models import Album, Song 


# def index(request):

# 	all_albums = Album.objects.all()     #creates a list 
	
# 	# template = loader.get_template('music/index.html') #django already looks into templates directory

# 	# context = {	'all_albums': all_albums }
# 	return render(request, 'music/index.html', {'all_albums': all_albums})


# def detail(request, album_id):
# 	# try:
# 	# 	album = Album.objects.get(pk=album_id)
# 	# except Album.DoesNotExist:
# 	# 	raise Http404("Album does not exist")
# 	album = get_object_or_404(Album, pk=album_id)    #shortcut to above code
# 	return render(request, 'music/detail.html', {'album': album })

# def favourite(request, album_id):
# 	album = get_object_or_404(Album, pk=album_id)    #shortcut to above code
# 	try:
# 		selected_song = album.song_set.get(pk=request.POST['song'])
# 	except (KeyError, Song.DoesNotExist):
# 		return render(request, 'music/detail.html', {
# 			'album': album,
# 			'error_message': "You did not select a valid song"
# 			})	

# 	else:
# 		selected_song.is_favourite = True
# 		selected_song.save()
# 		return render(request, 'music/detail.html', {'album': album})





# # Create your views here.
