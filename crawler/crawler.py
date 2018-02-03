import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


class EpisodeData:

    def __init__(self, episode_id, url_thumbnail, title, rating, created_date):
        self.episode_id = episode_id
        self.url_thumbnail = url_thumbnail
        self.title = title
        self.rating = rating
        self.created_date = created_date

    def __str__(self):
        return f'에피소드ID: {self.episode_id} (제목: {self.title}, 별점: {self.rating}, 등록일: {self.created_date})'


def get_episode_list(webtoon_id, page):

    url = 'https://comic.naver.com/config/list.nhn'
    params = {
        'titleId': webtoon_id,
        'page': page,
    }
    response = requests.get(url, params)
    soup = BeautifulSoup(response.text, 'lxml')

    viewlist_episode = soup.select('table.viewList > tr')

    result = []
    for episode in viewlist_episode:
        td_episode = episode.select('td')

        if td_episode and len(td_episode) == 4:
            episode_id_urlparse = urlparse(td_episode[0].select_one('a').get('href'))
            episode_id = parse_qs(episode_id_urlparse.query)['no'][0]
            url_thumbnail = td_episode[0].select_one('img').get('src')
            title = td_episode[1].get_text(strip=True)
            rating = td_episode[2].select_one('strong').get_text(strip=True)
            created_date = td_episode[3].get_text(strip=True)

            episodedata = EpisodeData(episode_id=episode_id, url_thumbnail=url_thumbnail, title=title, rating=rating,
                                      created_date=created_date)
            result.append(episodedata)

    return result