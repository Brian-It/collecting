# coding: utf-8


class Dict(dict):
    '''
    To extend a dict supports object-like property access.
    Warning: Just support property access, property assign is invalid.
    '''

    def __init__(self, *args, **kwargs):
        super(Dict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        # print "key:", key
        try:
            # if type(self[key]) in (dict, OrderedDict):
            if isinstance(self[key], dict):
                d = Dict(self[key])

                return d
            return self[key]
        except KeyError:
            raise AttributeError(key)

    # def __setattr__(self, key, value):
    #     self[key] = value
    #     pass

if __name__ == '__main__':
    dd = {'a': {'b': {'c': 1}}}
    D = Dict(dd)
    print D.a, '*'*10
    print D.a.b, '*'*10
    print D.a.b.c, '*'*10

