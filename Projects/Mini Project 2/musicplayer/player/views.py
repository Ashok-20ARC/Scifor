from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Song
from .forms import SongUploadForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Home Page
def home(request):
    return render(request, "home.html")

# Register View
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "register.html")


# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Welcome back.")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("login")

    return render(request, "login.html")


# Logout View
def user_logout(request):
    logout(request)
    return redirect("home")

# Upload View (Requires Login)
@login_required
def upload_song(request):
    if request.method == "POST":
        title = request.POST.get("title")
        artist = request.POST.get("artist")
        movie_name = request.POST.get("movie_name")
        audio_file = request.FILES.get("audio_file")
        cover_image = request.FILES.get("cover_image")

        if title and artist and movie_name and audio_file:
            song = Song.objects.create(
                user=request.user,
                title=title,
                artist=artist,
                movie_name=movie_name,
                audio_file=audio_file,
                cover_image=cover_image
            )
            return redirect("playlist")

    return render(request, "upload.html")


# Playlist View (Requires Login)
@login_required
def playlist(request):
    user_songs = Song.objects.filter(user=request.user)  # Only show logged-in user's songs
    admin_songs=Song.objects.filter(user__is_superuser=True)
    return render(request, 'playlist.html', {'user_songs': user_songs,'admin_songs':admin_songs})

# Now Playing Page (Current Song + Playlist)
@login_required
def now_playing(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    request.session['last_played_song'] = song.id

    # Check whether the song came from "User Songs" or "Admin Songs"
    source = request.GET.get("source", "user")  # Default to "user" if no source is provided

    if source == "admin":
        playlist_songs = Song.objects.filter(user__is_superuser=True)  # Admin's Songs
    else:
        playlist_songs = Song.objects.filter(user=request.user)  # User's Songs

    return render(request, "now_playing.html", {
        "current_song": song,
        "playlist_songs": playlist_songs,
        "source":source
    })


@login_required
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    # Only allow deletion if the user uploaded the song OR is an admin
    if request.user == song.user or request.user.is_superuser:
        song.delete()
    
    return redirect('playlist')