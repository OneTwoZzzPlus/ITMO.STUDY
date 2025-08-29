import requests, bs4

def get_names():
    try:
        response = requests.get('https://randomus.ru/name?type=5&sex=10&count=20')
        if response.ok:
            soup = bs4.BeautifulSoup(response.content, 'lxml')
            data = soup.find('textarea', id="result_textarea").text.split()
            data.sort()
            return data
    except BaseException:
        return ['ошибка', 'при', 'получении', 'имен']


if __name__ == "__main__":
    print(get_names())
