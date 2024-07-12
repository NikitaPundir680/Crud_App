# from django import forms
# from .models import Employee

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['empcode','username', 'department','designation','qualification','email','extension','mobile']

from django import forms
from .models import Employee
from .models import Comment

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empcode','username', 'department','designation','qualification','email','extension','mobile', 'gender','dob' ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10, 'cols': 93}),
        }