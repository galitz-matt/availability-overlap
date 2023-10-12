from datetime import time
from json_reader import DAYS_OF_THE_WEEK


def get_availability_overlap(availability):
    overlap = {}
    for day in DAYS_OF_THE_WEEK:
        day_overlap = get_availability_overlap_for_day(availability, day)
        overlap[day] = day_overlap
    return overlap


def get_availability_overlap_for_day(availability, day):
    employees = list(availability.keys())
    day_overlap = availability[employees[0]][day]
    for employee in employees[1:]:
        day_overlap = update_overlap(day_overlap, availability[employee][day])
    return day_overlap


def update_overlap(overlap: [(time, time)], employee_availability: [(time, time)]) -> [(time, time)]:
    new_overlap = []
    for availability_interval in employee_availability:
        if availability_interval == "N/A":
            return []
        new_start, new_end = availability_interval
        if new_start >= new_end:
            raise ValueError(f"Invalid time interval {new_start} - {new_end}")
        for interval in overlap:
            start, end = interval
            if new_start >= end or new_end <= start:
                continue
            else:
                new_overlap.append((max(start, new_start), min(end, new_end)))
    return new_overlap