import pytest
import requests


class TestApi:
    # sera executado conforme escocpe declarado, default é function (para cada função)
    # para class (uma vez ante da classe)
    # Scopes: funcion, class, module
    @pytest.fixture(scope='class')
    def url(self):
        return 'http://localhost:5000/data'

    @pytest.fixture(scope='class')
    def data(self):
        return [1, 2, 3, 4]

    @pytest.fixture(scope='class')
    def uuid(self, url, data):
        response = requests.post(url, json={'data': data})

        return response.json()['uuid']

    def test_save_data(self, uuid):
        assert uuid is not None

    def test_get_data(self, url, uuid, data):
        get_url = (url + f'/{uuid}')
        response = requests.get(get_url)

        assert response.ok
        assert response.json()['data'] == data

    @pytest.mark.skip
    def test_calc_mean(self, url, uuid):
        get_url = (url + f'/{uuid}/mean')
        response = requests.get(get_url)

        assert response.ok
        assert response.json()['result'] == pytest.approx(2.5)

    @pytest.mark.skip
    def test_calc_min(self, url, uuid):
        get_url = (url + f'/{uuid}/min')
        response = requests.get(get_url)

        assert response.ok
        assert response.json()['result'] == pytest.approx(1)

    @pytest.mark.skip
    def test_calc_max(self, url, uuid):
        get_url = (url + f'/{uuid}/max')
        response = requests.get(get_url)

        assert response.ok
        assert response.json()['result'] == pytest.approx(4)

    @pytest.mark.parametrize('operation, expected_result', [('mean', 2.5), ('min', 1), ('max', 4)])
    def test_calc_parametrized(self, uuid, url, operation, expected_result):
        get_url = (url + f'/{uuid}/{operation}')
        response = requests.get(get_url)

        assert response.ok
        assert response.json()['result'] == pytest.approx(expected_result)
