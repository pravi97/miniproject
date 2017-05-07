from django.conf.urls import *
from admissions import views
from sis.views import SpaView
from responsive_dashboard.views import generate_dashboard
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', generate_dashboard, {'app_name': 'admissions'}),
    url(r'^applicants_to_students/(?P<year_id>\d+)/$', views.applicants_to_students),
    url(r'^ajax_check_duplicate_applicant/(?P<fname>[A-z]+)/(?P<lname>[A-z]+)/$', views.ajax_check_duplicate_applicant),
    url(r'^reports/$', views.reports),
    url(r'^reports/funnel/$', views.funnel),
    url(r'^inquiry_form/$', views.inquiry_form),
    url(r'^custom-application-editor/', 
        TemplateView.as_view(template_name='admissions/custom_application_editor.html'),
        name="custom-application-editor"
        ),
    url(r'^application/(?P<pk>\d+)/$', SpaView.as_view()),
    url(r'^application/$', SpaView.as_view()),
]
