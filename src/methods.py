from dotenv import dotenv_values
import requests
import json
import re
from twilio.rest import Client


def get_yosemite_rooms() -> int:
    url = "https://reservations.ahlsmsworld.com/Yosemite/Search/GetInventoryCountData"

    querystring = {"callback": "$.wxa.on_datepicker_general_availability_loaded", "CresPropCode": "000000",
                   "MultiPropCode": "Y", "StartDate": "Sun Jun 18 2023", "EndDate": "Sun Jun 18 2023", "_": "1678660305060"}

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
    try:
        text = json.loads(text)
        available = text["AvailableCount"]
    except:
        print("Error: " + text)
        available = 0

    return available


def get_sequoia_rooms() -> dict:
    url = "https://services-p1.synxis.com/gw/product/v1/getLeadAvailability"
    available = {}

    wuksachi_payload = {
        "Version": "1",
        "Criterion": {
            "listAllocationBlocks": True,
            "NumRooms": 1,
            "Currency": {"Code": "USD"},
            "ChannelList": {
                "PrimaryChannel": {"code": "WEB"},
                "SecondaryChannel": {"code": "GC"}
            },
            "StartDate": "2023-06-11",
            "EndDate": "2023-06-12",
            "LengthOfStay": 1,
            "LoyaltyList": [],
            "onlyCheckRequested": False,
            "AgentInfo": {},
            "AccessCode": {},
            "RoomStay": {
                "GuestCount": [
                    {
                        "ageQualifyingCode": "Adult",
                        "numGuests": 2
                    },
                    {
                        "ageQualifyingCode": "Child",
                        "numGuests": 0,
                        "Ages": []
                    }
                ],
                "RateList": [],
                "RoomList": [],
                "RateFilterList": []
            }
        },
        "HotelList": [{"id": "404"}],
        "UserDetails": {"Preferences": {"ResponseOptions": "ReturnAllocationBlocks"}},
        "Chain": {"id": "398"}
    }

    wuksachi_headers = {
        "cookie": "apisession=MDAxMjF-eHJIZVo2RldLTFQwTzJ6eDczbGEyaFBDeHMwTGU1SlhISnhDRUZaRnR0VXNhV09ESWhsTTNDaUtTS3pLSnR0K1NhK01PdWRneTdPb2UwWmJRZTNCajkyTGlIYXJCL2pEclpwZktMWHVxYmhvbVNNa2FkQ0xrMjdKSEFsOGxGNHdOOFozS0lDNnVXeFlsSW4vVnkwK1VxLzJNUHhJcWRHeitUV2wwUHhTOUswZWF2OGFzTVQxcnd5TjlDVFcvZUhUa0UxcUFiRzdJNnQ3QTArWW5ZMFM4U3kvS2Q0RjlmSWd6UFJNVG4rSXZkWT0; visid_incap_2695530=VTdbpQ%2BhTweMjOBH5rZpKjV1NGQAAAAAQUIPAAAAAABgxu1PmB%2BNaQF1uPwuHGIT; incap_ses_891_2695530=tvLSbgm%2Br2yDSl61pHhdDDV1NGQAAAAA5lVXEIuN8pNxS11Eq4LLiA%3D%3D",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "ApiKey MDAxMjF+dVNKZlBxNkNpazBlb2Q5SkEwL0xmYU9DMFdSVzZxUW5sNnpCQkhNR3RhZVVVVkFRYzFOazdDQlhKa0xGRFZBTWVtUVFXdkFEcThkNjVoUVB2Wjd4dHc9PQ==",
        "Content-Type": "application/json",
        "Origin": "https://be.synxis.com",
        "Referer": "https://be.synxis.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "activityid": "YpfHclIXpf"
    }

    wuksachi_response = requests.request(
        "POST", url, json=wuksachi_payload, headers=wuksachi_headers)

    try:
        text = json.loads(wuksachi_response.text)
        available["wuksachi"] = text["LeadAvailabilityList"][0]["Available"]
    except:
        print("Error: " + wuksachi_response.text)
        available["wuksachi"] = False

    john_muir_payload = {
        "Version": "1",
        "Criterion": {
            "listAllocationBlocks": True,
            "NumRooms": 1,
            "Currency": {"Code": "USD"},
            "ChannelList": {
                "PrimaryChannel": {"code": "WEB"},
                "SecondaryChannel": {"code": "GC"}
            },
            "StartDate": "2023-06-01",
            "EndDate": "2023-07-31",
            "LengthOfStay": 1,
            "LoyaltyList": [],
            "onlyCheckRequested": False,
            "AgentInfo": {},
            "AccessCode": {},
            "RoomStay": {
                "GuestCount": [
                    {
                        "ageQualifyingCode": "Adult",
                        "numGuests": 2
                    },
                    {
                        "ageQualifyingCode": "Child",
                        "numGuests": 0,
                        "Ages": []
                    }
                ],
                "RateList": [],
                "RoomList": [],
                "RateFilterList": []
            }
        },
        "HotelList": [{"id": "59989"}],
        "UserDetails": {"Preferences": {"ResponseOptions": "ReturnAllocationBlocks"}},
        "Chain": {"id": "398"}
    }

    john_muir_headers = {
        "cookie": "apisession=MDAxMjF-RkNMTGY2RjFMUGViYkVWL1NwRzZCOTNBY25hQkUzR3V5UFlmSVhZcjVGaFVicDEzRzZBS20zeVUwSytTQ3JxUWVHTTdlTW9MUGpJRjhaVHZUSVVoKzhucGNWVWZQbVJqTXZCT1UxK2M2SHBkZTRveitzRUVRV09nTEozK3l4UDlLNy9jd2J2d05Qc0lERWVXTHUvNkFzVE81SUxKcjZRc3RmUWh4amN5SVBSVW9yUE1SOTFWaUVJUXN5MUc4S1ZKSjZGYURPeHBHZVYvMGZyaVNySGx1Qi94L2JRTGt5ZWNaOFJha0JlcmFWcz0; visid_incap_2695530=VTdbpQ%2BhTweMjOBH5rZpKjV1NGQAAAAAQUIPAAAAAABgxu1PmB%2BNaQF1uPwuHGIT; incap_ses_891_2695530=tvLSbgm%2Br2yDSl61pHhdDDV1NGQAAAAA5lVXEIuN8pNxS11Eq4LLiA%3D%3D",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "ApiKey MDAxMjF+dVNKZlBxNkNpazBlb2Q5SkEwL0xmYU9DMFdSVzZxUW5sNnpCQkhNR3RhZVVVVkFRYzFOazdDQlhKa0xGRFZBTWVtUVFXdkFEcThkNjVoUVB2Wjd4dHc9PQ==",
        "Content-Type": "application/json",
        "Origin": "https://be.synxis.com",
        "Referer": "https://be.synxis.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "activityid": "shsfClnAwQ"
    }

    john_muir_response = requests.request(
        "POST", url, json=john_muir_payload, headers=john_muir_headers)
    try:
        text = json.loads(john_muir_response.text)
        available["john_muir"] = text["LeadAvailabilityList"][0]["Available"]
    except:
        print("Error: " + john_muir_response.text)
        available["john_muir"] = False

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
