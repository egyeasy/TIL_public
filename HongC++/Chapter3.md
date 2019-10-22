## 3.1 연산자 우선순위와 결합법칙

### 위키피디아(영어) 연산자 우선순위 표

*, /, %는 level 5로 같은 우선순위. +와 -는 level 6. 5가 더 높은 걸로 인정된다.

`Left-to-right`은 우선순위가 같을 때 어떻게 처리할 것이냐 -> 좌에서 우 순을 말하는 것

linery plus/minus는 +3, -3과 같은 것. !(logically not), ~(bitwisely not)과 함께 level 3이다.

`=` : direct assignment

애매하면 괄호를 쳐서 우선순위를 명확하게 설정하자.





## 3.2 산술 연산자 arithmetic operator

```cpp
using namespace std;

int x = 1;
int y = -x; // 단항 연산자는 붙여서 쓰도록 하자
y = 1 - -x; 

return 0;
```



### 나누기와 나머지

정수 나머지, float 나머지가 다르다.

```cpp
int x = 7;
int y = 4;

cout << x / y << endl; // 1
cout << float(x) / y << endl; // 1.75
cout << x / float(y) << endl; // 1.75
cout << float(x) / float(y) << endl; // 1.75
```

나눗셈 둘 중 하나만 실수여도 결과는 실수다.



C++11부터는 -5 / 2를 버림해서 -2가 나오게 됨. 이전에는 어떻게 처리할지 애매했었다.

-5 % 2의 경우에도 왼쪽 숫자가 마이너스면 나머지도 마이너스, 플러스면 나머지도 플러스로 처리하기로.



```cpp
int x = 7;
int y = 4;

int z = x; // z = 7
z += y; // z = z + y;
```



## 3.3 증감 연산자 increment decrement operators

```cpp
using namespace std;

int x = 5;
int y = ++x;
int z = x--;

cout << y << endl; // 4
cout << z << endl; // 4

return 0;
```



다음부터가 중요한 얘기

```cpp
int x = 6, y = 6;
cout << x << " " << y << endl; // 6 6
// cout << ++x << " " << --y << endl; // 7 5
cout << x++ << " " << y-- << endl; // 6 6
cout << x << " " << y << endl; // 7 5
```

x++, y--는 출력한 다음에 연산을 적용하는 개념



부작용이 될 수 있는 경우를 알아보자

```cpp
int add(int a, int b)
{
    return a + b;
}

int main()
{
    using namespace std;
    
    int x = 1;
    int v = add(x, ++x); // do not use like this - 다른 변수 y를 만들어서 ++y로 넣는 것은 괜춘
    
    cout << v << endl;
    
    return 0;
}
```



```cpp
int main()
{
    using namespace std;
    
    int x = 1;
    // x = x++; // 결과가 명확하지 않다
    ++x;
    
    cout << x << endl;
    
    return 0;
}
```











































