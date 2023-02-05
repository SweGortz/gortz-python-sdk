import requests
import json
import urllib.parse


def _generate_request_search_criteria(search_criteria):
    url = ""
    for key, value in search_criteria:
        url += "&" + urllib.parse.quote(key) + "=" + urllib.parse.quote(str(value))
    return url


class Client:
    # Static
    # server_url = "http://localhost:8080"
    server_url = "https://api.gortz.org"
    __oauth2_client_name = "api"

    # User settings;
    access_token = ""
    refresh_token = ""

    def __init__(self):
        pass

    def authenticate(self, username, password):
        """ Uses user's credentials to authenticate.
        Generates the url to authenticate and request the access token as well
        as the refresh token from the server.
        Parameters
        ----------
        :param username:
            Username used to authenticate
        :param password:
            Password used to authenticates
        Raises
        ------
        :exception
            Exception raised when the server response is invalid
        """
        url = self.server_url + "/oauth/token?client_id=" + self.__oauth2_client_name + "&grant_type=password" \
                                                                                        "&username=" + \
              urllib.parse.quote(username) + \
              "&password=" + \
              urllib.parse.quote(password)
        # print(url)
        response = requests.post(url)

        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']
        elif response.status_code != 200:
            raise Exception(response.content.decode("utf-8"))

    def renew_access_token(self):
        """ Handles the renewal of the access token.
        """
        url = self.server_url + "/oauth/token?client_id=api&grant_type=refresh_token&refresh_token=" + \
              urllib.parse.quote(self.refresh_token)
        print(url)
        response = requests.post(url)
        if response.status_code == 200:
            response_json = json.loads(response.content.decode("utf-8"))
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']
            print(response_json)
        else:
            raise Exception(response.content.decode("utf-8"))

    def user(self):
        """ Handles the query to get the user.
        Returns
        -------
        :return:
            The query result in JSON format
        """
        url = self.server_url + "/v0/users/me?access_token=" + \
              urllib.parse.quote(self.access_token)
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))

    def user_roles(self):
        """ Handles the query to get users roles.
        Returns
        -------
        :return:
            The query result in JSON format
        """
        url = self.server_url + "/v0/users/me/roles?access_token=" + \
              urllib.parse.quote(self.access_token)
        # print(url)
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            # print(response.content.decode("utf-8"))
            raise Exception(response.content.decode("utf-8"))
        return json.loads(response.content.decode("utf-8"))
