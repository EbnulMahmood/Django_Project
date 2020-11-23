from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import PDF
from django.contrib import messages
from .forms import PDFUpdateForm
from django.contrib.auth.decorators import login_required


PDF_FILE_TYPES = ['pdf', 'ps', 'eps']

class PDFListView(ListView):
    model = PDF
    template_name = 'audiobook/audiobook.html'
    context_object_name = 'pdfs'
    ordering = ['-date_posted']
    paginate_by = 5

class PDFDetailView(DetailView):
    model = PDF

@login_required
def upload_book(request):
    form = PDFUpdateForm()
    if request.method == 'POST':
        form = PDFUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user_au = form.save(commit=False)
            user_au.user = request.user
            user_au.pdf_file = request.FILES['pdf_file']
            file_type = user_au.pdf_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in PDF_FILE_TYPES:
                return render(request, 'audiobook/error.html')
            user_au.save()
            messages.success(request, f'Your file has been uploaded!')
            return render(request, 'audiobook/audiobook.html', {'user_au': user_au})
    else:
        context = {"form": form,}
        return render(request, 'audiobook/upload.html', context)

class PDFUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PDF
    fields = ['title', 'author', 'summary']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        pdf = self.get_object()
        if self.request.user == pdf.user:
            return True
        return False

class PDFDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PDF
    success_url = '/audiobook/'

    def test_func(self):
        pdf = self.get_object()
        if self.request.user == pdf.user:
            return True
        return False