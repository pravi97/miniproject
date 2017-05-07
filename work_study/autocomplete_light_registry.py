import autocomplete_light.shortcuts as al
from .models import StudentWorker
from sis.autocomplete_light_registry import UserAutocomplete

al.register(StudentWorker, UserAutocomplete)
