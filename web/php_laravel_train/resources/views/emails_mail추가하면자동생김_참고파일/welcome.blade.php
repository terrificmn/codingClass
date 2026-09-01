@component('mail::message')
# Introduction: Hello World

(The body of your message.)
Welcome to our cool application
테스트 메일 입니다.

@component('mail::button', ['url' => ''])
Button Text
@endcomponent

Thanks,<br>
{{ config('app.name') }}
@endcomponent
