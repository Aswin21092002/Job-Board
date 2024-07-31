# jobs/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .models import Job

def employer_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'jobs/employer_register.html', {'form': form})

def job_seeker_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'jobs/job_seeker_register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('job_list')
        else:
            return render(request, 'jobs/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'jobs/login.html')

def post_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        salary = request.POST['salary']
        Job.objects.create(title=title, description=description, location=location, salary=salary)
        return redirect('job_list')
    return render(request, 'jobs/post_job.html')

def job_list(request):
    query = request.GET.get('search')
    location = request.GET.get('location')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(title__icontains=query)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if min_salary:
        jobs = jobs.filter(salary__gte=min_salary)
    if max_salary:
        jobs = jobs.filter(salary__lte=max_salary)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})
