import os

class Config:
    SECRET_KEY = '3691bb1ce3f7e83705e5946b16942f53104c10825b7da7b3bb302ddb93294ccc'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/instance/notesoft.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
