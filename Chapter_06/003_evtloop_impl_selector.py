
import sys
import selectors

# Frankly,
#   I have no idea about this module.
#   TODO Might dive into the 'selectors' later :p


def read(fh):
    """ 
        To get thie code running, 
        ya must specify a filename ("halo.txt" for now)
    """

    print(f"got input from stdin -- {fh.readline()!r}")


if __name__ == '__main__':

    # create defaut selector (that meas there're more)
    selector = selectors.DefaultSelector()

    # register the 'read' func for the READ event on stdin
    selector.register(sys.stdin, selectors.EVENT_READ, read)

    while True:
        for key, mask in selector.select():
            callback = key.data
            callback(key.fileobj)
