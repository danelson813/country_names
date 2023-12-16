import requests
from bs4 import BeautifulSoup as bs


def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    return soup


def parse(lst: list):
    cap = lst[1][9:]
    pop = lst[2][12:]
    area = lst[3][12:]
    return [cap, pop, area] 