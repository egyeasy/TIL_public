#include <iostream>
#include <GL/glew.h>
#include <GL/freeglut.h>

void draw()
{
	glClearColor(0.0, 191.0 / 255.0, 255.0 / 255.0, 1.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// draw something

	glutSwapBuffers();
	// glFlush(); // cout << "...." << flush;
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	glutInitWindowPosition(100, 100);
	glutInitWindowSize(500, 500);
	glutCreateWindow("My first GLUT window");

	glutDisplayFunc(draw);

	glutMainLoop();
}
