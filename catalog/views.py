from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Job,JobInstance,Skill,Company

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_jobs = Job.objects.all().count()
    num_instances = JobInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = JobInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_companies = Company.objects.count()

    context = {
        'num_jobs': num_jobs,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_companies': num_companies,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class JobListView(generic.ListView):
    model = Job
    paginate_by=10

class JobDetailView(generic.DetailView):
    model = Job

class CompanyListView(generic.ListView):
    model = Company
    paginate_by=10

class CompanyDetailView(generic.DetailView):
    model= Company