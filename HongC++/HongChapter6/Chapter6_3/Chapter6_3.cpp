#include <iostream>

using namespace std;

int main()
{
	const int num_students = 5;
	int scores[num_students] = { 84, 92, 76, 81, 56 };

	int total_score = 0;
	int max_score = 0;

	for (int i = 0; i < num_students; i++)
	{
		total_score += scores[i];
		max_score = (max_score < scores[i]) ? scores[i] : max_score;
	}

	double avg_score = static_cast<double>(total_score) / num_students;

	cout << avg_score << endl;

	const int num_stdts = sizeof(scores) / sizeof(int); // 로 개수를 알아낼 수도 있다.

	cout << "max score: " << max_score << endl;
}