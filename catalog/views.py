#     from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.contrib.auth.models import User
# from typing_extensions import Required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from catalog.forms import Lfeedback,Cfeedback
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import sign_up_form


# Create your views here.
from catalog.models import Lecturer,LecturerFeedback,College,CollegeFeedback, Lrating,Crating

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_lecturers = Lecturer.objects.all().count()
    num_colleges = College.objects.all().count()


    context = {
        'num_lecturers': num_lecturers,
        'num_colleges': num_colleges,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class LecturerListView(generic.ListView):
    model = Lecturer
    paginate_by=10

class LecturerDetailView(generic.DetailView):
    model = Lecturer

class CollegeListView(generic.ListView):
    model = College
    paginate_by=10

# @login_required
class CollegeDetailView(LoginRequiredMixin, generic.DetailView):
    model= College



def feedback_lecturer(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    feedbackform=LecturerFeedback.objects.get(id=1)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Lfeedback(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            one=int(form.cleaned_data['one'])
            two=int(form.cleaned_data['two'])
            three=int( form.cleaned_data['three'])
            four=int(form.cleaned_data['four'])
            obj=Lrating(lecturer=lecturer,form=feedbackform,r1=one,r2=two,r3=three,r4=four)
            w1=feedbackform.w1
            w2=feedbackform.w2
            w3=feedbackform.w3
            w4=feedbackform.w4
            obj.total=2*(w1/10.0*one+w2/10.0*two+w3/10.0*three+w4/10.0*four)
            obj.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('thanku') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = Lfeedback()

    context = {
        'form': form,
        'lecturer_instance': lecturer,
    }

    return render(request, 'catalog/lecturer_feedback_form.html', context)


def feedback_college(request, pk):
    college = get_object_or_404(College, pk=pk)
    feedbackform=CollegeFeedback.objects.get(id=1)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Cfeedback(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            one=int(form.cleaned_data['one'])
            two=int(form.cleaned_data['two'])
            three=int( form.cleaned_data['three'])
            four=int(form.cleaned_data['four'])
            obj=Crating(college=college,form=feedbackform,r1=one,r2=two,r3=three,r4=four)
            w1=feedbackform.w1
            w2=feedbackform.w2
            w3=feedbackform.w3
            w4=feedbackform.w4
            obj.total=2*(w1/10.0*one+w2/10.0*two+w3/10.0*three+w4/10.0*four)
            obj.save()
            return HttpResponseRedirect(reverse('thanku') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = Lfeedback()

    context = {
        'form': form,
        'college_instance': college,
    }

    return render(request, 'catalog/college_feedback_form.html', context)


def Thanku(request):
    return HttpResponse("Thank you for your feedback")




def signup(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = sign_up_form(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user = User.objects.create_user(form.cleaned_data['first_name'],form.cleaned_data['email_id'], form.cleaned_data['password'])
            user.last_name = form.cleaned_data['last_name']
            user.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = sign_up_form()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)