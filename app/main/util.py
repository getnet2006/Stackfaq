import requests
from bs4 import BeautifulSoup

def freq_questions(tag):
    req = requests.get(f'https://stackoverflow.com/questions/tagged/{tag}?tab=frequent&page=1&pagesize=15')
    soup = BeautifulSoup(req.text, 'html.parser')
    return [{'title' : i.text.strip(),'link' : i.find('a')['href'].replace('/','*')} for i in soup.find_all('h3', class_='s-post-summary--content-title')]

def answer(question_link):
    response = requests.get(question_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return {
                    'answer': soup.find('div', class_="answer js-answer accepted-answer js-accepted-answer").find('div', class_='s-prose js-post-body'),
                    'question': soup.find('h1', class_='fs-headline1 ow-break-word mb8 flex--item fl1'),
                    'body': soup.find('div', class_='s-prose js-post-body')
                }