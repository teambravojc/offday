from django import forms
from .models import TeamMember, OffDay

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name']
        
class OffDayForm(forms.ModelForm):
    class Meta:
        model = OffDay
        fields = ['team_member', 'day']
        widgets = {
            'day': forms.Select(choices=[
                ("Monday", "Monday"),
                ("Tuesday", "Tuesday"),
                ("Wednesday", "Wednesday"),
                ("Thursday", "Thursday"),
                ("Friday", "Friday"),
                ("Saturday", "Saturday"),
                ("Sunday", "Sunday"),
            ])
        }
