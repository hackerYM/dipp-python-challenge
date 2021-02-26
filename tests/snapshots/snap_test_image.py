# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_400_by_ghost_image_url 1'] = {
    'code': 400,
    'message': "Can not get file's data from url"
}

snapshots['test_400_by_small_box 1'] = {
    'code': 400,
    'message': 'Can not make a text fit in a box'
}

snapshots['test_400_by_wrong_height 1'] = {
    'code': 400,
    'message': [
        "['box', 'height'] / -100 is less than the minimum of 0"
    ]
}

snapshots['test_400_by_wrong_image_url 1'] = {
    'code': 400,
    'message': [
        "['image_url'] / 'no-image-url' does not match '(http|https)://([\\\\w_-]+(?:(?:\\\\.[\\\\w_-]+)+))([\\\\w.,@?^=%&:/~+#-]*[\\\\w@?^=%&/~+#-])?'"
    ]
}

snapshots['test_400_by_wrong_text_color 1'] = {
    'code': 400,
    'message': [
        "['text', 'text_color'] / 'no-hex-code' does not match '#([a-fA-F0-9]{6}|[a-fA-F0-9]{8})$'"
    ]
}

snapshots['test_400_by_wrong_width 1'] = {
    'code': 400,
    'message': [
        "['box', 'width'] / -100 is less than the minimum of 0"
    ]
}

snapshots['test_api_image_with_horizontal_rectangle 1'] = [
    {
        'content': 'Dipp inc, thinking out of how',
        'font_size': 43,
        'x': 60,
        'y': 102
    },
    {
        'content': 'to draw a text on the box.',
        'font_size': 43,
        'x': 60,
        'y': 145
    }
]

snapshots['test_api_image_with_square_box 1'] = [
    {
        'content': 'Dipp inc,',
        'font_size': 90,
        'x': 50,
        'y': 112
    },
    {
        'content': 'thinking out',
        'font_size': 90,
        'x': 50,
        'y': 202
    },
    {
        'content': 'of how to',
        'font_size': 90,
        'x': 50,
        'y': 292
    },
    {
        'content': 'draw a text',
        'font_size': 90,
        'x': 50,
        'y': 382
    },
    {
        'content': 'on the box.',
        'font_size': 90,
        'x': 50,
        'y': 472
    }
]

snapshots['test_api_image_with_super_long_content 1'] = [
    {
        'content': 'draw the text box with a super long',
        'font_size': 29,
        'x': 50,
        'y': 112
    },
    {
        'content': 'content draw the text box with a',
        'font_size': 29,
        'x': 50,
        'y': 141
    },
    {
        'content': 'super long content draw the text',
        'font_size': 29,
        'x': 50,
        'y': 170
    },
    {
        'content': 'box with a super long content draw',
        'font_size': 29,
        'x': 50,
        'y': 199
    },
    {
        'content': 'the text box with a super long',
        'font_size': 29,
        'x': 50,
        'y': 228
    },
    {
        'content': 'content draw the text box with a',
        'font_size': 29,
        'x': 50,
        'y': 257
    },
    {
        'content': 'super long content draw the text',
        'font_size': 29,
        'x': 50,
        'y': 286
    },
    {
        'content': 'box with a super long content draw',
        'font_size': 29,
        'x': 50,
        'y': 315
    },
    {
        'content': 'the text box with a super long',
        'font_size': 29,
        'x': 50,
        'y': 344
    },
    {
        'content': 'content draw the text box with a',
        'font_size': 29,
        'x': 50,
        'y': 373
    },
    {
        'content': 'super long content draw the text',
        'font_size': 29,
        'x': 50,
        'y': 402
    },
    {
        'content': 'box with a super long content draw',
        'font_size': 29,
        'x': 50,
        'y': 431
    },
    {
        'content': 'the text box with a super long',
        'font_size': 29,
        'x': 50,
        'y': 460
    },
    {
        'content': 'content',
        'font_size': 29,
        'x': 50,
        'y': 489
    }
]

snapshots['test_api_image_with_vertical_rectangle 1'] = [
    {
        'content': 'Dipp',
        'font_size': 26,
        'x': 42,
        'y': 125
    },
    {
        'content': 'inc,',
        'font_size': 26,
        'x': 42,
        'y': 151
    },
    {
        'content': 'thinking',
        'font_size': 26,
        'x': 42,
        'y': 177
    },
    {
        'content': 'out of',
        'font_size': 26,
        'x': 42,
        'y': 203
    },
    {
        'content': 'how to',
        'font_size': 26,
        'x': 42,
        'y': 229
    },
    {
        'content': 'draw a',
        'font_size': 26,
        'x': 42,
        'y': 255
    },
    {
        'content': 'text on',
        'font_size': 26,
        'x': 42,
        'y': 281
    },
    {
        'content': 'the box.',
        'font_size': 26,
        'x': 42,
        'y': 307
    }
]
