import datetime

from talk import talk


def calender_events(num, service):
    talk("Hey there! Good day. Hope you are doing fine. These are the events to do today")

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print(f'Getting the upcoming {num} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=num, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        talk('No upcoming events found.')
        return

    # Prints the start and name of the next 10 events
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        events_today = (event['summary'])
        start_time = str(start.split("T")[1].split("-")[0])

        if int(start_time.split(':')[0]) < 12:
            start_time = start_time + "am"

        else:
            start_time = str(int(start_time.split(":")[0]) - 12)
            start_time = start_time + "pm"

        talk(f'{events_today} at {start_time}')
