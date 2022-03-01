from django.test import TestCase
from .functions import to_coordinates, network_coverage_by_x_y,network_coverage_by_address

class NetworkCoverageTest(TestCase):
    def setUp(self):
        self.valid_address="9 rue Saint-Denis 44000 Nantes"
        self.invalid_address="555555"
        self.empty_address=None

        #exact coordinates for each provider in the csv file
        self.orange_coordinates_x=102980
        self.orange_coordinates_y=6847973
        self.sfr_coordinates_x=103113
        self.sfr_coordinates_y=6848661
        self.free_coordinates_x=128760
        self.free_coordinates_y=6833539
        self.bouygues_coordinates_x=103114
        self.bouygues_coordinates_y=6848664

    def test_to_coordinates(self):
        self.assertEqual(to_coordinates(self.valid_address), ("9 Rue Saint Denis 44000 Nantes",355689.3,6689665.04))
    
    def test_network_coverage_by_x_y(self):
        self.assertEqual(network_coverage_by_x_y(self.orange_coordinates_x,self.orange_coordinates_y)["Orange"], {"2G":True,"3G":True,"4G":False})
        self.assertEqual(network_coverage_by_x_y(self.sfr_coordinates_x,self.sfr_coordinates_y)["SFR"], {"2G":True,"3G":True,"4G":False})
        self.assertEqual(network_coverage_by_x_y(self.free_coordinates_x,self.free_coordinates_y)["Free"], {"2G":False,"3G":True,"4G":True})
        self.assertEqual(network_coverage_by_x_y(self.bouygues_coordinates_x,self.bouygues_coordinates_y)["Bouygues"], {"2G":True,"3G":True,"4G":True})
    
    def test_network_coverage_by_address(self):
        self.assertEqual(network_coverage_by_address(self.invalid_address), "invalid adress")
        self.assertEqual(network_coverage_by_address(self.empty_address), "No address provided")