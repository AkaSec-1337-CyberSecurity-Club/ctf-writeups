## Xor (On-campus only)

XOR the data after XOR once to get the original data XOR the input character and serial number, and then compare it with the target array, so you only need to reverse the target array and XOR again to get the flag

```c
#include<cstdio>
#include<cstring>
#include<cstdlib>
char flag[100]={0x4D,0x53,0x41,0x57,0x42,0x7E,0x46,0x58,0x5A,0x3A,0x4A,0x3A,0x60,0x74,0x51,0x4A,0x22,0x4E,0x40,0x20,0x62,0x70,0x64,0x64,0x7D,0x38,0x67};
int main()
{
	for(int i=0;i<strlen(flag);i++)
	{
		unsigned char tmp=flag[i];
		tmp^=i;
		printf("%c",tmp);
	}
	return 0;
}
```

Get flag: MRCTF{@_R3@1ly_E2_R3verse!}
