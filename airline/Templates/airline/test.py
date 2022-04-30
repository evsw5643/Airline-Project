from django.test import TestCase


class AirplaneTestCase(TestCase):
    def setUp(self):
        Airplane.objects.create(name="H&W5643", airplane="")
        Flight.objects.create(name="", age="")

    def flightscheck(self):
       
        flight = Flight.objects.get(name=" ")
        flight2 = Flight.objects.get(name=" ")
        self.assertEqual(test.speak(), '"')
        self.assertEqual(test.speak(), '"')
        ()