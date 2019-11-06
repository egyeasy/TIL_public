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





## 6.2 배열 기초 array

### 주소 출력

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_students = 20;

	int students_scores[num_students];

	cout << (int)&students_scores << endl;			// +0
	cout << (int) & (students_scores[0]) << endl;	// +0
	cout << (int) & (students_scores[1]) << endl;	// +4
	cout << (int) & (students_scores[2]) << endl;	// +8
	cout << (int) & (students_scores[3]) << endl;	// +12

	cout << sizeof(students_scores)
}
```



### 함수 인자로 배열 전달 가능

```cpp
void doSomething(int students_scores[20])
{
	cout << students_scores[0] << endl;
	cout << students_scores[1] << endl;
	cout << students_scores[2] << endl;
    
	cout << (int)&students_scores << endl;
	cout << "size: " << sizeof(students_scores) << endl;

}

int main()
{
	const int num_students = 20;

	int students_scores[num_students] = { 1, 2, 3, 4, 5 };

	cout << "size: " << sizeof(students_scores) << endl;
    
	doSomething(students_scores); // 함수의 인자로 전달 가능

	return 0;
}
```

but 실제 주소는 함수 안에서 출력했을 때와 다르다. 복사를 해서 넣기 때문. 속도의 문제가 발생할 수 있다.



```cpp
void doSomething(int students_scores[]) // size 표시하지 않아도 됨
```





## 6.3 배열과 반복문

```cpp
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
```





## 6.4 배열과 선택 정렬 selection sort

왼쪽으로 오른쪽으로 가면서 제일 작은 숫자를 찾아서 맨 왼쪽으로 옮겨주는 정렬



```cpp
#include <iostream>

using namespace std;

int main()
{
    
    const int length = 5;
}
```





### 내가 쓴 답안

```cpp
#include <iostream>

using namespace std;

void printArray(int array[], int length)
{
	for (int index = 0; index < length; index++)
		cout << array[index] << " ";
	cout << endl;
}

int main()
{

	const int length = 5;

	int array[length] = { 3, 5, 2, 1, 4 };

	printArray(array, length);


	for (int start = 0; start < length; start++)
	{
		int min_idx = start;
		for (int i = start; i < length; i++)
		{
			if (array[i] < array[min_idx])
			{
				min_idx = i;
			}
		}
		int copy = array[start];
		array[start] = array[min_idx];
		array[min_idx] = copy;
	}

	printArray(array, length);


}
```





## 6.5 정적 다차원 배열

### 2차원 배열

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_rows = 3;
	const int num_columns = 5;

	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_columns; ++col)
			cout << '[' << row << ']' << '[' << col << ']' << '\t';
		
		cout << endl;
	}

	cout << endl;

	int array[num_rows][num_columns] =
	{
		{1, 2, 3, 4, 5}, // row 0
		{6, 7, 8, 9, 10}, // row 1
		{11, 12, 13, 14, 15} // row 2
	};

	return 0;

}
```



### 메모리 주소

```cpp
	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_columns; ++col)
			//cout << array[row][col] << '\t';
			cout << (int) & array[row][col] << '\t';

		cout << endl;
	}

	return 0;
```

row, col 순으로 4씩 증가하는 것을 볼 수 있다. 사실상 일방향으로 메모리에 입력되고 있던 것.



### 생략 가능

num_columns 까지는 생략 불가

```cpp
	int array[][num_columns] =
	{
		{1, 2, 3, 4, 5}, // row 0
		{6, 7, 8, 9, 10}, // row 1
		{11, 12, 13, 14, 15} // row 2
	};
```





## 6.6 C언어 스타일의 배열 문자열

```cpp
#include <iostream>

using namespace std;

int main()
{
	char myString[] = "string";

	for (int i = 0; i < 7; ++i)
	{
		cout << (int)myString[i] << endl; // ASCII 출력

		cout << sizeof(myString) / sizeof(myString[0]) << endl;
	}


	return 0;
}
```





배열처럼 취급하면 된다.

```cpp
#include <iostream>

using namespace std;

int main()
{

	char string[255];

	cin >> string;

	string[0] = 'A';
	string[4] = '\0';

	cout << string << endl;


	return 0;
}
```

4번 index부터 출력이 되지 않는다. \0을 중단 지점으로 인식하기 때문.



### 띄어쓰기 입력받기

```cpp
	cin.getline(string, 255);
```

```cpp
	int ix = 0;
	while (true)
	{
		if (string[ix] == '\0') break;

		cout << string[ix] << " " << (int)string[ix] << endl;
		++ix;
	}
```

스페이스바는 32번



### strcpy

```cpp
#include <cstring>

	// string copy
	char source[] = "Copy this!";
	char dest[50];
	strcpy(dest, source); // source를 dest에 넣음

	cout << source << endl;
	cout << dest << endl;

```

but dest의 사이즈가 더 작을 경우 런타임 에러 발생. 이를 막기 위해 `strcpy_s`가 권장됨. 입력할 수 있는 최대 사이즈를 입력하도록 되어있다.



```cpp
	// string copy
	char source[] = "Copy this!";
	char dest[50];
	//strcpy(dest, source); // source를 dest에 넣음
	strcpy_s(dest, 50, source);

	cout << source << endl;
	cout << dest << endl;

```



### strcat, strcmp

```cpp
	// strcat() - 한 문자열 뒤에 다른 문자열 붙이기
	// strcmp() - 두 문자열 동일한지 비교

	strcat_s(dest, source);

	cout << source << endl;
	cout << dest << endl;

	cout << strcmp(source, dest) << endl;
```

strcmp는 같으면 0, 다르면 -1을 출력



실전에서는 string을 쓰는 게 좋음. 배열을 연습하기에 cstring 방식이 좋다.





## 6.7 포인터의 기본적인 사용법 Pointer



```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 5;

	cout << x << endl;
	cout << &x << endl; // & : address of operator
	cout << (int)&x << endl;

	// de-reference operator (*)
	cout << *&x << endl; // 이 메모리 주소에 실제로 담겨있는게 뭐냐



	return 0;
}
```



포인터도 결국 주소를 저장하는 변수에 불과하다.



### 포인터 변수

```cpp
	int *ptr_x = &x; //  변수가 포인터임을 표시
	int *ptr_y = &x, *ptr_z = &x;

	typedef int* pint;
	pint ptr_k = &x, ptr_j = &x;

	cout << *ptr_x << endl;
```



함수의 인자, 리턴 값으로도 포인터를 전달할 수 있다.

타입을 명시하는 이유는 de-reference할 때 타입을 알고 가야하기 때문.



### 왜 포인터를 쓰는가?

array 때문에 그렇다. 포인터로 array의 첫 번째 주소, 데이터 개수만 알려주면 위치를 직접적으로 접근할 수 있어서 편하다. 다 복사할 필요가 없음.

또 변수를 사용할 때 직접적으로 보내지 않고 쓰기 위해.



```cpp
	double d = 1.0;
	double* ptr_d = &d;
	cout << ptr_d << endl;
	cout << *ptr_d << endl;
```



### typeinfo

```cpp
#include <typeinfo>

cout << typeid(ptr_x).name() << endl; // int *
```



### 주소의 size

```cpp
	cout << sizeof(x) << endl; // 4
	cout << sizeof(d) << endl; // 8
	cout << sizeof(&x) << " " << sizeof(ptr_x) << endl; // 4 4
	cout << sizeof(&d) << " " << sizeof(ptr_d) << endl; // 4 4
```

주소를 저장하는 곳은 사이즈가 4로 똑같다.

64비트로 빌드하면 주소 사이즈가 8비트로 늘어난다. 

=> 포인터도 값을 저장한 변수다.



### struct

```cpp
struct Something
{
	int a, b, c, d; // 4 x 4 = 16 bytes
};

	Something ss;
	Something* ptr_s;

	cout << sizeof(Something) << endl; // 16
	cout << sizeof(ptr_s) << endl;	   // 4
```



### 문제가 될 만한 부분

```cpp
	int* ptr_a;

	cout << *ptr_a << endl; // error - uninitialized

```

실제로 사용하는 게 아닌 상태에서 메모리에 접근.













































