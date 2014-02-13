from progressbar import ProgressBar
import time


if __name__ == '__main__':
    print 'Beginning boring task...'
    with ProgressBar(50) as p:
        for i in range(500):
            p.tick(1.0/(500))
            time.sleep(0.02 - (.00003 * i))
    print 'Done!'
