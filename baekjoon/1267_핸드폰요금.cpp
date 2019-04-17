#include <iostream>

using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	int young = 0;
	int min = 0;
	int each_call;

	for (int i = 0; i < N; i++) {
		cin >> each_call;
		young += (each_call / 30 + 1) * 10;
		min += (each_call / 60 + 1) * 15;
	}

	// int young, min;
	// young = (sum_call / 30 + 1) * 10;
	// min = (sum_call / 60 + 1) * 15;

	if (young < min){
		cout << "Y " << young << "\n";
	}
	else if (young > min) {
		cout << "M " << min << "\n";
	}
	else {
		cout << "Y M " << young << "\n";
	}


	return 0;
}