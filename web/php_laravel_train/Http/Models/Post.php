<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;

     /*
     * The table associated with the model.
     * @var string
     */

    // Eloquent 모델은 클래스이름을 보고 테이블을 결정하는데 
    // 클래스이름이 Post인데 복수형으로 테이블을 결정한다고 함(기본)
    // 그래서 posts 가 테이블이 이름이 되어서 찾아옴
    // 이름을 바꾸려면 프로퍼티를 바꿔줘야함 (아래처럼)
    protected $table = 'post';
}
