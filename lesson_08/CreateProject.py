import requests
import json


class CreateProject:
    def __init__(self, baseURL: str):
        self.url = baseURL

    def create_project(self, title: str, users: object, key: str):
        self.title = title
        payload = {
            "title": title,
            "users": users
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        response = requests.get(self.url+"/api-v2/projects", headers=headers)
        self.list1 = json.loads(response.text)["paging"]["count"]

        self.response = requests.post(
            self.url+"/api-v2/projects", json=payload, headers=headers)

        id_project = json.loads(self.response.text)["id"]
        with open('id_project.txt', 'w') as file:
            file.write(id_project)

    def test_adding_project(self, key):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        response = requests.get(self.url+"/api-v2/projects", headers=headers)

        list2 = json.loads(response.text)["paging"]["count"]
        return list2

    def neg_create_project(self, title: str, users: object, key: str):
        payload = {
            "title": title,
            "users": users
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        response = requests.post(
            self.url+"/api-v2/projects", json=payload, headers=headers)

        resp = json.loads(response.text)
        neg_response = f"Статус-код: {
            resp["statusCode"]}, {resp["message"]}"
        return neg_response
