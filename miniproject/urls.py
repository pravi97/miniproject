"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import admin
from responsive_dashboard import views as dashboard_views
from django.http import HttpResponse
from sis import views
from sis.views import AttendanceReportView

def robots(request):
    ''' Try to prevent search engines from indexing
    uploaded media. Make sure your web server is
    configured to deny directory listings. '''
    return HttpResponse(
        'User-agent: *\r\nDisallow: /media/\r\n',
        content_type='text/plain'
    )

urlpatterns = [
    url(r'^robots.txt', robots),
    url(r'^admin/', include("massadmin.urls")),
    url(r'^admin_export/', include("admin_export.urls")),
    url(r'^grappelli/', include('grappelli.urls')),
    # url(r'^ckeditor/', include('ckeditor_urls')),
    url(r'^$',views.index),
    url(r'^sis/', include('sis.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^simple_import/', include('simple_import.urls')),
    # url(r'^accounts/password_change/$',views.password_change),
    # url(r'^accounts/password_change_done/$',views.password_change_done, name="password_change_done"),
    url(r'^logout/$', views.logout_view),
    url(r'^admin/', admin.site.urls),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^reports/(?P<name>attendance_report)/$', AttendanceReportView.as_view()),
    url(r'^reports/', include('scaffold_report.urls')),
    url(r'^discipline/', include('discipline.urls')),
    url(r'^attendance/', include('attendance.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^grades/', include('grades.urls')),
    url(r'^course/', include('grades.urls')),
    url(r'^work_study/', include('work_study.urls')),
    url(r'^admissions/', include('admissions.urls')),
    url(r'^benchmark_grade/', include('benchmark_grade.urls')),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    # url(r'^file_import/', include('file_import.urls')),
    url(r'^', include('responsive_dashboard.urls')),
    url(r'^administration/', include('administration.urls')),
]
