#coding=utf-8
import sys


class ProgressBar(object):
    def __init__(self, width=80, fillcolor=33, bordercolor=None):
        self.width = width
        self.progress = 0.0

        reset = '\033[39m'
        color = '\033[38;5;{}m'
        self.fill = color.format(fillcolor) if fillcolor else reset
        self.border = color.format(bordercolor) if bordercolor else reset


    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        pass

    def render(self):
        # Topbar
        sys.stdout.write(self.border)
        sys.stdout.write(u'▁' * self.width)
        sys.stdout.write('\n')

        # Left edge
        sys.stdout.write(u'█')

        # Contents
        sys.stdout.write(self.fill)
        full_width = (self.width - 2) * self.progress
        blocks = int(full_width)
        remainder = full_width - blocks

        sys.stdout.write(u'█' * blocks)

        if remainder:
            sys.stdout.write(u' ▏▎▍▌▋▊▉█'[int(remainder * 8)])

        sys.stdout.write(u' ' * (self.width - 3 - blocks))

        # Right edge
        sys.stdout.write(self.border)
        sys.stdout.write(u'█')
        sys.stdout.write('\n')

        # Bottom bar
        sys.stdout.write(u'▔' * self.width)
        sys.stdout.write('\n')
        sys.stdout.write('\033[39m')

    def start(self):
        self.render()

    def set(self, progress):
        """
        Set progress to a specific value and redraw.

        :param progress: Fraction of the bar to fill. Clamped to [0, 1].
        """
        self.progress = min(max(progress, 0.0), 1.0)

        # Restore cursor position and redraw
        sys.stdout.write('\x1b[3F')
        self.render()

    def tick(self, amount):
        """
        Increment progress by the specified fraction and redraw.
        """
        self.set(self.progress + amount)
