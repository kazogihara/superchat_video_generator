import os, sys
import unittest
from unittest.mock import patch, mock_open, MagicMock

# Allow direct execution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # noqa

from superchat_video_generator import Chat, ChatBulder


class ChatBuilderTest(unittest.TestCase):
    
    def test_create_FourChatRow_TwoRow(self):
        chat_builder =  ChatBulder('test_videoid')
        file_content_mock =  """{"user": "test1", "timestampUsec": "1642150951651549", "time": "-57:54", "authorbadge": "test1 authorbadge", "text": "test1 text", "purchaseAmount": "￥500", "type": "NORMALCHAT", "video_id": "jiW29RDj5Tc", "Chat_No": "00001"}
{"user": "test2", "timestampUsec": "1642150976967054", "time": "5:00", "authorbadge": "test2 authorbadge", "text": "test2 text", "purchaseAmount": "￥500", "type": "NORMALCHAT", "video_id": "jiW29RDj5Tc", "Chat_No": "00002"}
{"user": "test3", "timestampUsec": "1642151816223176", "time": "10:00", "authorbadge": "test3 authorbadge", "text": "test3 text", "purchaseAmount": "", "type": "NORMALCHAT", "video_id": "jiW29RDj5Tc", "Chat_No": "00003"}
{"user": "test4", "timestampUsec": "1642151936681859", "time": "1:00:00", "authorbadge": "test4 authorbadge", "text": "test4 text", "purchaseAmount": "￥500", "type": "NORMALCHAT", "video_id": "jiW29RDj5Tc", "Chat_No": "00004"}"""
        open_chat_file_mock = mock_open(read_data=file_content_mock)
        
        positive_purchased_below_minutes_chat = Chat('test2', '5:00', 'test2 authorbadge', 'test2 text', '￥500', 300)
        positive_purchased__chat = Chat('test4', '1:00:00', 'test4 authorbadge', 'test4 text', '￥500', 3600)
        with patch("superchat_video_generator.open", open_chat_file_mock, create=True):
            chat_list = chat_builder.create()
            self.assertEqual([positive_purchased_below_minutes_chat, positive_purchased__chat],chat_list)
if __name__ == '__main__':
    unittest.main()

