from pytest import fail
import json


def test_create_user(client, app):
    user = dict(
        name='jhon valderrama',
        email='jhonvalderramaa7@gmail.com',
        city='Cali, Valle del Cauca'
    )

    response = client.post("/", data=user, follow_redirects=True)
    # print(response.data)
    assert b'guardada exitosamente' in response.data
    assert response.status_code == 200


def test_list_users(client, app):
    user_list = []
    for i in ['juan', 'jhon', 'jairo', 'manuel', 'santiago']:
        user = dict(
            name=i,
            email='jhonvalderramaa7@gmail.com',
            city='Cali, Valle del Cauca'
        )
        client.post("/", data=user)

    response = client.get("/get_users")
    assert response.status_code == 200
    assert b'juan' in response.data
    assert b'jhon' in response.data
    assert b'jairo' in response.data
    assert b'manuel' in response.data
    assert b'santiago' in response.data
