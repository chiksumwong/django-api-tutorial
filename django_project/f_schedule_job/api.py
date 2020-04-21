import json
import requests

apiKey = '1C5E789ABB9694668CD4AE3BCAC003324CF604AF373B16CC384E6B07C711FB5B'
email = 'chiksumwong@codefreesoft.com'
subscriberId = 'DEMO'
headers = {
    'content-Type': 'application/json',
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
    r = requests.post(initRecordURL, data=json.dumps(body), headers=headers)
    print('Response: ', r.json())
    return r.json()


def commit_application_record_to_pending(tmp_record_id, data):
    body = {
        'environment': environment,
        'app': appShop,
        'page': pageApplication,
        'form_id': fApplication,
        'action': 'workflow',
        'tmp_record_id': tmp_record_id,
        'data': data
    }
    # Get the status = "ok"
    r = requests.post(commitRecordURL, data=json.dumps(body), headers=headers)
    print('Create Record Json: ', r.json())
    return r.json()


def create_application_record(application_id, customer, timestamp):
    tem_r = init_application_record()
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
    commit_application_record_to_pending(str(tem_r.get('tmp_record_id')), json.dumps(data))


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
    url = listTableURL
    headers = {
        'content-Type': 'application/json',
        'X-Dragonce-API-Key': '1C5E789ABB9694668CD4AE3BCAC003324CF604AF373B16CC384E6B07C711FB5B',
        'X-Dragonce-Email': 'chiksumwong@codefreesoft.com',
        'X-Dragonce-Subscriber-ID': 'DEMO'
    }
    body = {
        'environment': 'developing',
        'app': 'App299425',
        'page': 'Page261544',
        'table_id': 'R_si36ia'
    }

    # Get the data
    r = requests.post(url, data=json.dumps(body), headers=headers)
    return r.text


if __name__ == '__main__':
    create_application_record()
