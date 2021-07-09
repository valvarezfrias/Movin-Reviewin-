import unittest
import requests
import json
import pandas as pd
import csv
import os
import random
from unittest import mock
from unittest.mock import patch
from main import displayCities, displayOccupation, userInfoApiRequest, informationDataFrame, randomIndex, randUserDataFrame


class TestFileName(unittest.TestCase):
    @mock.patch('builtins.input', create=True)
    def test_displayCities(self, mocked_input):
      displayCities.side_effect = '41620'
      self.assertEqual(displayCities, 41620)
      
      
    def test_displayOccupation(self):
      self.assertEqual(displayOccupation(151251), 151251)
      
    
    def test_userInfoApiRequest(self):
      data = {
        "41620" : "Salt Lake, Utah",
        "151251": "Computer Programmer"
      }
      df = pd.DataFrame(data, index=[0])
      self.assertEqual(userInfoApiRequest(41620, 151251), df)
      
      
    def test_informationDataFrame(self):
      vdf = pd.read_csv("visual_info.csv")
      self.assertEqual(informationDataFrame(), vdf)
      
    #We can test randomness  
    #def test_randomIndex(self):
      
    #This relies on the previous method  
#     def randUserDataFrame(self):
#         self.assertEqual(randUserDataFrame(2,1), 3)
#         self.assertEqual(randUserDataFrame(2.1, 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()