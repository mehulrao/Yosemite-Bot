from methods import *
from time import sleep

yosemite_count = 0
sequoia_count = 0
total_count = 0

yosemite_rooms = get_yosemite_rooms()
sequoia_rooms = get_sequoia_rooms()
wuksachi_text = ""
john_muir_text = ""
if sequoia_rooms["wuksachi"] == True:
    wuksachi_text = "Wuksachi is available"
else:
    wuksachi_text = "Wuksachi is not available"
if sequoia_rooms["john_muir"] == True:
    john_muir_text = "John Muir is available"
else:
    john_muir_text = "John Muir is not available"

start_text = "Starting script... Number of Rooms in Yosemite: " + \
    str(yosemite_rooms) + " " + wuksachi_text + " " + john_muir_text

send_sms(start_text)

while True:
    yosemite_rooms = get_yosemite_rooms()
    sequoia_rooms = get_sequoia_rooms()
    # --- Yosemite ---
    if yosemite_rooms <= 0:
        print("Yosemite Not available")
        if count == 72:
            message_fail_text = "No Yosemite rooms available for the past 24 hours... Current availablity: " + \
                str(yosemite_rooms)
            message_fail = send_sms(message_fail_text)
            print(message_fail)
            count = 0
        count += 1
    else:
        message_text = "There are " + \
            str(yosemite_rooms) + " rooms available!"
        message_success = send_sms(message_text)
        success_text = "YOSEMITE SUCCESS!! " + \
            "Total checks: " + str(total_count)
        send_sms(success_text)
        print(success_text)
        count = 0
    # --- Sequoia ---
    if sequoia_rooms["wuksachi"] == False and sequoia_rooms["john_muir"] == False:
        print("Sequoia Not available")
        if count == 72:
            message_fail_text = "No Sequoia rooms available for the past 24 hours..."
            message_fail = send_sms(message_fail_text)
            print(message_fail)
            count = 0
    else:
        message_text = ""
        wuksachi_text = ""
        john_muir_text = ""
        if sequoia_rooms["wuksachi"] == True:
            wuksachi_text = "Wuksachi is available"
        else:
            wuksachi_text = "Wuksachi is not available"
        if sequoia_rooms["john_muir"] == True:
            john_muir_text = "John Muir is available"
        else:
            john_muir_text = "John Muir is not available"
        message_text = wuksachi_text + " and " + john_muir_text
        message_text.strip()
        message_success = send_sms(message_text)
        success_text = "SEQUIOA SUCCESS!! " + \
            "Total checks: " + str(total_count)
        send_sms(success_text)
        print(success_text)
        count = 0

    total_count += 1
    sleep(1200)
