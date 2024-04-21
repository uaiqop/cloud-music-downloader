# - coding: utf-8 -*-
import requests
import json
import os

from utils import download, get_config, get_data

# 主函数
if __name__ == "__main__":
    artist_id = input(
        "请输入歌手ID："
    )  # 歌手ID，这里以陈奕迅为例，歌手id可以在网易云音乐上搜索歌手，进入歌手的主页，查看url中的id参数即为该歌手的id。
    num_songs = int(input("请输入下载歌曲数量："))  # 下载歌曲数量
    songs = get_data.get_artist_songs(artist_id)  # 获取歌手的歌曲信息
    if songs:
        save_dir = get_config.download_dir()  # 保存目录
        for i, song in enumerate(songs):
            if i >= num_songs:
                break
            song_name, song_url, song_pic, album, singer = get_data.get_song_info(
                song
            )  # 获取歌曲名称和播放链接
            download.download_song(
                song_name, song_url, save_dir, song_pic, singer, album
            )  # 下载歌曲
    else:
        print("获取歌曲信息失败！")  # 如果获取歌曲信息失败
