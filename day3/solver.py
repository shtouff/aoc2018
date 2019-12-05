#! /usr/bin/env python3

import click
import re

CLAIM_REGEX = re.compile(r'^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$')


class ClaimParseError(ValueError):
    pass


class Claim:
    def __init__(self, cid, x, y, w, h):
        self.cid = int(cid)
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)

    @staticmethod
    def parse_claim(claim):
        """
        return: id, x, y, w, h
        """
        m = CLAIM_REGEX.match(claim)
        if m is None:
            raise ClaimParseError
        return Claim(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5))

    def get_points(self):
        for x in range(self.x, self.x + self.w):
            for y in range(self.y, self.y + self.h):
                yield x, y


class Grid:
    def __init__(self):
        self.grid = {}

    def add_claim(self, claim: Claim):
        for point in claim.get_points():
            if point in self.grid:
                self.grid[point].append(claim.cid)
            else:
                self.grid[point] = [claim.cid]

    def overlaps(self):
        return [point for point in self.grid if len(self.grid[point]) >= 2]


def load_claims():
    with open('input', 'r') as _f:
        for claim in _f.readlines():
            yield Claim.parse_claim(claim.rstrip())


def main():
    grid = Grid()
    for claim in load_claims():
        grid.add_claim(claim)

    click.secho(f'Overlaps count={len(grid.overlaps())}')


main()
