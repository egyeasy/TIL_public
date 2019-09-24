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





# 두 번째 강의

아래와 같은 방식으로 vector를 쓸 수 있다. 대략적인 가이드라인만 제시해본다.

```c++
#include <vector>

    //Vector3 color[3] = {
    //        Vector3(1.0, 0.0, 0.0),
    //        Vector3(0.0, 1.0, 0.0),
    //       Vector3(0.0, 0.0, 1.0)
    //  }

	std::vector<Vector3> colors;
	colors.reserve(3);
	colors[0].r_ = 1; // ...(something more)

	// ... //

	glEnableClientState(GL_COLOR_ARRAY);  // enable to use color array
	glEnableClientState(GL_VERTEX_ARRAY); // enable to use vertext array

	colors.data(); // colors의 data에 접근할 수 있게 된다.

	glColorPointer(3, GL_FLOAT, 0, color);   // send color array to GPU(dimension, 자료타입(float == GL_FLOAT), stride)
	// stride : array 내에서 필요없는 element를 건너뛰기 위함. but harms performance a little bit
	glVertexPointer(3, GL_FLOAT, 0, vertex); // send vertex array to GPU

	glDrawArrays(GL_TRIANGLES, 0, 9); // (GLenum mode, array의 첫번째 index, element의 수)

	glDisableClientState(GL_COLOR_ARRAY);
	glDisableClientState(GL_VERTEX_ARRAY);
```





## GLEW

OS에서 program으로 메모리 chunk를 전달해주기 위해서는

```cpp
float *my_array = new float[...];
```



마찬가지로 GLEW를 써서 GPU로 동일한 일을 할 수 있다.(vertex buffer object)



```cpp
/* Make the window's context current */
glfwMakeContextCurrent(window);

// 아래 내용을 doc 파일에서 복붙해온다 - Enable GLEW
/* Make the window's context current */
	glfwMakeContextCurrent(window);

	// Initialize GLEW
	glewExperimental = true; // Needed for core profile
	if (glewInit() != GLEW_OK) {
		fprintf(stderr, "Failed to initialize GLEW\n");
		getchar();
		glfwTerminate();
		return -1;
	}


printf("%s\n", glGetString(GL_VERSION));

glClearColor(102.0 / 255.0 ...)
```

glfw와 context window를 연결시켜준 다음 glfw를 가져온다.



### Allocate memory in GPU

```cpp
	int num_vertices = 3;

	//float *my_array = new float[...];

	// 아래 내용을 복붙해온다.
	GLuint vbo[3]; // GLuint는 unsigned int, 이미 pointer로 기능하고 있음(float*와 같다)
	glGenBuffers(3, vbo); // vbo라는 pointer를 통해 메모리를 GPU에 전달 - 3개의 array를 쓸 수 있게 됨.

	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]); // 첫 번째 array의 메모리를 잡아준다. buffer를 bind한다 -> data를 GPU 안의 이 array에게 전달하겠다
	glBufferData(GL_ARRAY_BUFFER, sizeof(float) * num_vertices * 3, colors, GL_STATIC_DRAW); // execute sending data - 9는 3 vertices(triangle). 또한 moving object를 생각하지 않으므로 GL_STATIC_DRAW

	glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(float) * 9, vertex, GL_STATIC_DRAW); // vertex(geometry data)를 GPU에 알려준다.

	glBindBuffer(GL_ARRAY_BUFFER, vbo[2]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(GLubyte) * 3, indices, GL_STATIC_DRAW);

```

GPU랑 통신을 해야하기 때문에 이런 방식으로 쓰는 것.

bottleneck의 통신 양을 줄이기 위해 이런 스타일로 씀.

그래서 보통 좋아하는 스타일을 class로 묶어서 재사용함 -> 하드코딩 된 숫자를 최소한으로 줄여야 한다.





이에 따라 다음 부분이 필요없게 된다.

![301](.\301.png)



대신 다음을 써준다(doc에서 복붙)

```cpp
		//TODO: draw here
		glBindBuffer(GL_ARRAY_BUFFER, vbo[0]); // bind buffer
		glEnableClientState(GL_COLOR_ARRAY); // color 알려줌
		glColorPointer(3, GL_FLOAT, 0, 0); // 이전 방식에서는 마지막 인자가 'colors'였으나, 우리가 이미 GPU에 보내줬으므로 0으로 쓴다.

		glBindBuffer(GL_ARRAY_BUFFER, vbo[1]); // bind buffer
		glEnableClientState(GL_VERTEX_ARRAY); // vertex position
		glVertexPointer(3, GL_FLOAT, 0, 0); // 이전에는 'vertex'로 전달해줬으나, 지금은 위에서 전달해줬으므로 여기서 전달해줄 필요가 없다. - pipeline performance 상승.

		//glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo[2]);
		//glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, 0);

		glDrawArrays(GL_TRIANGLES, 0, 9); // 이 부분은 위에서 그대로 가져와서 쓴다.

		glDisableClientState(GL_COLOR_ARRAY);
		glDisableClientState(GL_VERTEX_ARRAY);

```



이렇게 함으로써 data를 GPU에서 reuse 할 수 있다.



## 한 변을 공유하는 삼각형

v0, v2를 공유하고 있는 두 삼각형이 있다고 할 때,

한 삼각형에서의 v0, v2를 다른 삼각형에서 v3, v4이라고 구별해서 써주면 구분이 돼서 편하다.

대신 v0, v2만 쓰는 것이 메모리 절약 측면에서는 좋다.

두 방법 다 알고 있어야 한다.



변을 공유하는 삼각형 두 개를 그려보도록 하자.

삼각형의 점 찍히는 순서가 시계방향으로 같게 설정한다.

```cpp
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <GL/GLU.h>
#include <cstring>
#include <stdlib.h>		  // srand, rand
#include <thread>         // std::this_thread::sleep_for
#include <chrono>         // std::chrono::seconds
#include <iostream>
#include "math.h"
#include <vector>

const int width_window = 640;
const int height_window = 640;

class Vec3
{
public:
	union {
		struct { float x_, y_, z_; };
		float v_[3];
	};

	Vec3(const float& _x, const float& _y, const float& _z)
		: x_(_x), y_(_y), z_(_z)
	{}
};

/// 6 colors
Vec3 colors[6] = { Vec3(1.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 1.0), Vec3(1.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 1.0) };

/// 6 verteces
float vertex[6][3] = {
    {0.0, 0.0, 0.0},
    {0.5, 0.0, 0.0},
    {0.25, 0.5, 0.0},
    {0.25, 0.5, 0.0},
    {0.5, 0.0, 0.0},
    {0.5, 0.5, 0.0}
}

// Vec3 pos[3] = { Vec3(0.0, 0.0, 0.0), Vec3(1.0f, 0.0, 0.0), Vec3(0.0f, 1.0f, 0.0) };
GLubyte indices[] = { 0, 1, 2 };

void update()
{
	//pos[0].x_ += 0.01;

	static float theta = 0.0;

	pos[1].x_ = cos(theta);
	pos[1].z_ = sin(theta);

	theta += 1.0 / 360.0 * 2.0* 3.141592;
}

int main(void)
{
	GLFWwindow *window = nullptr;

	/* Initialize the library */
	if (!glfwInit())
		return -1;

	//glfwWindowHint(GLFW_SAMPLES, 4);
	//glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	//glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	//glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
	//glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	/* Create a windowed mode window and its OpenGL context */
	window = glfwCreateWindow(width_window, height_window, "Hello World", NULL, NULL);

	if (!window)
	{
		glfwTerminate();
		return -1;
	}

	// callbacks here

	/* Make the window's context current */
	glfwMakeContextCurrent(window);

	// Initialize GLEW
	glewExperimental = true; // Needed for core profile
	if (glewInit() != GLEW_OK) {
		fprintf(stderr, "Failed to initialize GLEW\n");
		getchar();
		glfwTerminate();
		return -1;
	}

	glClearColor(1, 1, 1, 1); // while background

	printf("%s\n", glGetString(GL_VERSION));

	int width, height;
	glfwGetFramebufferSize(window, &width, &height);
	glViewport(0, 0, width, height);
	glOrtho(-0.2, 1.2, -0.2, 1.2, -10.0, 10.0);
	//TODO: consider anisotropic view
	gluLookAt(2, 2, 2, 0.5, 0.5, 0.5, 0, 1, 0);
	//glEnableVertexAttribArray(0);
	//GLuint VertexArrayID;
	//glGenVertexArrays(1, &VertexArrayID);
	//glBindVertexArray(VertexArrayID);

	GLuint vbo[3];
	glGenBuffers(3, vbo);
    
	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(float) * num_vertices * sizeof(Vector3), colors, GL_STATIC_DRAW
    
    /// 수정
	glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(float) * 6 * 3, vertex, GL_STATIC_DRAW);
	//glBindBuffer(GL_ARRAY_BUFFER, vbo[2]);
	//glBufferData(GL_ARRAY_BUFFER, sizeof(GLubyte) * 3, indices, GL_STATIC_DRAW);

	//NOTE: don't forget glDeleteBuffersARB(1, &vbo);

	/* Loop until the user closes the window */
	while (!glfwWindowShouldClose(window))
	{
		update();
		//if(updated == true)
		{
			glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
			glBufferData(GL_ARRAY_BUFFER, sizeof(float) * 9, pos, GL_STATIC_DRAW);
		}


		/* Render here */
		glClear(GL_COLOR_BUFFER_BIT);

		//TODO: draw here
		glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
		glEnableClientState(GL_COLOR_ARRAY);
		glColorPointer(3, GL_FLOAT, 0, 0);

		glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
		glEnableClientState(GL_VERTEX_ARRAY);
		glVertexPointer(3, GL_FLOAT, 0, 0);

		// glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo[2]);
		// glPolygonMode(GL_FRONT, GL_LINE);
		// glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, 0);
        
        /// 개수 수정
        glDrawArrays(GL_TRIANGLES, 0, 6 * 3);

		glDisableClientState(GL_COLOR_ARRAY);
		glDisableClientState(GL_VERTEX_ARRAY);

		/* Swap front and back buffers */
		glfwSwapBuffers(window);

		/* Poll for and process events */
		glfwPollEvents();

		std::this_thread::sleep_for(std::chrono::milliseconds(100));
	}

	glDeleteBuffersARB(3, vbo);

	glfwTerminate();

	return 0;
}
```

자료 폴더에서 복사해서 일부만 수정. 돌아가는지는 불확실



### 더 적은 vertex로 구성해보기

topology 수학과 관련된 것.

T1 : v0 v1 v2

T2 : v0 v2 v3

6개의 vertex를 보내는 대신 4개의 vertex를 보내서 2개의 triangle을 그려보자



```cpp
/// 4 colors
Vec3 colors[4] = { Vec3(1.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 1.0), Vec3(0.0, 0.0, 1.0) };

/// 4 verteces
float vertex[4][3] = {
    {0.0, 0.0, 0.0},
    {0.5, 0.0, 0.0},
    {0.25, 0.5, 0.0},
    {0.5, 0.5, 0.0}
}

/// docs에서 다음을 복붙해온다.
GLubyte indices[] = { 0, 1, 2, 1, 2, 3 };  // GLubyte은 unsigned char

// ... //

	GLuint vbo[3];
	glGenBuffers(3, vbo);
    
	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(float) * num_vertices * sizeof(Vector3), colors, GL_STATIC_DRAW
    
    
	glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(float) * 6 * 3, vertex, GL_STATIC_DRAW);
	
    /// 여기가 connectivity 정의하는 곳             
    glBindBuffer(GL_ARRAY_BUFFER, vbo[2]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(GLubyte) * 6, indices, GL_STATIC_DRAW);
                 
    // ... //
           
		glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
		glEnableClientState(GL_COLOR_ARRAY);
		glColorPointer(3, GL_FLOAT, 0, 0);

		glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
		glEnableClientState(GL_VERTEX_ARRAY);
		glVertexPointer(3, GL_FLOAT, 0, 0);

        /// 위와는 다르게 여기서는 Element Array buffer를 사용
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo[2]);
		glPolygonMode(GL_FRONT, GL_LINE);
		glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_BYTE, 0); // 3을 6으로 바꾸어야 삼각형 두개를 그림(3이면 하나만 그림)
```





### 3D 입체 도형

Z축을 0에서 바꿔보자.

```cpp
float vertex[4][3] = {
    {0.0, 0.0, 0.0},
    {0.5, 0.0, 0.0},
    {0.25, 0.5, 0.0},
    {0.5, 0.5, -0.5}
}
```

하지만 이렇게 변경해도 2D로만 그려지게 된다. view와 shading에 대해 설정을 해줘야 3D로 그릴 수 있다.

4번째 점을 이동시켰지만 이전과 같은 곳에서 바라보고 있기 때문에 같은 모양으로 나오는 것.



project 우클릭 -> properties -> linker -> input -> dependency에 glu32.lib 추가

```cpp
#include <GL/GLU.h>

// ... //

glClearColor(...)

gluLookAt(0.6, 0.6, 0.6, 0.5, 0.5, 0.5, 0, 1, 0);

int width, height;
glfwGetFramebufferSize(window, &width, &height);
```



gluLookAt은 9개의 숫자들로 이루어져있다. 첫번째 3개는 eye position x, y, z / 두 번째 3개는 바라보고 있는 지점(center position) x, y, z / 세 번째 3개는 어디가 위인지를 가리키는 것(up direction - camera rotation과 관련) x, y, z









































