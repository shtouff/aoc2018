#! /usr/bin/env python3

import click


def load_box_ids():
    with open('input', 'r') as _f:
        for box_id in _f.readlines():
            yield box_id.rstrip()


two = three = 0
for box_id in load_box_ids():
    letters = {}
    for c in box_id:
        letters[c] = letters.get(c, 0) + 1
    if 2 in letters.values():
        two += 1
    if 3 in letters.values():
        three += 1

click.secho(f'checksum is {two * three}')
