
from .models import Student, Teacher
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user']


class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'position': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),

        }
