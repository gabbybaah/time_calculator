def add_time(start, duration, day=None):

    # Splitting the strings and converting to integers
    start_parts = start.split()
    time_parts = start_parts[0].split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    meridian = start_parts[1]

    # convert to 24hour format
    if meridian == 'PM' and hours != 12:
        hours += 12
    elif meridian == 'AM' and hours == 12:
        hours = 0

    # Convert duration time to hours and minutes
    duration_parts = duration.split(':')
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    # Calculate the total number of minutes for the new_time
    total_minutes = minutes + duration_minutes
    extra_hours = total_minutes // 60
    total_minutes = total_minutes % 60

    # Calculate the total number of hours and days for the new_time
    total_hours = hours + duration_hours + extra_hours
    days_later = total_hours // 24
    total_hours = total_hours % 24

    # Convert back to 12-hour clock format
    meridian = 'AM' if total_hours < 12 else 'PM'
    new_hours = total_hours % 12
    if new_hours == 0:
        new_hours = 12

    # Format the result string
    new_time = f"{new_hours}:{total_minutes:02d} {meridian}"
    if day:
        start_day = day.capitalize()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_index = days.index(start_day)
        end_index = (start_index + days_later) % 7
        new_time += f", {days[end_index]}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time