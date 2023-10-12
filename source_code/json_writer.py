import json


def write_to_json(data):
	with open("results.json", "w") as json_file:
		json.dump(data, json_file, indent=4)