import requests
from datetime import datetime, timedelta


def get_trending_repositories(days_amount, page_count):
    user_datetime = datetime.now()
    github_datetime = user_datetime - timedelta(days=days_amount)
    github_datetime_string = github_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    github_url = "https://api.github.com/search/repositories"
    payload = {'q': '{}{}'.format('created:>=', github_datetime_string),
               'sort': 'stars', 'order': 'desc', 'per_page': page_count}
    trending_repositories_data = requests.get(github_url, params=payload)
    return trending_repositories_data.json()['items']


def print_trending_repositories(trending_repositories, days_amount):
    print("Самые популярные репозитории за %s дней:" % days_amount)
    for repo in trending_repositories:
        print(u'\nРепозиторий {}:\nЗвезд:{}; Открытых задач:{}'
              '\nСсылка :{}'.format(repo['name'],
                                    repo['stargazers_count'],
                                    repo['open_issues_count'],
                                    repo['html_url']))

if __name__ == '__main__':
    days_amount = 7
    page_count = 20
    trending_repositories = get_trending_repositories(days_amount, page_count)
    print_trending_repositories(trending_repositories, days_amount)
