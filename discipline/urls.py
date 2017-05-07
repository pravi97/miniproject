from django.conf.urls import *
from .views import enter_discipline, discipline_list, view_discipline, discipline_report, discipline_report_view, generate_from_attendance
from responsive_dashboard.views import generate_dashboard

urlpatterns = [
    url(r'^$', generate_dashboard, {'app_name': 'discipline'}),
    url(r'^disc/$', enter_discipline),
    url(r'^disc/list$', discipline_list),
    url(r'^disc/view$', view_discipline),
    url(r'^disc/list/(?P<type>[a-z]+)$', discipline_list),
    url(r'^disc/report/(?P<student_id>\d+)/$', discipline_report),
    url(r'^disc/stats/$', discipline_report_view),
    url(r'^generate_from_attendance/$', generate_from_attendance),
]
