#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[]) // ����, ����
{
	for (int count = 0; count < argc; ++count)
	{
		std::string argv_single = argv[count];

		if (count == 1) // 0���� �������� path
		{
			int input_number = std::stoi(argv_single); // ������ �ٲ��ֱ�
			cout << input_number + 1 << endl;
		}
		cout << argv[count] << endl; // �������� ���(�̸�) ���
	}
	


	return 0;
}