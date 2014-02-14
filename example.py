from progressbar import ProgressBar
import time


spectrum = \
    [196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46, 47, 48,
     49, 50, 51, 45, 39, 33, 27, 21, 57, 93, 129, 165, 201]

g2 = [5, 99, 105, 111, 117, 123, 86, 80, 74, 68, 62]
gradient = (g2 + list(reversed(g2))) * 6

if __name__ == '__main__':
    print 'Beginning boring task...'
    with ProgressBar(fill=gradient) as p:
        for i in range(500):
            p.tick(1.0/(500))
            time.sleep(0.02 - (.000025 * i))
    print 'Done!'
