import requests

from django_project.settings_dev_local import FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET


def get_app_token():
    params = {
        'grant_type': 'client_credentials',
        'client_id': FACEBOOK_CLIENT_ID,
        'client_secret': FACEBOOK_CLIENT_SECRET
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


def get_long_lived_token(access_token):
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': FACEBOOK_CLIENT_ID,
        'client_secret': FACEBOOK_CLIENT_SECRET,
        'fb_exchange_token': access_token
    }
    r = requests.get('https://graph.facebook.com/oauth/access_token?', params=params)
    return r.json()


def get_user_profile(access_token):
    params = {
        'access_token': access_token,
        'fields': 'id,name,email'
    }
    r = requests.get('https://graph.facebook.com/me?', params=params)
    return r.json()


if __name__ == '__main__':
    short_access_token = 'EAADo0w7jw7YBAGPw8PHp4zfiQYe9Av4atmoBZCJQ3hzPKaT5GL2vN1DCbPUFAsADKnRAeEJOEryNZCEY3qaZCq7eJB5Fj60NqZAlXaT6NqVxwMfJT9bgVFpHmNZBTqRQgOXLBXUIiM3kZCGuLldOLmZBXn5hfLEefz8S0K3Ef0Li84uZCDA03ETrR7l9UfvpXpDX4hq9ZArYJNZB47NFqOMvqH'
    rr = verify_token(short_access_token, get_app_token())
    print(rr)
    print(rr.get('data').get('is_valid'))
    long_access_token = get_long_lived_token(short_access_token)
    print(long_access_token)
    at_long = long_access_token.get('access_token')
    print(get_user_profile(at_long))
