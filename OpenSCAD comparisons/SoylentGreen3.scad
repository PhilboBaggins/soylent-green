
DEFAULT_X_NUM = 10;
DEFAULT_Y_NUM = 10;
DEFAULT_X_WIDTH = 20;
DEFAULT_Y_WIDTH = 20;
DEFAULT_SPACING = 1;

module SoylentGreen3(
    xNum = DEFAULT_X_NUM,
    yNum = DEFAULT_Y_NUM,
    xWidth = DEFAULT_X_WIDTH,
    yWidth = DEFAULT_Y_WIDTH)
{
    for (x = [0 : xNum - 1])
    for (y = [0 : yNum - 1])
    {
        if ((x + y) % 2 == 0)
        {
            color([x / xNum, y / yNum, 0])
            translate([x * xWidth, y * yWidth])
            square([xWidth, yWidth]);
        }
    }
}

SoylentGreen3();
