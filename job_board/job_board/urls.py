# job_board/urls.py
from django.contrib import admin
from django.urls import path
from jobs import views  # Ensure this import is correct and views are defined in the jobs app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employer/register/', views.employer_register, name='employer_register'),
    path('job-seeker/register/', views.job_seeker_register, name='job_seeker_register'),
    path('login/', views.login, name='login'),
    path('post-job/', views.post_job, name='post_job'),
    path('jobs/', views.job_list, name='job_list'),
]
