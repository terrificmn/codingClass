# x11 clip 
깃 클론
```
git clone https://github.com/dacap/clip
```

사용할 자신의 패키지의 디렉토리 안으로 이동 시켜주거나, 아예 깃 클론을 사용할 자신의 패키지에서 한다   

이후 CMakeLists.txt (적용할 자신의 패키지)
```c
# Disable clip examples and tests
set(CLIP_EXAMPLES OFF CACHE BOOL "Compile clip examples")
set(CLIP_TESTS OFF CACHE BOOL "Compile clip tests")

# In case that you have ${PNG_LIBRARY} set to support copy/paste images on Linux
#set(CLIP_X11_PNG_LIBRARY "${PNG_LIBRARY}")

# Add clip subdirectory to compile the library
add_subdirectory(clip)
target_link_libraries(my-project clip)

```

clip 라이브러리의 examples, tests 는 set()에서 OFF 시켜서 사용, 필요시 ON   
images 카피도 필요 없을 듯 하다   

`add_subdirectory(clip)`와 `target_link_libraries(my-project clip)` 만 자신의 패키지에 포함 시켜주면 된다   



### 사용
```cpp
#include "clip/clip.h"

int main() {
  clip::set_text("Hello World");
}
```