#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstring>
#include <stdlib.h>
#include <thread>
#include <chrono>
#include <iostream>
#include "math.h"
#include <vector> // do not use list - because linked list is very slow

const int width_window = 640;
const int height_window = 480;

void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
	// keyboard 'E'가 눌러졌을 때 해당 함수를 실행
	if (key == GLFW_KEY_E && action == GLFW_PRESS)
	{
		std::cout << "Key Pressed" << std::endl;
	}
}

int main(void)
{
	GLFWwindow* window = nullptr;

	if (!glfwInit())
		return -1;

	window = glfwCreateWindow(width_window, height_window, "Lecture Example", NULL, NULL);

	if (!window)
	{
		glfwTerminate();
		return -1;
	}

	glfwSetKeyCallback(window, key_callback);

	glfwMakeContextCurrent(window);
	glClearColor(102.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1);

	// 원 그리기
	int width, height;
	glfwGetFramebufferSize(window, &width, &height);
	glViewport(0, 0, width, height);

	glOrtho(-1, 1, -1, 1, -1.0, 1.0);

	while (!glfwWindowShouldClose(window))
	{
		glClear(GL_COLOR_BUFFER_BIT);

		glBegin(GL_TRIANGLE_FAN);

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
}