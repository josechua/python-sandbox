"""
String Reverser Module

This module provides functions to reverse strings using different methods.
"""


def reverse_string(text: str) -> str:
    """
    Reverse a string using Python's slicing notation.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text[::-1]


def reverse_string_iterative(text: str) -> str:
    """
    Reverse a string using an iterative approach.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    reversed_chars = []
    for char in text:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)


def reverse_string_recursive(text: str) -> str:
    """
    Reverse a string using recursion.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Base case
    if len(text) <= 1:
        return text
    
    # Recursive case
    return text[-1] + reverse_string_recursive(text[:-1])


def main():
    """
    Demonstration of the string reversal functions.
    """
    test_strings = [
        "hello",
        "Python",
        "12345",
        "A man a plan a canal Panama",
        "",
        "a"
    ]
    
    print("String Reversal Demonstration")
    print("=" * 40)
    
    for test_str in test_strings:
        print(f"\nOriginal: '{test_str}'")
        print(f"Slicing:    '{reverse_string(test_str)}'")
        print(f"Iterative:  '{reverse_string_iterative(test_str)}'")
        print(f"Recursive:  '{reverse_string_recursive(test_str)}'")


if __name__ == "__main__":
    main()
