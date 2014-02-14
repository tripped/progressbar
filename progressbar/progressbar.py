#coding=utf-8
import sys
import math


class ProgressBar(object):

    FG = '\033[38;5;{}m'
    BG = '\033[48;5;{}m'
    RESETFG = '\033[39m'
    RESETBG = '\033[49m'

    COLORS = {
        'fill': [33],
        'border': [None],
        'text': [235]
    }

    def __init__(self, width=80, **kwargs):
        self.width = width
        self.progress = 0.0

        self.colors = dict(self.COLORS)
        for k, v in kwargs.items():
            if k in self.COLORS:
                if type(v) in (int, str, type(None)):
                    v = [v]
                self.colors[k] = v

    def _progressive_color(self, n):
        colorset = self.colors[n]
        n = len(colorset)
        return colorset[int(math.ceil(self.progress * n) - 1)]

    def setfg(self, colortype):
        c = self._progressive_color(colortype)
        if c is not None:
            sys.stdout.write(self.FG.format(c))
        else:
            self.resetfg()

    def resetfg(self):
        sys.stdout.write(self.RESETFG)

    def setbg(self, colortype):
        c = self._progressive_color(colortype)
        if c is not None:
            sys.stdout.write(self.BG.format(c))
        else:
            self.resetbg()

    def resetbg(self):
        sys.stdout.write(self.RESETBG)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        pass

    def render(self):
        # Topbar
        self.setfg('border')
        sys.stdout.write(u'▁' * self.width)
        sys.stdout.write('\n')

        # Left edge
        sys.stdout.write(u'█')

        # Contents
        self.setfg('fill')
        full_width = (self.width - 2) * self.progress
        blocks = int(full_width)
        remainder = full_width - blocks

        sys.stdout.write(u'█' * blocks)

        if remainder:
            sys.stdout.write(u' ▏▎▍▌▋▊▉█'[int(remainder * 8)])

        sys.stdout.write(u' ' * (self.width - 3 - blocks))

        # Right edge
        self.setfg('border')
        sys.stdout.write(u'█')
        sys.stdout.write('\n')

        # Bottom bar
        sys.stdout.write(u'▔' * self.width)
        sys.stdout.write('\n')

        # Interior text indicator
        percent = ' ' + str(int(self.progress * 100)) + '%'
        if blocks >= len(percent):
            sys.stdout.write('\x1b7\x1b[2G\x1b[2A')
            self.setbg('fill')
            self.setfg('text')
            sys.stdout.write(percent)
            sys.stdout.write('\x1b8')

        self.resetfg()
        self.resetbg()
        sys.stdout.flush()

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
