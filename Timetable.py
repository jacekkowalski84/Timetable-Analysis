FILEPATH = "track.csv"

import csv
from typing import Dict

class Entry:
    def __init__(self, time: int, tag: str):
        self.time  = time
        self.tag = tag

    def __str__(self):
        return (f"{self.time:10} {self.tag}")

def data_csv_to_dict (filepath: str) -> list[dict]:
    with open (filepath) as stream:
        record = csv.DictReader (stream)
        tasks = [ row for row in record]
        return tasks


def time_tag_list_extraction (tasks: list[dict]) -> list[list]:
    time_tag_list = [
                [int(dict["time"]), tag] 
                for dict in tasks
                for tag in dict["tags"].split()
                ]
    return time_tag_list


def unique_tags_extraction (elements: list) -> set:
    tags_set = [e[1] for e in elements]
    return set(tags_set)


def Entry_element (unique_tag, time_tag_list):
    return Entry(
                tag=unique_tag,
                time = sum(
                        [tt[0] 
                        for tt in time_tag_list
                        if tt[1] == unique_tag]
                        )
                )

def print_raport(unique_tags: set, time_tag_list: list[list]):        
    print ("TOTAL TIME   TAG")
    for ut in unique_tags:
        print (Entry_element(ut, time_tag_list))

def main(filepath: str)-> None:
    tasks = data_csv_to_dict (filepath)
    time_tag_list = time_tag_list_extraction(tasks)
    unique_tags = unique_tags_extraction(time_tag_list)
    print_raport (unique_tags, time_tag_list)


if __name__ == "__main__":
    main(FILEPATH)