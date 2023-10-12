from datetime import time
import json
import re

DAYS_OF_THE_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def get_availability(json_file_path: str) -> {str: {str: [(time, time)]}}:
	data = get_json_data(json_file_path)
	availability = {}
	employees = data.keys()
	for employee in employees:
		raw_employee_availability = data[employee]
		availability[employee] = get_employee_availability(raw_employee_availability)
	return availability


def get_json_data(json_file_path: str):
	with open(json_file_path, "r") as json_file:
		return json.load(json_file)


def get_employee_availability(raw_employee_availability):
	return {
		day: [get_interval(raw_interval) for raw_interval in raw_employee_availability[day].split(", ")]
		for day in DAYS_OF_THE_WEEK
	}


def get_interval(raw_interval):
	if raw_interval == "N/A":
		return raw_interval
	raw_start_time, raw_end_time = raw_interval.split(" - ")
	start_time = get_time_object(raw_start_time)
	end_time = get_time_object(raw_end_time)
	interval = (start_time, end_time)
	return interval


def get_time_object(raw_time):
	raw_hour, raw_minute, meridiem = re.split(r"[:\s]", raw_time)
	hour = get_nato_hour(raw_hour, meridiem)
	minute = int(raw_minute)
	return time(hour, minute)


def get_nato_hour(raw_hour, meridiem):
	hour = int(raw_hour)
	if meridiem == "PM" and hour < 12:
		hour += 12
	elif hour == "12":
		hour = 0
	return hour
