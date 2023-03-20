from datetime import datetime

# Create a string with a date
date_str = "2022-03-17 10:45:30"

date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# Print date
print(formatted_date)
