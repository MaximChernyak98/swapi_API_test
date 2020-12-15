import requests


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("https://swapi.dev/api/planets")
    print(response.content)
    assert response.status_code == 200
    with open('outputfile.json', 'wb') as outf:
        outf.write(response.content)


if __name__ == "__main__":
    test_get_locations_for_us_90210_check_status_code_equals_200()
