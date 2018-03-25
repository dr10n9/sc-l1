"""lab1 req module"""

import requests
URL = "http://api.tvmaze.com/schedule"


class Request:
    """class for request obj"""

    def __init__(self):
        self.__region = ""
        self.__date = ""
        self.__start_time = ""
        self.__end_time = ""

    def set_region(self, region):
        self.__region = region

    def set_date(self, date):
        self.__date = date

    def set_time(self, start_time, end_time):
        if end_time < start_time:
            print("wrong time")
        else:
            self.__start_time = start_time
            self.__end_time = end_time

    def clear_fields(self):
        self.__region = ""
        self.__date = ""
        self.__start_time = ""
        self.__end_time = ""
        print("fields are empty now")

    def get_infos(self, channel):
        if self.__region == "":
            print("no region set")
        if self.__date == "":
            print("no data set")
        if self.__start_time == "":
            print('no time set')
        req_url = URL + '?country=' + self.__region + '&date=' + self.__date
        res = requests.get(req_url).json()
        for obj in res:
            if (obj['show']['network']['name']) == channel:
                print(obj['show']['name'])