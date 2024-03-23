from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ApplyForm, JobForm
from .filters import JobFilter

# Create your views here.

def job_list(request):
  job_list = Job.objects.all()
  
  ## filter 
  myfilter = JobFilter(request.GET, queryset=job_list)
  job_list = myfilter.qs
  
  paginator = Paginator(job_list, 2)  # Show 25 contacts per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)


  context = {'jobs':page_obj, 'mfilter':myfilter}  
  
  return render(request, 'job/jobs.html', context )


def job_detail(request, job_slug):
  job_details = Job.objects.get(slug = job_slug)
  
  if request.method=='POST' :
    form = ApplyForm(request.POST, request.FILES)
    if form.is_valid():
      myform = form.save(commit=False)
      myform.job = job_details
      myform.save()
  else:
    form = ApplyForm()
  
  context = {'jobs':job_details, 'form1':form}
  return render(request, 'job/job_details.html', context)

@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('job_list'))

    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})