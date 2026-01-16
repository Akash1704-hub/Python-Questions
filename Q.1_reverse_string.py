def reverse_string(text: str) -> str:
    """
    Function to reverses the given string.

    Args:
        text (str): The string that needs to be reversed

    Returns:
        str: Reversed version of the input string

    Raises:
        TypeError: If the input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if text == "":
        return ""

    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


if __name__ == "__main__":
    try:
        print(reverse_string("Hello World"))
        print(reverse_string("Python"))
        reverse_string(123)   # Invalid input example
    except TypeError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)
