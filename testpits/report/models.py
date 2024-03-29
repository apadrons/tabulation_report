from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Project(models.Model):

  project_number = models.CharField(max_length=100,unique=True)
  project_title = models.CharField(max_length=200,default= 'test')
  address = models.CharField(max_length= 250)
  client = models.CharField(max_length=100, default='0000')
  agreement_number = models.CharField(max_length=100, default='0000')
  client_project_number = models.CharField(max_length=100, default='0000')

  def __str__(self):
    return self.project_number


class Report(models.Model):
  test_pit = models.IntegerField(default=1)
  field_coordinator = models.CharField(max_length=200,default='Paul Monteleone')
  tech_name = models.CharField(max_length=200,default='Paul Monteleone')
  weather = models.CharField(default='Sunny', max_length=200)
  date_project = models.DateField(auto_now=True)
  timeproject = models.TimeField()
  utility_found = models.BooleanField(default=True)
  project_number = ForeignKey(Project,related_name='reports', on_delete=models.CASCADE)
  #Pavement information
  pavement_type = models.CharField(max_length=200)
  pavement_thickness = models.CharField(max_length=200)
  #Utility information
  excavation_method = models.CharField(max_length=200)
  utility_size = models.CharField(max_length=200,default='8 inches')
  material = models.CharField(max_length=200,default='Concrete duct')
  utility_type = models.CharField(max_length=200,default='Water')
  coordinate_system = models.CharField(max_length=200,default="NAD83 New Jersey State Planes - US foot")
  field_coordination = models.CharField(max_length=200,default='Regular traffic condition')
  utility_top_depth = models.IntegerField(default=36)
  utility_bottom_depth = models.IntegerField(default=42)
  utility_width = models.IntegerField(default=8)
  #Traffic control protocols
  lane_closure = models.CharField(max_length=200,default='N/A')
  police_presence = models.CharField(max_length=200,default='N/A')
  mpt = models.CharField(max_length=200,default='N/A')


  #REMARKS
  remarks = models.TextField(max_length=200)


  #IMAGES
  before_excavation = models.ImageField(upload_to='test_pits/',null=True,blank=True,default='noimage.jpg')
  excavated_area= models.ImageField(upload_to='test_pits/',null=True,blank=True,default='noimage.jpg')
  after_excavation= models.ImageField(upload_to='test_pits/',null=True,blank=True,default='noimage.jpg')


  
  def __str__(self):
    return ( str(self.project_number))
  
