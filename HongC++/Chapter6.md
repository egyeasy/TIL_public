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



















