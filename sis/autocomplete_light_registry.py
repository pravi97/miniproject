import autocomplete_light.shortcuts as al
from sis.models import Student, EmergencyContact, Faculty

al.register(Student,
    split_words = True,
    search_fields=['first_name', 'last_name'],
    attrs = {
        'placeholder': 'Lookup Student(s)',
    }
)

al.register(Faculty,
    attrs = {
        'placeholder': 'Lookup Faculty',
    }
)

al.register(EmergencyContact,
    split_words = True,
    search_fields=['fname', 'lname'],
    choice_template = 'sis/autocomplete_contact.html',
    attrs = {
        'placeholder': 'Lookup Contact(s)',
    }
)


al.register(Student,
    choices=Student.objects.filter(is_active=True)
)

al.register(Student,
    autocomplete_template = 'sis/lookup_student.html'
)
