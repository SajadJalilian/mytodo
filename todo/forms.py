from django import forms
from .models import Todo


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40)


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']