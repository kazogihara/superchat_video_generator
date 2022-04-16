import os
import json
from moviepy.editor import *
from datetime import datetime
from datetime import timedelta


class Video:
    name = None
    extension = None
    def __init__(self,name = 'default', extension = 'mp4'):
        self.name = name
        self.extension = extension
    def fileName(self):
        return self.name + '.' + self.extension
    
def video_downloader():
    #TODO: implement download process
    downloaded_video = Video('nenemaru','mp4')
    return downloaded_video

def chat_downloader():
    return './chatlog_replay_PF2ylueaAQU.json'

def extract_superchat_comment(chat):
    chat_open = open(chat, 'r',encoding='utf-8')
    chat_load = json.load(chat_open)
    return [x for x in chat_load if x['purchaseAmount'] != '']

def video_audio_recognize():
    #TODO video_split後に文字おこしをする処理を入れる。
    pass


def video_split(video,superchat_comment):
    output_videos = []
    #TODO:スパチャの内容の返答まで時間の幅をとれるようにしたい
    time_range = 60
    file_clipper = VideoFileClip('./' + video.fileName())
    for i in superchat_comment:
        #TODO: 配信開始前のスパチャにも対応できるようにする
        if int(not '-' in i['time']):
            superchat_time = None
            #TODO:共通化する
            if i['time'].count(':') == 1:
                time = datetime.strptime(i['time'], '%M:%S')
                superchat_time = time.minute * 60 +  time.second

            elif i['time'].count(':') == 2:
                time = datetime.strptime(i['time'], '%H:%M:%S')
                superchat_time = time.hour * 3600 + time.minute * 60 +  time.second

            clip = file_clipper.subclip(superchat_time, superchat_time + time_range)
            output_videos.append(clip)
            concatenate_videoclips([clip]).write_videofile(video.name + str(superchat_time) + '_' + str(superchat_time + time_range) + '.' + video.extension, codec='libx264')
    return output_videos

def video_combine(video_list,name):
    concatenate_videoclips(video_list).write_videofile(name)

def createabstract(superchat_comment,video_url):
    #TODO: 文言を考える
    abstract = open('abstract.txt', 'a',encoding='utf-8')
    #TODO: 共通化する
    a = 0
    for i in superchat_comment:
        if int(not '-' in i['time']):
            superchat_time = None
            if i['time'].count(':') == 1:
                time = datetime.strptime(i['time'], '%M:%S')
                superchat_time = time.minute * 60 +  time.second

            elif i['time'].count(':') == 2:
                time = datetime.strptime(i['time'], '%H:%M:%S')
                superchat_time = time.hour * 3600 + time.minute * 60 +  time.second
            #TODO: 成形する
            abstract.write(str(timedelta(seconds = a)) + ' ' + i['user'] + 'さん' + ' ' + video_url + str(superchat_time) + 's\n')
            a += 60
    abstract.close()
    pass

def uploadVideo():
    #TODO: Youtubeに自動アップロードするようにする
    pass

video = video_downloader()
chat = chat_downloader()
superchat_comment = extract_superchat_comment(chat)
video_audio_recognize()
video_list = video_split(video,superchat_comment)
video_combine(video_list,'test.mp4')
#TODO: videoのurlは外部から渡せるようにする
user_list = createabstract(superchat_comment, 'https://www.youtube.com/watch?v=PF2ylueaAQU&t=')