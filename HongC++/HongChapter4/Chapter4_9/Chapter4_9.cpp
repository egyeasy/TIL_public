#include <iostream>
#include <vector>
#include <cstdint>

int main()
{
	using namespace std;

	typedef double distance_t;

	std::int8_t i(97); // ���� ������� ���̶�� ���� ��

	double		my_distance;
	distance_t  home2work;

	typedef vector<pair<string, int>> pairlist_t;
	// �Ǵ�
	using pairlist_t = vector<pair<string, int> >;

	vector<pair<string, int>> pairlist1;
	pairlist_t				  pairlist2;


	return 0;
}