from unittest import mock
from superchat_video_generator import Video, video_split
import json

def testVideoSplit01():
    video = Video('./nenemaru.mp4','mp4')
    superchat_comment = open('video_split_test_data.json')
    video_split(video,superchat_comment)