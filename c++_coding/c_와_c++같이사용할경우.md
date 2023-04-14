# c c++ 같이 사용
c++에 c를 사용할 수 있지만, 문제를 일으킬 수 있으므로 try catch를 사용하거나,   
컴파일러를 지정해서 사용하는 것이 좋다!


FILE *f = fopen("test.txt", "r");
try {
    // C++ code
} catch(...) {
    // handle error
}
fclose(f);






if you want to use your C code and compile it as C++ it is recomennded to use it like this:

#ifdef __cplusplus
extern "C" {
#endif

Your C code

#ifdef __cplusplus
}
#endif

with this preprocessor directive you inform g++ that this part of code should be compiled with gcc, extern "C" {} is a linkage-specification. Problem with C code compiled by g++ without this specifier would be eg. NULL, because C NULL equivalent in C++ is nullptr, but in C++ NULL still exists, but means something different from C NULL, so it would/might create some problems
