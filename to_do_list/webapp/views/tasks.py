from django.shortcuts import get_object_or_404, redirect
from webapp.forms import TaskForm
from webapp.models import Tasks
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse



class TaskDetailView(DetailView):
    template_name = 'task_detail.html'
    model = Tasks
    context_object_name = 'task'


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
