# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_404_error 1'] = {
    'code': 404,
    'message': 'Nothing matches the given URI'
}

snapshots['test_405_error 1'] = {
    'code': 405,
    'message': 'Specified method is invalid for this resource'
}

snapshots['test_api_index 1'] = {
    'code': 200,
    'message': "Welcome to Dipp's code challenge."
}
