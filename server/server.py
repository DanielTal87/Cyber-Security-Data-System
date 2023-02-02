import json

from flask import Flask
from flask_restful import Api, Resource, reqparse

from providers.health_check import random_health_check
from providers.cyber_security_data import insert_cyber_security_data, get_collection
from services.logger import LoggerService

logger = LoggerService().logger
app = Flask(__name__)
api = Api(app)


class HealthCheck(Resource):
    def get(self):
        """
        Checking if the service is alive.
        For the assignment the API may return a failure
        :return: True/False randomly
        """
        logger.info(f'Server / HealthCheck | start')
        try:
            random_health_check()
        except Exception as error:
            logger.error(
                f'Server / HealthCheck | failed with an error: type = {error.__class__.__name__}, message = {error}')
            return {
                'message': 'Health check failed'
            }, 503
        else:
            logger.info(f'Server / HealthCheck | Ended successfully')
            return {
                'message': "It's Alive, It's Alive..."
            }, 200


class CyberSecurityData(Resource):
    def post(self, source):
        """
        Add a new cyber security data from the source
        :param source - the source of the cyber security data
        :return: success - if insert a new security data to the db insert succeeded, failure otherwise
        """
        logger.info(f'CyberSecurityData / post | Start')
        try:
            args = parser.parse_args()
            if args['data'] is None:
                return {
                    'message': "The request must be json with format {'data': 'data_to_insert_as_json'}"
                }, 422
            data = args['data']
            logger.debug(
                f'CyberSecurityData / post | Insert a new cyber security data to the db | source = {source}, data = {data}')
            json_acceptable_string = data.replace("'", "\"")
            connector = insert_cyber_security_data(source,
                                                   json.loads(json_acceptable_string))  # need to raise exception
            logger.debug(
                f'CyberSecurityData / post | A new cyber security data to the db insert successfully | connector = {connector}')
        except Exception as error:
            logger.error(
                f'CyberSecurityData / post | Ended with failure | Error: type = {error.__class__.__name__}, message = {error}')
            return {
                'message': "Insert a new cyber security data",
                'status': 'failed'
            }, 400
        else:
            logger.info(f'CyberSecurityData / post | Ended successfully')
            return {
                'id': connector.id,
                'message': "Insert a new cyber security data",
                'status': 'success'
            }, 201

    def get(self, source):
        """
        Print all the cyber security data for the given source
        :param source - the source of the cyber security data
        :return: success - if getting the source collection succeeded, failure otherwise
        """
        logger.info(f'CyberSecurityData / get | Start')
        try:
            get_collection(source)
        except Exception as error:
            logger.error(
                f'CyberSecurityData / get | Ended with failure | Error: type = {error.__class__.__name__}, message = {error}')
            return {
                'message': 'Printing the {source} collection',
                'status': 'failed'
            }, 400
        else:
            logger.info(f'CyberSecurityData / post | Ended successfully')
            return {
                'message': f'Printing the {source} collection',
                'status': 'success'
            }, 201


api.add_resource(HealthCheck, '/health-check')
api.add_resource(CyberSecurityData, '/cyber-security-data/<string:source>')
parser = reqparse.RequestParser()
parser.add_argument('data')
