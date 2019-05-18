from authorization.utils import rand_str
from responses import RequestsMock


def test_access_token(client, db):
    with RequestsMock() as rsps:
        rsps.add(
            method=rsps.POST, url='https://www.reddit.com/api/v1/access_token',
            json={
                'access_token': '89561363064-bWRjKRTOgw4isn6wcBDEmnBZ3nc',
                'token_type': 'bearer', 'expires_in': 3600, 'scope': 'identity'
            },
        )
        response = client.get(
            path=f'/api/access_token/?state={rand_str()}&code={rand_str()}'
        )
        assert response.status_code == 200
        assert response.data['access_token'] == '89561363064-bWRjKRTOgw4isn6wcBDEmnBZ3nc'
