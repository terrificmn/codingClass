<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateAssignmentsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('assignments', function (Blueprint $table) {
            $table->id();
            $table->text('body');
            // default(false)로 지정하기, false로 지정안하면 기본은 1, 그러면 나중에 처리할 떄 한게 되므로 
            $table->boolean('completed')->default(false);
            // 0/1으로 처리할 수 있음 0면 not complete, 1이면 completed
            //또는
            // 타임스탬프로하면 완료된 것도 알 수 있지만, 정확한 시간도 알 수 있는 장점이 있음
            // 교육상 일단 boolean방식으로 함
            //$table->timestamp('completed_at')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('assignments');
    }
}
