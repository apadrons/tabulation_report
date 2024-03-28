from django.db.models.base import Model
from django.forms import ModelForm
from .models import Report, Project
from django import forms

class ReportForm(ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fields['test_pit'].widget.attrs.update({'value':'1'})
    self.fields['field_coordinator'].widget.attrs.update({'value':'Paul Monteleone'})
    self.fields['tech_name'].widget.attrs.update({'value':'Alejandro Padron'})
    self.fields['weather'].widget.attrs.update({'value':'Sunny'})
    self.fields['timeproject'].widget.attrs.update({'value':'12:00'})
    self.fields['pavement_type'].widget.attrs.update({'value':'Pavement'})
    self.fields['pavement_thickness'].widget.attrs.update({'value':'6'})
    self.fields['excavation_method'].widget.attrs.update({'value':'Air Knife'})
    self.fields['utility_size'].widget.attrs.update({'value':'6'})
    self.fields['material'].widget.attrs.update({'value':'Concrete'})
    self.fields['utility_type'].widget.attrs.update({'value':'Water'})
    self.fields['coordinate_system'].widget.attrs.update({'value':'NAD83 New Jersey State Planes - US foot'})
    self.fields['field_coordination'].widget.attrs.update({'value':'Regular traffic condition'})
    self.fields['utility_top_depth'].widget.attrs.update({'value':'36'})
    self.fields['utility_bottom_depth'].widget.attrs.update({'value':'42'})
    self.fields['utility_width'].widget.attrs.update({'value':'8'})
    self.fields['lane_closure'].widget.attrs.update({'value':'N/A'})
    self.fields['police_presence'].widget.attrs.update({'value':'N/A'})
    self.fields['mpt'].widget.attrs.update({'value':'N/A'})
    self.fields['remarks'].widget.attrs.update({'placeholder':'What were the findings?'})

  class Meta:
    model = Report
    fields = "__all__"

  def clean_unique_field(self):
        data = self.cleaned_data['test_pit']
        if ReportForm.objects.filter(test_pit=data).exists():
            raise forms.ValidationError("This field must be unique.")
        return data
  
class ProjectForm(ModelForm):

  class Meta:
    model = Project
    fields = "__all__"

  def clean_unique_field(self):
        data = self.cleaned_data['project_number']
        if ReportForm.objects.filter(project_number=data).exists():
            raise forms.ValidationError("This field must be unique.")
        return data
