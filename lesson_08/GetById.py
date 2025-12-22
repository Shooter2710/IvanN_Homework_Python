import requests
import json


class GetById:
    def __init__(self, baseURL: str):
        self.url = baseURL

    def get_by_id(self, key: str):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        with open("id_project.txt", "r") as file:
            project_id = file.read()

        self.response = requests.get(
            self.url+f"/api-v2/projects/{project_id}", headers=headers)

        self.title = json.loads(self.response.text)["title"]
        return (self.response.json)

    def neg_get_by_id(self, key: str):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        project_id = "11111111-2222-3333-4444-555555555555"

        response = requests.get(
            self.url+f"/api-v2/projects/{project_id}", headers=headers)

        resp = json.loads(response.text)
        neg_response = f"Статус-код: {
            resp["statusCode"]}, {resp["message"]}"
        return (neg_response)
