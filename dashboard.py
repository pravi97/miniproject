from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.modules import DashboardModule

from sis.forms import *

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for ecwsp.
    """
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        self.children.append(modules.Group(
            column=1,
            title='CWSP',
            children=[
                modules.ModelList(
                    models=(
                        'work_study.models.StudentWorker',
                        'work_study.models.StudentInteraction',
                        'work_study.models.Attendance',
                        'work_study.models.PickupLocation',
                        'work_study.models.CraContact',
                        'work_study.models.Personality',
                        'work_study.models.Handout33',
                        'work_study.models.PresetComment',
                        'work_study.models.AttendanceFee',
                        'work_study.models.AttendanceReason',
                    ),
                ),
                modules.ModelList(
                    title="Company Data",
                    models=(
                        'work_study.models.Company',
                        'work_study.models.WorkTeam',
                        'work_study.models.WorkTeamUser',
                        'work_study.models.TimeSheet',
                        'work_study.models.TimeSheetPerformanceChoice',
                        'work_study.models.Contact',
                        'work_study.models.CompanyContract',
                        'work_study.models.CompanyHistory',
                        'work_study.models.ClientVisit',
                        'work_study.models.PaymentOption',
                        'work_study.models.StudentDesiredSkill',
                        'work_study.models.StudentFunctionalResponsibility',
                        'work_study.models.CompContract',
                        'work_study.models.MessageToSupervisor',
                    ),
                ),
            ]
        ))

        self.children.append(modules.ModelList(
            title=_('School Information'),
            column=1,
            models=(
                'sis.models.SchoolYear',
                'sis.models.Student',
                'sis.models.EmergencyContact',
                'sis.models.Cohort',
                'sis.models.PerCourseSectionCohort',
                'sis.models.ReasonLeft',
                'sis.models.Faculty',
                'sis.models.MessageToStudent',
                'sis.models.FamilyAccessUser',
                'sis.models.GradeScale',
            ),
        ))
        #
        # self.children.append(modules.ModelList(
        #     title=('Volunteer Tracking'),
        #     column=1,
        #     models=(
        #         'ecwsp.volunteer_track.*',
        #     ),
        # ))

        self.children.append(modules.ModelList(
            title=_('Attendance'),
            column=1,
            models=('sis.models.StudentAttendance',
                    'sis.models.AttendanceStatus',
                    'sis.models.ASPAttendance',
                ),
        ))

        self.children.append(modules.ModelList(
            title = 'Discipline',
            column=1,
            models=(
                'discipline.models.StudentDiscipline',
                'discipline.models.DisciplineAction',
                'discipline.models.PresetComment',
            ),
        ))

        self.children.append(modules.ModelList(
            title = 'Attendance',
            column=1,
            models=(
                'attendance.*',
            ),
        ))

        self.children.append(modules.ModelList(
            title='Courses and Grades',
            column=1,
            models=('schedule.*', 'benchmark_grade.*', 'benchmarks.*'),
        ))
        #
        # self.children.append(modules.ModelList(
        #     title='Standard Tests',
        #     column=1,
        #     models=('ecwsstandard_test.*',),
        # ))

        self.children.append(modules.ModelList(
            title='Admissions',
            column=1,
            models=('admissions.*',),
        ))
        #
        # self.children.append(modules.ModelList(
        #     title='Counseling',
        #     column=1,
        #     models=('eccounseling.*',),
        # ))
        #
        # self.children.append(modules.ModelList(
        #     title='Alumni',
        #     column=1,
        #     models=('ecwsp.alumni.*',),
        # ))

        self.children.append(modules.AppList(
            title='Administration',
            column=2,
            models=(
                'django.contrib.*',
                'administration.*',
                'constance.*',
                # 'ecwsp.engrade_sync.*',
                # 'ldap_groups.*',
                # 'google_auth.*',
            )
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title='Recent Actions',
            column=2,
            limit=5
        ))

        self.children.append(modules.LinkList(
            column=2,
            children=(
                {
                    'title': 'Schooldriver Manual',
                    'url': 'http://docs.schooldriver.org',
                    'external': True,
                },
                {
                    'title': 'Schooldriver Community',
                    'url': 'http://github.com/burke-software/django-sis',
                    'external': True,
                },
                {
                    'title': 'Burke Software',
                    'url': 'http://burkesoftware.com',
                    'external': True,
                },
            )
        ))
