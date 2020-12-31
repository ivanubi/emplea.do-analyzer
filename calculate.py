#!/usr/bin/env python3
import re
import json

DATA_OUTPUT_PATH: str = "data/result"
DATA_SOURCE_PATH: str = "data/source"
TECHNOLOGIES_FILE_PATH: str = f"{DATA_SOURCE_PATH}/technologies.json"
JOB_POSTS_FILE_PATH: str = f"{DATA_SOURCE_PATH}/data.json"
TECHNOLOGIES_TYPES: list = [
    "languages",
    "frontend",
    "frameworks",
    "databases",
    "clouds",
    "mobile",
]


def check_presence(technology, text: str) -> bool:
    if isinstance(technology, str):
        escaped_technology = re.escape(technology)
        return bool(re.search(rf"(^|[^a-zA-Z]){escaped_technology}([^a-zA-Z]|$)", text))

    if isinstance(technology, list):
        for name_variation in technology:
            escaped_name_variation = re.escape(name_variation)
            if re.search(rf"(^|[^a-zA-Z]){escaped_name_variation}([^a-zA-Z]|$)", text):
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


def count_technologies(technologies: list, job_posts: list):
    technologies_count: dict = {}
    for technology in technologies:
        if isinstance(technology, list):
            technologies_count[technology[0]] = count_occurrences(technology, job_posts)
        else:
            technologies_count[technology] = count_occurrences(technology, job_posts)
    return sort_dict(technologies_count, descending=True)


def count_technologies_by_year(_job_posts_by_year: dict, _technologies: list):
    _technologies_count_by_year: dict = {}
    for year, year_job_posts in _job_posts_by_year.items():
        _technologies_count_by_year[year] = {}
        _technologies_count_by_year[year] = count_technologies(
            _technologies, year_job_posts
        )
    return _technologies_count_by_year


def save_data_to_file(data: str, file_path: str):
    with open(file_path, "w") as f:
        print(data, file=f)


if __name__ == "__main__":
    print("Counting technologies, this might take a while...")
    technologies_data: dict = get_data_from_file(TECHNOLOGIES_FILE_PATH)
    job_posts: list = get_data_from_file(JOB_POSTS_FILE_PATH)
    job_posts_by_year: dict = group_job_posts_by_year(job_posts)
    for technology_type in TECHNOLOGIES_TYPES:
        technologies_count: dict = count_technologies(
            technologies_data[technology_type], job_posts
        )
        technologies_count_by_year: dict = count_technologies_by_year(
            job_posts_by_year, technologies_data[technology_type]
        )
        save_data_to_file(
            json.dumps(technologies_count),
            f"{DATA_OUTPUT_PATH}/{technology_type}_result.json",
        )
        save_data_to_file(
            json.dumps(technologies_count_by_year),
            f"{DATA_OUTPUT_PATH}/{technology_type}_by_year_result.json",
        )
    print(f"Done! Check the results at ./{DATA_OUTPUT_PATH}.")