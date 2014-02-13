from progressbar import ProgressBar
import time


spectrum = \
    [196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46, 47, 48,
     49, 50, 51, 45, 39, 33, 27, 21, 57, 93, 129, 165, 201]

if __name__ == '__main__':
    print 'Beginning boring task...'
    with ProgressBar(fillcolor=spectrum) as p:
        for i in range(500):
            p.tick(1.0/(500))
            time.sleep(0.02 - (.00003 * i))
    print 'Done!'
