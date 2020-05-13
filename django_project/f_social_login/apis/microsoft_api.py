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
    input_access_token = ""
    m_dict = get_user_info(input_access_token)
    print(m_dict['id'])
