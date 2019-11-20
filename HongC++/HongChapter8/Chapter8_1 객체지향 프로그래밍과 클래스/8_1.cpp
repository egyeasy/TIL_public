#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Friend
{
public: // access specifier (public, private, protected)
	string	m_name;
	string	address;
	int		age;
	double	height;
	double	weight;

	void print()
	{
		cout << m_name << " " << address << " " << age << " " << height << " " << weight << endl;
	}
};

void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

void print(const Friend& fr)
{
	cout << fr.m_name << " " << fr.address << " " << fr.age << " " << fr.height << " " << fr.weight << endl;
}

int main()
{
	Friend jj{ "Jack Jack", "Uptown", 20, 167, 57 }; // uniform initialization(instantiation), jj = instance
	jj.m_name = "Jack Jack";
	jj.age = 2;

	print(jj.m_name, jj.address, jj.age, jj.height, jj.weight);
	print(jj);
	jj.print();

	vector<string>	name_vec;
	vector<string>	addr_vec;
	vector<int>		age_vec;
	vector<double>	height_vec;
	vector<double>	weight_vec;

	//print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);

	// 친구가 여러 명이다
	vector<Friend> my_friends;
	my_friends.resize(2);

	//my_friends[0].print();
	//my_friends[1].print();
	
	for (auto& ele : my_friends)
		ele.print();
}
