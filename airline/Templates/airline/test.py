from django.test import TestCase


class FlightTestCase(TestCase):
    def setUp(self):
        Flight.objects.create(name="", age="")
        Flight.objects.create(name="", age="")

    def flightscheck(self):
       
        flight = Flight.objects.get(name=" ")
        flight2 = Flight.objects.get(name=" ")
        self.assertEqual(test.speak(), '"')
        self.assertEqual(test.speak(), '"')
        ()

