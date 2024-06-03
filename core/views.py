from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, TaskForm
from django.contrib.auth import authenticate, login, logout
from .models import Task
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


def home_view(request ):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request, 'core/index.html', context)

class HomeView(ListView):
    model = Task
    template_name = 'core/index.html'
    context_object_name = 'tasks'

class SearchResultView(HomeView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        return self.model.objects.filter(title__iregex=query )

class TaskDetailView(DetailView):
    model = Task
    template_name = 'core/task_detail.html'
    context_object_name = 'task_detail'


class DeleteArticle(DeleteView):
    model = Task
    template_name = 'core/task_confirm_delete.html'
    success_url = '/'
    context_object_name = 'task_detail'


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('home')
            else:

                return redirect('sign_in')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'core/sign_in.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('sign_in')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'core/sign_up.html', context)


def logout_(request):
    logout(request)
    return redirect('home')

@login_required
def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('home')
    else:
        form = TaskForm()

    context = {
        'form': form
    }

    return render(request, 'core/create.html', context)

class UpdateArticle(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'core/create.html'