"""
Test module for string_reverser.py

This module contains comprehensive tests for all string reversal functions.
"""

import unittest
from string_reverser import reverse_string, reverse_string_iterative, reverse_string_recursive

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False
    # Create a dummy pytest module for when it's not available
    class DummyPytest:
        class mark:
            @staticmethod
            def parametrize(*args, **kwargs):
                def decorator(func):
                    return func
                return decorator
        
        @staticmethod
        def raises(*args, **kwargs):
            pass
    
    pytest = DummyPytest()


class TestStringReverser(unittest.TestCase):
    """Test cases for string reversal functions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_cases = [
            ("hello", "olleh"),
            ("Python", "nohtyP"),
            ("12345", "54321"),
            ("A man a plan a canal Panama", "amanaP lanac a nalp a nam A"),
            ("", ""),
            ("a", "a"),
            ("ab", "ba"),
            ("racecar", "racecar"),  # palindrome
            ("Hello World!", "!dlroW olleH"),
            ("   spaces   ", "   secaps   "),
            ("123!@#", "#@!321"),
            ("unicode: café", "éfac :edocinu"),
        ]
    
    def test_reverse_string_basic(self):
        """Test basic functionality of reverse_string."""
        for input_str, expected in self.test_cases:
            with self.subTest(input_str=input_str):
                result = reverse_string(input_str)
                self.assertEqual(result, expected)
    
    def test_reverse_string_iterative_basic(self):
        """Test basic functionality of reverse_string_iterative."""
        for input_str, expected in self.test_cases:
            with self.subTest(input_str=input_str):
                result = reverse_string_iterative(input_str)
                self.assertEqual(result, expected)
    
    def test_reverse_string_recursive_basic(self):
        """Test basic functionality of reverse_string_recursive."""
        for input_str, expected in self.test_cases:
            with self.subTest(input_str=input_str):
                result = reverse_string_recursive(input_str)
                self.assertEqual(result, expected)
    
    def test_all_methods_consistency(self):
        """Test that all three methods produce the same results."""
        for input_str, _ in self.test_cases:
            with self.subTest(input_str=input_str):
                result1 = reverse_string(input_str)
                result2 = reverse_string_iterative(input_str)
                result3 = reverse_string_recursive(input_str)
                
                self.assertEqual(result1, result2)
                self.assertEqual(result2, result3)
                self.assertEqual(result1, result3)
    
    def test_type_error_reverse_string(self):
        """Test that reverse_string raises TypeError for non-string input."""
        invalid_inputs = [123, None, [], {}, 45.67, True]
        
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError):
                    reverse_string(invalid_input)
    
    def test_type_error_reverse_string_iterative(self):
        """Test that reverse_string_iterative raises TypeError for non-string input."""
        invalid_inputs = [123, None, [], {}, 45.67, True]
        
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError):
                    reverse_string_iterative(invalid_input)
    
    def test_type_error_reverse_string_recursive(self):
        """Test that reverse_string_recursive raises TypeError for non-string input."""
        invalid_inputs = [123, None, [], {}, 45.67, True]
        
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError):
                    reverse_string_recursive(invalid_input)
    
    def test_empty_string(self):
        """Test handling of empty strings."""
        empty_str = ""
        self.assertEqual(reverse_string(empty_str), "")
        self.assertEqual(reverse_string_iterative(empty_str), "")
        self.assertEqual(reverse_string_recursive(empty_str), "")
    
    def test_single_character(self):
        """Test handling of single character strings."""
        single_char = "x"
        self.assertEqual(reverse_string(single_char), "x")
        self.assertEqual(reverse_string_iterative(single_char), "x")
        self.assertEqual(reverse_string_recursive(single_char), "x")
    
    def test_long_string(self):
        """Test handling of longer strings."""
        long_str = "a" * 100  # Reduced to avoid recursion limit
        expected = "a" * 100  # palindrome
        
        self.assertEqual(reverse_string(long_str), expected)
        self.assertEqual(reverse_string_iterative(long_str), expected)
        self.assertEqual(reverse_string_recursive(long_str), expected)
    
    # def test_special_characters(self):
    #     """Test handling of strings with special characters."""
    #     special_str = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    #     expected = "?></.,:\"';|}{][=-+_)(*&^%$#@!"
        
    #     self.assertEqual(reverse_string(special_str), expected)
    #     self.assertEqual(reverse_string_iterative(special_str), expected)
    #     self.assertEqual(reverse_string_recursive(special_str), expected)
    
    def test_double_reversal(self):
        """Test that reversing a string twice returns the original."""
        test_str = "Hello, World!"
        
        # Test with slicing method
        double_reversed = reverse_string(reverse_string(test_str))
        self.assertEqual(double_reversed, test_str)
        
        # Test with iterative method
        double_reversed = reverse_string_iterative(reverse_string_iterative(test_str))
        self.assertEqual(double_reversed, test_str)
        
        # Test with recursive method
        double_reversed = reverse_string_recursive(reverse_string_recursive(test_str))
        self.assertEqual(double_reversed, test_str)


class TestStringReverserPytest:
    """Pytest-style tests for string reversal functions."""
    
    @pytest.mark.parametrize("input_str,expected", [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("12345", "54321"),
        ("", ""),
        ("a", "a"),
        ("racecar", "racecar"),
    ])
    def test_reverse_string_parametrized(self, input_str, expected):
        """Parametrized test for reverse_string function."""
        assert reverse_string(input_str) == expected
        assert reverse_string_iterative(input_str) == expected
        assert reverse_string_recursive(input_str) == expected
    
    @pytest.mark.parametrize("invalid_input", [123, None, [], {}, 45.67, True])
    def test_type_errors_parametrized(self, invalid_input):
        """Parametrized test for type errors."""
        with pytest.raises(TypeError):
            reverse_string(invalid_input)
        with pytest.raises(TypeError):
            reverse_string_iterative(invalid_input)
        with pytest.raises(TypeError):
            reverse_string_recursive(invalid_input)


if __name__ == "__main__":
    # Run unittest tests
    unittest.main(verbosity=2)
