import requests

def get_site_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

print(get_site_status('https://www.autodominicana.rent'))