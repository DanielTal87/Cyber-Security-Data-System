#!/usr/bin/python3

from server.server import app
from services.singleton import SingletonMetaClass
from services.logger import LoggerService
from services.mongoDB import MongoDbService

logger = LoggerService().logger

try:
    logger.info('##### CyBear - Cyber Security Data System #####')
    logger.info('Run mongo DB...')
    mongodb = MongoDbService()
# logging.debug('Run sqlite db...')
    # SqliteService()
    logger.info('Run server...')
    app.run(debug=True)
    logger.info('##### CyBear - Cyber Security Data System #####')
except KeyError as e:
    SingletonMetaClass.clear()