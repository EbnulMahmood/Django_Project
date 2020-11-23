from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post
from music.models import Audio
from audiobook.models import PDF
from video.models import Video


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                 request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = Post.objects.all().filter(title__icontains=search)
        audios = Audio.objects.all().filter(title__icontains=search)
        pdfs = PDF.objects.all().filter(title__icontains=search)
        videos = Video.objects.all().filter(title__icontains=search)
        results = {
            'posts': posts,
            'audios': audios,
            'pdfs': pdfs,
            'videos': videos,
        }
        return render(request, 'users/search.html', {'results': results})