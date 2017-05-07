from django.conf.urls import *
from .views import transcript_nonofficial, photo_flash_card, thumbnail, paper_attendance
from .views import user_preferences, view_student, ajax_include_deleted, import_naviance, increment_year, increment_year_confirm, StudentViewDashletView
from responsive_dashboard.views import generate_dashboard

urlpatterns = [
    url(r'^$', generate_dashboard, {'app_name': 'sis'}),
    url(r'^reports/transcript_nonofficial/(?P<student_id>\d+)/$', transcript_nonofficial),
    url(r'^flashcard/$', photo_flash_card),
    url(r'^flashcard/(?P<year>\d+)/$', photo_flash_card),
    url(r'^preferences/$', user_preferences),
    url(r'^view_student/$', view_student),
    url(r'^view_student/(?P<id>\d+)/$', view_student, name="view-student"),
    url(r'^ajax_view_student_dashlet/(?P<pk>\d+)/$', StudentViewDashletView.as_view()),
    url(r'^ajax_include_deleted/$', ajax_include_deleted),
    url(r'^student/naviance/$', import_naviance),
    url(r'^increment_year/$', increment_year),
    url(r'^increment_year_confirm/(?P<year_id>\d+)/$', increment_year_confirm),
    url(r'^thumbnail/(?P<year>\d+)/$', thumbnail),
    url(r'^paper_attendance/(?P<day>\d+)/$', paper_attendance),
]
