
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def joblistapi(request):
  all_jobs = Job.objects.all()
  data = JobSerializer(all_jobs, many=True).data
  return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request, job_id):
  job_detail = Job.objects.get(id = job_id)
  data = JobSerializer(job_detail).data
  return Response({'data':data})