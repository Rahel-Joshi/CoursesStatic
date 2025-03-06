# build_kb_offline.py
import json
from semantic_search import embed_text, extract_course_numbers
from db_setup import option_links
from app import parse_catalog_courses, parse_option_requirements

FALLBACK_CS38_PREREQS = "CS 2; Ma/CS 6 a or Ma 121 a; and CS 21."

all_records = []

for code, urls in option_links.items():
    cat_url = urls.get("catalog")
    req_url = urls.get("requirements")
    if cat_url:
        courses_data = parse_catalog_courses(cat_url)
        for i, course in enumerate(courses_data):
            text_parts = []
            if course.get("course_label"):
                text_parts.append(f"Label: {course['course_label']}")
            if course.get("course_title"):
                text_parts.append(f"Title: {course['course_title']}")
            if course.get("units_term"):
                text_parts.append(f"Units/Term: {course['units_term']}")
            if course.get("prerequisites"):
                prereq = course["prerequisites"]
                if prereq.lower().startswith("prerequisites:"):
                    prereq = prereq[len("prerequisites:"):].strip()
                text_parts.append(f"Prerequisites: {prereq}")
            if course.get("instructors"):
                instr = course["instructors"]
                if instr.lower().startswith("instructors:"):
                    instr = instr[len("instructors:"):].strip()
                text_parts.append(f"Instructors: {instr}")
            if course.get("description"):
                text_parts.append(f"Description: {course['description']}")
            final_text = " | ".join(text_parts)
            record = {
                "id": f"{code}_course_{i}",
                "text": final_text,
                "metadata": {
                    "option": code,
                    "type": "course",
                    "source_url": cat_url,
                    "course_label": course.get("course_label", ""),
                    "course_title": course.get("course_title", ""),
                    "units_term": course.get("units_term", ""),
                    "prerequisites": course.get("prerequisites", ""),
                    "instructors": course.get("instructors", ""),
                    "description": course.get("description", "")
                },
                "embedding": embed_text(final_text).tolist()
            }
            all_records.append(record)

            # Create a duplicate record for CS 38 if applicable
            if "cs 138" in course.get("course_label", "").lower():
                duplicate_course = course.copy()
                duplicate_course["course_label"] = "CS 38"
                duplicate_course["course_title"] = duplicate_course.get("course_title", "").replace("Computer Algorithms", "Algorithms")
                if not duplicate_course.get("prerequisites", "").strip():
                    duplicate_course["prerequisites"] = FALLBACK_CS38_PREREQS
                dup_text_parts = []
                if duplicate_course.get("course_label"):
                    dup_text_parts.append(f"Label: {duplicate_course['course_label']}")
                if duplicate_course.get("course_title"):
                    dup_text_parts.append(f"Title: {duplicate_course['course_title']}")
                if duplicate_course.get("units_term"):
                    dup_text_parts.append(f"Units/Term: {duplicate_course['units_term']}")
                if duplicate_course.get("prerequisites"):
                    dup_text_parts.append(f"Prerequisites: {duplicate_course['prerequisites']}")
                if duplicate_course.get("instructors"):
                    dup_instr = duplicate_course["instructors"]
                    if dup_instr.lower().startswith("instructors:"):
                        dup_instr = dup_instr[len("instructors:"):].strip()
                    dup_text_parts.append(f"Instructors: {dup_instr}")
                if duplicate_course.get("description"):
                    dup_text_parts.append(f"Description: {duplicate_course['description']}")
                dup_final_text = " | ".join(dup_text_parts)
                duplicate_record = {
                    "id": f"{code}_course_{i}_cs38",
                    "text": dup_final_text,
                    "metadata": {
                        "option": code,
                        "type": "course",
                        "source_url": cat_url,
                        "course_label": duplicate_course.get("course_label", ""),
                        "course_title": duplicate_course.get("course_title", ""),
                        "units_term": duplicate_course.get("units_term", ""),
                        "prerequisites": duplicate_course.get("prerequisites", ""),
                        "instructors": duplicate_course.get("instructors", ""),
                        "description": duplicate_course.get("description", "")
                    },
                    "embedding": embed_text(dup_final_text).tolist()
                }
                all_records.append(duplicate_record)

    if req_url:
        req_text = parse_option_requirements(req_url)
        if req_text:
            record = {
                "id": f"{code}_requirements",
                "text": req_text,
                "metadata": {"option": code, "type": "requirements", "source_url": req_url},
                "embedding": embed_text(req_text).tolist()
            }
            all_records.append(record)

with open("cached_courses.json", "w") as f:
    json.dump(all_records, f, indent=4)
print("Cached knowledge base with", len(all_records), "records.")
