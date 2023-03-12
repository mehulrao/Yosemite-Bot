from dotenv import dotenv_values
import requests
import json
import re
from twilio.rest import Client


def get_available_rooms():
    url = "https://reservations.ahlsmsworld.com/Yosemite/Search/GetInventoryCountData"

    querystring = {"callback": "$.wxa.on_datepicker_general_availability_loaded", "CresPropCode": "000000",
                   "MultiPropCode": "Y", "StartDate": "Mon Jun 19 2023", "EndDate": "Mon Jun 19 2023", "_": "1678660305060"}

    payload = ""
    headers = {
        "cookie": "ASP.NET_SessionId=0nc1ub4aqsawsxvxmrm3yo2e",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

    response = requests.request(
        "GET", url, data=payload, headers=headers, params=querystring)

    regex = "\{(.*?)\}"
    text = re.search(regex, response.text).group(0)
    text = json.loads(text)

    available = text["AvailableCount"]
    return available


def send_sms(body):
    config = dotenv_values(".env")
    account_sid = config["TWILIO_ACCOUNT_SID"]
    auth_token = config["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=config["TWILIO_FROM_NUMBER"],
        to=config["TWILIO_TO_NUMBER"],
        body=body,
    )
    return message
