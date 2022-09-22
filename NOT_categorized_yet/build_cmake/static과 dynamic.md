clang++ 을 이용해서 컴파일할 때  

Flags are options that can be passed to Clang to configure the compilation. We have already used a few flags at the time in the previous seccions, those were **`-E`**, **`-s`**, **`-c`** and **`-o`**. Here is what they do:

**-E**: Run the preprocessor stage.

**-S**: Run the previous stages as well as LLVM generation (compiler technology) and optimization stages (optimize compilation process at the cost of compilation time) and target-specific code generation, producing an assembly file.

**-c**: Run all of the above, plus the assembler, generating a target “.o” object file.

**-o `<file>`**: Write output to file

**std=`<standard>`**: Specify the language standard to compile for.


static과 dynamic (.a, .so 파일)

-   **Static**: Faster, takes up more space (because a copy of static library becomes a part of every executable that uses it), becomes a part of end binary, named as lib*.a. Static libraries are archives just like zip/tar. Static libraries cannot be upgraded easily. To update a static library the entire executable needs to be replaced.
    
-   **Dynamic**: Slower, can be copied, referenced by a program. Named lib*.so. When you compile a program that uses a dynamic library, the library does not become a part of your executable. It remains a separate unit. Dynamic libraries can be upgraded to a newer version without replacing all the executables that use it.

