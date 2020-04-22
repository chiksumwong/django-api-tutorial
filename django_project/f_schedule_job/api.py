import json
import time
import asyncio
import aiohttp
import requests

apiKey = '1C5E789ABB9694668CD4AE3BCAC003324CF604AF373B16CC384E6B07C711FB5B'
email = 'chiksumwong@codefreesoft.com'
subscriberId = 'DEMO'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Dragonce-API-Key': apiKey,
    'X-Dragonce-Email': email,
    'X-Dragonce-Subscriber-ID': subscriberId
}

initRecordURL = 'https://api.dragoncerc.com/v1/runtime/record/init'
commitRecordURL = 'https://api.dragoncerc.com/v1/runtime/record/commit'
listTableURL = 'https://api.dragoncerc.com/v1/runtime/record/list/table'

# Page Application Info
environment = 'developing'
appShop = 'App136032'
pageApplication = 'Page161832'

# Application Form Info
fApplication = 'R_i40o40'
tApplication = 'R_cz6qbe'
wApplicationId = 'R_pr72wp'
wCustomer = 'R_y3aqa2'
wCreateAt = 'R_hs2o3a'
bSubmit = 'Eutrkrvq'


def init_application_record():
    body = {
        'environment': environment,
        'app': appShop,
        'page': pageApplication,
        'form_id': fApplication
    }
    r = requests.post(initRecordURL, data=body, headers=headers)
    return r.json()


def commit_application_record_to_pending(tmp_record_id, data):
    body = {
        'environment': environment,
        'app': appShop,
        'page': pageApplication,
        'form_id': fApplication,
        'action': 'workflow',
        'tmp_record_id': tmp_record_id,
        'data': json.dumps(data)
    }
    print('Input Body Str: ', json.dumps(body))
    r = requests.post(commitRecordURL, data=body, headers=headers)
    return r.text


def create_application_record(application_id, customer, timestamp):
    r_dict = init_application_record()
    tmp_record_id = r_dict.get('tmp_record_id')
    time.sleep(2)
    print('Get Tep Record ID: ', tmp_record_id)
    # hard code timestamp for now
    timestamp = 1587462949
    data = {
        "R_hs2o3a": {
            "sec": timestamp,
            "usec": 0
        },
        "R_pr72wp": application_id,
        "R_y3aqa2": customer
    }
    r = commit_application_record_to_pending(tmp_record_id, data)
    print('Drangoce Response: ', r)


def push_application_record():
    url = listTableURL
    headers = {
        'content-Type': 'application/json',
        'X-Dragonce-API-Key': apiKey,
        'X-Dragonce-Email': email,
        'X-Dragonce-Subscriber-ID': subscriberId
    }
    body = {
        'environment': environment,
        'app': appShop,
        'page': pageApplication,
        'table_id': 'R_si36ia'
    }

    # Get the data
    r = requests.post(url, data=json.dumps(body), headers=headers)


def get_application_table():
    body = {
        'environment': environment,
        'app': appShop,
        'page': pageApplication,
        'table_id': tApplication
    }
    # Get the data
    r = requests.post(listTableURL, data=body, headers=headers)
    print('Get Table of Application: ', r.text)
    return r.text


if __name__ == '__main__':

    # # get_application_table()
    res_dict = init_application_record()
    tmp_record_id = res_dict.get('tmp_record_id')
    print('Get Tep Record ID: ', tmp_record_id)
    # time.sleep(2)
    # body = {
    #     'environment': environment,
    #     'app': appShop,
    #     'page': pageApplication,
    #     'form_id': fApplication,
    #     'action': 'workflow',
    #     'tmp_record_id': tmp_record_id,
    #     'data': {"R_pr72wp": "QQ"}
    # }
    # # Get the status = "ok"
    # print('Input Body: ', body)
    # r2 = requests.post(commitRecordURL, data=body, headers=headers)
    # print('Drangoce Response: ', r2.text)
    # create_application_record("df", "dfd", "df")
    timestamp = "1587462949"
    application_id = 'not bad'
    customer = 'Sam'
    payload = 'environment=developing&app=App136032&page=Page161832&form_id=R_i40o40&tmp_record_id='+tmp_record_id+'&action=workflow&workflow_id=Eutrkrvq&data=%7B%22R_hs2o3a%22%3A%20%7B%22sec%22%3A%20'+timestamp+'%2C%20%22usec%22%3A%200%7D%2C%20%22R_pr72wp%22%3A%20%22'+application_id+'%22%2C%20%22R_y3aqa2%22%3A%20%22'+customer+'%22%7D '
    response = requests.request("POST", commitRecordURL, headers=headers, data=payload)
    print(response.text.encode('utf8'))
