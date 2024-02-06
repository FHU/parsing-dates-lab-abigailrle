#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    if month == 'January':
        month = '01'
    elif month == 'February':
        month = '02'
    elif month == 'March':
        month = '03'
    elif month == 'April':
        month = '04'
    elif month == 'May':
        month = '05'
    elif month == 'June':
        month = '06'
    elif month == 'July':
        month = '07'
    elif month == 'August':
        month = '08'
    elif month == 'September':
        month = '09'
    elif month == 'October':
        month = '10'
    elif month == 'November':
        month = '11'
    elif month == 'December':
        month = '12'
    else:
        month = '33'

    return month


def parse_number_date(date):
    index = date.find(',')
    date = date[0:index]
    if len(date) == 1:
        return '0' + date
    else:
        return date


#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    split_string = user_string.split()
    month = split_string[0]
    date = split_string[1]
    year = split_string[2]
    new_month = parse_month(month)
    new_date = parse_number_date(date)
    new_year = year
    print(new_month + '/' + new_date + '/' + new_year)

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    i = 0
    while i < 1:
        original_date = input('Enter a date: ')
        if original_date == '-1':
            i += 1
        else:
            parse_date(original_date)
    print('-1')
    #try new commit