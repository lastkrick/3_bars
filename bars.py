import json
import requests

DATA_URL = "https://devman.org/fshare/1503831681/4/"
DATA_FILE = "bars.json"

def get_seats_count(item):
    return item['properties']['Attributes']['SeatsCount']

def download_data(url, filepath):
    res = requests.get(url)
    data = res.json()
    with open(filepath, 'w') as f:
        json.dump(data, f)
    return 0


def load_data(filepath):
    with open(filepath) as f:
        data = json.loads(f.read())
    return data['features']


def get_biggest_bar(data):
    return max(data, key=get_seats_count)


def get_smallest_bar(data):
    return min(data, key=get_seats_count)


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    download_data(DATA_URL, DATA_FILE)
    data = load_data(DATA_FILE)
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))

