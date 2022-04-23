import os, sys
import unittest
from unittest.mock import patch, mock_open

# Allow direct execution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # noqa

from superchat_video_generator import Chat, DetailBuilder


class DetailBuildeTest(unittest.TestCase):
    
    def test_makeUserList_twoChatUser_twoDescriptionRow(self):
        description_mock = mock_open()

        test_chat1 = Chat('testchat1' ,'00:00', '', 'this is testchat1', '200', '0')
        test_chat2 = Chat('testchat2' ,'10:00', '', 'this is testchat2', '300', '600')
        detail_builder =  DetailBuilder()
        
        with patch("superchat_video_generator.open", description_mock, create=True):
            detail_builder.makeUserList([test_chat1, test_chat2], 'https://www.youtube.com/watch?v=test&ab_channel=test')
            description_mock.assert_called_with("./description.txt", "w", encoding='utf-8')
            description_mock.return_value.write.assert_any_call('00:00 testchat1さん https://www.youtube.com/watch?v=test&ab_channel=test&t=0s\n')
            description_mock.return_value.write.assert_any_call('10:00 testchat2さん https://www.youtube.com/watch?v=test&ab_channel=test&t=600s\n')

if __name__ == '__main__':
    unittest.main()

