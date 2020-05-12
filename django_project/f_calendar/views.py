import datetime
from googleapiclient.discovery import build
import google.oauth2.credentials


def main():
    credentials = google.oauth2.credentials.Credentials(
        'ya29.a0AfH6SMDW80JS4WhZF5aKySeZyeiW15mK06Q34UyPm1U7fEw2scUGfbegIFSv6tSOJUV21MWn765g0cx2oEA2SvwkgePL_cwnLR9wTAuenhhYqKtKAJcupClih0kdpOiRrm7d_uadjqGmncfR8OIZUbUGVX4vo-1RX1g')

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
    main()
