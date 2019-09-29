# Week 1. Programming matrix and vector



### Vector2D.h

```c++
class Vector2D
{
    public:
    	float x_, y_;
    	
    	Vector2D()
            : x_(0.0), y_(0.0)
            {}
    
    	void assign(const float& _x, const float& _y)
        {
            x_ = _x;
            y_ = _y;
        }
};
```



### main.cpp

```c++
#include <iostream>
#include "Vector2D.h"

int main()
{
    std::cout << "Hello World" << std::endl;
    
    Vector2D v0;
    v0.assign(1, 2);
    v0.print();
    
    Vector2D v1;
    v1.assign(2, 3);
    v1.print();
    
    void print()
    {
        std::cout << x_ << " " << y_ << std::endl;
    }
    
    return 0;
}
```



## 연산자 오버로딩

c++ 연산자 오버로딩에 대한 자료를 웹에서 찾을 수 있다.

### Vector2D.h

```c++
class Vector2D
{
    public:
    	float x_, y_;
    	
    	Vector2D()
            : x_(0.0), y_(0.0)
            {}
    
    	void assign(const float& _x, const float& _y)
        {
            x_ = _x;
            y_ = _y;
        }
    
        Vector2D& operator += (const Vector2D& v_input)
        {
            x_ += v_input.x_;
            y_ += v_input.y_;

            return *this;
        }
};
```



### main.cpp

```c++
#include <iostream>
#include "Vector2D.h"

int main()
{
    std::cout << "Hello World" << std::endl;
    
    Vector2D v0;
    v0.assign(1, 2);
    v0.print();
    
    Vector2D v1;
    v1.assign(2, 3);
    v1.print();
    
    void print()
    {
        std::cout << x_ << " " << y_ << std::endl;
    }
    
    v0 += v1;
    v0.print();
    
    return 0;
}
```

(1, 2) vector와 (2, 3) vector를 합쳐서 (3, 5) 벡터를 구할 수 있다.





## 스칼라곱(Dot product)

### Vector2D.h

```c++
float dotProduct(const Vector2D& v0, const Vector2D v1)
{
    return v0.x_ * v1.x_ + v0.y_ * v1.y_
}
```



### main.cpp

```c++
std::cout << "Dot product = " << dotProduct(v0, v1) << std:endl;
```



2D vector를 3D vector로 바꿔서 cross product를 구해볼 것



### Vector3D.h

```c++
class Vector3D
{
    public:
    	float x_, y_, z_;
    
    Vector3D()
        : x_(0.0), y_(0.0), z_(0.0)
    {}
    
    void assign(const float& _x, const float& _y, const float& _z)
    {
        x_ = _x;
        y_ = _y;
        z_ = _z;
    }
    
    void print()
    {
        std::cout << x_ << " " << y_ << " " << z_ << std::endl;
    }
    
    Vector3D crossProduct(const Vector3D& v0, const Vector3D& v1)
    {
        x_ = v0.y_ * v1.z_ - v0.z_ * v1.y_;
        y_ = v0.x_ * v1.z_ - v0.z_ * v1.x_;
        z_ = v0.x_ * v1.y_ - v0.y_ * v1.x_;
        
        return *this;
    }
}
```



TT로 템플릿 프로그래밍을 해보자 -> 공부할 것



### Vector3D.h

```c++
class Vector3D
{
    public:
    	TT x_, y_, z_;
    
    Vector3D()
        : x_(0.0), y_(0.0), z_(0.0)
    {}
    
    Vector3D(const TT& _x, const TT& _y, const TT& _Z)
        : x_(_x), y_(_y), z_(_z)
    {}
    
    void assign(const TT& _x, const TT& _y, const TT& _z)
    {
        x_ = _x;
        y_ = _y;
        z_ = _z;
    }
    
    void print()
    {
        std::cout << x_ << " " << y_ << " " << z_ << std::endl;
    }
    
    Vector3D crossProduct(const Vector3D& v0, const Vector3D& v1)
    {
        x_ = v0.y_ * v1.z_ - v0.z_ * v1.y_;
        y_ = v0.x_ * v1.z_ - v0.z_ * v1.x_;
        z_ = v0.x_ * v1.y_ - v0.y_ * v1.x_;
        
        return *this;
    }
}
```



### main.cpp

```c++
// TT를 썼으므로 template type을 지정해줘야 한다
Vector3D<float> v0(1, 0, 0), v1(0, 1, 0);

Vector3D<float> cr = crossProduct(v0, v1);

cr.print();
```

(1, 0, 0)과 (0, 1, 0)의 내적은 (0, 0, 1)이 나와야 맞다.



## 벡터 구현

### main.cpp

```cpp
#include <iostream>

class Vector2D
{
public:
	float x_, y_;

	Vector2D()
		: x_(0.0f), y_(0.0f)
	{}

	Vector2D(const float& _x, const float& _y)
		: x_(_x), y_(_y)
	{}

	// over-riding stream operator
	friend std::ostream & operator << (std::ostream& stream, const Vector2D& vec)
	{
		stream << "(" << vec.x_ << ", " << vec.y_ << ")";

		return stream;
	}
};

int main()
{
	Vector2D my_vec(1.0f, 2.0f);
	std::cout << my_vec << std::endl;

	return 0;
}
```







