import unittest


from unittest.mock import Mock

from src.pragmatists.snowmocks.SnowRescueService import SnowRescueService
from src.pragmatists.snowmocks.dependencies.PressService import PressServices
from src.pragmatists.snowmocks.dependencies.MunicipalServices import MunicipalServices
from src.pragmatists.snowmocks.dependencies.SnowplowMalfunctioningException import SnowplowMulfunctioningException
from src.pragmatists.snowmocks.dependencies.WeatherForecastService import WeatherForecastService


class SnowRescueServiceTest(unittest.TestCase):

    def setUp(self):
        self.weather_forecast_service = Mock(spec=WeatherForecastService)
        self.municipal_services = Mock(spec=MunicipalServices)
        self.press_services = Mock(spec=PressServices)

        self.weather_forecast_service.get_average_temperature_in_celsius.return_value = 1
        self.weather_forecast_service.get_snow_fall_height_in_mm.return_value = 0

        self.snow_resource_service = SnowRescueService(self.municipal_services, self.weather_forecast_service,
                                                       self.press_services)

    def test_send_sander_when_temperature_is_below_0(self):
        self.weather_forecast_service.get_average_temperature_in_celsius.return_value = -1

        self.snow_resource_service.check_forecast_and_rescue()

        self.municipal_services.send_sander.assert_called()

    def test_do_not_send_sander_when_temperature_is_greater_or_equal_0(self):
        self.weather_forecast_service.get_average_temperature_in_celsius.return_value = 1

        self.snow_resource_service.check_forecast_and_rescue()

        self.municipal_services.send_sander.assert_not_called()

    def test_send_snowplow_when_snowfall_exceed_3_mm(self):
        self.weather_forecast_service.get_snow_fall_height_in_mm.return_value = 3

        self.snow_resource_service.check_forecast_and_rescue()

        self.municipal_services.send_snowplow.assert_called_once()

    def test_do_not_send_snowplow_when_snowfall_do_not_exceed_3_mm(self):
        self.weather_forecast_service.get_snow_fall_height_in_mm.return_value = 0

        self.snow_resource_service.check_forecast_and_rescue()

        self.municipal_services.send_snowplow.assert_not_called()

    def test_send_another_snowplow_when_first_will_fail(self):
        self.weather_forecast_service.get_snow_fall_height_in_mm.return_value = 3
        self.municipal_services.send_snowplow.side_effect = [SnowplowMulfunctioningException, None]

        self.snow_resource_service.check_forecast_and_rescue()

        self.assertEqual(2, self.municipal_services.send_snowplow.call_count)

    def test_send_two_snowplows_when_snowfall_exceed_5_mm(self):
        self.weather_forecast_service.get_snow_fall_height_in_mm.return_value = 5

        self.snow_resource_service.check_forecast_and_rescue()

        self.assertEqual(2, self.municipal_services.send_snowplow.call_count)

    def test_send_3_snowplows_sander_and_notify_press_when_snowfall_exceed_10_mm_and_temperature_exceed_minus10(self):
        self.weather_forecast_service.get_snow_fall_height_in_mm.return_value = 10
        self.weather_forecast_service.get_average_temperature_in_celsius.return_value = -10

        self.snow_resource_service.check_forecast_and_rescue()

        self.assertEqual(3, self.municipal_services.send_snowplow.call_count)
        self.municipal_services.send_sander.assert_called()
        self.press_services.send_weather_alert.assert_called()


if __name__ == '__main__':
    unittest.main()

