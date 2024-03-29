import requests
import configuration
import data

#CORRECCION CREAR USUARIO PARA TENER TOKEN
def create_user_post(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

#CORRECCION OBTENER EL TOKEN Y AGREGARLO EN LOS HEADERS
def post_create_kit(kit_name):
    response = create_user_post(data.user_body)
    response_auth = response.json()["authToken"]
    auth_token = {"Content-Type": "application/json",
                  "Authorization": "Bearer " + response_auth}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_name,
                         headers=auth_token)


def get_kits_table(id):
    kits_with_id = configuration.KITS_TABLE + "?cardId=" + id
    return requests.get(configuration.URL_SERVICE + kits_with_id
                        )

response = get_kits_table("2")
print(response.status_code)
print(response.json())
