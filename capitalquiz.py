capitals = {'Alabama':'Montgomery',
            'Alaska':'Juneau',
            'Arizona':'Phoenix',
            'Arkansas':'Little Rock',
            'California':'Sacramento',
            'Colorado':'Denver',
            'Connecticut':'Hartford',
            'Delaware':'Dover',
            'Florida':'Tallahassee',
            'Georgia':'Atlanta',
            'Hawaii':'Honolulu',
            'Idaho':'Boise',
            'Illinios':'Springfield',
            'Indiana':'Indianapolis',
            'Iowa':'Des Monies',
            'Kansas':'Topeka',
            'Kentucky':'Frankfort',
            'Louisiana':'Baton Rouge',
            'Maine':'Augusta',
            'Maryland':'Annapolis',
            'Massachusetts':'Boston',
            'Michigan':'Lansing',
            'Minnesota':'St. Paul',
            'Mississippi':'Jackson',
            'Missouri':'Jefferson City',
            'Montana':'Helena',
            'Nebraska':'Lincoln',
            'Neveda':'Carson City',
            'New Hampshire':'Concord',
            'New Jersey':'Trenton',
            'New Mexico':'Santa Fe',
            'New York':'Albany',
            'North Carolina':'Raleigh',
            'North Dakota':'Bismarck',
            'Ohio':'Columbus',
            'Oklahoma':'Oklahoma City',
            'Oregon':'Salem',
            'Pennsylvania':'Harrisburg',
            'Rhoda Island':'Providence',
            'South Carolina':'Columbia',
            'South Dakoda':'Pierre',
            'Tennessee':'Nashville',
            'Texas':'Austin',
            'Utah':'Salt Lake City',
            'Vermont':'Montpelier',
            'Virginia':'Richmond',
            'Washington':'Olympia',
            'West Virginia':'Charleston',
            'Wisconsin':'Madison',
            'Wyoming':'Cheyenne'}

right = 0
wrong = 0

for capital in capitals:
    question = str(input("What is the capital of " + capital + "? "))
    
    if question == capitals[capital]:
        right = right + 1
    else:
        wrong = wrong + 1
        
print("You got " + str(right) + " right.")
print("You got " + str(wrong) + " wrong.")
