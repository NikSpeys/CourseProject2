from unittest.mock import Mock

import requests

from src.api_base import ConnectionApiHH


def test_load_vacancies(mocker):
    mock_response = Mock()
    mock_response.json.return_value = {
        "items": [
            {"id": 1, "name": "Python-разработчик", "salary": {"from": 100000, "to": 150000}},
            {"id": 2, "name": "Java-разработчик", "salary": {"from": 80000, "to": 120000}},
        ]
    }
    mock_response.raise_for_status.return_value = None
    mocker.patch("requests.get", return_value=mock_response)

    hh_api = ConnectionApiHH()
    hh_api.download_vacancy("Python", max_pages=1)

    assert len(hh_api.list_vacancy()) == 2
    assert hh_api.list_vacancy()[0]["name"] == "Python-разработчик"


def test_load_vacancies_break(mocker):
    mock_response = Mock()
    mock_response.json.return_value = {"items": []}
    mock_response.raise_for_status.return_value = None
    mocker.patch("requests.get", return_value=mock_response)

    hh_api = ConnectionApiHH()
    hh_api.download_vacancy("Python", max_pages=1)

    assert len(hh_api.list_vacancy()) == 0


def test_get_vacancies_filter(mocker):
    mock_response = Mock()
    mock_response.json.return_value = {
        "items": [
            {"id": 1, "name": "Python-разработчик", "salary": {"from": 100000, "to": 150000}},
            {"id": 2, "name": "Java-разработчик", "salary": {"from": 80000, "to": 120000}},
        ]
    }
    mock_response.raise_for_status.return_value = None
    mocker.patch("requests.get", return_value=mock_response)

    hh_api = ConnectionApiHH()
    hh_api.download_vacancy("Python", max_pages=1)

    filtered_vacancies = hh_api.list_vacancy(lambda v: v.get("salary", {}).get("from", 0) > 90000)

    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0]["name"] == "Python-разработчик"


def test_load_vacancies_api_error(mocker):
    mock_get = mocker.patch("requests.get")
    mock_get.side_effect = requests.exceptions.RequestException("Ошибка")

    hh_api = ConnectionApiHH()
    hh_api.download_vacancy("Python")

    assert len(hh_api.list_vacancy()) == 0