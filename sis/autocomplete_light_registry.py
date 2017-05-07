import autocomplete_light.shortcuts as al
from sis.models import Student, EmergencyContact, Faculty

class UserAutocomplete(al.AutocompleteModelBase):
    split_words = True
    search_fields = ['first_name', 'last_name']
    attrs = {
        'placeholder': 'Lookup Student(s)',
    }

class FacultyAutocomplete(UserAutocomplete):
    attrs = {
        'placeholder': 'Lookup Faculty',
    }


class ActiveStudentAutocomplete(UserAutocomplete):
    choices=Student.objects.filter(is_active=True)

class LookupStudentAutocomplete(UserAutocomplete, al.AutocompleteModelTemplate):
    autocomplete_template = 'sis/lookup_student.html'

class ContactAutocomplete(al.AutocompleteModelTemplate):
    split_words = True
    search_fields = ['fname', 'lname']
    attrs = {
        'placeholder': 'Lookup Contact(s)',
    }
    choice_template = 'sis/autocomplete_contact.html'

al.register(EmergencyContact, ContactAutocomplete)
al.register(Student, UserAutocomplete)
al.register(Student, ActiveStudentAutocomplete)
al.register(Faculty, FacultyAutocomplete)
al.register(Student, LookupStudentAutocomplete)
