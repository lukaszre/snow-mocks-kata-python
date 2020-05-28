Snow Mocks
==========

## Run tests

`python SnowRescueServiceTest.py`


## Task

Your task is to implement SnowRescueService class - this is your System Under Test. Treat all other classes as dependencies.

1. Send sander if temperature will be below 0 C

2. Send snowplow if snowfall exceed 3 mm
	
3. If snowplow fails (SnowplowMalfunctioningException) - send another
		
4. Send two snowplows if snowfall exceed 5 mm

5. If temperature drops below -10 and snowfall exceed 10 mm, send three snowplows, a sander and notify press. 


## Zadanie

Zaimplementuj klasę SnowRescueService - to jest Twój SUT.
	wszystkie pozostałe klasy potraktuj jako zależności.

1. Wyślij piaskarkę (sander) tylko jeśli temperatura będzie poniżej 0 C

2. Wyślij pług (snowplow) tylko jeśli opady śniegu przekroczą 3 mm
	2a) jeśli pług nawali (SnowplowMalfunctioningException) - wyślij kolejny
		
3. Wyślij dwa pługi tylko jeśli opady śniegu przekroczą 5 mm

4. Jeśli temperatura będzie poniżej -10 i opady śniegu przekroczą 10 mm, najpierw wyślij trzy pługi, potem piaskarkę a potem powiadom prasę. 	 


## unittest framework

https://docs.python.org/3/library/unittest.html#module-unittest
