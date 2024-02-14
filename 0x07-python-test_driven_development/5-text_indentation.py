"""
My module
"""


def text_indentation(text):
    """
    function
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    
    for c in range(len(text)):
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            print()
            print()
        else:
            print(text[c], end="")
