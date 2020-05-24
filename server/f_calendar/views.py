import datetime
from googleapiclient.discovery import build
import google.oauth2.credentials


def get_events(access_token):
    credentials = google.oauth2.credentials.Credentials(
        access_token)

    service = build('calendar', 'v3', credentials=credentials)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    print('Getting the upcoming 10 events')

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()

    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    input_access_token = ''
    get_events(input_access_token)
