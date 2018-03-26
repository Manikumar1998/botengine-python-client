import uuid
import requests
from QueryMessage import Message
from InvokeTrigger import Trigger

class BotEngine(object):
    """
    Main endpoint for using botengine.ai
    provices request.
    """

    @property
    def developer_access_token(self):
        """
            Developer access token provided by https://botengine.ai/

            :rtype: str or unicode
        """
        return self._developer_access_token

    @developer_access_token.setter
    def developer_access_token(self, developer_access_token):
        """
            :type: str or unicode
        """
        self._developer_access_token = developer_access_token

    @property
    def session_id(self):
        """
            session_id user for unique identifier of current application user.

            :rtype: str or unicode
        """

        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
            :type session_id: str or unicode
        """

        self._session_id = session_id

    def __init__(self, developer_access_token, session_id=None):
        super(BotEngine, self).__init__()
        self._developer_access_token = developer_access_token
        self._base_url = "https://api.botengine.ai/query"

        if session_id is None:
            self._session_id = uuid.uuid4().hex
        else:
            self._session_id = session_id

    def message(self):
        """
            Construct a text message request
            :rtype Message:
        """

        request = Message(
            self.developer_access_token,
            self._base_url,
            self.session_id
        )
        return request

    def trigger(self):
        """
            Invoke a trigger at endpoints
            :rtype Trigger:
        """
        request = Trigger(
            self.developer_access_token,
            self._base_url,
            self.session_id
        )
        return request
