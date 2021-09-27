from django import forms
from django.forms import ModelForm
from .models import algorithm, placement, language, development, enquiry
 
class algorithmForm(forms.ModelForm):
  class Meta:
    model = algorithm
    fields = ["name","email","phone","college",]
    
class placementForm(forms.ModelForm):
  class Meta:
    model = placement
    fields = ["name","email","phone","college",]


class languageForm(forms.ModelForm):
  class Meta:
    model = language
    fields = ["name","email","phone","college",]


class developmentForm(forms.ModelForm):
  class Meta:
    model = development
    fields = ["name","email","phone","college",]

class enquiryForm(forms.ModelForm):
  class Meta: 
    model = enquiry
    fields = ["name", "email","message",]
    
