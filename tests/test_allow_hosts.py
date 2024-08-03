from django.test import override_settings
from django.conf import settings


@override_settings(ALLOWED_HOSTS=['localhost'])
def test_private_ip_1(client):
    assert settings.ALLOWED_HOSTS == ['localhost']

    assert '192.168.0.0/16' in settings.ALLOWED_CIDR_NETS

    response = client.get('/health', headers={'host': '192.168.14.2'})
    assert response.status_code == 200


@override_settings(ALLOWED_HOSTS=['localhost'])
def test_private_ip_2(client):
    assert settings.ALLOWED_HOSTS == ['localhost']

    assert '172.16.0.0/12' in settings.ALLOWED_CIDR_NETS

    response = client.get('/health', headers={'host': '172.16.14.2'})
    assert response.status_code == 200


@override_settings(ALLOWED_HOSTS=['localhost'])
def test_private_ip_3(client):
    assert settings.ALLOWED_HOSTS == ['localhost']

    assert '10.0.0.0/8' in settings.ALLOWED_CIDR_NETS

    response = client.get('/health', headers={'host': '10.1.0.2'})
    assert response.status_code == 200
