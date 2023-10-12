import sys
import data_format
import json_reader
import json_writer
import overlap_handler

JSON_FILE_PATH_INDEX = 1


if __name__ == "__main__":
	json_file_path = sys.argv[JSON_FILE_PATH_INDEX]
	data = json_reader.get_availability(json_file_path)
	overlap = overlap_handler.get_availability_overlap(data)
	reformatted_overlap = data_format.get_reformatted_overlap(overlap)
	json_writer.write_to_json(reformatted_overlap)