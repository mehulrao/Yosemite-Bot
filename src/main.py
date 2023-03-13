from methods import *
from time import sleep

count = 0
total_count = 0

send_sms("Starting script...")

while True:
    if get_available_rooms() <= 0:
        print("Not available")
        if count == 72:
            message_fail_text = "No rooms available for the past 24 hours... Current availablity: " + \
                str(get_available_rooms())
            message_fail = send_sms(message_fail_text)
            print(message_fail)
            count = 0
        count += 1
    else:
        message_text = "There are " + \
            str(get_available_rooms()) + " rooms available!"
        message_success = send_sms(message_text)
        success_text = "SUCCESS!! " + "Total checks: " + str(total_count)
        send_sms(success_text)
        print(success_text)

    total_count += 1
    sleep(1200)
