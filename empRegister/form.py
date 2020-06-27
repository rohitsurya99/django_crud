from django import forms

from .models import Employee

class Employeeform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = dict(fullname='Full Name', emp_code='EMP. Code')

    def __init__(self, *args, **kwargs):
        super(Employeeform, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False