# Week 3. Polygonal Geometry and Modern OpenGL

CPU는 메모리와 함께 동작하고, 그래픽카드는 3D 가속을 이용하며 또한 메모리를 가지고 있다. 3D application에서 무언가를 그리도록 CPU에 명령하면, CPU는 polygons or geometric data를 GPU에 보낸다. GPU는 픽셀의 색깔 등을 정해서 display에 그려준다.

이러한 렌더링 프로세스에 있어서 bottle neck은 **CPU -> GPU 데이터 보내주는 과정**이다. input을 받는 과정, display하는 과정은 빠르게 이루어진다. `glColor3f(1.0, 0.0, 0.0)`와 같은 명령에 시간이 많이 소요되게 된다. -> 모던 OpenGL 방식을 사용해 개선할 수 있음



cf. Print OpenGL Version

```cpp
printf("%s\n", glGetString(GL_VERSION));
```



### Modern 삼각형

```cpp
float color[3][3] = {
    { 1.0, 0.0, 0.0 }, // the color of the first vertex
    { 0.0, 1.0, 0.0 }, // the color of the 2nd vertex
    { 0.0, 0.0, 1.0 }  // the color of the 3rd vertex
};

float vertex[3][3] = {
    { 0.0, 0.0, 0.0 } // first vertex
    { 0.5, 0.0, 0.0 } // second vertex
    { 0.25, 0.5, 0.0 } // third vertex
};

int num_vertices = 3;

while (!glfwWindowShouldClose(window))
{
    glClear(GL_COLOR_BUFFER_BIT);
    
	glBegin(GL_TRIANGLES);
    
    for(int v = 0; v < num_vertices; v++)
    {
        // 모두 동일
        // glColor3f(color[v][0], color[v][1], color[v][2]);
        // glColor3fv(color[v]);
        glColor3fv(&color[v][0]);
        
        glVertex3f(vertex[v][0], color[v][1], color[v][2]);
    }
    
}

```

벡터를 좀 더 인간답게 쓰기 위해 클래스를 만들어보자.



```cpp
class Vector3
{
    public:
    float x_, y_, z_;
    
    Vector3(const float& _x, const float& _y, const float& _z)
        : x_(_x), y_(_y), z_(_z)
        {}
}


// ... //

	Vector3 color[3] = {
        Vector3(1.0, 0.0, 0.0),
        Vector3(0.0, 1.0, 0.0),
        Vector3(0.0, 0.0, 1.0)
    }

	// ... //

	for(int v = 0; v < num_vertices; v++)
    {
        // 모두 동일
        glColor3f(color[v][0], color[v][1], color[v][2]);  // 이것만 가능하다.
        // glColor3fv(color[v]);
        // glColor3fv(&color[v][0]);
        
        glVertex3f(vertex[v][0], color[v][1], color[v][2]);
    }

```



Vector3의 array를 만들게 되면 메모리 상에 x, y, z, x, y, z, x, y, z 순으로 연속해서 나열되게 된다. 이건 위에서 직접 3x3 matrix를 만들어줬던 것과 똑같은 것으로 컴퓨터가 인식함. 그래서 위와 비슷하지만 조금 다른 방법을 사용한다. union을 사용하면 편리함.



```cpp
class Vector3
{
public:
    union
    {
        struct {float x_, y_, z_; };
        float v_[3]; // 3개의 float만 쓰고, memory를 share함
    };
    
    Vector3 color[3] = {
            Vector3(1.0, 0.0, 0.0),
            Vector3(0.0, 1.0, 0.0),
            Vector3(0.0, 0.0, 1.0)
        }

	// ... //
    Vector3(const float& _x, const float& _y, const float& _z)
        : x_(_x), y_(_y), z_(_z)
        {}
    
    for(int v = 0; v < num_vertices; v++)
    {
        // 모두 동일
        // glColor3f(color[v][0], color[v][1], color[v][2]);
        glColor3fv(colors[v].v_);
        // glColor3fv(&color[v][0]);
        
        glVertex3f(vertex[v][0], color[v][1], color[v][2]);
    }
}
```



x, y, z 대신에 rgb를 쓰고 싶다면?



```cpp
class Vector3
{
public:
    union
    {
        struct {float x_, y_, z_; };
        struct {float r_, g_, b_; };
        float v_[3]; // 3개의 float만 쓰고, memory를 share함
    };
    
    Vector3 color[3] = {
            Vector3(1.0, 0.0, 0.0),
            Vector3(0.0, 1.0, 0.0),
            Vector3(0.0, 0.0, 1.0)
        }

	// ... //
    Vector3(const float& _x, const float& _y, const float& _z)
        : x_(_x), y_(_y), z_(_z)
        {}
    
    for(int v = 0; v < num_vertices; v++)
    {
        // 모두 동일
        glColor3f(color[v].r_, color[v].g_), color[v].b_);
        // glColor3fv(colors[v].v_);
        // glColor3fv(&color[v][0]);
        
        glVertex3f(vertex[v][0], color[v][1], color[v][2]);
    }
}
```



Vector 3 클래스의 size를 알아ㅗㅂ자.



```cpp
int main(void)
{
    std::cout << "Size of Vec3: " << sizeof(Vector3) << std::endl;
}
```

Vec3은 12바이트. (4바이트x3) 이전에 비해 적으므로 union의 장점이 드러남. 



### 다른 버전 - 자료에서 복붙

```cpp
	// glBegin(GL_TRIANGLES);
	// ... //
	// glEnd();

	glEnableClientState(GL_COLOR_ARRAY);  // enable to use color array
	glEnableClientState(GL_VERTEX_ARRAY); // enable to use vertext array

	glColorPointer(3, GL_FLOAT, 0, color);   // send color array to GPU(dimension, 자료타입(float == GL_FLOAT), stride)
	// stride : array 내에서 필요없는 element를 건너뛰기 위함. but harms performance a little bit
	glVertexPointer(3, GL_FLOAT, 0, vertex); // send vertex array to GPU

	glDrawArrays(GL_TRIANGLES, 0, 9); // (GLenum mode, array의 첫번째 index, element의 수)

	glDisableClientState(GL_COLOR_ARRAY);
	glDisableClientState(GL_VERTEX_ARRAY);
```



모던 방식을 통해 훨씬 efficient하게 짤 수 있다. but 바로 위 방식의 단점은 데이터의 변경(애니메이션)을 할 때 계속해서 geometric data를 보내줘야한다는 것. 이걸 좀 더 쉽게 한 번만 보내주고 처리하는 방법을 다뤄보자.















