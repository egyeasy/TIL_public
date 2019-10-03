
void my_function()
{

}

int main()
{
	// void my_void; // void는 메모리를 차지하지 않기 때문에 선언 불가
	int i = 123;
	float f = 123.456f;

	void* my_void; // 주소를 저장하는 것은 가능

	my_void = (void*)&i;
	my_void = (void*)&f;

	return 0;
}