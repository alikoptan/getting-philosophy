from bs4 import BeautifulSoup
import requests
import re 
import time
import sys


def get_valid_links(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # Finding all <p> elements.
    paragraphs = soup.find('div', {'id': 'mw-content-text'}).find_all('p')

    # Removing any content between brackets '()', '[]' from raw HTML.
    paragraphs = list(map(lambda p: re.sub('[\(\[].*?[\)\]]', '', str(p)), paragraphs))
    paragraphs = (''.join(paragraphs))

    # Finding all valid links (that redirects to other wiki pages), excluding links to files.
    soup = BeautifulSoup(paragraphs, 'html.parser')
    paragraphs = soup.find_all('a', href = re.compile(r'^/wiki/(?!File:)'))

    links = []
    for p in paragraphs:
        links.append(str(p['href']))

    return links


def iterate(url):
    next_link = 'N/A'
    candidate_links = get_valid_links(url)
    for link in candidate_links:
        picked_link = 'https://en.wikipedia.org' + link
        if picked_link != url:
            next_link = picked_link
            break
    return next_link


def run(url):
    destination = 'https://en.wikipedia.org/wiki/Philosophy'
    print('Start:', url)
    visited_links = {}
    while True:
        visited_links[url] = True
        time.sleep(0.5)
        url = iterate(url)

        if url == 'N/A' or url in visited_links:
            print('Reached a dead-end or a loop.')
            return False

        print('Navigated to:', url)

        if url == destination:
            print('Reached Philosophy!')
            return True


for i in range(1, len(sys.argv)):
    run(sys.argv[i])



