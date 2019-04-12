#include <iostream>

using namespace std;

int main()
{
	const int A = 1000000;
	int visited[A][2];

	for (int i = 0; i < A; i++) {
		visited[i][0] = 1;
		visited[i][1] = i + 1;
	}

	visited[0][0] = 0;
	visited[1][0] = 0;

	int j = 2;
	int temp = 1;

	int testcase;
	cin >> testcase;

	while (j < A)
	{
		if (visited[j][0]) {
			visited[temp][1] = j;
			temp = j;
			for (int k = j * 2; k < A; k = k + j) {
				visited[k][0] = 0;
			}
		}
		j = visited[j][1];
	}

	for (int tc = 0; tc < testcase; tc++) {
		int N;
		cin >> N;
		int ans = 0;
		int x = 3;
		while (x < N) {
			if (visited[(N - x) / 2][0]) {
				ans += 1;
			}
			x = visited[x][1];
		}
		cout << ans << "\n";
	}

	return 0;
}