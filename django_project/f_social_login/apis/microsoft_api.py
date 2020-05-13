import requests


def get_user_info(access_token):
    url = 'https://graph.microsoft.com/v1.0/me'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    r = requests.get(url, headers=headers)
    print('Get Microsoft User Info: ', r.json())
    return r.json()


if __name__ == '__main__':
    input_access_token = "EwBwA8l6BAAUO9chh8cJscQLmU LSWpbnr0vmwwAAf7JUwCoPVjgyp3KKoOCLu88Ar GyBT8ytJNHEBXJa77wi3KuYa0J2yFdmOi6BSu2MnyJIPhePl1pEUO97IZM2SucmNaZJYkQDiRVJa fc6GZQBFFo6ZM iwo9lWUodQZo37JTYG2tsXmJzyVtgKx4UnoL63HBFUiFFny/W7/YzgrgAI9DfctZSd1Si27uBaj7QswdyoMpQwtBl/dwu17S49UW0DyB66WLQciySkemCXU5sJOZ9oAgeZQQFyhXF1XdoPRCoBRO1RCjDnhTYhXycBU2b/Iqk2GabYkaSoYlj7t8M8hn9KGZ Byl87CGEY1VNRB5ViyACguAfjczuOOxEDZgAACMtWkGZbJvWFQAJVRmAFRQJQrRuAMmjlwc0wP4XJqULM7P3VT4Lo5cTH/QjM0BvvDAsEauLmIKDabSeDLiDiVpAuv9KVhgdmca KJLDVN6TXsdPW8omOj2Wh6DAS4vFvcIkFD5fbjnG/CWDKqZxDY2ZE4abq7vCacNPhXdyO8ogpaJNyROMHno5Pr2AAQExMYAeD3RKefyVpKY1I/EfJBp7fplCOiN1iqyIUqnAj5nztSVlPsESIaHixZ3bFBrBLlj/HAWs22yGDU0kWzH0N tVzQDo7f1Rt4E60yc6xJpXdzji6W2k5uu1vUsn2nYY3AV5Ny99thZs2JjWJ 84O8jEANGv  rVESuvCzTVqfBD47oc7uBQJypccOizBWHMqtHWR9hJj/fsr2Y0Je0Y5VxZz6fa8akJNHX/yrwVhvIkB8nWqT7SiOEVoGXIIp so Ynj60UE1FXDqw matU1dZOveRsIFC xfqGKxddGTgPJRx450GZF4AtR0WyROaAAvPXLaWS8noEdXQ0SuO5wBtsgaY77ndlVgiiVM dGMxRU2tW7JnU1EiU5nAGaVpFFMgf9ASC79xzscUkhbOVSFuyyyCyZIBEv3coJW08p9HqJnAGUkV VrbBTj0gmlhIhhW0G2a8cVRHuJ6arWlZEj3UCDEu5 gpgqEnhUdd/PebQNAvTuzOJipvHykRclu5VBIUiS7Fq2gM/xW/IbInpVN4SpAaovmFtwgyEmk4M5m8 nqa4pSxLZVab4 8CfN03WmVxC6wr7v vz6 FAg=="
    m_dict = get_user_info(input_access_token)
    print(m_dict['id'])
