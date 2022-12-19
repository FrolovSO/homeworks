def text_up(func):
    def wrap(words):
        output = func(words)
        return output.upper()
    return wrap


@text_up
def get_text(words):
    words = ' '.join(words)
    return words


print(get_text(['Hello', 'world']))
