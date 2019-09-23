import unittest
from unittest.mock import patch, mock_open
from src.DataPreparation.FetchCommits import FetchCommits

def openMock(self, file: str, mode: str, encoding: str):
    return None

#TODO How to mock open
class FetchCommitsTest(unittest.TestCase):
    def test_when_setup_then_values_are_set(self):
        file = 'test/commit.csv'
        mode = 'r'
        encoding = 'utf-8'
        delimiter = '\t'

        t = FetchCommits(openMock, file, mode, encoding, delimiter)
        t.Load()

        self.assertEqual(file, t)