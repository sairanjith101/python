class NetworkError(RuntimeError):
    def __init__(self, args):
        self.msg = args

try:
    raise NetworkError('Bad Host')
except RuntimeError as re:
    print(re.msg)