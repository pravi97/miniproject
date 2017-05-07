from django.conf.urls import *
from attendance import views

urlpatterns = [
    url(r'^teacher_submissions/$', views.teacher_submissions),
    url(r'^studentattendance/report/$', views.attendance_report),
    url(r'^studentattendance/student/(?P<id>\d+)/$', views.attendance_student),
    url(r'^studentattendance/add_multiple/$', views.add_multiple),
    url(r'^teacher_attendance/$', views.teacher_attendance),
    url(r'^teacher_attendance/$', views.teacher_attendance),
    url(r'^teacher_attendance/(?P<course_section>\d+)/$', views.teacher_attendance),
    url(r'^course_section_attendance/$', views.select_course_section_for_attendance),
    url(r'^course_section_attendance/(?P<course_section_id>\d+)/$', views.course_section_attendance),
    url(r'^daily_attendance_report/$', views.daily_attendance_report_wrapper),
]
