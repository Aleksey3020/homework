def text_up(func):
    def wrap(words):
        res = func(words)
        return res.upper()
    return wrap


@text_up
def get_text(words):
    return ' '.join(words)


print(get_text(['my', 'name', 'Aleksey']))
