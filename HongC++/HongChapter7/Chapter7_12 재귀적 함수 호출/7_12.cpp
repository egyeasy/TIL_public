#include <iostream>
using namespace std;

void countDown(int count)
{
	cout << count << endl;

	if(count > 0)
		countDown(count - 1);
}

int sumTo(int sumto)
{
	if (sumto <= 0)
		return 0;
	else if (sumto <= 1)
		return 1;
	else
		return sumTo(sumto - 1) + sumto;
}

int fibo(int N)
{
	if (N == 0)
		return 1;
	else if (N == 1)
		return 1;
	else
		return fibo(N - 1) + fibo(N - 2);
}

int main()
{
	cout << sumTo(4) << endl;

	cout << fibo(2) << endl;

	return 0;
}