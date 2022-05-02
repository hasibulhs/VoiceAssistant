import datetime
import calendar


def today_date():  # for date and time
    now = datetime.datetime.now()  # returns year, month, date, hours and second
    date_now = datetime.datetime.today()  # returns present date and time
    week_now = calendar.day_name[date_now.weekday()]  # returns day of the week
    month_now = now.month  # returns current month
    day_now = now.day  # returns current date

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21th",
        "22th",
        "23th",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return f'Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.'  # month and day starts from 0 in python, that's why we are subtracing 1
