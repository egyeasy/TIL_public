# Week 2. Beginning OpenGL with GLFW

## 개발환경 세팅

https://webnautes.tistory.com/1102



## Polygon basics

**Polygonized circle** - 원을 삼각형으로 분할하여 그려보자.

분할 수를 늘릴수록 원에 가깝게 근사할 수 있게 된다.

```cpp
// OpenGL 개발환경 설정을 못해서 코드 일부만 따라침
int main()
{
	glfwMakeContextCurrent(window);
	glClearColor(102.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1);

	int width, height;
	glfwGetFramebufferSize(window, &width, &height);
	glViewpoint(0, 0, width, height);

	glOrtho(-1, 1, -1, 1, -1.0, 1.0);

	while(*!glfwWindowShouldClose(window))
	{
		/* render here */
		glClear(GL_COLOR_BUFFER_BIT);

		glBegin(GL_TRIANGLE_FAN); // GL_TRIANGLE 대신 triangle fan을 만들어준다.

		// center of polygonized circle
		glVertex2f(0.0, 0.0);

		const int num_triangles = 5;
		const float dtheta = 2.0 * 3.141592 / (float)num_triangles;
		const float radius = 0.5;

		float theta = 0.0;
		for (int i = 0; i <= num_triangles; i++, theta += dtheta)
		{
			const float x = radius * cos(theta);
			const float y = radius * sin(theta);

			glVertex2f(x, y);
		}
	}

	glEnd();
}
```



타원이 아니라 원처럼 보이게 비율을 화면에 맞게 조정해보자.



```cpp
	const float aspect_ratio = (float)width / (float)height; // 1.66, 1.9 TV display
	glOrtho(-1 / aspect_ratio, 1 / aspect_ratio, -1, 1, -1.0, 1.0);
```





## event model and callback

mouse, keyboard input

google : `glfw keyboard input example`

다음을 복사해서 main 함수 위에 복붙한다

```cpp
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
    if (key == GLFW_KEY_E && action == GLFW_PRESS)
        activate_airship();
}
```



### main.cpp

`GLFW_KEY_LEFT`, `GLFW_KEY_RIGHT` 등이 가능하다.

```cpp
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstring>
#include <stdlib.h>		// srand, rand
#include <thread>		// std::this_thread::sleep_for
#include <chrono>		// std::chrono::seconds
#include <iostream>
#include "math.h"

const int width_window = 640;
const int height_window = 480;

void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
    // keyboard 'E'가 눌러졌을 때 해당 함수를 실행
	if (key == GLFW_KEY_E && action == GLFW_PRESS)
		// activate_airship();
		std::cout << "Key pressed" << std::endl;
}

int main(void)
{
	GLFWwindow* window = nullptr;

	/* Initialize the library */
	if (!glfwInit())
		return -1;

	/* Create a windowed mode window and its OpenGL context */
	window = glfwCreatedWindow(width_window, height_window, "Lecture Example", NULL, NULL);

	if (!window)
	{
		glfwTerminate();
		return -1;
	}
	
	// callbacks here - 키 콜백
	glfwSetKeyCallback(window, key_callback);

	glfwMakeContextCurrent(window);
	glClearColor(102.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1);
```



방향키를 누를 때 좌우로 움직이게 만들어보자.



```cpp
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstring>
#include <stdlib.h>		// srand, rand
#include <thread>		// std::this_thread::sleep_for
#include <chrono>		// std::chrono::seconds
#include <iostream>
#include "math.h"

const int width_window = 640;
const int height_window = 480;

float circle_center_x = 0.0;
float circle_center_y = 0.0;

void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
	if (key == GLFW_KEY_E && action == GLFW_PRESS)
		// activate_airship();
		std::cout << "Key pressed" << std::endl;

	if (key == GLFW_KEY_LEFT && action == GLFW_PRESS)
	{
		circle_center_x -= 0.05;
	}
	if (key == GLFW_KEY_RIGHT && action == GLFW_PRESS)
	{
		circle_center_x += 0.05;
	}
}

int main(void)
{
	GLFWwindow* window = nullptr;

	/* Initialize the library */
	if (!glfwInit())
		return -1;

	/* Create a windowed mode window and its OpenGL context */
	window = glfwCreatedWindow(width_window, height_window, "Lecture Example", NULL, NULL);

	if (!window)
	{
		glfwTerminate();
		return -1;
	}
	
	// callbacks here - 키 콜백
	glfwSetKeyCallback(window, key_callback);

	glfwMakeContextCurrent(window);
	glClearColor(102.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1);

	int width, height;
	glfwGetFramebufferSize(window, &width, &height);
	glViewpoint(0, 0, width, height);

	const float aspect_ratio = (float)width / (float)height; // 1.66, 1.9 TV display
	glOrtho(-1 / aspect_ratio, 1 / aspect_ratio, -1, 1, -1.0, 1.0);

	while(*!glfwWindowShouldClose(window))
	{
		/* render here */
		glClear(GL_COLOR_BUFFER_BIT);

		glBegin(GL_TRIANGLE_FAN); // GL_TRIANGLE 대신 triangle fan을 만들어준다.

		// center of polygonized circle
		glVertex2f(circle_center_x, circle_center_y);

		const int num_triangles = 5;
		const float dtheta = 2.0 * 3.141592 / (float)num_triangles;
		const float radius = 0.5;

		float theta = 0.0;
		for (int i = 0; i <= num_triangles; i++, theta += dtheta)
		{
			const float x = radius * cos(theta + circle_center_x);
			const float y = radius * sin(theta + circle_center_y);

			glVertex2f(x, y);
		}
	}

	glEnd();
}
```



### Mouse input

구글링한 자료에서

**Cursor position**으로 이동

callback function 복붙

```cpp
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
	if (key == GLFW_KEY_E && action == GLFW_PRESS)
		// activate_airship();
		std::cout << "Key pressed" << std::endl;

	if (key == GLFW_KEY_LEFT && action == GLFW_PRESS)
	{
		circle_center_x -= 0.05;
	}
	if (key == GLFW_KEY_RIGHT && action == GLFW_PRESS)
	{
		circle_center_x += 0.05;
	}
}

static void cursor_position_callback(GLFWwindow* window, double xpos, double ypos)
{
	std::cout << xpos << " " << ypos << std::endl;
}

// ... //

	// callbacks here - 키 콜백, 마우스 콜백
	glfwSetKeyCallback(window, key_callback);
	glfwSetCursorPosCallback(window, cursor_position_callback);
```





















