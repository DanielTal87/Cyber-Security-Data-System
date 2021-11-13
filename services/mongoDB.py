#!/usr/bin/python3

import pymongo

from services.config import ConfigService
from services.logger import LoggerService
from services.singleton import SingletonMetaClass

config = ConfigService().config
logger = LoggerService().logger
DB_NAME = 'CSDS'  # Cyber Security Data System


class MongoDbService(metaclass=SingletonMetaClass):
    def __init__(self):
        logger.info(f'MongoDbService / init - start')
        self.__client = pymongo.MongoClient(config['mongodb']['url'], config['mongodb']['port'])
        logger.info(f'MongoDbService/init - end')

    @property
    def client(self):
        return self.__client
