## 6.1 배열 기초 array

### 런타임 에러

디버그 모드에서 5개 사이즈의 배열을 생성하고 array[5]에 변수를 할당하면 빌드는 되지만 OS 측에서 런타임 에러를 날림. 해당 배열에 할당되지 않은 공간을 침범한 것.



### struct의 array

```cpp
#include <iostream>

using namespace std;

struct Rectangle
{
	int length;
	int width;
};

int main()
{
	cout << sizeof(Rectangle) << endl; // 8

	Rectangle rect_arr[10];

	cout << sizeof(rect_arr) << endl;  // 8 * 10 = 80
}
```



```cpp
	//int my_array[5] = { 1, 2, 3, 4, 5 };
	int my_array[] {1, 2, 3, 4, 5}; // C++ 17
	
	cout << my_array[4] << endl;
```



### enumeration

```cpp
enum StudentName
{
	JACKJACK,	// = 0
	DASH,		// = 1
	VIOLET,		// = 2
	NUM_STUDENTS, // = 3
};

	int my_array[] {1, 2, 3, 4, 5}; // C++ 17
	
	cout << my_array[JACKJACK] << endl;
	cout << my_array[VIOLET] << endl;
	cout << my_array[4] << endl;

	int students_scores[NUM_STUDENTS];
```



### 배열 사이즈

```cpp
	int num_students = 0; // const int로 선언하면 배열 사이즈로 선언 가능
	cin >> num_students; // 런타임에 결정된다 = 실행을 하는 때에 값이 정해진다. 

	// int students_scores[num_students]; // 빨간 줄
```

array length는 컴파일 타임에 결정이 되어있어야 함. 따라서 입력 받은 숫자로 배열을 만들려고 할 시 안 된다.

C 스타일에서는 `#define NUM_STUDENT 100000` 같은 식으로 큰 숫자로 할당함.

C++에서는 동적 할당을 주로 쓴다.













