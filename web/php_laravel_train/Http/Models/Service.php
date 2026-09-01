<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Service extends Model
{
    use HasFactory;
    protected $fillable = ['name']; //['name', 'date', 'title', 'another'] 이런식으로 계속 추가해주는것이 보호차원에서 좋다

    // protected $guarded = []; 모델의 프로텍트 기능을 끄고 내가 알아서 하겠다는 것
}
