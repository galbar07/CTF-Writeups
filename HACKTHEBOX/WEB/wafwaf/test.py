import requests
import re

# Configuring a request with URL and valid headers
URL = "https://the-internet.herokuapp.com/context_menu"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

STR1 = "Right-click in the box below to see one called 'the-internet'"
STR2 = "Alibaba"


def find_text(word):
    result = requests.get(URL, HEADERS)
    html_content = result.text
    return re.search(word, html_content)


def test_right_click_in_html():
    assert find_text(STR1)


def test_alibaba_in_html():
    assert find_text(STR2)
