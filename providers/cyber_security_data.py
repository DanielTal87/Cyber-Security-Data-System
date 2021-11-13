from providers.connector import Connector
from services.logger import LoggerService
from services.mongoDB import MongoDbService

logger = LoggerService().logger
mongoDbService = MongoDbService().client


def insert_cyber_security_data(source, payload) -> Connector:
    logger.info(f'Cyber Security Data Service / insert_cyber_security_data - Start')
    connector = Connector(source, payload)
    print(f'connector = {connector.payload}')
    _id = insert_cyber_security_data_to_db(connector)
    logger.info(f'Cyber Security Data Service / insert_cyber_security_data - End successfully '
                f'| connector = {connector}, id = {_id}')
    return connector


def insert_cyber_security_data_to_db(connector: Connector):
    logger.info(f'Insert connector to DB | Connector = {connector}')
    print(f'Insert connector to DB | Connector = {connector}')  # just for the reviewers
    return mongoDbService.CSDS[connector.source].insert_one(connector.payload).inserted_id


def get_collection(source):
    cursor = mongoDbService.CSDS[source].find({})
    print(f'Get all {source} data from DB')  # just for the reviewers
    for document in cursor:
        print(document)
