""" BIG MARKER API CONNECTION MODULE """
import requests
from requests.exceptions import HTTPError

#Bigmarker V1 API Endpoints
bm_show_conf_details_url = "https://www.bigmarker.com/api/v1/conferences/conference_id"
bm_show_atendee_list_url = "https://www.bigmarker.com/api/v1/conferences/"
bm_show_conf_list_url = "https://www.bigmarker.com/api/v1/conferences/"



class Bmconn:
    def __init__(self,api_key):
        self.api_key = api_key

    def get_conferences(self):
        """ Retrieves a list of conferences from Big Marker"""
        url = bm_show_conf_list_url        
        header = {'Content-type': 'application/json', 'API-KEY':self.api_key}
        try:
            response = requests.get(url,headers = header)
            print("Status code: ", response.status_code)
            response_Json = response.json()
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')
            print("Printing Post JSON data")
            print(response_Json['conferences'])
            return response_Json['conferences']

    def get_conf_id(self,title):
        """ Returns a conference id from a given conference title """

    def get_atendees(self,conference_id):
        """ Retrieves the list of atendees from a given Big Marker conference id"""
        url = bm_show_atendee_list_url + conference_id + "/attendees"
        print("Attendees url:",url)

        header = {'Content-type': 'application/json', 'API-KEY':self.api_key}
        try:
            response = requests.get(url,headers = header)
            print("Status code: ", response.status_code)
            response_Json = response.json()
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')
            print("Printing Post JSON data")
            print(response_Json)
            return response_Json
    