import requests

from django_project.settings_dev_local import FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET


def get_app_token():
    params = {
        'client_id': FACEBOOK_CLIENT_ID,
        'client_secret': FACEBOOK_CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    r = requests.get('https://graph.facebook.com/oauth/access_token?', params=params)
    print('Get Facebook App Token: ', r.json().get('access_token'))
    return r.json().get('access_token')


def verify_token(input_token, app_token):
    params = {
        'input_token': input_token,
        'access_token': app_token
    }
    r = requests.get('https://graph.facebook.com/debug_token?', params=params)
    return r.json()


def get_user_profile(access_token):
    params = {
        'access_token': access_token,
        'fields': 'id,name,email'
    }
    r = requests.get('https://graph.facebook.com/me?', params=params)
    return r.json()


if __name__ == '__main__':
    access_token = 'EAADo0w7jw7YBAKVxLWCnqN8LdfjM7mCrWtmQZAhuwVZBRW1rWNSJb2Ll8Uo5lct5rZBUZB0vrp7HZC1rVK7pZAQ2kck7xn6UZA2cEd5BPs9PPxlGKwiiePtPEoSlF9JCKgfESNTPCD0CdKCBZAmpfqZBRk6Eu4pD3iNqwZCPJUNy4zE6rpDxaRPNqGs1Sva8WbZC3DREXt9KeBXGqJThTTPeqlpxQHo17TmRmsZD'
    r = verify_token(access_token, get_app_token())
    print(r)
    print(r.get('data').get('is_valid'))
    print(get_user_profile(access_token))

