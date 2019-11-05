#include <iostream>
#include <cstdlib> // std::radn(), std::srand()
#include <ctime> // std::time()
#include <random>

using namespace std;

unsigned int PRNG() // Pseudo Random number generator
{
	static unsigned int seed = 5523; // seed number

	seed = 8253729 * seed + 2396403; // �ݺ������� �ٲٱ� ���� static ���� ���

	return seed % 32768;
}


int getRandomeNumber(int min, int max)
{
	static const double fraction = 1.0 / (RAND_MAX + 1.0);

	return min + static_cast<int>((max - min + 1) * (std::rand() * fraction));
}


int main()
{
	//std::srand(5323);
	std::srand(static_cast<unsigned int>(std::time(0)));
	for (int count = 1; count <= 100; ++count)
	{
		//cout << PRNG() << "\t";
		cout << std::rand() << "\t";

		if (count % 5 == 0) cout << endl;

	}

	std::random_device rd;
	std::mt19937 mersenne(rd()); // create a mersenne twister - ���ڸ� �����ش�.
	std::uniform_int_distribution<> dice(1, 6); // 1~6���� ������ Ȯ���� ���´�.

	for (int count = 1; count <= 20; ++count)
	{
		cout << dice(mersenne) << endl;
	}


	return 0;
}