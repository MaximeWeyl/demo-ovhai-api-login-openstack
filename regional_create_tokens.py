from regional import connect_regionnal, get_config

import urllib.parse


if __name__ == '__main__':
    config = get_config()
    session = connect_regionnal(config)
    base_url = config['regionalApiUrl']

    print("----- Creating a new app token -------")
    response = session.post(
        urllib.parse.urljoin(base_url, "v1/token"),
        json={
            "name": "app-token",
            "role": "ai_training_operator"
        }
    )

    print(response.status_code)
    print(response.content)

    responseData = response.json()
    print("Token value : ", responseData['status']['value'])
    print("Token id : ", responseData['id'])

