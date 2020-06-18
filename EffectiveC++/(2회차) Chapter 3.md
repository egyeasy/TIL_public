# Chapter 3. Resource Management

리소스는 쓰고 나면 시스템에 반환해야 하는 것이다. c++에서 주로 리소스는 동적으로 할당한 메모리를 의미하지만, 메모리 뿐만 아니라 파일 디스크립터, mutex lock, font, brush, database connection, network socket이 포함 된다. 

## Item 13: 리소스 관리에 객체를 사용해라.

```cpp
void f()
{
    Investment *plnv = createInvestment();
    //...
    delete plnv;
}
```

이 예제에서 중간에 return이 불리거나, loop 안에 delete를 뒀는데 break 등을 통해 탈출하거나, throw가 발생하는 등으로 delete가 불리지 않게 되면 리소스를 회수하지 못하게 된다.

코드가 오랜 시간 동안 유지보수 되면서 그렇게 바뀌게 될 가능성이 충분히 존재한다.

-> 리소스를 객체 안에 넣어서 그 객체가 소멸될 때 리소스를 반환하도록 하자.



### auto_ptr

block이나 function을 벗어났을 때 알아서 동적 할당된 메모리를 반환해주는 standard library의 리소스 매니징 객체.

```cpp
void f()
{
    std::auto_ptr<Investment> plnv(createInvestment());
}
```

여기서 auto_ptr과 같은 리소스 매니징 객체의 두 가지 특징을 알 수 있다

1. 리소스는 획득된 즉시 리소스 매니징 객체에게 넘겨진다.
2. 리소스 매니징 객체는 자신의 destructor를 이용해서 리소스가 해제될 것을 보장한다.



**copying 방지**

auto_ptr이 소멸되면서 리소스를 반환하게 되면 또 다시 auto_ptr이 가리키는 대상에 접근했을 때 undefined behavior가 발생할 것이다. 이를 방지하기 위해 auto_ptr에서는 copy를 했을 때 copy를 시도한 auto_ptr 객체가 null이 되도록 해놓았다.

따라서 하나의 대상에 대해 여러 auto_ptr이 생길 수 없다. 하지만 STL container들의 경우 자신의 item들이 정상적인 copying behavior를 제공해야 할 것을 요구하기 때문에, 이 경우에는 auto_ptr을 쓸 수 없게 된다.

그럴 때는 RCSP를 쓸 수 있다.



### 레퍼런스 카운팅 스마트 포인터 - shared_ptr 

얼마나 많은 객체가 특정한 리소스를 가리키는지 카운팅하다가, 0개가 될 때 리소스 delete 해주는 포인터.

```cpp
void f()
{
    std::tr1::shared_ptr<Investment>
        plnv(createInvestment());
}

std::tr1::shared_ptr<Investment> plnv2(plnv1);
plnv1 = plnv2;
```

복사나 할당의 경우에도 예상한대로 작동한다.



### 동적 할당 배열에서는 사용하지 말 것

단 auto_ptr이나 tr1::shared_ptr은 동적 할당 배열을 delete할 경우에는 제대로 작동하지 않는다. 그 대안으로 vector나 string과 같은 container를 쓸 것을 권장하지만, 그것도 싫다면 Boost에서 제공하는 boost::scoped_array, boost::shared_array를 사용해라.

```cpp
std::auto_ptr<std::string> aps(new std::string[10]);	// wrong delete가 이루어짐
std::tr1::shared_ptr<int> spi(new int[1024]);			// 마찬가지
```



특정 리소스에 대해서는 auto_ptr이나 shared_ptr을 사용하지 못할 수도 있다. 그 때에는 스스로 리소스 매니징 객체를 만들어서 써야 한다.



추가적으로 덧붙여서, createInvestment라는 팩토리 함수의 return type을 raw pointer로 설정해두는 것은 리소스 leak의 위험을 높인다. 이것은 Item 18에서 다루겠다.





## Item 14: 리소스 매니징 클래스에서 복사하는 것에 대해 신중하게 생각해라.

RAII : Resource Acqusition은 Initialization이다.

heap-based 리소스를 사용하는 게 아니라면 auto_ptr이나 shared_ptr을 쓸 수 없다. 그렇다면 때때로 너가 직접 리소스 매니징 클래스를 만들어줘야 한다.



### mutex 관리 C API를 쓰는 예제

```cpp
void lock(Mutex *pm);
void unlock(Mutex *pm);
```



클래스로 관리해보자.

```cpp
class Lock {
  public:
	explicit Lock(Mutex *pm)
      : mutexPtr(pm)
      {
          lock(mutexPtr);
      }
    ~Lock() {
        unlock(mutexPtr);
    }
  private:
    Mutex *mutexPtr;   
}
```



그러면 클라이언트는 RAII 방식으로 Lock을 쓸 수 있게 된다.

```cpp
Mutex m;
{
    Lock ml(&m);
}
```



그런데 Lock object가 복사된다면 어떻게 될까?

```cpp
Lock ml1(&m);
Lock m12(ml1);
```

이 경우의 대처 방안을 선택해야 한다.



1. 복사를 금지한다

   synchronization primitive를 복사하는 것이 말이 안되기 때문에 금지하는 방법을 쓸 수 있다.

   ```cpp
   class Lock: private Uncopyable {
       
   }
   ```

   Item 6에서 설명한 방식을 통해 Uncopyable의 복사 operation을 private으로 선언해서 상속받게 한다.

2. 리소스의 레퍼런스를 카운트한다

   사용자는 리소스를 쓰는 객체가 모두 파괴되기 전까지 리소스를 들고 있는 것을 원할 수도 있다.

   그 경우 shared_ptr\<Mutex\> 타입의 멤버 변수를 두는 방식으로 설계가 가능하다.

   ```cpp
   class Lock {
     public:
       explicit Lock(Mutex *pm)
         : mutexPtr(pm, unlock)
         {
             lock(mutexPtr.get());
         }
     private:
       std::tr1::shared_ptr<Mutex> mutexPtr;
   }
   ```

   여기서 shared_ptr이 소멸 시에 Mutex를 delete하는 게 아니라 unlock 해줘야 하는데, shared_ptr에서는 소소멸 시 delete 대신 수행할 처리(deleter)를 지정해줄 수 있다(auto_ptr에서는 불가능)

   이렇게 하면 사용자가 Lock의 소멸자를 정의해주지 않아도 알아서 unlock이 불리게 된다.

3. 리소스를 카피한다

   리소스 매니징 객체를 복사할 때 이것이 감싸고 있는 리소스 또한 복사하게 할 수 있다.(deep copying)

   standard string 타입의 구현체 중에서 heap memory에 대한 포인터를 가지고 있는 경우가 있다. 이 경우에 string을 복사 하게 되면 포인터와 그 heap memory의 주소를 함께 복사해서 deep copying이 발생한다.

4. 리소스의 소유권을 넘긴다

   copied object에서 copying object로 소유권을 넘기는 방법도 있다. 이것은 auto_ptr에서 사용되는 copy 방식이다.























