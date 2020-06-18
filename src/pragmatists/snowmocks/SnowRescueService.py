from src.pragmatists.snowmocks.dependencies.SnowplowMalfunctioningException import SnowplowMulfunctioningException


class SnowRescueService(object):
    def __init__(self, municipal_service, weather_forecast_service, press_services):
        self.municipal_service = municipal_service
        self.weather_forecast_service = weather_forecast_service
        self.press_services = press_services

    def check_forecast_and_rescue(self):
        if self.weather_forecast_service.get_average_temperature_in_celsius() < 0:
            self.municipal_service.send_sander()
        if self.weather_forecast_service.get_snow_fall_height_in_mm() >= 3:
            self.send_snowplow()
            if self.weather_forecast_service.get_snow_fall_height_in_mm() >= 5:
                self.send_snowplow()
                if self.weather_forecast_service.get_snow_fall_height_in_mm() >= 10:
                    self.send_snowplow()
                    self.press_services.send_weather_alert()

    def send_snowplow(self):
        try:
            self.municipal_service.send_snowplow()
        except SnowplowMulfunctioningException:
            self.municipal_service.send_snowplow()
            pass
