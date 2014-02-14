#coding=utf-8
import sys
import math


class ProgressBar(object):
    def __init__(self, width=80, fillcolor=33, bordercolor=None):
        self.width = width
        self.progress = 0.0

        reset = '\033[39m'
        color = '\033[38;5;{}m'

        self.colors = []

        def clr(c):
            return color.format(c) if c is not None else reset

        for colorset in fillcolor, bordercolor:
            if type(colorset) in (int, str, type(None)):
                colorset = [colorset]
            self.colors.append(map(clr, colorset))

    def _progressive_color(self, n):
        colorset = self.colors[n]
        n = len(colorset)
        return colorset[int(math.ceil(self.progress * n) -1)]

    @property
    def fill(self):
        return self._progressive_color(0)

    @property
    def border(self):
        return self._progressive_color(1)

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
        sys.stdout.write('\x1b[?25l')
        sys.stdout.write('\x1b[3F')
        self.render()
        sys.stdout.write('\x1b[?25h')

    def tick(self, amount):
        """
        Increment progress by the specified fraction and redraw.
        """
        self.set(self.progress + amount)
