from abc import ABCMeta, abstractmethod


class MunicipalServices:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def send_snowplow(self):
        pass

    @abstractmethod
    def send_sander(self):
        pass
