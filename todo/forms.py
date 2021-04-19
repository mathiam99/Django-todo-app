from django.forms import ModelForm, TextInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title','description','completed', 'programmed_date')
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Enter a todo here'}),
            'description': TextInput(attrs={'placeholder': 'Type the description...'}),
        }