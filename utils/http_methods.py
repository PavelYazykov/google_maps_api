import requests
from utils.logger import Logger


class Http_method:

    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        Logger.add_request(url, 'Get')
        result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, 'Post')
        result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, 'Put')
        result = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, 'Delete')
        result = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result
    