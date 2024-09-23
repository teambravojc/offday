from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from .models import TeamMember, OffDay
from .forms import TeamMemberForm, OffDayForm

def offdayapp(request):
    team_members = TeamMember.objects.all()
    
    # Prepare team schedule and off days for each member
    team_schedule = []
    for member in team_members:
        off_days = OffDay.objects.filter(team_member=member).values_list('day', flat=True)
        team_schedule.append({
            'member': member,
            'off_days': list(off_days)
        })
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Initialize the forms
    form = TeamMemberForm()
    off_day_form = OffDayForm()  # Always initialize the off day form here

    if request.method == 'POST':
        print("POST request received")  # Debugging
        
        # Handle adding a member
        if 'add_member' in request.POST:
            print("Add member action triggered")  # Debugging
            form = TeamMemberForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('offdayapp')
        
        # Handle submitting an off day
        elif 'submit_off_day' in request.POST:
            print("Submit off day action triggered")  # Debugging
            off_day_form = OffDayForm(request.POST)  # Reinitialize with POST data
            if off_day_form.is_valid():
                team_member = off_day_form.cleaned_data['team_member']
                current_off_days_count = OffDay.objects.filter(team_member=team_member).count()
                
                # Validate that each member can have at most 2 off days
                if current_off_days_count >= 2:
                    off_day_form.add_error(None, "Each member can only have 2 off days.")
                else:
                    selected_day = off_day_form.cleaned_data['day']
                    weekday_limit = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                    weekend_limit = ["Saturday", "Sunday"]

                    # Validate that no more than 4 members can be off on weekdays
                    if selected_day in weekday_limit:
                        if OffDay.objects.filter(day=selected_day).count() >= 4:
                            off_day_form.add_error('day', "Only 4 members can be off on weekdays (Mon-Fri).")
                        else:
                            off_day_form.save()
                            return redirect('offdayapp')
                    
                    # Validate that no more than 3 members can be off on weekends
                    elif selected_day in weekend_limit:
                        if OffDay.objects.filter(day=selected_day).count() >= 3:
                            off_day_form.add_error('day', "Only 3 members can be off on weekends (Sat-Sun).")
                        else:
                            off_day_form.save()
                            return redirect('offdayapp')

        # Handle deleting a member
        elif 'delete_member' in request.POST:
            print("Delete member action triggered")  # Debugging
            member_id = request.POST.get('member_id')
            member_to_delete = get_object_or_404(TeamMember, id=member_id)
            member_to_delete.delete()
            return redirect('offdayapp')

    return render(request, 'home.html', {
        'team_members': team_members,
        'team_schedule': team_schedule,
        'days_of_week': days_of_week,
        'form': form,
        'off_day_form': off_day_form,
    })
