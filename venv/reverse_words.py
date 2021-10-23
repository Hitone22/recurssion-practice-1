def reverse_words(string):
    """ Takes a string and returns the words in reverse

    ex: reverse_words("dog is huge") >>> huge is dog
    """
    stripped_string = string.strip()
    first_space = stripped_string.find(" ")
    string_len = len(stripped_string)

    if stripped_string.find(" ") == -1:
        return stripped_string
    else:
        return reverse_words(stripped_string[first_space:string_len]) + " " + stripped_string[0:first_space]


print(reverse_words("    shalp the dog is  huge"))


