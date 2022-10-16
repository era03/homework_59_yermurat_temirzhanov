from django.views.generic import ListView, DetailView, CreateView
from webapp.models import Projects, Tasks
from django.urls import reverse
from webapp.forms import ProjectForm, TaskForm
from django.shortcuts import redirect, get_object_or_404



class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})

class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Projects
    context_object_name = 'projects'
    ordering = ('created_at',)


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Projects
    context_object_name = 'project'


class ProjectCreateView(CreateView, SuccessDetailUrlMixin):
    template_name = 'project_create.html'
    form_class = ProjectForm
    model = Projects

    def get_success_url(self):
        return reverse('projects')


class ProjectTaskCreateView(CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'task_create.html'

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects')