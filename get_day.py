# Accept date from user and show what day of week 

from datetime import datetime

date = input("Enter date format dd mm yyyy : ")

# List of day names of week 
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

# Get number of day on that day
day_num = datetime.strptime(date, '%d %m %Y').weekday()

day = week[day_num]
print('Day on ',date,' is: ', day)
