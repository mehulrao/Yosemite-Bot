from methods import *
from time import sleep

count = 0
total_count = 0

send_sms("Starting script...")

while get_available_rooms() <= 0:
    print("Not available")
    sleep(60)
    if count == 1440:
        message_fail = send_sms("No rooms available for the past 24 hours...")
        print(message_fail)
        count = 0
    count += 1
    total_count += 1


message_text = "There are " + str(get_available_rooms()) + " rooms available!"
message_success = send_sms(message_text)
success_text = "SUCCESS!! " + "Total checks: " + str(total_count)
send_sms(success_text)
print(success_text)
