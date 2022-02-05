from bs4 import BeautifulSoup
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
# response.raise_for_status()
soup = BeautifulSoup(response.text, features='html.parser')

posts = soup.find_all('article', class_='post')
for post in posts:
    post_id = post.parent.attrs.get('id')
    if not post_id:
        continue
    post_id = int(post_id.split('_')[-1]) #нужно или нет ?
    print('post', post_id)

    hubs = post.find_all('a', class_='hub-link')
    for hub in hubs:
        Hub = hub.text

        if any([Hub in incoming for incoming in KEYWORDS]):
            print('она тута есть')

            title_element = post.find('a', class_='post__title_link')
            print(title_element.text, title_element.attrs.get('href'))