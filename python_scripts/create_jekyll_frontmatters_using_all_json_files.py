# Author: E/18/227 Dinuka Mudalige - e18227@eng.pdn.ac.lk

import os
import json # to get data from _data/courses/semester#.json
# import requests

i = 0
if __name__ == "__main__":

    print("Extracting data in _data/courses/semester#.json files to create jekyll frontmatters...")
    
    for i in range(1, 9):
        # select student from json file

        # jsonPath = f"../_data/courses/semester1.json"
        jsonPath = f"_data/courses/semester{i}.json"
        dataInJSON = json.load(open(jsonPath))

        for thisCourse in dataInJSON:
            # print(thisCourse)
            course_code = thisCourse["code"]
            # course_title = thisCourse["name"]
            # course_credits = thisCourse["credits"]
            # core_or_elective = thisCourse["core/elective"]
            # prerequisties = thisCourse["prerequisites"]
            # ilos_knowledge = thisCourse["ILOs"]["Knowledge"]
            # ilos_skill = thisCourse["ILOs"]["Skill"]
            # ilos_attitude = thisCourse["ILOs"]["Attitude"]
            # textbooks_references = thisCourse["references"]
            
            outputString = f"""---
layout: courses
permalink: "/courses/semester1/{thisCourse["code"].lower()}/"
title: {thisCourse["name"]}

course_number : {thisCourse["code"].upper()} 
course_title : {thisCourse["name"]}
credits : {thisCourse["credits"]}
core_or_elective : {thisCourse["core/elective"]} 
prerequisites : {thisCourse["prerequisites"]}
ilos_knowledge : {thisCourse["ILOs"]["Knowledge"]}
ilos_skill : {thisCourse["ILOs"]["Skill"]}
ilos_attitude : {thisCourse["ILOs"]["Attitude"]}
textbooks_references : {thisCourse["references"]}
---"""
            # print(outputString)

            # # write to html file (jekyll frontmatter)
            # # file_url = "../"+f"pages/courses/semester1/{course_code.lower()}.html"
            # file_url = f"pages/courses/semester1/{course_code.lower()}.html"
            # os.makedirs(os.path.dirname(file_url), exist_ok=True)
            # htmlFile = open(file_url, "w")
            # htmlFile.write(outputString)
            # htmlFile.close()
            # print("Create or Update file: " + course_code.lower() + ".html")
            # print("---------------------------------")
