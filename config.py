import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'J\xbc\x02\xd6\x7f\x8a\x14X\xf3<\x9e\x04!J\xd1'

    MONGODB_SETTINGS = { 'db' : 'sample_enrolment' }
