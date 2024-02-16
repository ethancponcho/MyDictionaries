student = {"name": 'Ethan Poncho',
           "age": '21',
           "major": 'MIS',
           "hobbies": ['Reading', 'Baseball', 'Golf']}

student['state'] = 'Texas'
student['age'] = '22'

for k, v in student.items():
    print(f'{k}: {v}')
#print(f"Name: {student['name']}\nAge: {student['age']}\nMajor: {student['major']}\nHobbies: {student['hobbies']}\nState of Residence: {student['state']}")
    