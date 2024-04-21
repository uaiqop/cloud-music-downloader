import requests
import json
from bs4 import BeautifulSoup  # 导入 BeautifulSoup 的方法


# 获取指定歌手的歌曲信息
def get_artist_songs(artist_id):
    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    url = "https://music.163.com/api/v1/artist/songs"  ## 歌手歌曲信息api的url
    params = {
        "id": artist_id,  # 歌手id
        "offset": 0,  # 偏移量
        "total": True,  # 是否获取全部歌曲信息
        "limit": 1000,  # 获取歌曲数量
    }
    response = requests.get(
        url, headers=headers, params=params
    )  # 使用requests模块发送get请求
    if response.status_code == 200:  # 如果请求成功
        result = json.loads(response.text)  # 将response的文本内容转为json格式
        # with open('data.txt', 'w') as f:
        #     f.write(str(result))
        songs = result["songs"]  # 获取歌曲列表
        return songs
    else:
        print("请求出错：", response.status_code)  # 如果请求失败
        return None


# 获取歌曲名称和播放链接
def get_song_info(song):
    song_name = song["name"]  # 歌曲名称
    song_id = song["id"]  # 歌曲id
    song_pic = song["album"]["picUrl"]  # 歌曲封面下载链接
    album = song["album"]["name"]
    singer = song["artists"][0]["name"]
    file_url = "https://music.163.com/song/media/outer/url?id={}.mp3".format(
        song_id
    )  # 歌曲播放链接
    return song_name, file_url, song_pic, album, singer


def grt_song_cover(song):
    song_id = song["id"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    url = "https://music.163.com/#/song?id={}".format(song_id)
    res = requests.get(url)
    BeautifulSoup.select("")
