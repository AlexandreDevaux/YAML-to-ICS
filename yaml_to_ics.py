import yaml
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import argparse

def generate_event(summary, start_time, end_time):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    return event

def day_name_to_weekday(day_name):
    mapping = {
        "Lundi": 0,
        "Mardi": 1,
        "Mercredi": 2,
        "Jeudi": 3,
        "Vendredi": 4,
        "Samedi": 5,
        "Dimanche": 6,
    }
    return mapping[day_name]

def yaml_to_ics(yaml_string, nb_weeks):
    yaml_data = yaml.load(yaml_string, Loader=yaml.SafeLoader)
    cal = Calendar()

    # Customize this date as needed
    start_date = datetime(2023, 4, 10)
    # Customize this number as needed
    num_weeks = nb_weeks
    for week in range(num_weeks):
        for day, schedule in yaml_data.items():
            current_date = start_date + timedelta(weeks=week)
            while current_date.weekday() != day_name_to_weekday(day):
                current_date += timedelta(days=1)

            for time_range, activity in schedule.items():
                start_time_str, end_time_str = time_range.split('-')
                start_time = datetime.strptime(start_time_str, '%Hh%M').time()
                end_time = datetime.strptime(end_time_str, '%Hh%M').time()
                start_datetime = current_date.replace(hour=start_time.hour, minute=start_time.minute)
                end_datetime = current_date.replace(hour=end_time.hour, minute=end_time.minute)

                summary = activity
                event = generate_event(summary, start_datetime, end_datetime)
                cal.add_component(event)

            # Save the calendar to an ICS file
        with open('schedule.ics', 'wb') as ics_file:
            ics_file.write(cal.to_ical())

def main(input_file, nb_weeks=1):
    with open(input_file, 'r', encoding='utf-8') as file:
        yaml_string = file.read()
    yaml_to_ics(yaml_string, nb_weeks)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a YAML schedule file to an ICS file.')
    parser.add_argument('input_file', help='Path to the YAML schedule file.')
    parser.add_argument('--nb_weeks', type=int, default=1, help='Number of weeks to generate.')

    args = parser.parse_args()
    main(args.input_file)
