import autocomplete_light.shortcuts as al
from .models import CourseSection

class CourseSectionAutocomplete(al.AutocompleteModelBase):
    split_words = True
    search_fields = ['name', 'course__fullname', 'course__shortname']

al.register(CourseSection, CourseSectionAutocomplete)
