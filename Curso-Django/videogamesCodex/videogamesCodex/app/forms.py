"""
Definition of forms.
"""

from django import forms


from app.models import Videogames

class Gameform(forms.ModelForm):
    class Meta:
        model = Videogames
        fields = ('name',
                  'publisher',
                  'year',
                  'genre',
                  'plataform',
                  'score',
                  'online',
                  'pegi',
)
