#include <vector>
#include <algorithm>
using namespace std;

class KiwiJuiceEasy
{
public:
    vector<int> thePouring(vector <int> capacities,
                           vector <int> bottles,
                           vector <int> fromId,
                           vector <int> toId) {
        for (int i = 0; i < fromId.size(); i++) {
            int f = fromId[i];
            int t = toId[i];
            
            // compare "amount to move" and "amount remaining to make toBottle full" -> MINer is moving amount
            int vol = min(bottles[f], capacities[t] - bottles[t]);

            bottles[f] -= vol;
            bottles[t] += vol;
        }

        return bottles;
    }
};


int main()
{
    
    return 0;
}