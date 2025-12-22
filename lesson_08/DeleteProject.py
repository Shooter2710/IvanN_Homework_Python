import requests
import json


class DeleteProject:
    def __init__(self, baseURL: str):
        self.url = baseURL

    def delete_project(
            self, deleted: bool, title: str, users: object, key: str):
        payload = {
            "deleted": deleted,
            "title": title,
            "users": users
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        with open("id_project.txt", "r") as file:
            project_id = file.read()

        self.response = requests.put(
            self.url+f"/api-v2/projects/{project_id}",
            json=payload, headers=headers)

    def test_deleted_project(self, key: str):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        with open("id_project.txt", "r") as file:
            project_id = file.read()

        response = requests.get(
            self.url+f"/api-v2/projects/{project_id}", headers=headers)

        deleted = json.loads(response.text)["deleted"]
        return deleted

    def neg_delete_project(
            self, deleted: bool, title: str, users: object, key: str):
        payload = {
            "deleted": deleted,
            "title": title,
            "users": users
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        project_id = "11111111-2222-3333-4444-555555555555"

        response = requests.put(
            self.url+f"/api-v2/projects/{project_id}",
            json=payload, headers=headers)

        resp = json.loads(response.text)
        neg_response = f"Статус-код: {
            resp["statusCode"]}, {resp["message"]}"
        return (neg_response)
