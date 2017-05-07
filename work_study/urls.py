from django.conf.urls import *
from work_study import views
from responsive_dashboard.views import generate_dashboard

urlpatterns = [
    url(r'^$', generate_dashboard, {'app_name': 'work_study'}),
    url(r'^reports/$', views.report_builder_view),
    url(r'^student_timesheet/$', views.student_timesheet),
    url(r'^supervisor/create_timesheet/(?P<studentId>\d+)/$', views.create_time_card),
    url(r'^supervisor/change_supervisor/(?P<studentId>\d+)/$', views.change_supervisor),
    url(r'^supervisor/$', views.supervisor_dash),
    url(r'^supervisor/view/$', views.supervisor_view),
    url(r'^supervisor/view/xls/$', views.supervisor_xls),
    url(r'^student/view/$', views.student_view),
    url(r'^student/edit/(?P<tsid>\d+)/$', views.student_edit),
    url(r'^approve/$', views.approve),
    url(r'^supervisor/delete/$', views.timesheet_delete),
    url(r'^dol/$',views.dol_form),
    url(r'^dol/(?P<id>\d+)$', views.dol_form),
    url(r'^student_meeting/$', views.student_meeting),
    url(r'^company_contract/(?P<id>\d+)/$', views.company_contract1),
    url(r'^company_contract2/(?P<id>\d+)/$', views.company_contract2),
    url(r'^company_contract3/(?P<id>\d+)/$', views.company_contract3),
    url(r'^company_contract_complete/(?P<id>\d+)/$', views.company_contract_complete),
    url(r'^company_contract_pdf/(?P<id>\d+)/$', views.company_contract_pdf),
    url(r'^fte_chart/$', views.fte_chart),
    url(r'^routes/$', views.routes),
    url(r'^take_attendance/$', views.take_attendance),
    url(r'^take_attendance/(?P<work_day>\d+)/$', views.take_attendance),
]
