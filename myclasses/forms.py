from django import forms
from users.models import Syllabus

class UploadSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['title', 'syllabus']
