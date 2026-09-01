<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Project extends Model
{
    use HasFactory;

    public function user()
    {
        # code...
        // $user->project
        // 이 user메소드는 user클래스에 속했다고 (서로 관계)
        return $this->belongsTo(user::class); // select * from user where project_id = 1 이런식으로 
        // $project->user 를 부르면 응답한다고 함
    }


}
// 이 Project 클래스와 관련되는 ..
// 메소드 설명
// hasOne -----  코멘트가 속해있기도 하고, 아니면 프로파일 (하나만 있으므로)
// hasMany ----- 많은 아티클이 있을 수도 있고, tasks, 등
// belongsTo --- 어딘가에 속해있는 것, user() user_id를 통해 서로 관계에 있다든가
// belongsToMany --- 하나가 아닌 여러군데 관련, 속해있는것

