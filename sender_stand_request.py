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
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_name,
                         headers=data.kit_headers)


def get_kits_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE,
                        headers=data.kit_headers
                        )

