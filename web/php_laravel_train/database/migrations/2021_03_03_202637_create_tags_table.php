<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTagsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('tags', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->string('name');
            $table->timestamps();
        });

        // convention: 아티클_태그 언더스코어로 연결
        Schema::create('article_tag', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->unsignedBigInteger('article_id'); // article table과 연결
            $table->unsignedBigInteger('tag_id');
            $table->timestamps();

            $table->unique( ['article_id', 'tag_id' ]); //중복을 방지하기 위해서 unique

            // foreign키 설정: article_id 레퍼렌스 aritcles테이블의 id를 참조 id가 지워지면 여기도 article_id 지워지게 설정
            $table->foreign('article_id')->references('id')->on('articles')->onDelete('cascade');
            // tag_id 에도 같은 설정 (tags 테이블의 id 참조)
            $table->foreign('tag_id')->references('id')->on('tags')->onDelete('cascade');
            
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('tags');
    }
}
