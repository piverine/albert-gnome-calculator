# -*- coding: utf-8 -*-

"""Gnome Calculator

Synopsis: <trigger> <filter>"""

from albert import *
import subprocess

__title__ = 'GnomeCalculator'
__version__ = '0.0.1'
__triggers__ = 'calc '
__authors__ = 'Rohan Kumar'
__exec_deps__ = ['gnome-calculator']


iconPath = iconLookup('gnome-calculator')


def handleQuery(query):
    if query.isTriggered:
        stripped = query.string.strip()
        result = subprocess.run(
            ["gnome-calculator", "-s", stripped], stdout=subprocess.PIPE, text=True
        ).stdout
        return Item(id=__title__,
                    icon=iconPath,
                    text=result,
                    subtext="Gnome Calculator type any equation eg: \"sin(90)\", \"5^2\" ",
                    actions=[ClipAction("Copy result to clipboard", result)])
