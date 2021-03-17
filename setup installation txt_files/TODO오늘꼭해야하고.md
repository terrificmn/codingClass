# 꼭 push 할 것!!!!

PostController의 store() 메소드 일부 수정할 것  
CustomValidationController 만들어서 사용할 것인지 생각해볼 것

또 우분투 키보드 다른 프로그램 찾아볼 것
code .로 실행하는 법 찾기- insiders 

```php
$request->validate([
        'title' => 'required',
        'description' => 'required',
        //'image' => 'required|mimes:jpg,png,jpeg|max:5048',
    ]);
    
    if (isset($_FILES['mdfile'])) {
        
        $fileError = $_FILES['mdfile']['error'];

        if ($fileError === 0) {
            $fileName = $_FILES['mdfile']['name'];
            $fileTmpName = $_FILES['mdfile']['tmp_name'];
            $fileSize = $_FILES['mdfile']['size'];
            
            $fileType = $_FILES['mdfile']['type'];
            
            $fileExt = explode('.', $fileName);
            $fileActualExt = strtolower(end($fileExt));
            $allowed = array('md');
        
            if($fileType == 'text/markdown' && $fileExt)  {
                dd('ok');
            }
        }   
    }

```


blog/create.blade.php 파일에 file 폼 수정
```php
<div class="bg-gray-lighter pt-15">
    <label class="w-44 flex flex-col items-center px-2 py-3 bg-white-rounded-lg shadow-lg tracking-wide uppercase border border-blue cursor-pointer">
        <span class="mt-2 text-base leading-normal">
            이미지 파일
        </span>
        <input type="file" name="image" class="hidden">

</div>

<div class="bg-gray-lighter pt-5">
    <label class="w-44 flex flex-col items-center px-2 py-3 bg-white-rounded-lg shadow-lg tracking-wide uppercase border border-blue cursor-pointer">
        <span class="mt-2 text-base leading-normal">
            Select a file
        </span>
        <input type="file" name="mdfile" class="hidden">
</div>

```