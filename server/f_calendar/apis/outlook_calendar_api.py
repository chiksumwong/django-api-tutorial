import json

import requests


def list_calendars(access_token):
    url = 'https://graph.microsoft.com/v1.0/me/calendars'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    r = requests.get(url, headers=headers)
    return r.json()


def create_calendars(access_token):
    url = 'https://graph.microsoft.com/v1.0/me/calendars'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    data = {
        'name': 'Volunteer2'
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def delete_calendars(access_token):
    calendar_id = 'AQMkADAwATM3ZmYAZS0xMQA0MS0zNWYyLTAwAi0wMAoARgAAA_SpH_BJYLZIic0_qb37wQYHABMvTQHDI9hCkrZvJXgAxRoAAAIBBgAAABMvTQHDI9hCkrZvJXgAxRoAAfejjMYAAAA='
    url = 'https://graph.microsoft.com/v1.0/me/calendars/' + calendar_id
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    r = requests.delete(url, headers=headers)
    return r


def create_event(access_token):
    calendar_id = 'AQMkADAwATM3ZmYAZS0xMQA0MS0zNWYyLTAwAi0wMAoARgAAA_SpH_BJYLZIic0_qb37wQYHABMvTQHDI9hCkrZvJXgAxRoAAAIBBgAAABMvTQHDI9hCkrZvJXgAxRoAAfejjMUAAAA='
    url = "https://graph.microsoft.com/v1.0/me/calendars/"+calendar_id+"/events"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    data = {
        "subject": "Let's go for lunch",
        "body": {
            "contentType": "HTML",
            "content": "Does mid month work for you?"
        },
        "start": {
            "dateTime": "2020-07-01T12:00:00",
            "timeZone": "Pacific Standard Time"
        },
        "end": {
            "dateTime": "2020-07-01T14:00:00",
            "timeZone": "Pacific Standard Time"
        },
        "location": {
            "displayName": "Harry's Bar"
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


if __name__ == '__main__':
    input_access_token = "EwBwA8l6BAAUO9chh8cJscQLmU LSWpbnr0vmwwAAVnhM6v5GrYoTB7Oiqd12vn2USeoRy5hYFLZHN6oRduJrAHFftXqWTBhnbt9Jh0gI9pcbDvJETjhAmk 6HmEZX/rK6cUDvDnkznTNonFnmGDF3uDQYGdeMJPaMpBS/uaQD5fC6FGGJiZO3iqYR2YkVICFiNM0XTO6NCLx I82eLhxHS7AzneL1drdLVBXABkKgsh8dqgNZYoNQIv2xk i1EU/Dqa3fb25FNJs6Nb vbaMWuRVO1XvPHKic N88gEtXQml8DLrM8hRVz6LvxfqCSoasgil8XIXjSA1UPZEKzYYbXEohlfM8j36/YRk7QkKj6NhCrnnxcaWZpCyV9CFREDZgAACIEIDWgRQ0mrQAJmOIqBhskySrECuikqatnQu/WoHvDLBFceAx5/dvJTpXr0/XNjZxcTsiWdDUNZ1sObC1O/fOY 0iNV/VXIPGViS9nouQC1hLtUPrxX5 KR2EhuhMBe8fPLjbF5f5u69AUdPg4kilvsppY6XH7Gu3f XTu5lJCWRwTCJyyfrKyVecG7tJP5a79ms5PAutuYpSujCY574LTNzdIKAyc3MsryuIvWMo6ROKsm0fABvCM2 wrmxj MYod5dC3ZX8swAOdtE6kQBEZTDh6T9w3WkOJ8HwdTRb7PhCCaK/V1hf8eKKTPv5uTeqYHUMorGsTR1x6SgBZoCYLvTXZRr/ hUkc06AYbWteyk37jOAGpMWaCUkraTncHZRBBhRsKUCQemHketK6Vww4o325D6gyh1 zx7BIv0XPkycD7S8dmqp61dLYa05zfJgoGqbkJg0t5YpMB3wG4pbyacfXQbfoRIFr61C9BwbENXyGE JADEa8Lff QGM/V31y8OChK297djsflHRLzodU m Z6IxwGeme3KUHY6wlptHgr5bByofVIhX2NxVWmj1J8 VIF8Ix1/iP5m1g8KFkds7b5rLqYcVvQo22y/A86DWl0b4AyVKTUHb6kYPLcQ4OYALCOo/7zBdymrjY7r7FZ30PLPXVBCF1MTjDTw/qhqCia2UVEI3DXsDyf1mx/Cl5sEHfRnPsh/1u4KkxRtDKNdFbB ZYCWnWmShvPhLGSQJp0dXH5FoEWk1heuwz3TUwSuxki0SC4icuFAg=="
    # print(list_calendars(input_access_token))
    # print(create_calendars(input_access_token))
    # print(delete_calendars(input_access_token))
    print(create_event(input_access_token))
