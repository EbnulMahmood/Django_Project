from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Video
from django.contrib import messages
from .forms import VideoUpdateForm
from django.contrib.auth.decorators import login_required


VIDEO_FILE_TYPES = ['mp4', 'mov', 'wmv', 'flv', 'avi', 'mkv']

class VideoListView(ListView):
    model = Video
    template_name = 'video/video.html'
    context_object_name = 'videos'
    ordering = ['-date_posted']
    paginate_by = 4

class VideoDetailView(DetailView):
    model = Video

@login_required
def updoad_video(request):
    form = VideoUpdateForm()
    if request.method == 'POST':
        form = VideoUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user_au = form.save(commit=False)
            user_au.author = request.user
            user_au.video_file = request.FILES['video_file']
            file_type = user_au.video_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in VIDEO_FILE_TYPES:
                return render(request, 'video/error.html')
            user_au.save()
            messages.success(request, f'Your file has been uploaded!')
            return render(request, 'video/video.html', {'user_au': user_au})
    else:
        context = {"form": form,}
        return render(request, 'video/upload.html', context)

class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'artist', 'lyrics']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False

class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = '/video/'

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False