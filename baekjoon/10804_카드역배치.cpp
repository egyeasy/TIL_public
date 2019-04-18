#include <iostream>

using namespace std;

inline void swap(int &i, int &j) {
	int temp = i;
	i = j;
	j = temp;
}

int main() {
	int arr[21];
	for (int i = 0; i < 21; i++) {
		arr[i] = i;
	}
	for (int time = 0; time < 10; time++) {
		int s, e;
		cin >> s >> e;
		for (int idx = s; idx < s + (e - s + 1) / 2; idx++) {
			swap(arr[idx], arr[e - (idx - s)]);
		}
	}
	for (int i = 1; i < 21; i++) {
		cout << arr[i] << " ";
	}
	cout << "\n";
}