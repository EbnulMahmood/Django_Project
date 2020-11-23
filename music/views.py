from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Audio
from django.contrib import messages
from .forms import AudioUpdateForm
from django.contrib.auth.decorators import login_required


AUDIO_FILE_TYPES = ['mp3', 'wav', 'm4a', 'wma']

class AudioListView(ListView):
    model = Audio
    template_name = 'music/music.html'
    context_object_name = 'audios'
    ordering = ['-date_posted']
    paginate_by = 5

class AudioDetailView(DetailView):
    model = Audio

@login_required
def updoad_audio(request):
    form = AudioUpdateForm()
    if request.method == 'POST':
        form = AudioUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user_au = form.save(commit=False)
            user_au.author = request.user
            user_au.audio_file = request.FILES['audio_file']
            file_type = user_au.audio_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in AUDIO_FILE_TYPES:
                return render(request, 'music/error.html')
            user_au.save()
            messages.success(request, f'Your file has been uploaded!')
            return render(request, 'music/music.html', {'user_au': user_au})
    else:
        context = {"form": form,}
        return render(request, 'music/upload.html', context)

class AudioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Audio
    fields = ['title', 'artist', 'lyrics']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        audio = self.get_object()
        if self.request.user == audio.author:
            return True
        return False

class AudioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Audio
    success_url = '/music/'

    def test_func(self):
        audio = self.get_object()
        if self.request.user == audio.author:
            return True
        return False