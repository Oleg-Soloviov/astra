from django.views.generic.edit import CreateView
from .models import Blog
from django.urls import reverse_lazy


class CreateMessage(CreateView):
    model = Blog
    fields = ['text']
    success_url = reverse_lazy('blog-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_list'] = Blog.objects.values_list('text', flat=True)
        return context
