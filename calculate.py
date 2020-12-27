#!/usr/bin/env python3
import re
import json

DATA_PATH: str = "data"


def check_presence(technology, text: str) -> bool:
    if isinstance(technology, str):
        escaped_technology = re.escape(technology)
        return bool(re.search(rf"(^|[^a-zA-Z]){escaped_technology}([^a-zA-Z]|$)", text))

    if isinstance(technology, list):
        for name_variation in technology:
            name_variation_escaped = re.escape(name_variation)
            if re.search(rf"(^|[^a-zA-Z]){name_variation_escaped}([^a-zA-Z]|$)", text):
                return True
        return False
    return False


def count_occurrences(technology, job_posts: list) -> int:
    count: int = 0
    for job_post in job_posts:
        if (
            job_post != {}
            and job_post["title"]
            and job_post["description"]
            and (
                (check_presence(technology, job_post["title"].lower()))
                or (check_presence(technology, job_post["description"].lower()))
            )
        ):
            count += 1
    return count


def sort_dict(dictionary: dict, descending: bool = False) -> dict:
    return dict(
        sorted(dictionary.items(), key=lambda item: item[1], reverse=descending)
    )


def get_data_from_file(file_path: str):
    with open(file_path) as data_file:
        return json.load(data_file)


def group_job_posts_by_year(job_posts: list) -> dict:
    job_posts_by_year = {}
    for job_post in job_posts:
        if job_post and not job_post["year"] in job_posts_by_year:
            job_posts_by_year[job_post["year"]] = []
        job_posts_by_year[job_post["year"]].append(job_post)
    return job_posts_by_year


if __name__ == "__main__":

    technologies_data: dict = get_data_from_file(f"{DATA_PATH}/technologies.json")
    job_posts: list = get_data_from_file(f"{DATA_PATH}/data.json")
    job_posts_by_year: dict = group_job_posts_by_year(job_posts)
    technologies_count: dict = {}

    for technology in technologies_data["clouds"]:
        if isinstance(technology, list):
            technologies_count[technology[0]] = count_occurrences(technology, job_posts)
        else:
            technologies_count[technology] = count_occurrences(technology, job_posts)
    # print(sort_dict(new_dict, descending=True))
