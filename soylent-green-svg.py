#!/usr/bin/env python

#
# https://github.com/mozman/svgwrite
# https://svgwrite.readthedocs.io/en/latest/
#

import svgwrite
from six.moves import range


def createDXF(drawFn, fileName, *args):
    dwg = svgwrite.Drawing(fileName, profile='tiny')
    drawFn(dwg, *args)
    dwg.save()


def soylentGreen(dwg, xNum, yNum, xWidth, yWidth):
    lineKwArgs = {
        'stroke' : svgwrite.rgb(10, 10, 16, '%')
    }

    xSize = xNum * xWidth
    ySize = yNum * yWidth

    print('Total size is', xSize, 'mm x', ySize, 'mm')

    for x in dir(dwg):
        if 'unit' in x:
            print(x)

    for x in range(xNum + 1):
        x = x * xWidth
        dwg.add(dwg.line((x, 0), (x, xSize), **lineKwArgs))

    for y in range(yNum + 1):
        y = y * yWidth
        dwg.add(dwg.line((0, y), (ySize, y), **lineKwArgs))

    for x in range(xNum):
        for y in range(yNum):
            xPos = (x + 0.5) * xWidth
            yPos = (y + 0.5) * yWidth
            dwg.add(dwg.text('A', insert=(0, 0.2), fill='red'))


createDXF(soylentGreen, 'soylent-green.svg', 10, 10, 20, 20)