student = {"name": 'Ethan Poncho',
           "age": '21',
           "major": 'MIS',
           "hobbies": ['Reading', 'Baseball', 'Golf']}

student['state'] = 'Texas'
student['age'] = '22'

for key in student:
    print(f"Name: {student['name']}\n Age: {student['age']}\n Major: {student['major']}\n Hobbies: {student['hobbies']}\n State of Residence: {student[state]}")
    