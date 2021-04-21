# https://www.urionlinejudge.com.br/judge/pt/problems/view/1115

from typing import NamedTuple


class Coordinate(NamedTuple):
    x: int
    y: int

    def has_any_zero(self) -> bool:
        return self.x == 0 or self.y == 0

    def quadrant(self) -> str:
        if self.x > 0 and self.y > 0:
            return 'primeiro'
        elif self.x > 0 and self.y < 0:
            return 'quarto'
        elif self.x < 0 and self.y > 0:
            return 'segundo'
        else:
            return 'terceiro'


while True:

    x, y = tuple(int(i) for i in input().split())
    coord = Coordinate(x, y)
    if coord.has_any_zero():
        break

    print(coord.quadrant())
