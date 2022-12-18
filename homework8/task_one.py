def text_up(func):
    def wrap(words):
        words = [' '.join(words).upper()]
        output = func(words)
        return output
    return wrap


@text_up
def get_text(words):
    return words


print(get_text(['Hello', 'world']))
