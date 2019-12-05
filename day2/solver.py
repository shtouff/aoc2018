#! /usr/bin/env python3

import click
import sys


def load_box_ids():
    with open('input', 'r') as _f:
        for box_id in _f.readlines():
            yield box_id.rstrip()


box_ids = list(load_box_ids())

for box_id in box_ids[0:len(box_ids) // 2]:
    for other in box_ids:
        diffs = 0
        commons = []
        for c1, c2 in zip(box_id, other):
            if c1 != c2:
                diffs += 1
            else:
                commons.append(c1)
            if diffs > 1:
                break
        if diffs == 1:
            click.secho(f'{box_id} and {other} are quite the same')
            click.secho(f'They share the following letters: {"".join(commons)}')
            sys.exit(0)
