from django import forms
from .models import LeaveRequest


class LeaveRequestForm(forms.ModelForm):
    
    class Meta:
        model = LeaveRequest
        fields = ['person', 'start_date', 'end_date', 'leave_type']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date must be on or after the start date.")
        
        return cleaned_data
