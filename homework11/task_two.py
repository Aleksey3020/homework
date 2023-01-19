class text_up:
    def __init__(self, func):
        self._func = func

    def __call__(self, words):
        res = self._func(words)
        return res.upper()


@text_up
def get_text(words):
    return ' '.join(words)


print(get_text(['my', 'name', 'Aleksey']))
