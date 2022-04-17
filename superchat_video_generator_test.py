import filecmp
import unittest
from superchat_video_generator import Video, createOverview, getChatFile, getVideoFile, extractSuperChatComment
import json
from unittest import mock
import filecmp

class SuperChantVideoGeneratorTest(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetFileName(self):
        self.assertEqual(Video('test','mp4').getFileName(),'test.mp4')

    def testGetVideoFile(self):
        self.assertEqual(type(getVideoFile()),type(Video('test','mp4')))
    
    def testgetChatFile(self):
        self.assertEqual(getChatFile(),'./chatlog_replay_PF2ylueaAQU.json')
    
    def testExtractSuperchatComment(self):
        self.assertEqual(extractSuperChatComment('./test/test_chatlog_replay.json'),[{'user': 'れんこん', 'timestampUsec': '1649848205102944', 'time': '5:46', 'authorbadge': '', 'text': '助かる代', 'purchaseAmount': '￥250', 'type': 'SUPERCHAT', 'video_id': 'PF2ylueaAQU', 'Chat_No': '00263'},{'user':'TeraKun', 'timestampUsec':'1649848201712242', 'time':'5:46', 'authorbadge':'新規メンバー', 'text':'なってますねー', 'purchaseAmount':'￥500', 'type':'NORMALCHAT', 'video_id':'PF2ylueaAQU', 'Chat_No':'00262'}])

    def testCreateOverview(self):
        overviewTestFile = open("./test/abstract_test.txt",'r')
        createOverview([{'user': 'れんこん', 'timestampUsec': '1649848205102944', 'time': '5:46', 'authorbadge': '', 'text': '助かる代', 'purchaseAmount': '￥250', 'type': 'SUPERCHAT', 'video_id': 'PF2ylueaAQU', 'Chat_No': '00263'},{'user':'TeraKun', 'timestampUsec':'1649848201712242', 'time':'5:46', 'authorbadge':'新規メンバー', 'text':'なってますねー', 'purchaseAmount':'￥500', 'type':'NORMALCHAT', 'video_id':'PF2ylueaAQU', 'Chat_No':'00262'}], 'https://www.youtube.com/watch?v=PF2ylueaAQU&t=')
        overviewFile = open("./abstract.txt",'r')
        self.assertEqual(overviewTestFile.readlines(),overviewFile.readlines())
        overviewTestFile.close()