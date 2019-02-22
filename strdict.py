class StrDict(dict):
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Key must be str or unicode.')
        dict.__setitem__(self, key, value)