import os

class Config:
    SECRET_KEY = os.environ.get('Anaheim')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://uapja7qv2u2sg4:p00802806ca704c63ed598aab27828902898e87a27ae62c932d71d0aaab1c0711@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d33pslt2mm5jv2')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


