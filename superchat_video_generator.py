import json
from moviepy.editor import *
from datetime import datetime



class Video:
    def __init__(self, name, path, extension, clip = None):
        self.__name = name
        self.__path = path
        self.__extension = extension
        self.__filename = self.name + self.extension
        self.__clip = clip
    @property
    def name(self):
        return self.__name
    
    @property
    def fileName(self):
        return self.__filename

    @property
    def extension(self):
        return self.__extension

    @property
    def path(self):
        return self.__path

    @property
    def clip(self):
        return self.__clip

    def download(self, url):
        #TODO: Implement video downloader
        self.__clip = VideoFileClip(self.path)
        return True

    def upload(self, detail):
        #TODO: Implement Video Uploader
        return True

    def close(self):
        self.__clip.close()
        return True




class Detail:
    def __init__(self, title, description, keyword, category, privacy_status):
        self.__title = title
        self.__description = description
        self.__keyword = keyword
        self.__category = category
        self.__privacy_status = privacy_status
    
    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def keyword(self):
        return self.__keyword

    @property
    def category(self):
        return self.__category

    @property
    def privacy_status(self):
        return self.__privacy_status



class DetailBuilder:
    def __init__(self, title = None, description = None, keyword = None, category = None, privacy_status = None):
        self.__title = title
        self.__description = description
        self.__keyword = keyword
        self.__category = category
        self.__privacy_status = privacy_status
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, arg):
        self.__title = arg
     
    @property
    def description(self):
        return self.__description
    
    #TODO: Builderパターンに沿うようにする
    def makeUserList(self, chat_list, url):
        #TODO: 文言を考える(できればSEO対策とかしたい)
        descirption = open('./description.txt', 'w',encoding='utf-8')
        a = 0
        for chat in chat_list:
            #TODO: 成形する
            descirption.write(str(chat.time) + ' ' + chat.user + 'さん' + ' ' + url + '&t=' + str(chat.seconds) + 's\n')
            a += 60
        descirption.close()


    @property
    def keyword(self):
        return self.__keyword
    
    @keyword.setter
    def keyword(self, arg):
        self.__keyword = arg

    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, arg):
        self.__category = arg   

    @property
    def privacy_status(self):
        return self.__privacy_status
    
    @privacy_status.setter
    def privacy_status(self, arg):
        self.__privacy_status = arg   

    def construct(self):
        #TODO: Implement With Uploader
        return Detail(self.__title, self.__description, self.__keyword, self.__category, self.__privacy_status)


class Chat:
    def __init__(self, user, time, authorbadge, text, purchase_amount, seconds):
        self.__user = user
        self.__time = time
        self.__authorbadge = authorbadge
        self.__text = text
        self.__purchase_amount = purchase_amount
        self.__seconds = seconds
    
    @property
    def user(self):
        return self.__user
        
    @property
    def time(self):
        return self.__time

    @property
    def authorbadge(self):
        return self.__authorbadge

    @property
    def text(self):
        return self.__text

    @property
    def purchase_amount(self):
        return self.__purchase_amount

    @property
    def seconds(self):
        return self.__seconds



class ChatBulder:
    def __init__(self, video_id):
        self.__video_id = video_id
        self.__download()

    def create(self):
        self.__chat_list = []
        with open(self.__file_path,'r',encoding='utf-8') as f:
            for line in f:
                s = json.loads(line)
                chat = Chat(s['user'], s['time'], s['authorbadge'], s['text'], s['purchaseAmount'], self.__getSeconds(s['time']))
                #TODO: 開始前のスパチャにも対応できるようにする
                if(s['purchaseAmount'] != '' and self.__isPotiveTime(chat.time)):
                    self.__register(chat)

        return self.__chat_list
    
    def __getSeconds(self, time):
        seconds = None

        if self.__isBelowMinutes(time) and self.__isPotiveTime(time):
            str_time = datetime.strptime(time, '%M:%S')
            seconds = str_time.minute * 60 +  str_time.second

        elif self.__isPotiveTime(time):
            str_time = datetime.strptime(time, '%H:%M:%S')
            seconds = str_time.hour * 3600 + str_time.minute * 60 +  str_time.second

        elif not self.__isPotiveTime(time) and self.__isBelowMinutes(time):
            str_time = datetime.strptime(time.strip('-'), '%M:%S')
            seconds = (str_time.minute * 60 +  str_time.second) * -1

        else:
            str_time = datetime.strptime(time, '%H:%M:%S')
            seconds = (str_time.hour * 3600 + str_time.minute * 60 +  str_time.second) * -1

        return seconds

    def __isBelowMinutes(self, time):
        return time.count(':') == 1
    
    def __isPotiveTime(self, time):
        return not '-' in time

    def __download(self):
        #TODO: 自動ダウンロードを実装
        self.__file_path = './chatlog_replay_jiW29RDj5Tc.json'
        return True

    def __register(self,chat):
        self.__chat_list.append(chat)



class VideoEditor:
    def __init__(self, detail, video):
        self.detail = detail
        self.video_list = [video]
    
    def edit(self):
        #TODO: Implement edit feature
        return self
    
    def combine(self, file_name):
        clips = self.__getClip()
        concatenate_videoclips(clips).write_videofile(file_name, codec='libx264')
        return Video(file_name, './' + file_name, '.mp4')

    def clip(self, chat_list):
        new_video_list = []
        #TODO:スパチャの内容の返答まで時間の幅をとれるようにしたい
        time_range = 60
        source = self.video_list[0]

        for chat in chat_list:
            #TODO: 配信開始前のスパチャにも対応できるようにする
            new_clip = source.clip.subclip(chat.seconds, chat.seconds + time_range)
            new_clip_name = source.name + str(chat.seconds) + '_' + str(chat.seconds + time_range) + '.' + source.extension
            new_video_list.append(Video(new_clip_name, './' + new_clip_name, '.mp4', new_clip))
            concatenate_videoclips([new_clip]).write_videofile(new_clip_name, codec='libx264')
        
        self.video_list = new_video_list
        return self

    def __getClip(self):
        clip_list = []
        for video in self.video_list:
            clip_list.append(video.clip)
        return clip_list



def main():
    chat_builder = ChatBulder('jiW29RDj5Tc')
    chat = chat_builder.create()
    detail_builder = DetailBuilder()
    detail_builder.makeUserList(chat, 'https://www.youtube.com/watch?v=jiW29RDj5Tc&ab_channel=%E5%B0%8F%E5%9F%8E%E5%A4%9C%E3%81%BF%E3%82%8B%E3%81%8F')
    detail = detail_builder.construct()
    video = Video('ogya', './ogya.mp4', '.mp4')
    video.download('test')
    video_editor = VideoEditor(detail, video)
    new_video = video_editor.clip(chat).combine('test.mp4')


if __name__ == "__main__":
    main()