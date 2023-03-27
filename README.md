# YAML Schedule to ICS Converter
This Python script converts a YAML schedule file into an ICS (iCalendar) file that can be imported into various calendar applications like Google Calendar, Microsoft Outlook, and Apple Calendar.

## Requirements
- Python 3.6 or higher
- Python libraries: pyyaml, icalendar
## Installation
- Clone the repository or download the script yaml_to_ics.py.
- Install the required libraries using pip:
    ```bash
    pip install pyyaml icalendar
    ````
## Usage
- Create a YAML file with your schedule using the provided example format. Save it with a .yaml extension (e.g., my_schedule.yaml).
- Run the script with the YAML file as the input:
```bash
python yaml_to_ics.py my_schedule.yaml
```
- The script will generate an ICS file named schedule.ics in the same directory.
- Import the schedule.ics file into your preferred calendar application.
## YAML Schedule Format
The YAML schedule file should have the following format:

```yaml
Day_name:
  HHhMM-HHhMM: Activity
```
- Replace Day_name with the name of the day in French (e.g., Lundi, Mardi, Mercredi, etc.).
- Replace HHhMM-HHhMM with the time range for the activity using 24-hour format (e.g., 06h00-07h00,