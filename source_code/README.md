# JSON Availability Overlap

## To-Run
1) Open a CLI
2) Change location so that ```find_overlap``` is your working directory
3) Enter the command: ```./main.exe [formatted JSON file (see "JSON File Format")]```
4) Executable will create a JSON file, ```results.json``` (this contains the overlap between availability)

## JSON File Format
* Each key-value pair is the employee name mapped to an object
    * ex. ```"Joe": {...}```
* Each object contains key-value pairs mapping the days of the week to the respective availability for that day
    * ex. ```"Monday": "1:00 PM - 2:00 PM"```
* Several intervals are separated by the ", " delimiter.
    * ex. ```"1:00 PM - 2:00 PM, 3:30 PM - 5:00 PM"```
* If there is no availability for a day it is denoted by ```"N/A"```
    * ex. ```"Tuesday": "N/A"```

Below is an example of a JSON file with the correct format:

```
{
  "Employee_1": {
    "Monday": "1:00 PM - 2:00 PM, 3:30 PM - 5:00 PM"
    "Tuesday": "N/A"
    "Wednesday": "1:00 PM - 2:00 PM, 2:30 PM - 5:00 PM",
    "Thursday": "8:00 AM - 2:00 PM, 4:30 PM - 7:00 PM",
    "Friday": "9:30 AM - 12:00 PM"
  },

  "Employee_2": {
    "Monday": "1:30 PM - 4:00 PM",
    "Tuesday": "1:00 PM - 2:00 PM, 2:30 PM - 5:00 PM",
    "Wednesday": "N/A",
    "Thursday": "1:00 PM - 5:00 PM"
    "Friday": "N/A"
  }
}
```
