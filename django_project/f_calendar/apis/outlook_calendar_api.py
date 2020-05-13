import requests


def list_calendars(access_token):
    url = 'https://graph.microsoft.com/v1.0/me/calendars'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    r = requests.get(url, headers=headers)
    return r.json()


if __name__ == '__main__':
    input_access_token = ""
    print(list_calendars(input_access_token))
