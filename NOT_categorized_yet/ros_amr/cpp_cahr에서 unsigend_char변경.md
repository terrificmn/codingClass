

```cpp
signed char x = -100;
unsigned char y;

y = (unsigned char)x;                    // C static
y = *(unsigned char*)(&x);               // C reinterpret
y = static_cast<unsigned char>(x);       // C++ static
y = reinterpret_cast<unsigned char&>(x); // C++ reinterpret
```

```cpp
jbyte memory_buffer[nr_pixels];
unsigned char* pixels = reinterpret_cast<unsigned char*>(memory_buffer);
```

