import json
import requests

class Message(object):
    """
        Message request classes

        Send simple text queries.
    """

    @property
    def query(self):
        """
            Query parameter can be a string
            Default equal None, The user should fill this field
            before sending the request
        """
        return self._query

    @query.setter
    def query(self, query):
        self._query = query


    @property
    def parameters(self):
        """
            parameters dict
            Default equal {}, Optional field
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        if type(parameters) is not dict:
            raise TypeError('parameters should be a dict')
        self._parameters = parameters

    @property
    def developer_access_token(self):
        """
            The developer_access_token access token to
            connect to botengine agent
        """
        return self._developer_access_token

    @developer_access_token.setter
    def developer_access_token(self, developer_access_token):
        self._developer_access_token = developer_access_token


    def __init__(self, developer_access_token, base_url, session_id):
        self.query = None
        self.parameters = {}
        self.developer_access_token = developer_access_token
        self.base_url = base_url
        self.session_id = session_id

    def _prepare_headers(self):
        Authorization = 'Bearer '+ self.developer_access_token
        return {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': Authorization}

    def _prepare_json_body(self):
        return {'sessionId':self.session_id, 'query':self.query,
                'parameters': self.parameters}

    def getresponse(self):
        """
            Send all the data to agent and wait for response
        """
        response = requests.post(self.base_url, headers=self._prepare_headers(),\
                                json=self._prepare_json_body())
        return response

