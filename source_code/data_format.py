from datetime import time
from json_reader import DAYS_OF_THE_WEEK

START_INDEX = 0
END_INDEX = 1
ZERO_PADDING = "0"
ANALOG_FORMAT = "%I:%M %p"


def get_reformatted_overlap(overlap: {str: [(time, time)]}):
	return {day: get_overlap_string_for_day(overlap[day]) for day in DAYS_OF_THE_WEEK}


def get_overlap_string_for_day(overlap_for_day):
	day_string = ""
	if len(overlap_for_day) == 0:
		return day_string + "N/A"
	for interval in overlap_for_day:
		day_string += f"{get_interval_string(interval)}, "
	day_string = day_string.rstrip(", ")
	return day_string


def get_interval_string(interval: (time, time)):
	start_string = get_time_string(interval[START_INDEX])
	end_string = get_time_string(interval[END_INDEX])
	return f"{start_string} - {end_string}"


def get_time_string(_time: time):
	return _time.strftime(ANALOG_FORMAT).lstrip(ZERO_PADDING)