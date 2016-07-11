import os

from django.core.files import File

import tests


def create_test_video():
    video_file = open(os.path.join(tests.__path__[0], 'small.mp4'), 'rb')
    return File(video_file, name='small.mp4')
