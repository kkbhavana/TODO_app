from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView

from .models import Task


# Create your views here.


def send_test_email(request):
    subject = 'hi welcome to Django email configuration session'
    message = 'This is test email sent using django'
    from_email = 'kkbhavana6@gmail.com'
    recipient_list = ['bhavanababukk@gmail.com']
    send_mail(subject,message,from_email,recipient_list)
    return HttpResponse('Test mail sent successfully...!')
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterView, self).get(*args, *kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        context['count'] = context['task'].filter(completed=False).count()
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'taskdetails.html'


def home(request):
    return render(request, 'home.html')
