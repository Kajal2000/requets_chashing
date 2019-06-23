import json
import requests
import os
url_link = "http://saral.navgurukul.org/api/courses"
def get_Url_data(link):
    url_data = requests.get(link)
    return (url_data.text)
# get_data = get_Url_data(url_link)
# print get_data

def get_Write(url_data):
    with open("courses.json","w") as file:
        file.write(url_data)
    return file
# get_Write(get_data)

def get_Read(url_data):
    with open("courses.json","r") as file:
        read_data = file.read()
        data_lode = json.loads(read_data)
    return data_lode

courses_Id_list = []
def get_Av_Courses(data_lode):
    index = 0
    while index < len(data_lode["availableCourses"]):
        available_Courses=(data_lode["availableCourses"][index])
        coursesName = available_Courses["name"]
        coursesId = available_Courses["id"]
        courses_Id_list.append(coursesId)
        print (index),coursesName,coursesId
        index = index + 1
    return courses_Id_list

if os.path.exists("courses.json"):
    getData = get_Read("courses.json")
    get_Av_Courses(getData)
    print "kkkkkkkkkkkkkkkkk"
else:
    requests(url_link)
    getData = get_Read("courses.json")
    get_Av_Courses(getData)


# user_ex = int(raw_input("enter a number"))
# userEx = courses_Id_list [user_ex - 1]
# print userEx

# exercise_url = url_link+"/"+str(userEx)+"/exercises"
# def get_exercise(link):
#     ex_data = requests.get(exercise_url)
#     return (ex_data.json())
# data_e = get_exercise(exercise_url)
# data_exer=data_e["data"]

# def ex_get_Write(ex_data,user_ex):
#     with open("ex_courses"+str(user_ex)+".json","w") as file:
#         file.write(ex_data)
#     return file
# ex_get_Write(data_e,user_ex)

# def ex_get_Read(url_data):
#     with open("ex_couurses"+str(user_ex)+".json","r") as file:
#         ex_read_data = file.read()
#         ex_data_lode = json.loads(ex_read_data)
#     return ex_data_lode
