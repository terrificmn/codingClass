<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateArticlesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('articles', function (Blueprint $table) {
            //$table->id();
            $table->bigIncrements('id'); // bingIncrements 는 primary key가 됨
            $table->unsignedBigInteger('user_id');  // 아이디로 associate 할 수 있음  // 실제 user 테이블의 id 와 같은 형식을 써야함 BigInteger
            // user의 id는 bigIncremets 이므로 BigInteger를 사용하면 됨
            $table->string('title');
            $table->text('excerpt');
            $table->text('body');
            $table->timestamps();

            // 만약 user테이블에서 해당아이디로 참조하는데 그 해당아이디가 지워졌거나 없다면(탈퇴 등으로..)
            // 그러면 문제가 생긴다. 왜냐하면 users 테이블에서는 아이디가 없는데
            // 이미 참조해서 만들어진 articles 테이블에는 해당아이디가 남아있으므로
            // 이때 사용할 수 있는 것이 아래 코드 
            // foreign('user_id')를 지정 이것은 users테이블의 id이고 id가 지워졌으면 'cascade' 해라
            // DB에 가보면 Articles테이블에 user_id에 foreign_key가 설정되어 있게 됨
            $table->foreign('user_id')
                ->references('id')
                ->on('users')
                ->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('articles');
    }
}
