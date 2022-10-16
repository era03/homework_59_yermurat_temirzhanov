from django.shortcuts import get_object_or_404, redirect
from webapp.forms import TaskForm
from webapp.models import Tasks
from django.views.generic import UpdateView, TemplateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse



class TaskDetailView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    model = Tasks

    def get_success_url(self):
        return reverse('index')


class TaskUpdateView(UpdateView):
    template_name = 'task_edit.html'
    form_class = TaskForm
    model = Tasks
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('index')


class TaskDeleteView(DeleteView):
    template_name = 'task_confirm_delete.html'
    model = Tasks
    success_url = reverse_lazy('index')
    context_object_name = 'task'
