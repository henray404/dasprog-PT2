from datetime import datetime, timedelta


def convert_datetime(time):
    return datetime.strptime(time, '%H:%M:%S')


event_time_gmt2 = input("input event time in GMT+2 ")
current_time_gmt7 = input('input current time in GMT+7 ')

event_time = convert_datetime(event_time_gmt2)
current_time = convert_datetime(current_time_gmt7)

event_time_gmt7 = event_time + timedelta(hours=5)

waiting_time = event_time_gmt7 - current_time

if waiting_time.total_seconds() < 0:
    print("See you on the next Pear Event!")
else:
    print(f"See you in {waiting_time}!")
