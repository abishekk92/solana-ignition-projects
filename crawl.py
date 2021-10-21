import requests
from time import sleep


base_url = "https://ignition.devpost.com/project-gallery?page="
MAX_PAGES = 21


def get_page(page_no):
    url = base_url + str(page_no)
    data = requests.get(url)
    return data.text

def save_page(data, page_no):
    with open(f"data/{page_no}.html", "w") as out_file:
        out_file.write(data)

if __name__ == "__main__":
    for page_no in range(MAX_PAGES+1):
        page_data = get_page(page_no)
        save_page(page_data, page_no)
        sleep(1)
