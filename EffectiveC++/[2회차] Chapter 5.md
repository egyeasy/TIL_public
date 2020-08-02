# Chapter 4. Implementations

클래스의 적절한 정의, 함수의 적절한 선언은 가장 중요한 요소다.

그것만 잘하면 나머지 구현은 쉽다.

다만 그래도 주의할 점들이 많다.

1. 너무 일찍 변수를 정의하는 것은 성능 저하를 가져올 수 있다.
2. cast의 과도한 사용은 코드를 느리게 하고, 유지보수하기 어렵게 하고, 미묘한 버그들에 감염될 수 있다.
3. 객체의 internal에 대한 핸들을 리턴하는 것은 encapsulation을 좌절시키고 클라이언트들에게 dangling handle을 던져주게 될 수 있다.
4. exception의 영향을 생각하지 않으면 리소스 leak과 자료구조 corruption을 유발할 수 있다.
5. 과도한 inline 사용은 코드 양을 너무 불리게 될 수 있다.
6. 지나친 coupling은 지나치게 긴 빌드 타임을 초래할 수 있다.

앞으로 하나씩 알아보자.



## Item 26: 변수 정의를 가능한 한 뒤로 연기하라.

생성자나 소멸자가 있는 타입의 변수를 정의하게 되면, 변수를 정의할 때 생성 비용이 들게 되고, 변수가 scope 밖으로 벗어나면 소멸 비용이 든다.

쓰이지 않는 변수들에 대해서도 비용이 발생하므로 가능한 한 언제든 정의를 피하라.



너가 쓰이지 않는 변수를 정의하지 않는다고 생각하겠지만,

다음과 같은 예시를 생각해보라.

string encrypted를 정의한 후에 패스워드가 너무 짧아서 throw를 하게 되면 변수를 쓰지 않는 상황이 발생한다.

throw를 하게 되면 생성자와 소멸자에 대한 비용을 지불하게 된다.



따라서 필요할 때까지 encrypted의 정의를 연기하는 것이 좋다.

```cpp
	throw logic_error;
string encrypted;

return encrypted;
```

하지만 이것으로도 불충분하다.

encrypted는 argument 초기화 없이 정의되었기 때문이다.

item4에서 설명했듯이 지금 코드는 디폴트 생성자를 부르고 그 후에 값을 할당하는 것은 비효율적이다.



예를 들어 다음과 같이 encrypt가 수행된다고 하면:

```cpp
void encrypt(std::string& s);
```

다음과 같은 과정은 불필요하게 비효율적이다.

```cpp
{
    string encrypted;
    encrypted = password;
    ecrypt(password);
    return encrypted;
}
```

따라서 불필요하게 비용이 드는 기본 생성자를 부르지 않도록 하자.

```cpp
{
    string encrypted(password);
    
    encrypt(encrypted);
    return encrypted;
}
```

이것이 Item의 제목에서 "가능한 한 뒤로 연기하라"는 것의 진짜 의미다.

1. 변수를 쓰기 직전까지 변수의 정의를 연기해라.
2. 변수를 초기화하는 argument가 생길 때까지 변수의 정의를 연기해라.

이를 통해 불필요한 객체의 생성과 소멸을 피하고, 불필요한 기본 생성자를 피할 수 있다.

또한 변수들의 의미가 명확한 컨텍스트 속에서 변수를 초기화하는 목적을 문서화하기 쉽다.



### 루프의 경우는?

변수가 루프 안에서만 쓰이는 경우에 변수를 루프 안에서, 밖에서 중 어디서 정의할 것인가?

#### Approach A: outside

```cpp
Widget w;
for (int i = 0; i < n; ++i) {
    w = some value dependent on i;
}
```



#### Approach B: inside

```cpp
for (int i = 0; i < n; ++i) {
    Widget w(some value dependent on i);
}
```



두 접근법의 비용은 다음과 같다.

Approach A: 1 constructor + 1 destructor + n assignments

Approach B: n constructors + n destructors



assignment가 constructor&destructor pair보다 비용이 적게 들면 A가 효율적이다. 이는 주로 n이 큰 경우에 해당한다. 그렇지 않으면 B가 낫다.

게다가 A는 w를 larger scope에서도 보이게 하므로 이는 프로그램의 가독성과 유지보수성에 반한다.

결과적으로,

1. assignment가 constructor-destructor보다 비용이 싸고
2. 성능에 민감한 파트를 다룬다면

B를 쓰도록 하라.

























