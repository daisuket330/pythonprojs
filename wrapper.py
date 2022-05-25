


def wrap(text, line_length):
    # """wraps a string to a specified line length.
    # Args:
    #     text: the sring to wrap.
    #     line_length: the lne lenght in characters.
    # Returns:
    # A wrapped string.
    # """
    words = text.split()
    lines_of_words = []
    current_line_length = line_length
    for word in words:
        if current_line_length + len(word) > line_length:
            lines_of_words.append([]) #new line
            current_line_length = 0
        lines_of_words[-1].append(word)
        current_line_length += len(word) + len(' ')
    lines = [' '.join(lines_of_words) for lines_of_words in lines_of_words]
    result = '\n'.join(lines)
    assert all(len(line) <= line_length for line in result.splitlines())
    # this assertion takes the string we're about to return, splits it into lines using the splitlines method,and checks that the length of each line is less than or equal to the specified line lenght 
    
    return result    
    
 
test_line_text = "The waning moon shines dimly in the sky," \
"The night is blanketed by the gathering clouds" \
"Two baby chicks crucified together, a cruel trap" \
"Ah, if only the love that clouds the present could stay vividly in my heart"\
    
wrap(test_line_text, 5)