#!/usr/bin/env python

#
# https://pypi.org/project/ezdxf/
# https://ezdxf.mozman.at/docs/tutorials/text.html
#

import ezdxf
from six.moves import range


def createDXF(drawFn, fileName, *args):
    doc = ezdxf.new(dxfversion='R2018', setup=True)

    # Create new table entries (layers, linetypes, text styles, ...).
    #doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})

    # DXF entities (LINE, TEXT, ...) reside in a layout (modelspace,
    # paperspace layout or block definition).
    msp = doc.modelspace()

    drawFn(msp, *args)

    doc.saveas(fileName)


def soylentGreen(msp, xNum, yNum, xWidth, yWidth):
    lineAttribs = {'color': 7}
    #textAttribs = {'layer': 'TEXTLAYER'}
    textAttribs = {'color': 7, 'height': 15}

    xSize = xNum * xWidth
    ySize = yNum * yWidth

    print('Total size is', xSize, 'mm x', ySize, 'mm')

    for x in range(xNum + 1):
        x = x * xWidth
        msp.add_line((x, 0), (x, xSize), dxfattribs=lineAttribs)

    for y in range(yNum + 1):
        y = y * yWidth
        msp.add_line((0, y), (ySize, y), dxfattribs=lineAttribs)

    for x in range(xNum):
        for y in range(yNum):
            xPos = (x + 0.5) * xWidth
            yPos = (y + 0.5) * yWidth
            msp.add_text('A', dxfattribs=textAttribs).set_pos((xPos, yPos), align='MIDDLE_CENTER')


createDXF(soylentGreen, 'soylent-green.dxf', 10, 10, 20, 20)
