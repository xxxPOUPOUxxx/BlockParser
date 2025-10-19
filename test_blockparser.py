# test_blockparser.py
"""
Tests for BlockParser module.
"""

import unittest
from blockparser import BlockParser

class TestBlockParser(unittest.TestCase):
    """Test cases for BlockParser class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockParser()
        self.assertIsInstance(instance, BlockParser)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockParser()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
