#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

class Node {
  public:
    Node(std::vector<int> leftdown = {0, 0},
        std::vector<int> rightup = {0, 0},
        bool is_white = true)
        : leftdown_(leftdown),
          rightup_(rightup),
          is_white_(is_white) {}

    bool hasToBeSplited(int x, int y) {
        return !(x < leftdown_[0] || x > rightup_[0] ||
                y < leftdown_[1] || y > rightup_[1]);
    }
    
    int getSquare() {
        return abs(leftdown_[0] - rightup_[0]) * abs(leftdown_[1] - rightup_[1]);
    }

    std::vector<int> leftdown_;
    std::vector<int> rightup_;
    bool is_white_;
};

std::vector<int> make_vector(int x, int y) {
    std::vector<int> vector;
    vector.emplace_back(x);
    vector.emplace_back(y);
    return vector;
}

int main() {

    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL); std::cout.tie(NULL);

    int M_x, N_y, K;
    cin >> M_x;
    cin >> N_y;
    cin >> K;

    Node arr[60100];

    auto first_vector = make_vector(0, 0);
    auto second_vector = make_vector(M_x, N_y);
    
    Node head_node = Node(first_vector, second_vector, true);
    
    int i = 0;
    int node_count = 0;
    arr[node_count++] = head_node;
    for (int k = 0; k < K; k++) {
        int x, y;
        cin >> x;
        cin >> y;
        Node parent_node;
        for (i = 0; i < node_count; i++) {
            parent_node = arr[i];
            if (parent_node.hasToBeSplited(x, y)) {
                break;
            }
        }

        Node node1, node2;
        node1 = node2 = parent_node;

        if (parent_node.is_white_) {
            node1.rightup_[1] = y;
            node2.leftdown_[1] = y;
            node1.is_white_ = false;
            node2.is_white_ = false;
        } else {
            node1.rightup_[0] = x;
            node2.leftdown_[0] = x;
            node1.is_white_ = true;
            node2.is_white_ = true;
        }
        arr[i] = node1;
        arr[++node_count] = node2;
    }
    
    int min, max;
    min = INT_MAX, max = -INT_MAX;

    for (int j = 0; j < node_count + 1; j++) {
        int square = arr[j].getSquare();
        cout << "square " << square << endl;
        min = std::min(square, min);
        max = std::max(square, max);
    }

    cout << max << " " << min << endl;

    return 0;
}