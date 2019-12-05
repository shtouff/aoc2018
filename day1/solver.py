#! /usr/bin/env python3

import click
import sys


def load_changes():
    with open('input', 'r') as _f:
        for line in _f.readlines():
            yield line


f = 0
frequencies = []
changes = []

for change in load_changes():
    sign = change[0:1]
    value = int(change[1:])
    if sign == '+':
        changes.append(value)
    elif sign == '-':
        changes.append(-value)

while True:
    for change in changes:
        f += change

        if f not in frequencies:
            frequencies.append(f)
        else:
            click.secho(f'This frequency has already been seen: {f}')
            sys.exit(0)

    click.secho(f'loop frequency is: {f}')
