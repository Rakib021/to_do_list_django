from django import forms
from first_app.models import TaskModel

class TaskStoreForm(forms.ModelForm):
    class Meta:
        model =TaskModel
        fields =['id','taskTitle','taskDescription']
