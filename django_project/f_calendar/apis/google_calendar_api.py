import json

import requests


def get_calendar_setting(access_token):
    url = 'https://www.googleapis.com/calendar/v3/users/me/settings'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    r = requests.get(url, headers=headers)
    print('Get Google Calendar: ', r.json())
    return r.json()


def create_event(access_token, calendar_id):
    url = 'https://www.googleapis.com/calendar/v3/calendars/' + calendar_id + '/events'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    data = {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2020-05-12T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2020-05-12T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


if __name__ == '__main__':
    input_access_token = 'ya29.a0AfH6SMBzkJvkClx_ArE9DfXHfaLORR0UyvlwXuXh6Q09eoOPFbJMhCc8TCLJxz-_1L653-94OEeYMval1gCBBarw697-kwGagljVb8Gcj4JtBtvX0ZGQJEEpFvXFacGbpy3KJPHuWplrso3QiFPyKRUBwszr7MTBolM'
    input_calendar_id = ''
    # get_calendar_setting(input_access_token)
    print(create_event(input_access_token, input_calendar_id))
