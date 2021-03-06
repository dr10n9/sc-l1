"""lab1 req module"""

import requests
URL = "http://api.tvmaze.com/schedule"


class Request:
    """class for request obj"""

    def __init__(self, region=None, date=None, start_time=None, end_time=None):
        self.__region = region
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def set_region(self, region):
        self.__region = region

    def set_date(self, date):
        self.__date = date

    def set_time(self, start_time, end_time):
        if end_time < start_time:
            raise Exception("wrong time")
        else:
            self.__start_time = start_time
            self.__end_time = end_time

    def clear_fields(self):
        self.__region = ""
        self.__date = ""
        self.__start_time = ""
        self.__end_time = ""
        print("fields are empty now")

    def get_region(self):
        return self.__region

    def get_date(self):
        return self.__date

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_infos_List(self, channel):
        if self.__region == "":
            print("no region set")
        if self.__date == "":
            print("no data set")
        if self.__start_time == "":
            print('no time set')
        req_url = URL + '?country=' + self.__region + '&date=' + self.__date
        APIresponse = requests.get(req_url).json()
        output_response = []
        for obj in APIresponse:
            if obj is not None:
                try:
                    if (obj['show']['network']['name']) == channel:
                        if (obj['show']['type']) == "News":
                            obj_time = obj['show']['schedule']['time']
                            if (obj_time > self.__start_time) and (
                              obj_time < self.__end_time):
                                output_response.append(obj['show']['name'])
                except(TypeError):
                    print("Type err")

        return output_response
