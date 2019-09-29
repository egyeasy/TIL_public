# Week 4. Geometric Transformations I

자료 - week4_starting_full

### main.cpp

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
#include "Matrix4.h"

const int width_window = 640;
const int height_window = 640;

class Vector3
{
public:
	union {
		struct { float x_, y_, z_; };
		float v_[3];
	};

	Vector3(const float& _x, const float& _y, const float& _z)
		: x_(_x), y_(_y), z_(_z)
	{}
};

//Vec3 colors[3] = { Vec3(1.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 1.0) };
//Vec3 pos[3] = { Vec3(0.0, 0.0, 0.0), Vec3(1.0f, 0.0, 0.0), Vec3(0.0f, 1.0f, 0.0) };
//GLubyte indices[] = { 0, 1, 2 };

const int num_vertices = 24;
const int num_quads = 6;

const Vector3 colors[num_vertices] =
{
	Vector3(0, 0, 0.8),
	Vector3(0, 0, 0.8),
	Vector3(0, 0, 0.8),
	Vector3(0, 0, 0.8),

	Vector3(1, 0, 0),
	Vector3(1, 0, 0),
	Vector3(1, 0, 0),
	Vector3(1, 0, 0),

	Vector3(0, 1, 0),
	Vector3(0, 1, 0),
	Vector3(0, 1, 0),
	Vector3(0, 1, 0),

	Vector3(1, 1, 0),
	Vector3(1, 1, 0),
	Vector3(1, 1, 0),
	Vector3(1, 1, 0),

	Vector3(0.2, 0.2, 1),
	Vector3(0.2, 0.2, 1),
	Vector3(0.2, 0.2, 1),
	Vector3(0.2, 0.2, 1),

	Vector3(1, 0, 1),
	Vector3(1, 0, 1),
	Vector3(1, 0, 1),
	Vector3(1, 0, 1)
};

Vector4<float> positions[num_vertices] = 
{
	Vector4<float>(0.0, 0.0, 0.5, 1.0),
	Vector4<float>(0.5, 0.0, 0.5, 1.0),
	Vector4<float>(0.5, 0.0, 0.0, 1.0),
	Vector4<float>(0.0, 0.0, 0.0, 1.0),

	Vector4<float>(0.0, 0.0, 0.5, 1.0),
	Vector4<float>(0.5, 0.0, 0.5, 1.0),
	Vector4<float>(0.5, 0.5, 0.5, 1.0),
	Vector4<float>(0.0, 0.5, 0.5, 1.0),

	Vector4<float>(0.5, 0.0, 0.5, 1.0),
	Vector4<float>(0.5, 0.0, 0.0, 1.0),
	Vector4<float>(0.5, 0.5, 0.0, 1.0),
	Vector4<float>(0.5, 0.5, 0.5, 1.0),

	Vector4<float>(0.0, 0.0, 0.5, 1.0),
	Vector4<float>(0.0, 0.0, 0.0, 1.0),
	Vector4<float>(0.0, 0.5, 0.0, 1.0),
	Vector4<float>(0.0, 0.5, 0.5, 1.0),

	Vector4<float>(0.0, 0.0, 0.0, 1.0),
	Vector4<float>(0.5, 0.0, 0.0, 1.0),
	Vector4<float>(0.5, 0.5, 0.0, 1.0),
	Vector4<float>(0.0, 0.5, 0.0, 1.0),

	Vector4<float>(0.0, 0.5, 0.5, 1.0),
	Vector4<float>(0.5, 0.5, 0.5, 1.0),
	Vector4<float>(0.5, 0.5, 0.0, 1.0),
	Vector4<float>(0.0, 0.5, 0.0, 1.0)
};

const GLbyte indices[num_quads * 4] = {
	0, 1, 2, 3,
	4, 5, 6, 7,
	8, 9, 10, 11,
	12, 13, 14, 15,
	16, 17, 18, 19,
	20, 21, 22, 23
};

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
	//glOrtho(-0.2, 1.2, -0.2, 1.2, -10.0, 10.0);
	glOrtho(-1.2, 1.2, -1.2, 1.2, -100.0, 100.0);
	//TODO: consider anisotropic view
	gluLookAt(12, 0.8, 12, 0.0, 0.0, 0.0, 0, 1, 0);
	//glLoadIdentity();
	//gluLookAt(1, 1, 1, 0.5, 0.5, 0.5, 0, 1, 0);
	//gluLookAt(0, 0, 0, 0.25, 0.25, 0.25, 0, 1, 0);
	//glEnableVertexAttribArray(0);
	//GLuint VertexArrayID;
	//glGenVertexArrays(1, &VertexArrayID);
	//glBindVertexArray(VertexArrayID);

	GLuint vbo[3];
	glGenBuffers(3, vbo);
	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(colors), colors, GL_STATIC_DRAW);
	glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(positions), positions, GL_STATIC_DRAW);
	glBindBuffer(GL_ARRAY_BUFFER, vbo[2]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

	//NOTE: don't forget glDeleteBuffersARB(1, &vbo);

	// depth test
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LESS);

	/* Loop until the user closes the window */
	while (!glfwWindowShouldClose(window))
	{
		/* Render here */
		//glClear(GL_COLOR_BUFFER_BIT);
        // Have to clear RGB color & depth
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // <- depth test

		//TODO: draw here
		glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
		glEnableClientState(GL_COLOR_ARRAY);
		glColorPointer(3, GL_FLOAT, 0, 0);

		glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
		glEnableClientState(GL_VERTEX_ARRAY);
		glVertexPointer(4, GL_FLOAT, 0, 0);		// Vector4

		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo[2]);
		glPolygonMode(GL_FRONT, GL_FILL);
		glDrawElements(GL_QUADS, num_quads * 4, GL_UNSIGNED_BYTE, 0);

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



### ray casting

눈에서 ray를 쏜다고 생각하면 됨. 

![401](.\401.png)

### set identity

Identity matrix : 대각 요소가 모두 1이고, 나머지는 0인 행렬



### point & vector

```cpp
	while (!glfwWindowShouldClose(window))
	{
		Vector4<float> point(0.0, 0.0, 0.0, 1.0); // point in homongeneous coordinates
		Vector4<float> vector(0.0, 0.0, 0.0, 0.0); // vector in homongeneous coordinates
```

vector를 이동시킬 수는 없다. 대신 회전 시킬 수는 있음.

point는 이동시킬 수 있다. 



```cpp
		// translate point from (0, 0, 0) to (1, 0, 0)
		point.x_ = 1.0;
		point.y_ = 0.0;
		point.z_ = 0.0;

		const float dx = 0.1;
		const float dy = 0.2;
		const float dz = 0.133;

		// translate point by (dx, dy, dz)
		point.x_ += dx;
		point.y_ += dy;
		point.z_ += dz;
```



### 여러 점들을 옮기기

```cpp
void moveBox()
{
	const float dx = 0.1;
	const float dy = 0.2;
	const float dz = 0.133;
	
	for (int v = 0; v < num_vertices; v++)
	{
		positions[v].x_ += dx;
		positions[v].z_ += dy;
		positions[v].z_ += dz;
	}
}

int main(void)
{
    
    // ... ///
   
    	while (!glfwWindowShouldClose(window))
	{
		moveBox(); // animate objects
```



### translation matrix

(0, 0, 0, 0) vector + d의 결과는

Translation matrix(identity 행렬에 마지막 column만 앞의 vector로 구성됨) x d의 결과와 같다.

따라서 multiply를 통해서도 transition을 표현할 수 있다.

```cpp
void moveBox()
{
	const float dx = 0.1;
	const float dy = 0.2;
	const float dz = 0.133;

	Matrix4<float> tr;
	tr.setRow(0, 1, 0, 0, dx);
	tr.setRow(1, 0, 1, 0, dy);
	tr.setRow(2, 0, 0, 1, dz);
	tr.setRow(3, 0, 0, 0, 1);


	for (int v = 0; v < num_vertices; v++)
	{
		/*positions[v].x_ += dx;
		positions[v].z_ += dy;
		positions[v].z_ += dz;*/

		Vector4<float> temp = positions[v];
		tr.multiply(temp, positions[v]);
	}
}
```



































































