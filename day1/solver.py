#! /usr/bin/env python3

import click


def load_changes():
    with open('input', 'r') as _f:
        for line in _f.readlines():
            yield line


f = 0
for change in load_changes():
    sign = change[0:1]
    value = int(change[1:])
    if sign == '+':
        f += value
    elif sign == '-':
        f -= value

click.secho(f'final frequency is: {f}')
