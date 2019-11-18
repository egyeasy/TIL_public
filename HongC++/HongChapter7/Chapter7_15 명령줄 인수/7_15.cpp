#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[]) // 개수, 내용
{
	for (int count = 0; count < argc; ++count)
	{
		std::string argv_single = argv[count];

		if (count == 1) // 0번은 실행파일 path
		{
			int input_number = std::stoi(argv_single); // 정수로 바꿔주기
			cout << input_number + 1 << endl;
		}
		cout << argv[count] << endl; // 실행파일 경로(이름) 출력
	}
	


	return 0;
}