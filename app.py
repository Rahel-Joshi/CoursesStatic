# app.py
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_html(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        print("Error fetching URL:", url, e)
    return ""

def parse_catalog_courses(url):
    html = fetch_html(url)
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    # Minimal parsing: adjust selectors based on actual page structure.
    courses = []
    for div in soup.find_all("div", class_="course"):
        course = {
            "course_label": div.find("span", class_="label").get_text().strip() if div.find("span", class_="label") else "",
            "course_title": div.find("span", class_="title").get_text().strip() if div.find("span", class_="title") else "",
            "units_term": div.find("span", class_="units").get_text().strip() if div.find("span", class_="units") else "",
            "prerequisites": div.find("span", class_="prereq").get_text().strip() if div.find("span", class_="prereq") else "",
            "instructors": div.find("span", class_="instructors").get_text().strip() if div.find("span", class_="instructors") else "",
            "description": div.find("span", class_="description").get_text().strip() if div.find("span", class_="description") else ""
        }
        courses.append(course)
    return courses

def parse_option_requirements(url):
    html = fetch_html(url)
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find("div", class_="content")
    if content_div:
        return content_div.get_text(separator="\n").strip()
    return soup.get_text(separator="\n").strip()
