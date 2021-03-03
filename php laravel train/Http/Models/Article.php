<?php

namespace App\Models;
use App\Models\User;
use App\Models\Tag;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use PDO;

class Article extends Model
{
    use HasFactory;
    protected $fillable = ['title', 'excerpt', 'body'];
    // ArticleController 에서 create()메소드를 이용해서 db에 입력하려고 하면
    // Add [title] to fillable property to allow mass assignment on [App\Models\Article]. 이런 에러가 남
    // 라라벨에서는 db의 컬럼을 다 입력이 될 때 모든 컬럼이 바꿔지면 안되기때문에
    // 어떤 특정한 컬럼은 사용자가 바꾸면 안되기 때문에 기본적으로 제한이 되어 있음 (보호차원에서)
    // 이거를 문제 없이 되게 하려면 (model) Article 클래스에 $fillable에 배열로 추가해주면됨

    public function user()
    {
        //이 user()메소드는 User클래스에 속함
        return $this->belongsTo(User::class); //user_id
    }

    public function tags() {
        return $this->belongsToMany('App\Models\Tag', 'article_tag');
        
    }

    
}

// $artilce->user

//