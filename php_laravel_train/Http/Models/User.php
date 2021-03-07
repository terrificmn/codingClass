<?php

namespace App\Models;
use App\Models\Article;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];

    public function article() {
        // user->article
        return $this->hasMany(Aritcle::class);  // select * from articles where user_id = 1
        // 위와 같은 커리가 실행되는 것과 처럼 진행
        // DB에서는 user_id 가 있어야 함
    }

    public function project() {
        return $this->hasMany(Article::class); // select * from project where user_id = 1
    }

    // $user = User::find(1); // select * from user where id = 1
    // $user->project; // select * from project where user_id = 1
    // $user->project->first(); //첫번째 db데이터를 가져와라
    // $user->project->last(); //마지막번째 db데이터를 가져와라
    // 이런식으로 사용이 가능해진다

        
}
