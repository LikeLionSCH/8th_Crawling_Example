import requests
from bs4 import BeautifulSoup


def melon_crawling():
    iamhuman = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36"
    }

    URL = "https://www.melon.com/chart/day/index.htm"
    result = requests.get(URL, headers=iamhuman)
    soup = BeautifulSoup(result.text, "html.parser")

    """ 순위 """
    rank = soup.find_all("span", {"class": "rank"})
    ranks = []
    for i in rank[1:]:  # 순위 타이틀 제거
        ranks.append(i.text)

    """ 노래 제목 """
    name = soup.find_all("div", {"class": "ellipsis rank01"})
    names = []
    for i in name:
        names.append(i.find("a").text)

    """ 가수 """
    singer = soup.find_all("div", {"class": "ellipsis rank02"})
    singers = []
    for i in singer:
        singers.append(i.find("a").text)

    """ 앨범명 """
    album = soup.find_all("div", {"class": "ellipsis rank03"})
    albums = []
    for i in album:
        albums.append(i.find("a").text)

    # for i in range(len(names)):
    #     print(ranks[i], names[i], singers[i], albums[i])

    song_list = list(zip(ranks, names, singers, albums))
    # print(song_list[0])
    return song_list