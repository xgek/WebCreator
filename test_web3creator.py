# test_web3creator.py
"""
Tests for Web3Creator module.
"""

import unittest
from web3creator import Web3Creator

class TestWeb3Creator(unittest.TestCase):
    """Test cases for Web3Creator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Creator()
        self.assertIsInstance(instance, Web3Creator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3Creator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
