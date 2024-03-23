"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from job.views import job_list, job_detail, add_job
from contact.views import send_message
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/', include('accounts.urls', namespace='accounts')),
  path('admin/', admin.site.urls),
  path('jobs/', job_list, name='job_list'),
  path('add/', add_job, name="add_job"),
  path('jobDetail/<str:job_slug>', job_detail, name="detail"),
  path('contact', send_message, name="contact"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
