import requests
import os
import eyed3


# 下载歌曲
def download_song(song_name, song_url, save_dir, song_cover_url, singer, album):
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    if not os.path.exists(save_dir):                            # 如果保存目录不存在，则创建目录
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, '{}.mp3'.format(song_name))      # 拼接保存路径和文件名
    if os.path.exists(save_path):                                          # 如果文件已存在，则跳过下载
        print('{} 已存在，跳过下载！'.format(song_name))
        return
    response = requests.get(song_url, headers=headers)               # 使用requests模块发送get请求
    if response.status_code == 200:
        with open(save_path, 'wb') as f:                                      # 以二进制写入模式打开文件
            f.write(response.content)
        write_tag(save_path, song_name, song_cover_url, singer, album)
        print('{} 下载完成！'.format(song_name))       #下载情况打印
    else:
        print('{} 下载失败！'.format(song_name))

def download_song_pic(song_pic_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # 检测是否存在cover.jpg存在的话就删除
    if os.path.exists("cover.jpg"):
        os.remove("cover.jpg")
    # 获取封面图片链接
    response = requests.get(song_pic_url, headers=headers)
    # 下载到运行目录下的cover.jpg
    if response.status_code == 200:
        with open("cover.jpg", 'wb') as f:                                      # 以二进制写入模式打开文件
            f.write(response.content)
        return True
    else:
        return False
    
def write_tag(song_path: str, song_name: str, song_cover_url: str, singer: str, album: str):
    if download_song_pic(song_cover_url) == False:
        return False
    try:
        audiofile = eyed3.load(song_path)
        audiofile.tag.title = song_name
        audiofile.tag.artist = singer
        audiofile.tag.album = album
        audiofile.tag.album_artist = singer
        audiofile.tag.composer = singer
        audiofile.tag.images.set(type_=3, img_data=open('cover.jpg', 'rb').read(), mime_type='image/jpeg')  # 封面
        audiofile.tag.save(version=eyed3.id3.ID3_DEFAULT_VERSION, encoding='utf-8')
    except:
        return False
    return True