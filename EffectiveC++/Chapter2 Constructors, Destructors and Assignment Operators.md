## Item 5: Know what functions C++ silently writes and calls.

비어있는 클래스의 경우에도 컴파일러가 선언하는 default constructor와 destructor가 있다. 이것들은 public이고 inline이다.



### copy constructor & copy assignment operator

이 둘을 정의하지 않으면 컴파일러는 non-static data member를 복사하는 방식으로 복사를 수행한다.

copy assignment operator의 경우 결과적으로 code가 legal해야 컴파일러가 컴파일을 수행한다. reference나 const 멤버를 copy assignment할 경우 이 멤버를 어떻게 처리해야할지 컴파일러가 결정할 수 없기 때문. (c++에서는 reference가 다른 object를 가리키는 것이 불가능) 컴파일러는 base class에서 operator가 private하게 선언된 상황에서 derived class가 implicit하게 copy assignment operator를 부를 경우에도 거부한다.



### Things To Remember

컴파일러는 클래스의 default constructor, copy constructor, copy assignment operator와 destructor를 implicit하게 생성한다.