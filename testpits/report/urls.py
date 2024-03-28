from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'report'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('project_list/', views.projects_view, name='project_list'),
    path('report_list/', views.reports_view, name='report_list'),
    path('project_form/', views.projects_form, name='project_form'),
    path('report/', views.report_form, name='report_form'),
    path('convert/<int:test_pit>/', views.excel_convertion, name='convert_report'),
    path('single/<int:test_pit>/', views.single_report, name='single_report'),
    path('project/<str:project_number>/', views.project_reports, name='project_reports'),
    
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)