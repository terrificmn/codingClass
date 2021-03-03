<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Tag extends Model
{
    use HasFactory;
    // 반대로 생각해보면 tag모델에서는 artcle과 서로 관계에 있음
    public function article() {
        return $this->belongsToMany('App\Models\Article', 'article_tag');
    }
}
