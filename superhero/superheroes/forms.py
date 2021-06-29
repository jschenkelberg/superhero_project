from django import forms

from .models import Superhero

class SuperheroForm(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = ('name', 'alter_ego',
                  'primary_superhero_ability',
                  'secondary_superhero_ability',
                  'catchphrase',)
