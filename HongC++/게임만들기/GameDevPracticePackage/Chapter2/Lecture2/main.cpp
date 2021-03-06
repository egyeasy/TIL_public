#include "Game2D.h"
#include "Examples/PrimitivesGallery.h"
#include "RandomNumberGenerator.h"

namespace jm
{
	class Example : public Game2D
	{
	public:
		Example()
			: Game2D()
		{}

		void update() override
		{
			// yellow triangle
			beginTransformation();
			{
				translate(vec2{ -0.5f, -0.05f });
				drawFilledTriangle(Colors::yellow, 0.3f);
			}
			endTransformation();

			// red circle
			beginTransformation();
			{
				drawFilledCircle(Colors::red, 0.15f);
			}
			endTransformation();

			// blue box
			beginTransformation();
			{
				translate(vec2{ 0.5f, 0.0f });
				drawFilledBox(Colors::blue, 0.25f, 0.3f);
			}
			endTransformation();
		}
	};
}

int main(void)
{
	jm::Example().run();
	//jm::Game2D().init("This is my digital canvas!", 1280, 960, false).run();
	//jm::PrimitivesGallery().run();

	return 0;
}
