import pytest
from CreateProject import CreateProject
from GetById import GetById
from DeleteProject import DeleteProject

baseURL = "https://ru.yougile.com"
key = ""  # <- Ввести "ключ"


def test_yougile():
    createProject = CreateProject(baseURL)
    getById = GetById(baseURL)
    deleteProject = DeleteProject(baseURL)

    createProject.create_project("BestProject", {}, key)
    assert createProject.response.status_code == 201
    with pytest.raises(AssertionError):
        assert createProject.response.status_code == 200
    assert createProject.test_adding_project(key) == createProject.list1 + 1
    assert createProject.neg_create_project(
        "", {}, key) == \
        "Статус-код: 400, ['title should not be empty']"

    getById.get_by_id(key)
    assert getById.response.status_code == 200
    with pytest.raises(AssertionError):
        assert getById.response.status_code == 201
    assert getById.title == createProject.title
    assert getById.neg_get_by_id(
        key) == \
        "Статус-код: 404, Проект не найден"

    deleteProject.delete_project(True, "BestProject", {}, key)
    assert deleteProject.response.status_code == 200
    with pytest.raises(AssertionError):
        assert deleteProject.response.status_code == 201
    assert deleteProject.test_deleted_project(key)
    assert deleteProject.neg_delete_project(
        True, "BestProject", {}, key) == \
        "Статус-код: 404, Проект не найден"
