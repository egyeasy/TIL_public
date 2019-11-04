#include <iostream>
#include <vector>
#include <cstdint>

int main()
{
	using namespace std;

	typedef double distance_t;

	std::int8_t i(97); // 가명 만들어준 것이라고 보면 됨

	double		my_distance;
	distance_t  home2work;

	typedef vector<pair<string, int>> pairlist_t;
	// 또는
	using pairlist_t = vector<pair<string, int> >;

	vector<pair<string, int>> pairlist1;
	pairlist_t				  pairlist2;


	return 0;
}