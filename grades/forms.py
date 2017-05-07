from django import forms

from sis.forms import UploadFileForm
from schedule.forms import MarkingPeriodSelectForm
from .models import *
from .forms import *

class GradeUpload(UploadFileForm, MarkingPeriodSelectForm):
    pass
