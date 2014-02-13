Progress Bar
============

A fairly pointless bit of terminal porn that allows you to plop a colorful,
smoothly animated progress bar into your CLI app. Useful? Maybe a little.
Pretty? Heck yes! Should work on any ANSI-compliant terminal emulator.

Usage
-----

Initialize a progress bar, giving the desired width in characters. Call
`start()` on it once to display it initially, then run your time-consuming
task, calling `tick()` whenever you see fit to increment the level of
progress:

    import time
    from progressbar import ProgressBar

    p = ProgressBar(width=80)
    p.start()
    for _ in range(500):
        p.tick(1.0 / 500)
        time.sleep(0.001)

A `ProgressBar` is also a context object, so you can use it in a `with`
block:

    with ProgressBar(width=80) as p:
        for _ in range(500):
            p.tick(1.0 / 500)

You can specify both a border color and a fill color for the bar:

    p = ProgressBar(width=80, fillcolor=24, bordercolor=1)

Valid color values are `0` through `255`, as long as your terminal has
256-color support. If your terminal doesn't support 256 colors please send
us a postcard from 1970, we hear it's nice there this time of year.
A value of `None` for either color will simply revert to the default text
color in your terminal.

License
-------

See the included LICENSE.txt file for the terms governing distribution of
this software.

ProgressBar is released under the terms of the WTFPL (www.wtfpl.net) with
an additional, but non-binding, provision: for every Joule/Kelvin of the
universe's entropy you waste running this code, you are enjoined strongly
(but non-bindingly) to stand very still, thinking about nothing, for
approximately 18 microseconds. In this manner the debt to future generations
may be paid.
