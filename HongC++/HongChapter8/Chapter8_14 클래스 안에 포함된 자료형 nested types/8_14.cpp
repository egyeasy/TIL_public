#include <iostream>


class Fruit
{
public:
	enum FruitType
	{
		APPLE, BANANA, CHERRY,
	};

private:
	FruitType m_type;

public:
	Fruit(FruitType type) : m_type(type)
	{}

	FruitType getType() { return m_type; }
};

int main() {
	Fruit apple(Fruit::FruitType::APPLE);
}