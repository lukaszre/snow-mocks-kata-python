from abc import ABCMeta, abstractmethod


class PressServices:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def send_weather_alert(self):
        pass
