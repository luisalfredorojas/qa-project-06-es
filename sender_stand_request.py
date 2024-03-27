import requests
import configuration
import data

def create_user_post(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

def post_create_kit(kit_name):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_name,
                         headers=data.kit_headers)


def get_kits_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE)


response = create_user_post(data.user_body)
print(response.status_code)
print(response.json())