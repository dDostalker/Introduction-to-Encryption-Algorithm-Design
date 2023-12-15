// pch.cpp: 与预编译标头对应的源文件

#include "pch.h"




extern"C" __declspec(dllexport) char* Xor(char* artical,int key)
{
   int length = strlen(artical);
   for (char* p = artical; artical + length - p > 0; p++)
   {
		*p ^= key;
   }
   return artical;

}


extern"C" __declspec(dllexport) char* KASAC(char* artical,int key)
{

		int length = strlen(artical);
		for (char* p = artical; artical + length - p - 1 > 0; p++)
		{
			if (*p >= 'a' && *p <= 'z')
				*p = ((*p - 97 + key) % 26) + 97;
			else if (*p >= 'A' && *p <= 'Z')
				*p = ((*p - 65 + key) % 26) + 65;
		}

	return artical;
}
extern"C" __declspec(dllexport) char* KASAU(char* artical, int key)
{

		int length = strlen(artical);
		for (char* p = artical; artical + length - p - 1 > 0; p++)
		{
			if (*p >= 'a' && *p <= 'z')
				*p = ((*p - 97 +26 - key) % 26) + 97;
			else if (*p >= 'A' && *p <= 'Z')
				*p = ((*p - 65+26 - key) % 26) + 65;
		}
	
	return artical;
}
// 当使用预编译的头时，需要使用此源文件，编译才能成功。
