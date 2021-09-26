from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import placementForm, algorithmForm, languageForm, developmentForm, enquiryForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView

# Add the two views we have been talking about  all this time :)
class IndexPageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
            
            
class CoursePageView(TemplateView):
    template_name = "course.html"
    
    
class ContactPageView(TemplateView):
    template_name = "contact.html"
    
class ThankyouPageView(TemplateView):
    template_name = "thankyou.html"
    
    
def placementform(request):
    form= placementForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        messages.error(request, "Error")
  
    return render(request, 'thankyou.html',)


def algorithmform(request):
    form= algorithmForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        messages.error(request, "Error")
        
        
    return render(request, 'thankyou.html',)


def languageform(request):
    form= languageForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        messages.error(request, "Error")    
    
  
    return render(request, 'thankyou.html',)


def developmentform(request):
    form= developmentForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        messages.error(request, "Error")
        
    return render(request, 'thankyou.html',)


def enquiryform(request):
    form= enquiryForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        messages.error(request, "Error")
  
    return render(request, 'thankyou.html',)

    
