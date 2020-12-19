#!/usr/bin/env python3


import requests
import json
from bs4 import BeautifulSoup
from typing import Dict

SOURCE_URL: str = "https://emplea.do"
JOBS_URL: str = f"{SOURCE_URL}/jobs"
SAVE_PATH: str = "data/data.json"


def normalize(job_element) -> Dict[str, str]:
    try:
        year: str = job_element.findAll("li", {"class": "list-inline-item"})[
            -1
        ].text.split(" ")[-1]
        title: str = job_element.find("h5", {"class": "title"}).text
        link: str = job_element.find("a").get("href")
        description: str = (
            BeautifulSoup(requests.get(f"{SOURCE_URL}{link}").content, "html.parser")
            .find("div", {"class": "tr-single-body preserve-spaces"})
            .text
        )
        return {"year": year, "title": title, "link": link, "description": description}
    except Exception:
        return {}


def get_jobs_elements() -> list:
    page = requests.get(JOBS_URL)
    jobs_elements = BeautifulSoup(page.content, "html.parser").findAll(
        "div", {"class": "vc-content"}
    )
    return list(jobs_elements)


def save_data(file_path: str, data: str) -> None:
    with open(file_path, "w") as text_file:
        print(json.dumps(data), file=text_file)


if __name__ == "__main__":
    data = list(map(normalize, get_jobs_elements()))
    save_data(SAVE_PATH, json.dumps(data))
