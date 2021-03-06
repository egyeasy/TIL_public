#include "Game2D.h"
#include "Examples/PrimitivesGallery.h"
#include "RandomNumberGenerator.h"
#include <vector>
#include <memory>

namespace jm
{
	class RigidCircle
	{
	public:
		vec2 pos;
		vec2 vel;
		float radius = 0.1f;

		void draw()
		{
			beginTransformation();
			{
				translate(pos);
				drawFilledCircle(Colors::hotpink, radius - 1e-3f);
				setLineWidth(2.0f);
				drawWiredCircle(Colors::black, radius);
			}
			endTransformation();
		}

		void update(const float & dt)
		{
			// numerical integration

			// wall collision, friction
		}
	};

	class Example : public Game2D
	{
	public:
		RigidCircle rigid_body;

		Example()
			: Game2D()
		{
			reset();
		}

		void reset()
		{
			// Initial position and velocity
			rigid_body.pos = vec2(-0.8f, 0.3f);
			rigid_body.vel = vec2(10.0f, 0.0f);
		}

		void drawWall()
		{
			setLineWidth(5.0f);
			drawLine(Colors::blue, { -1.0f, -1.0f }, Colors::blue, { 1.0f, -1.0f });
			drawLine(Colors::blue, { 1.0f, -1.0f }, Colors::blue, { 1.0f, 1.0f });
			drawLine(Colors::blue, { -1.0f, -1.0f }, Colors::blue, { -1.0f, 1.0f });
		}

		void update() override
		{
			// physics update
			rigid_body.update(getTimeStep() * 0.1f);

			// draw
			drawWall();
			rigid_body.draw();

			// reset button
			if (isKeyPressedAndReleased(GLFW_KEY_R)) reset();
		}
	};
}

int main(void)
{
	jm::Example().run();

	return 0;
}
