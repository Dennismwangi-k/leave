from django.db import models
from datetime import timedelta


class LeaveRequest(models.Model):
    
    LEAVE_TYPE_CHOICES = [
        ('normal', 'Normal Leave'),
        ('sick', 'Sick Leave'),
    ]
    
    person = models.CharField(max_length=200, help_text="Name of the person requesting leave")
    start_date = models.DateField(help_text="Start date of the leave period")
    end_date = models.DateField(help_text="End date of the leave period")
    leave_type = models.CharField(
        max_length=10,
        choices=LEAVE_TYPE_CHOICES,
        default='normal',
        help_text="Type of leave being requested"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.person} - {self.start_date} to {self.end_date}"
    
    @property
    def leave_days(self):
        if not self.start_date or not self.end_date:
            return 0
        
        days = 0
        current_date = self.start_date
        
        while current_date <= self.end_date:
            if current_date.weekday() < 5:
                days += 1
            current_date += timedelta(days=1)
        
        return days
