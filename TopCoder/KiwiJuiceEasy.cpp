#include <vector>
#include <iostream>
using namespace std;

class KiwiJuiceEasy
{
public:
    vector<int> thePouring(vector <int> capacities,
                           vector <int> bottles,
                           vector <int> fromId,
                           vector <int> toId) {
        for (int i = 0; i < fromId.size(); i++) {
            if (bottles[fromId[i]] + bottles[toId[i]] <= capacities[toId[i]]) {
                bottles[toId[i]] += bottles[fromId[i]];
                bottles[fromId[i]] = 0;
            } else {
                bottles[fromId[i]] -= capacities[toId[i]] - bottles[toId[i]];
                bottles[toId[i]] = capacities[toId[i]];
            }
        }

        return bottles;
    }
};


int main()
{
    
    return 0;
}