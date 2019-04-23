#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	int arr[100];
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	int find;
	cin >> find;
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		if (find == arr[i]) {
			cnt++;
		}
	}

	cout << cnt << "\n";

	return 0;
}