from django.db.models.base import Model
from django.forms import ModelForm
from .models import Report, Project
from django import forms

class ReportForm(ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fields['test_pit'].widget.attrs.update({'value':'1' , 'class':'w-3/4 text-center'})
    self.fields['field_coordinator'].widget.attrs.update({'value':'Paul Monteleone' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['tech_name'].widget.attrs.update({'value':'Alejandro Padron' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['weather'].widget.attrs.update({'value':'Sunny' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['timeproject'].widget.attrs.update({'value':'12:00' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['pavement_type'].widget.attrs.update({'value':'Pavement' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['pavement_thickness'].widget.attrs.update({'value':'6' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['excavation_method'].widget.attrs.update({'value':'Air Knife' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['utility_size'].widget.attrs.update({'value':'6' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['material'].widget.attrs.update({'value':'Concrete' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['utility_type'].widget.attrs.update({'value':'Water' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['coordinate_system'].widget.attrs.update({'value':'NAD83 New Jersey State Planes - US foot' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['field_coordination'].widget.attrs.update({'value':'Regular traffic condition' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['utility_top_depth'].widget.attrs.update({'value':'36' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['utility_bottom_depth'].widget.attrs.update({'value':'42' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['utility_width'].widget.attrs.update({'value':'8' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['lane_closure'].widget.attrs.update({'value':'N/A' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['police_presence'].widget.attrs.update({'value':'N/A' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['mpt'].widget.attrs.update({'value':'N/A' , 'class':'rounded-xl w-3/4 text-center'})
    self.fields['remarks'].widget.attrs.update({'placeholder':'What were the findings?' , 'class':'rounded-xl w-3/4 text-center'})

  class Meta:
    model = Report
    fields = "__all__"

  
class ProjectForm(ModelForm):

  class Meta:
    model = Project
    fields = "__all__"

  def clean_unique_field(self):
        data = self.cleaned_data['project_number']
        if ReportForm.objects.filter(project_number=data).exists():
            raise forms.ValidationError("This field must be unique.")
        return data
