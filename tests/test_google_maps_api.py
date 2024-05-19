import json

from utils.api import Google_maps_api
from utils.checking import Checking


class Test_create_place:
    """Созданиу, удаление и изменение новой локации"""

    def test_create_new_place(self):
        print('Метод POST')
        result_post = Google_maps_api.create_new_place()

        check = result_post.json()
        place_id = check.get('place_id')
        print(place_id)
        Checking.check_status_code(result_post, 200)
        list_field = json.loads(result_post.text)
        print(list(list_field))
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Метод Get')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        list_field = json.loads(result_get.text)
        print(list(list_field))
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])
        checks = result_get.json()
        check_info = checks.get('name')
        print(check_info)
        Checking.check_json_value(result_get, 'name', 'Frontline house')

        print('Метод PUT')
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        list_field = json.loads(result_put.text)
        print(list(list_field))
        Checking.check_json_token(result_put, ['msg'])

        print('Метод GET проверка PUT запроса')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        list_field = json.loads(result_get.text)
        print(list(list_field))
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])

        print('Метод DELETE')
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        list_field = json.loads(result_delete.text)
        print(list(list_field))
        Checking.check_json_token(result_delete, ['status'])

        print('Метод GET проверка DELETE запроса')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        list_field = json.loads(result_get.text)
        print(list(list_field))
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_search_word(result_get, 'msg', 'failed')

