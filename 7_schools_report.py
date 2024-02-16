"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json', 'r')

list_of_schools = json.load(infile)

#print(type(list_of_schools))

list_of_conferences = [372,108,107,130]
#determine schools with 75% graduation rate
for school in list_of_schools:
    school_conference = int(school["NCAA"]["NAIA conference number football (IC2020)"])
    if school_conference in list_of_conferences:
        women_gradrate = int(school["Graduation rate  women (DRVGR2020)"])
        if women_gradrate > 75:
            print(f'University: {school["instnm"]}\nGraduation Rate for Women: {women_gradrate}%\n')
        
                
for school in list_of_schools:
    school_conference = int(school["NCAA"]["NAIA conference number football (IC2020)"])
    if school_conference in list_of_conferences:
        total_price = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        if total_price != 'null' and total_price is not None:
            total_price = int(total_price)
            if total_price > 50000:
                print(f'University: {school["instnm"]}\nTotal price for in-state stidents living off campus: {total_price}\n')