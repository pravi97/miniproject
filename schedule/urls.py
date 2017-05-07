from django.conf.urls import *
from responsive_dashboard.views import generate_dashboard
from .views import schedule_enroll
from sis.views import SpaView

urlpatterns = [
    url(r'^$', generate_dashboard, {'app_name': 'schedule'}),
    url(r'^course/(.*)$', SpaView.as_view(), name="course"),
    url(r'^enroll/(?P<id>\d+)$', schedule_enroll),
]
