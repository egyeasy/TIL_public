#include <iostream>

using namespace std;

typedef struct __Point
{
    int xpos;
    int ypos;
} Point;

Point& PntAdder(const Point &p1, const Point &p2);

int main(void)
{
    Point * p1 = new Point;
    p1->xpos = 1;
    p1->ypos = 2;

    Point * p2 = new Point;
    p2->xpos = 3;
    p2->ypos = 4;

    Point &point = PntAdder(*p1, *p2);
    cout << point.xpos << endl;
    cout << point.ypos << endl;
    return 0;
}

Point& PntAdder(const Point &p1, const Point &p2)
{
    Point * new_point = new Point;
    new_point->xpos = p1.xpos + p2.xpos;
    new_point->ypos = p1.ypos + p2.ypos;
    return *new_point;
}