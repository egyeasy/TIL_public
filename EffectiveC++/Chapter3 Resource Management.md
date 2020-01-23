## Item 16: Use the same form in corresponding uses of new and delete.

### new

new를 사용할 때에는

1. 메모리가 할당되고
2. constructor가 호출된다.



### delete

delete를 사용할 때에는

1. destructor가 호출되고
2. 메모리가 해제된다.



single object용 메모리 layout은 array용과 다르다.

array에는 delete[]를 사용해야 한다.



c++에는 string과 vector가 있어서 dynamic allocate를 쓸 일이 거의 없을 것이다.



### Things To Remember

- new 표현에서 []를 쓰려면 이에 대응되는 delete에 []가 반드시 있어야 한다. new에서 []를 쓰지 않으면 delete에서도 []를 쓰지 말아야 한다.





## Item 17: Store newed objects in smart pointers in standalone statements.

```cpp
processWidget(std::tr1::shared_ptr<Widget>(new Widget), priority());
```

이 작업은 세 단계로 나뉠 수 있다.

1. Call priority
2. execute "new Widget"
3. call the tr1::shared_ptr constructor

하지만 C++ 컴파일러는 순서를 바꿔 버릴 수 있다.

1. Execute "new Widget"
2. Call priority
3. Call the tr1::shared_ptr contructor

2.에서 exception이 발생하면 new Widget의 포인터는 lost된다. 따라서 분리해서 쓰도록 하자.

```cpp
std::tr1::shared_ptr<Widget> pw(new Widget);

processWidget(pw, priority());
```



### Things to Remember

- 스마트 포인터 안에 있는 newed object를 단독 statement에 저장해라. exception이 throw됐을때 리소스 누출이 있을 수 있기 때문이다.