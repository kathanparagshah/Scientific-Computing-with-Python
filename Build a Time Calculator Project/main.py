def add_time(start, duration, start_day=None):
    # Parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    period = period.upper()
    
    # Convert start time to 24-hour minutes
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    if period == 'AM' and start_hour == 12:
        start_hour = 0
    start_total_minutes = start_hour * 60 + start_minute
    
    # Parse duration
    dur_hours, dur_minutes = map(int, duration.split(':'))
    duration_total_minutes = dur_hours * 60 + dur_minutes
    
    # Add duration
    end_total_minutes = start_total_minutes + duration_total_minutes
    days_passed = end_total_minutes // (24 * 60)
    end_minutes_of_day = end_total_minutes % (24 * 60)
    
    # Compute end time in hours and minutes
    end_hour_24 = end_minutes_of_day // 60
    end_minute = end_minutes_of_day % 60
    
    # Determine AM/PM
    end_period = 'AM'
    if end_hour_24 >= 12:
        end_period = 'PM'
    end_hour_12 = end_hour_24 % 12
    if end_hour_12 == 0:
        end_hour_12 = 12
    
    # Format time
    new_time = f"{end_hour_12}:{end_minute:02d} {end_period}"
    
    # Day of week calculation if given
    if start_day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_index = days.index(start_day.capitalize())
        end_index = (start_index + days_passed) % 7
        new_time += f", {days[end_index]}"
    
    # Append day indicator
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    return new_time