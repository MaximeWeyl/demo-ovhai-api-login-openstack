from regional import connect_regionnal, get_config

import urllib.parse


if __name__ == '__main__':
    config = get_config()
    session = connect_regionnal(config)
    base_url = config['regionalApiUrl']

    print("----- Getting information about the user -------")
    response = session.get(urllib.parse.urljoin(base_url, "v1/me"))
    print(response.status_code)
    print(response.content)
