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





## 6.7a 널 포인터 Null Pointer

```cpp
#include <iostream>

int main()
{
	double* ptr = 0; // c-style
	double* ptr2 = NULL;
	double* ptr3 = nullptr; // modern c++
	// double *ptr{ nullptr } // uniform initialization 가능

	if (ptr3 != nullptr)
	{
		// do something useful
	}
	else
	{
		// do nothing with ptr
	}

}
```



`nullptr`이 함수 인자로 넘어갈 때 유용하다



```cpp
#include <iostream>

void doSomething(double* ptr)
{
	if (ptr != nullptr)
	{
		// do something useful
		std::cout << *ptr << std::endl;
	}
	else
	{
		// do nothing with ptr
		std::cout << "Null ptr, do nothing" << std::endl;
	}

}

int main()
{
	double* ptr = 0; // c-style
	double* ptr2 = NULL;
	double* ptr3 = nullptr; // modern c++
	// double *ptr{ nullptr } // uniform initialization 가능

	if (ptr3 != nullptr)
	{
		// do something useful
	}
	else
	{
		// do nothing with ptr
	}

	doSomething(ptr3);
	doSomething(nullptr);

	double d = 123.4;
	doSomething(&d);

	ptr = &d;

	doSomething(ptr);

	return 0;

}
```



### nullptr_t

```cpp
#include <cstddef>

std::nullptr_t nptr; // null pointer밖에 못넣는다.
```





### 포인터 변수의 주소

```cpp
void doSomething(double* ptr)
{
	std::cout << "address of pointer variable in function: " << &ptr << std::endl;

	if (ptr != nullptr)
	{
		// do something useful
		std::cout << *ptr << std::endl;
	}
	else
	{
		// do nothing with ptr
		std::cout << "Null ptr, do nothing" << std::endl;
	}

}

	doSomething(ptr3);

	std::cout << "address of pointer variable in main: " << &ptr3 << std::endl;
```

서로 다르게 나온다. 함수에서 쓸 때 값을 복사해가기 때문.





## 6.8 포인터와 정적 배열

포인터와 배열은 같다.

```cpp
#include <iostream>

using namespace std;

int main()
{
	int array[5] = { 9, 7, 5, 3, 1 };

	cout << array << endl;

	cout << &(array[0]) << endl; // array 0번째 index의 요소의 주소

	return 0;
}
```

둘은 같다. array는 사실 첫 번째 요소의 주소를 가지고 있는 것



### de-reference

```cpp
	cout << *array << endl; // 9


	char name[] = "jackjack";
	cout << *name << endl; // j
```



### 포인터 변수

```cpp
	int* ptr = array;
	cout << ptr << endl;
	cout << *ptr << endl;
```

결과가 같게 나온다.



배열은 포인터와 같은 느낌이지만 좀 더 편하게 쓸 수 있게 해주는 기능들이 있는 것.



```cpp
	cout << sizeof(array) << endl; // 20

	cout << sizeof(ptr) << endl; // 4
```

ptr은 ptr 주소가 차지하는 공간이 4바이트라서.



### 문제가 될 경우 - 함수 파라미터로 전달될 때

```cpp
void printArray(int array[]) // int *array와 결과가 같다
{
	cout << sizeof(array) << endl; // 4
}



	printArray(array);
```

함수에 전달될 때는 포인터로 전달됨.



```cpp
void printArray(int array[]) // int *array와 결과가 같다
{
	cout << sizeof(array) << endl; // 4

	*array = 100;
}


	printArray(array);

	cout << array[0] << endl;

```

100이 출력. 변수에 접근할 수 있다.



### 포인터 연산

```cpp
cout << *ptr << " " << *(ptr + 1) << endl; // 포인터 연산
```

배열의 다음 숫자 출력



### Struct

```cpp
struct MyStruct
{
	int array[5] = { 9, 7, 5, 3, 1 };
};

void doSth(MyStruct ms)
{
	cout << sizeof(ms.array) << endl; // 20 - array 사이즈가 나옴
}
	MyStruct ms;
	doSth(ms);
```

제대로 나온다.

ms가 포인터로 전달되어도 같음

```cpp
void doSth(MyStruct *ms) // pointer
{
	// de-reference
	cout << sizeof((*ms).array) << endl; // 20 - array 사이즈가 나옴
}

	// struct
	MyStruct ms;
	doSth(&ms); // address
```





## 6.9 포인터 연산과 배열 인덱싱

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 7;
	int* ptr = &value;

	cout << uintptr_t(ptr - 1) << endl;
	cout << uintptr_t(ptr) << endl;
	cout << uintptr_t(ptr + 1) << endl;
	cout << uintptr_t(ptr + 2) << endl;
	return 0;
}
```

4씩 바뀐다.  int 사이즈에 따라 증가 감소하게 됨

double로 설정하면 8씩 바뀜.



### array

```cpp
	int array[] = { 9, 7, 5, 3, 1 };

	cout << array[0] << " " << (uintptr_t) & array[0] << endl;
	cout << array[1] << " " << (uintptr_t) & array[1] << endl;
	cout << array[2] << " " << (uintptr_t) & array[2] << endl;
	cout << array[3] << " " << (uintptr_t) & array[3] << endl;
	cout << array[4] << " " << (uintptr_t) & array[4] << endl;
```

4씩 증가함을 볼 수 있다.



```cpp
	int* ptr2 = array;
	for (int i = 0; i < 5; i++)
	{
		cout << *(ptr2 + i) << " " << (uintptr_t)(ptr2 + i) << endl;
	}

```

포인터로 접근해도 같은 결과



### 문자열

```cpp
	char name[] = "jack jack";
	const int n_name = sizeof(name) / sizeof(name[0]);

	cout << endl;

	for (int i = 0; i < n_name; i++)
	{
		cout << *(name + i); // jack jack
	}
```

array 타입의 name에 포인터 연산을 그대로 적용해도 됨.



### while문으로 출력

```cpp
	char* ptr3 = name;

	while (true)
	{
		if (*ptr3 == '\0')
			break;
		cout << *(ptr3++);
	}
```

https://stackoverflow.com/questions/14544043/operand-types-are-incompatible-char-and-const-char

Double quotes are the shortcut syntax for a *c-string* in C++. If you want to compare a single character, you must use single quotes instead. You can simply change your code to this:

```
char userInput_Text[3];

if (userInput_Text[1] == 'y') { // <-- Single quotes here.
    // Do stuff.
}
```

For reference:

- `"x"` = `const char *`
- `'x'` = `char`





## 6.10 C언어 스타일의 문자열 심볼릭 상수

```cpp
#include <iostream>

using namespace std;

int main()
{
	//char name[] = "Jack Jack";
	//char* name = "Jack Jack"; // 이건 빌드가 안 됨. Jack Jack은 리터럴임. 어디에 담을지가 명시되어있지 않음
	const char* name = "Jack Jack"; // 이건 가능
	const char* name2 = "Jack Jack";

	cout << (uintptr_t)name << endl;
	cout << (uintptr_t)name2 << endl;
}
```

주소가 같게 나온다. 컴파일러가 두 개 같은 걸 알고 주소를 공유하라고 한 것. 서로 다른 문자열을 넣으면 다른 주소가 나온다. 

const를 붙여야 기호적 상수로 쓸 수 있다는 것을 유의할 것.



```cpp
const char* getName()
{
	return "JackJack";
}
```

return으로도 가능



### 문자열 출력

```cpp
	int int_arr[5] = { 1, 2, 3, 4, 5 };
	char char_arr[] = "Hello, World!";
	const char* name3 = "Jack Jack";

	cout << int_arr << endl;
	cout << char_arr << endl;
	cout << name3 << endl;
```

```cpp
004FF72C
Hello, World!
Jack Jack
```

포인터(주소)를 출력했음에도 문자열 전체를 출력해준다 -> cout에서 문자열 출력을 독특하게 처리한다. 문자의 pointer가 들어오면 문자열일 것이라고 간주함.



### 문자 하나만

```cpp
	char c = 'Q';
	cout << &c << endl;

```

```txt
Q儆儆儆儆<쎱
```

컴파일러가 문자열일 것이라 예상하고 null 문자가 나올 때까지 계속해서 출력하게 된다. 





## 6.11 메모리 동적 할당 new와 delete

1. static memory allocation - 한번 만들면 프로그램이 끝날 때까지 메모리를 갖고 있는 것

2. 자동 메모리 할당 - 블록 밖으로 나가면 사라짐

3. 동적 메모리 할당 - 포인터와 관련지어 가장 까다로운 부분



```cpp
#include <iostream>

using namespace std;

int main()
{
	int array[1000000]; // stack

	

	return 0;
}
```

정적으로 할당된 것은 스택에 들어가는데, 스택은 크기가 작다. 따라서 빌드하면 안 됨.

동적 할당 된 것은 heap에 들어가는데, 여기에 많이 들어갈 수 있다.



### new

new는 해당 타입을 만든 다음에 주소를 준다. 따라서 주소로 받아야 한다.

```cpp
	//int var;
	//var = 7;

	int *ptr = new int;
	*ptr = 7; // dereference
```

```cpp
	int* ptr2 = new int{ 7 }; // new int(7)로도 가능
```



### delete

OS에 메모리를 돌려주는 것

```cpp
	delete ptr;
```

앞에서는 안 써줬다. 이건 프로그램이 끝나면서 OS가 알아서 거둬갔기 때문.



### 삭제 이후

```cpp
	// delete
	delete ptr;

	cout << "After delete" << endl;
	cout << ptr << endl;
	cout << *ptr << endl;
```

```txt
00008123

```

주소는 그대로 남아있다. 그 주소를 de refer하면 엉뚱한 값이 나오게 됨.



```cpp
	delete ptr;
	ptr = nullptr; // 쓸모가 없음을 명시

	cout << "After delete" << endl;
	if (ptr != nullptr)
	{
		cout << ptr << endl;
		cout << *ptr << endl;
	}
```

이렇게 nullptr을 넣어줘서 있는 경우에만 출력하게 한다.



### 그렇다면 메모리를 다른 데서 다 쓰고 있어서 못 쓰는 경우

new가 에러를 일으켜도 버티게 해야 한다.

```cpp
	int* ptr3 = new (std::nothrow) int{ 7 };

	if (ptr3)
	{
		cout << ptr3 << endl;
		cout << *ptr3 << endl;
	}
	else {
		cout << "Could not allocate memory" << endl;
	}
```

이렇게 처리하면 에러가 나지 않게 된다.



```cpp
	int* ptr2 = ptr;

	delete ptr;
	ptr = nullptr;
	// 여기서 ptr2도 nullptr이 되어야 하는데 그렇지 않는다.
	// ptr2 = nullptr; 이라고 해주는 방법이 1.
```



### memory leak

```cpp
	// memory leak
	while (true)
	{
		int* ptr = new int;
		cout << ptr << endl;
	}
	// 여기서는 block밖이므로 ptr이 사라짐. 그러나 할당되어 있음.
```



### 확인하는 방법 1.

프로그램이 크다면 task manager에서 performance -> memory 사용량이 증가하는 추세면 새고 있는 것.



### 방법 2.

debug - window - show diagnostic tools에서 메모리 사용량을 출력



new, delete은 OS에 가서 메모리를 가져오고 반납하는 과정이 필요하므로 속도가 느리다. 따라서 프로그래밍을 잘하려면 new, delete을 적게 쓰는 것이 중요하다. new, delete을 직접 관리할 수만 있으면 가장 좋다. 어렵기 때문에 이걸 보완하는 방식이 최근에 등장하고 있다.





## 6.12 동적 할당 배열

```cpp
#include <iostream>

using namespace std;

int main()
{
	int length;

	cin >> length;

	//int array[length];
	int* array = new int[length];

	array[0] = 1;
	array[1] = 2;

	for (int i = 0; i < length; ++i)
	{
		cout << (uintptr_t) & array[i] << endl;
		cout << array[i] << endl;
	}

	delete[] array; // 긴 사이즈의 메모리를 삭제

	return 0;

}
```

전부 0으로 초기화하고 싶다면

```cpp
	int* array = new int[length]();
```



```cpp
	int* array = new int[length] {11, 22, 33, 44, 55, 66};

	array[0] = 1;
	array[1] = 2;

	for (int i = 0; i < length; ++i)
	{
		cout << (uintptr_t) & array[i] << endl;
		cout << array[i] << endl;
	}

	delete[] array; // 긴 사이즈의 메모리를 삭제

	return 0;
```

6개 지정해놓고 length에 5를 입력하면 런타임 에러 발생. 다른 프로그램이 쓰고 있어서 메모리 충돌이 발생한다.



### 사이즈 지정 생성

```cpp
	int fixedArray[] = { 1, 2, 3, 4, 5 };

	int* array2 = new int[5]{ 1, 2, 3, 4, 5 }; // 강의에서는 안 된다고 함

	for (int i = 0; i < 5; i++)
	{
		cout << array2[i] << endl;
	}

	delete[] array2;
```



### resizing

1) 새로 만들어서 복사해오는 방법.

2) OS에 더 달라고 요청하는 방법

but std::vector에서 알아서 잘 해줌.



포인터 연산도 동일하게 값들에 접근할 수 있다.





## 6.14 참조 변수 reference variable

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 5;

	// pointer
	int* ptr = nullptr;
	ptr = &value;

	// reference
	int& ref = value;

	cout << ref << endl;

	ref = 10;

	cout << value << " " << ref << endl;


	
	return 0;
}
```

메모리 주소를 공유하는 변수를 만들 수 있음. 별명처럼 사용할 수 있다.



주소를 찍어보면 재밌다.

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 5;

	// pointer
	int* ptr = nullptr;
	ptr = &value;

	// reference
	int& ref = value;

	cout << ref << endl;

	ref = 10; // *ptr = 10;

	cout << value << " " << ref << endl;


	cout << &value << endl;
	cout << &ref << endl;
	cout << ptr << endl;
	cout << &ptr << endl;

	
	return 0;
}
```

value와 ref는 같은 주소를 공유한다.



### 특징

- ref는 반드시 초기화(값 할당) 되어야 함

- literal(`104`와 같은 상수)은 들어갈 수 없음

- const 문제

  ```cpp
  	int x = 5;
  	int& ref2 = x;
  	
  	const int y = 8;
  	//int& ref2 = y; // 불가함 - ref2가 막 바꿔버릴 수도 있기 때문
  	const int& ref2 = y;
  ```

- 재할당 가능

  ```CPP
  
  	int value1 = 5;
  	int value2 = 10;
  
  	int& ref3 = value1;
  
  	cout << ref3 << endl;
  
  	ref3 = value2;
  
  	cout << ref3 << endl;
  
  ```

  

### 함수 인자

```cpp
void doSomething(int n)
{
	n = 10;
	cout << "in doSth " << n << endl;
}


	int n = 5;
	cout << n << endl; //5

	doSomething(n);

	cout << n << endl; //5
```

n이 복사가 돼서 main 변수에 영향을 주지 않는다.

영향을 주려면 어떻게 해야할까?

```cpp
void doSomething2(int &n)
{
	n = 10;
	cout << "in doSth " << n << endl;
}

	cout << n << endl;

	doSomething2(n);

	cout << n << endl;

```

레퍼런스를 쓰면 변수 자체를 넘기는 것. 편리함.

값, 주소조차도 복사를 할 필요가 없다 -> 효율이 좋다.



그런데 레퍼런스를 함수 단에서 고칠 수 없게 하려면 어떡할까? const로 막을 수 있다.

```cpp
void doSomething2(const int &n)
{
	// n = 10;
	cout << "in doSth " << n << endl;
}
```

```cpp
void printElements(int(&arr)[5]) // 개수 표시해야 함
{
	for (int i = 0; i < 5; i++)
	{
		// do sth
	}
}
```



### struct

```cpp
struct Something
{
	int v1;
	float v2;
};

struct Other
{
	Something st;
};

	Other ot;
	ot.st.v1 = 1.0; // 계속해서 안으로 들어가기가 귀찮다

	int& v1 = ot.st.v1;
	v1 = 1;
```





### 레퍼런스와 포인터의 비교

기능상 동일하다

```cpp
	int value4 = 5;
	int* const ptr4 = &value4; // 주소를 못 바꾸는 것
	int& ref4 = value4;
```





## 참조와 const

참조는 함수의 파라미터로 사용할 때 아주 편리하다.

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 5;
	int& ref_x = x;
	const int& ref_x = x;

	const int x2 = 5;
	const int& ref2_x = x2;
	

	return 0;
}
```

x를 const로 선언하고 ref에서 const를 선언하지 않으면 안 된다



```cpp

	const int& ref_x2 = 3 + 4;

	cout << ref_x2 << endl;
	cout << &ref_x2 << endl;
```

그냥 int와의 차이가 뭘까? 함수 파라미터로 넣을 때 아주 유용



```cpp
void doSomething(const int x)
{
	cout << x << endl;
}

void doSomething2(const int& x) // 변수 복사 없이 가능
{
	cout << x << endl;
}

	int a = 1;

	cout << endl;

	doSomething(a);
	doSomething(a + 2);
	doSomething(3);

	doSomething2(a);
	doSomething2(3);
	doSomething2(a + 3);
```





## 6.16 포인터와 참조의 멤버 선택

포인터나 참조를 통해 구조체나 클래스의 멤버를 접근할 수 있다.



```cpp
#include <iostream>

struct Person
{
	int age;
	double weight;

};

int main()
{
	Person person;

	person.age = 5;
	person.weight = 30;

	Person& ref = person;
	ref.age = 15;
	
	// 포인터는 좀 다르다
	Person* ptr = &person;
	ptr->age = 30;

	return 0;
}
```



```cpp
#include <iostream>

struct Person
{
	int age;
	double weight;

};

int main()
{
	Person person;

	person.age = 5;
	person.weight = 30;

	Person& ref = person;
	ref.age = 15;
	
	// 포인터는 좀 다르다
	Person* ptr = &person;
	ptr->age = 30;
	(*ptr).age = 20; // dereference를 쓰면 점으로 접근 가능
	
	Person& ref2 = *ptr;
	ref2.age = 45;

	std::cout << &person << std::endl;
	std::cout << &ref2 << std::endl;

	return 0;
}
```





## 6.17 C++11 For-each 반복문

```cpp
#include <iostream>

using namespace std;

int main()
{
	int fibonacci[] = { 0, 1, 1, 2, 3, 5, 8, 13,
							21, 34, 55, 89 };

	for (int number : fibonacci)
		cout << number << " ";
	cout << endl;
}
```



### 값을 바꿔보자

```cpp

	// change
	for (int number : fibonacci)
		number = 10;


	for (int number : fibonacci)
		cout << number << " ";
	cout << endl;
```

값이 그대로다. 함수 파라미터 성격으로 전달 되기 때문 -> 이걸 ref를 활용하여 변경 가능하게 만들어줄 수 있다.



```cpp
	// change
	for (int& number : fibonacci)
		number = 10;


	for (int number : fibonacci)
		cout << number << " ";
	cout << endl;
```



### auto

```cpp
	// change
	for (auto& number : fibonacci)
		number = 10;


	for (auto number : fibonacci)
		cout << number << " ";
	cout << endl;
```



### const

일반적으로 이렇게 쓴다.

```cpp
	// change
	for (auto& number : fibonacci)
		number = 10;


	for (const auto number : fibonacci)
		cout << number << " ";
	cout << endl;

```



### 가장 큰 숫자 찾기

```cpp
	int max_number = std::numeric_limits<int>::lowest();

	for (const auto& n : fibonacci)
		max_number = std::max(max_number, n);

	cout << max_number << endl;
	
```



array를 동적 할당하면 for each를 쓸 수 없다.

대신 vector를 쓰면 더 좋다.



### vector

```cpp
#include <vector>


	vector<int> fibonacci = { 0, 1, 1, 2, 3, 5, 8, 13,
							21, 34, 55, 89 };
```

위에서와 같이 동일하게 쓸 수 있다.





## 6.18 보이드 포인터 void pointers

포인터는 주소다.자료형과 상관없이 포인터를 저장할 수 있지 않을까?

void pointer는 generic(포괄적) pointer라고도 불린다.



```cpp
#include <iostream>

int main()
{
	int		i = 5;
	float	f = 3.0;
	char	c = 'a';

	void* ptr = nullptr;

	ptr = &i;
	ptr = &f;
	ptr = &c;




	return 0;
}
```

이렇게 써도 문제가 없다.



but 실제로 어떤 타입이 들어갔는지 알 방법이 없다.

또한 포인터 연산이 불가함

```cpp
cout << ptr + 1 << endl; // 몇바이트 더해야 하는지 알 수 없음
```



de-reference도 불가

```cpp
	cout << *ptr << endl;
```



casting 해줘야한다.

```cpp
	cout << *static_cast<float*>(ptr) << endl;
```



다형성 구현을 하다보면 부득이하게 이렇게 써야 하는 경우가 있다.

```cpp
enum Type
{
	INT,
	FLOAT,
	CHAR
};

	Type type = FLOAT;

	if (type == FLOAT)
		cout << *static_cast<float*>(ptr) << endl;
	else if(type == INT)
		cout << *static_cast<int*>(ptr) << endl;

```



but 최근에는 새로운 문법으로 더 편하게 쓸 수 있다.





## 6.19 다중 포인터와 동적 다차원 배열

```cpp
#include <iostream>

using namespace std;

int main()
{
	int* ptr = nullptr;
	int** ptrptr = nullptr;

	int value = 5;

	ptr = &value;
	ptrptr = &ptr;

	cout << ptr << " " << *ptr << " " << &ptr << endl;
	cout << ptrptr << " " << *ptrptr << " " << &ptrptr << endl;
	cout << **ptrptr << endl;

	return 0;
}
```

삼중, 사중 포인터도 가능. 실제로 잘 사용하지는 않는다.



### 이중 포인터 이차원 행렬 구현

```cpp
	int* r1 = new int[col] {1, 2, 3, 4, 5};
	int* r2 = new int[col] {6, 7, 8, 9, 10};
	int* r3 = new int[col] {11, 12, 13, 14, 15};

	// integer pointer의 array를 만들자
	int** rows = new int* [row] {r1, r2, r3};

	for (int r = 0; r < row; ++r)
	{
		for (int c = 0; c < col; ++c)
			cout << rows[r][c] << " ";
		cout << endl;
	}

	delete[] r1;
	delete[] r2;
	delete[] r3;
	delete[] rows;
```



for 문으로 delete를 하게 해보자.



```cpp
	const int row = 3;
	const int col = 5;

	const int s2da[row][col] =
	{
	{1, 2, 3, 4, 5},
	{6, 7, 8, 9, 10},
	{11, 12, 13, 14, 15}
	};

	// integer pointer의 array를 만들자
	int** matrix = new int* [row];

	for (int r = 0; r < row; ++r)
		matrix[r] = new int[col];


	for (int r = 0; r < row; ++r)
	{
		for (int c = 0; c < col; ++c)
		{
			matrix[r][c] = s2da[r][c];
			cout << matrix[r][c] << " ";
		}
		cout << endl;
	}

	// delete
	for (int r = 0; r < row; ++r)
		delete matrix[r];

	delete[] matrix;
```



### 이중 포인터 쓰지 않기

```cpp
	// 2차원으로 만들지 않는 법
	int* matrix2 = new int[row*col];

	for (int r = 0; r < row; ++r)
	{
		for (int c = 0; c < col; ++c)
		{
			matrix2[c + col * r] = s2da[r][c];
			cout << matrix2[c + col * r] << " ";
		}
		cout << endl;
	}

	// delete
	delete[] matrix2;

```





## 6.20 std::array 소개

```cpp
#include <iostream>
#include <array>

using namespace std;

int main()
{
	// int array[5] = { 1, 2, 3, 4, 5 }

	array<int, 5> my_arr = { 1, 2, 3, 4, 5 };
	my_arr = { 0, 1, 2, 3, 4 };
	my_arr = { 0, 1, 2 }; // 나머지는 0으로 채워짐

	cout << my_arr[0] << endl;
	cout << my_arr.at(0) << endl; // 똑같이 작동


}
```

at을 사용하면 미리 번지를 체크해보고 에러가 나면 예외처리를 발동. 대신 좀 더 느리다. 퍼포먼스가 아주 중요한 프로그램을 만들 때는 전자를 사용.



```cpp
#include <iostream>
#include <array>

using namespace std;

void printLength(array<int, 5> my_array)
{
	cout << my_array.size() << endl;
}

int main()
{
	// int array[5] = { 1, 2, 3, 4, 5 }

	array<int, 5> my_arr = { 1, 2, 3, 4, 5 };
	my_arr = { 0, 1, 2, 3, 4 };
	my_arr = { 0, 1, 2 }; // 나머지는 0으로 채워짐

	cout << my_arr[0] << endl;
	cout << my_arr.at(0) << endl; // 똑같이 작동

	cout << my_arr.size() << endl;

}
```

함수에 넣을 경우 array에 복사가 된다. 클 경우에 시간이 오래 걸림

원래 배열을 변경하고 싶을 경우 레퍼런스를 쓰면 편하다.(변경하고 싶지 않다면 const)

```cpp
void printLength(const array<int, 5>& my_array)
{
	cout << my_array.size() << endl;
}

```



### for each

```cpp
	for (auto &element : my_arr)
		cout << element << " ";
	cout << endl;
```



### sort

sorting을 할 구간을 선택해야 한다.

```cpp
	std::sort(my_arr.begin(), my_arr.end());

	for (auto& element : my_arr)
		cout << element << " ";
	cout << endl;
```

내림차순으로 정렬하려면?

```cpp
	std::sort(my_arr.rbegin(), my_arr.rend());
```





## 6.21 std::vector 소개

정적 배열에 array가 있다면 동적 배열에 vector

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	// std::array<int, 5> array; // 사이즈를 반드시 적어줘야
	std::vector<int> array; // 필수가 아님

	std::vector<int> array2 = { 1, 2, 3, 4, 5 };

	cout << array2.size() << endl; // 5

	std::vector<int> array3 = { 1, 2, 3 };

	cout << array3.size() << endl; // 3

	std::vector<int> array4 = { 1, 2, 3, };

	cout << array4.size() << endl; // 3

}
```





### foreach

```cpp
	vector<int> arr = { 1,2, 3, 4,5 };

	for (auto& itr : arr)
		cout << itr << " ";
	cout << endl;
```



### at

```cpp
	cout << arr[1] << endl;
	cout << arr.at(1) << endl;
```



### delete?

delete을 해줄 필요가 없다. block을 벗어나면 알아서 없어짐. delete의 부담을 줄여준다.

배열의 길이를 스스로 알고 있다. 그냥 배열은 길이를 알 수가 없다.

```cpp
	cout << arr.size() << endl;
```



### resize 가능

```cpp
	arr.resize(10);

	arr.push_back(333);
```

줄이는 것도 가능하다. 뒤의 것들이 날아감.













































