#include <iostream>
using namespace std;

int main() {
    int hour, minute;
    cin >> hour >> minute;
    int new_minute, difference;
    difference = minute - 45;
    if (difference >= 0) {
        cout << hour << " " << difference << endl;
    } else {
        new_minute = 60 + difference;
        hour = (hour + 23) % 24;
        cout << hour << " " << new_minute << endl;
    }
}