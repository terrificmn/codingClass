collection 이용하기

tinker에서 사용

(base) [sgtocta@localhost exer]$ php artisan tinker
Psy Shell v0.10.6 (PHP 8.0.2 — cli) by Justin Hileman
첫번째 결과물 가져오기
>>> App\Models\Article::first();
=> App\Models\Article {#4086
     id: 1,
     user_id: 1,
     title: "Learn Laravel",
     excerpt: "Maxime occaecati voluptatem voluptatum atque atque.",
     body: "Exercitationem omnis doloribus magni quo inventore. Et aut quia natus velit. Modi atque repellat dolores quo ut.",
     created_at: "2021-03-02 22:18:00",
     updated_at: "2021-03-02 22:18:00",
   }

첫번째 결과물과 관련된->tags와 관련된 것들 (tag메소드)
>>> $tags = App\Models\Article::first()->tags;
=> Illuminate\Database\Eloquent\Collection {#4243
     all: [
       App\Models\Tag {#4299
         id: 1,
         name: "laravel",
         created_at: "2021-03-04 05:50:30",
         updated_at: "2021-03-04 05:50:30",
         pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4302
           article_id: 1,
           tag_id: 1,
           created_at: "2021-03-04 05:50:30",
           updated_at: "2021-03-04 05:50:30",
         },
       },
       App\Models\Tag {#4300
         id: 2,
         name: "php",
         created_at: "2021-03-04 05:50:30",
         updated_at: "2021-03-04 05:50:30",
         pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4298
           article_id: 1,
           tag_id: 2,
           created_at: "2021-03-04 05:50:30",
           updated_at: "2021-03-04 05:50:30",
         },
       },
       App\Models\Tag {#4303
         id: 3,
         name: "education",
         created_at: "2021-03-04 05:50:30",
         updated_at: "2021-03-04 05:50:30",
         pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4153
           article_id: 1,
           tag_id: 3,
           created_at: "2021-03-04 05:50:30",
           updated_at: "2021-03-04 05:50:30",
         },
       },
     ],
   }

그중에서 첫번째
>>> $tags->first();
=> App\Models\Tag {#4299
     id: 1,
     name: "laravel",
     created_at: "2021-03-04 05:50:30",
     updated_at: "2021-03-04 05:50:30",
     pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4302
       article_id: 1,
       tag_id: 1,
       created_at: "2021-03-04 05:50:30",
       updated_at: "2021-03-04 05:50:30",
     },
   }

마지막 결과
>>> $tags->last();
=> App\Models\Tag {#4303
     id: 3,
     name: "education",
     created_at: "2021-03-04 05:50:30",
     updated_at: "2021-03-04 05:50:30",
     pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4153
       article_id: 1,
       tag_id: 3,
       created_at: "2021-03-04 05:50:30",
       updated_at: "2021-03-04 05:50:30",
     },
   }

sql쿼리로 name 키가 laravel 인거 가져와라
>>> $tags->where('name', 'laravel');
=> Illuminate\Database\Eloquent\Collection {#3360
     all: [
       App\Models\Tag {#4299
         id: 1,
         name: "laravel",
         created_at: "2021-03-04 05:50:30",
         updated_at: "2021-03-04 05:50:30",
         pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4302
           article_id: 1,
           tag_id: 1,
           created_at: "2021-03-04 05:50:30",
           updated_at: "2021-03-04 05:50:30",
         },
       },
     ],
   }

쿼리로 가져온 것에 첫번째, 없나봄;;
>>> $tags->where('name', 'Laravel')->first()
=> null

$tags 결과에서 $tag->name 속성이 (컬럼) 글자수 5보다 작은거 가져와라
>>> $tags->first(function ($tag) { return strlen($tag->name) < 5; });
=> App\Models\Tag {#4300
     id: 2,
     name: "php",
     created_at: "2021-03-04 05:50:30",
     updated_at: "2021-03-04 05:50:30",
     pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4298
       article_id: 1,
       tag_id: 2,
       created_at: "2021-03-04 05:50:30",
       updated_at: "2021-03-04 05:50:30",
     },
   }

collect 하기 배열로 묶어주면 하나의 collection이 된다
>>> collect(['one', 'two', 'three']);
=> Illuminate\Support\Collection {#3356
     all: [
       "one",
       "two",
       "three",
     ],
   }

그 중 첫번째
>>> collect(['one', 'two', 'three'])->first();
=> "one"

배열속에 배열을 넣어줄 수도 있음 nested array
>>> collect(['one', 'two', 'three', ['four', 'five'], 'six']);
=> Illuminate\Support\Collection {#4305
     all: [
       "one",
       "two",
       "three",
       [
         "four",
         "five",
       ],
       "six",
     ],
   }

복잡한 구조 배열을 flatten 하라, 하나로 만듬
>>> collect(['one', 'two', 'three', ['four', 'five'], 'six'])->flatten();
=> Illuminate\Support\Collection {#4315
     all: [
       "one",
       "two",
       "three",
       "four",
       "five",
       "six",
     ],
   }

$items에 저장
>>> $items = collect( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
=> Illuminate\Support\Collection {#4323
     all: [
       1,
       2,
       3,
       4,
       5,
       6,
       7,
       8,
       9,
       10,
     ],
   }

filter메소드로 하느데 function ($item)은 자체 함수를 만드는것인지 잘 모르겠음, 어쨌든 item 목록이 5보다 크거나 같으면 가져와라 
$items as $item 같이 하나씩 불러와 쓰는 컨셉인듯.. 잘모르겠따;;
>>> $items->filter(function ($item) { return $item >= 5; });
=> Illuminate\Support\Collection {#4309
     all: [
       4 => 5,
       5 => 6,
       6 => 7,
       7 => 8,
       8 => 9,
       9 => 10,
     ],
   }


>>> $items
=> Illuminate\Support\Collection {#4323
     all: [
       1,
       2,
       3,
       4,
       5,
       6,
       7,
       8,
       9,
       10,
     ],
   }

위의 내용은 저장해야지 다음에 사용할 수 있다. 뭐. 저장하라
>>> $greterThan4 = $items->filter(function ($item) { return $item >= 5; });
=> Illuminate\Support\Collection {#4296
     all: [
       4 => 5,
       5 => 6,
       6 => 7,
       7 => 8,
       8 => 9,
       9 => 10,
     ],
   }

비슷한 내용
>>> $items->filter(function ($item) { return $item % 2 === 0; });
=> Illuminate\Support\Collection {#3681
     all: [
       1 => 2,
       3 => 4,
       5 => 6,
       7 => 8,
       9 => 10,
     ],
   }

필터한 내용은 map 으로 다시 묶어 주기 이번에는 3을 곱해서 
>>> $items->filter(function ($item) { return $item % 2 === 0; })->map(function ($item) { return $item *3; });
=> Illuminate\Support\Collection {#4244
     all: [
       1 => 6,
       3 => 12,
       5 => 18,
       7 => 24,
       9 => 30,
     ],
   }

이 결과에서 마지막만 보여달라
>>> $items->filter(function ($item) { return $item % 2 === 0; })->map(function ($item) { return $item *3; })->last();
=> 30

새로 변수~ 다가지고 와라
>>> $article = App\Models\Article::all();
=> Illuminate\Database\Eloquent\Collection {#4312
     all: [
       App\Models\Article {#4304
         id: 1,
         user_id: 1,
         title: "Learn Laravel",
         excerpt: "Maxime occaecati voluptatem voluptatum atque atque.",
         body: "Exercitationem omnis doloribus magni quo inventore. Et aut quia natus velit. Modi atque repellat dolores quo ut.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
       },
       App\Models\Article {#4311
         id: 2,
         user_id: 1,
         title: "Illo rerum molestiae itaque et repellendus.",
         excerpt: "Officiis quia soluta quod perspiciatis.",
         body: "Et quisquam aliquam quaerat. Facere amet dolor rerum nesciunt. Qui asperiores est et recusandae sed.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
       },
       App\Models\Article {#4297
         id: 3,
         user_id: 1,
         title: "Et et neque sit.",
         excerpt: "Et et corrupti voluptas dicta labore et in.",
         body: "Aspernatur quis hic porro. Eos et et quidem eius at. Placeat ut nisi porro illo et vel veniam sed. Officia quibusdam alias mollitia incidunt excepturi itaque. Ipsam sint quia quam ea.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
       },
       App\Models\Article {#3365
         id: 4,
         user_id: 1,
         title: "In molestias ipsam vel non.",
         excerpt: "Cum et voluptate necessitatibus culpa vel necessitatibus amet.",
         body: "Omnis asperiores veritatis neque nihil. Nostrum quia ipsum eligendi dignissimos dolorem. Nihil omnis et voluptate magni qui ratione corrupti.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
       },
       App\Models\Article {#3356
         id: 5,
         user_id: 1,
         title: "Libero natus enim ut quia.",
         excerpt: "Officiis nobis mollitia et unde eum minus dolor.",
         body: "Est quia vel inventore eveniet. Consequatur non quia qui labore aut. Dolore rem quisquam quam laborum voluptatum.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
       },
       App\Models\Article {#4087
         id: 6,
         user_id: 2,
         title: "Asperiores quis culpa voluptates eius.",
         excerpt: "Labore id fuga architecto.",
         body: "Quod dicta eveniet voluptas. Laboriosam recusandae quisquam inventore in eveniet quia laboriosam. Ex ut fuga placeat enim hic cumque. Repellendus nulla dolorem quasi vel odit.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
       },
       App\Models\Article {#3681
         id: 7,
         user_id: 2,
         title: "Voluptatem nobis odio tempora.",
         excerpt: "Est laboriosam suscipit amet repellat illum ea illum aperiam.",
         body: "Blanditiis et vitae quam nihil dignissimos voluptatibus reprehenderit id. Architecto dolor dolor dolore aliquam eos saepe. Sunt qui atque et assumenda. Doloremque temporibus commodi est natus soluta tempore eligendi quaerat. Sed saepe quasi blanditiis.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
       },
       App\Models\Article {#4049
         id: 8,
         user_id: 2,
         title: "Commodi voluptatem vero corrupti nostrum omnis praesentium.",
         excerpt: "Culpa nihil asperiores in.",
         body: "Dolorum omnis culpa eius molestiae magnam alias. Aut et et quia consequatur itaque ea. Ut adipisci aut quam nam possimus. In aperiam voluptatem aliquid maiores.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
       },
       App\Models\Article {#4086
         id: 9,
         user_id: 1,
         title: "test다시x테스트",
         excerpt: "test다시x테스트",
         body: "test다시x테스트",
         created_at: "2021-03-03 22:58:00",
         updated_at: "2021-03-03 22:58:00",
       },
       App\Models\Article {#3360
         id: 10,
         user_id: 1,
         title: "테스트테스트",
         excerpt: "테스트테스트",
         body: "테스트테스트",
         created_at: "2021-03-03 23:10:06",
         updated_at: "2021-03-03 23:10:06",
       },
     ],
   }

이제 그룹화 할 수 있음. 이런 내용
give me an aricle which is associated with tags

>>> $article = App\Models\Article::with('tags')->get();
=> Illuminate\Database\Eloquent\Collection {#4316
     all: [
       App\Models\Article {#4327
         id: 1,
         user_id: 1,
         title: "Learn Laravel",
         excerpt: "Maxime occaecati voluptatem voluptatum atque atque.",
         body: "Exercitationem omnis doloribus magni quo inventore. Et aut quia natus velit. Modi atque repellat dolores quo ut.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4343
           all: [
             App\Models\Tag {#4345
               id: 1,
               name: "laravel",
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
               pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4348
                 article_id: 1,
                 tag_id: 1,
                 created_at: "2021-03-04 05:50:30",
                 updated_at: "2021-03-04 05:50:30",
               },
             },
             App\Models\Tag {#4346
               id: 2,
               name: "php",
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
               pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4344
                 article_id: 1,
                 tag_id: 2,
                 created_at: "2021-03-04 05:50:30",
                 updated_at: "2021-03-04 05:50:30",
               },
             },
             App\Models\Tag {#4349
               id: 3,
               name: "education",
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
               pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4341
                 article_id: 1,
                 tag_id: 3,
                 created_at: "2021-03-04 05:50:30",
                 updated_at: "2021-03-04 05:50:30",
               },
             },
           ],
         },
       },
       App\Models\Article {#4328
         id: 2,
         user_id: 1,
         title: "Illo rerum molestiae itaque et repellendus.",
         excerpt: "Officiis quia soluta quod perspiciatis.",
         body: "Et quisquam aliquam quaerat. Facere amet dolor rerum nesciunt. Qui asperiores est et recusandae sed.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4305
           all: [],
         },
       },
       App\Models\Article {#4329
         id: 3,
         user_id: 1,
         title: "Et et neque sit.",
         excerpt: "Et et corrupti voluptas dicta labore et in.",
         body: "Aspernatur quis hic porro. Eos et et quidem eius at. Placeat ut nisi porro illo et vel veniam sed. Officia quibusdam alias mollitia incidunt excepturi itaque. Ipsam sint quia quam ea.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4306
           all: [],
         },
       },
       App\Models\Article {#4330
         id: 4,
         user_id: 1,
         title: "In molestias ipsam vel non.",
         excerpt: "Cum et voluptate necessitatibus culpa vel necessitatibus amet.",
         body: "Omnis asperiores veritatis neque nihil. Nostrum quia ipsum eligendi dignissimos dolorem. Nihil omnis et voluptate magni qui ratione corrupti.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4317
           all: [],
         },
       },
       App\Models\Article {#4331
         id: 5,
         user_id: 1,
         title: "Libero natus enim ut quia.",
         excerpt: "Officiis nobis mollitia et unde eum minus dolor.",
         body: "Est quia vel inventore eveniet. Consequatur non quia qui labore aut. Dolore rem quisquam quam laborum voluptatum.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4244
           all: [],
         },
       },
       App\Models\Article {#4332
         id: 6,
         user_id: 2,
         title: "Asperiores quis culpa voluptates eius.",
         excerpt: "Labore id fuga architecto.",
         body: "Quod dicta eveniet voluptas. Laboriosam recusandae quisquam inventore in eveniet quia laboriosam. Ex ut fuga placeat enim hic cumque. Repellendus nulla dolorem quasi vel odit.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
         tags: Illuminate\Database\Eloquent\Collection {#4301
           all: [],
         },
       },
       App\Models\Article {#4333
         id: 7,
         user_id: 2,
         title: "Voluptatem nobis odio tempora.",
         excerpt: "Est laboriosam suscipit amet repellat illum ea illum aperiam.",
         body: "Blanditiis et vitae quam nihil dignissimos voluptatibus reprehenderit id. Architecto dolor dolor dolore aliquam eos saepe. Sunt qui atque et assumenda. Doloremque temporibus commodi est natus soluta tempore eligendi quaerat. Sed saepe quasi blanditiis.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
         tags: Illuminate\Database\Eloquent\Collection {#4309
           all: [],
         },
       },
       App\Models\Article {#4334
         id: 8,
         user_id: 2,
         title: "Commodi voluptatem vero corrupti nostrum omnis praesentium.",
         excerpt: "Culpa nihil asperiores in.",
         body: "Dolorum omnis culpa eius molestiae magnam alias. Aut et et quia consequatur itaque ea. Ut adipisci aut quam nam possimus. In aperiam voluptatem aliquid maiores.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
         tags: Illuminate\Database\Eloquent\Collection {#4322
           all: [],
         },
       },
       App\Models\Article {#4335
         id: 9,
         user_id: 1,
         title: "test다시x테스트",
         excerpt: "test다시x테스트",
         body: "test다시x테스트",
         created_at: "2021-03-03 22:58:00",
         updated_at: "2021-03-03 22:58:00",
         tags: Illuminate\Database\Eloquent\Collection {#4337
           all: [],
         },
       },
       App\Models\Article {#4336
         id: 10,
         user_id: 1,
         title: "테스트테스트",
         excerpt: "테스트테스트",
         body: "테스트테스트",
         created_at: "2021-03-03 23:10:06",
         updated_at: "2021-03-03 23:10:06",
         tags: Illuminate\Database\Eloquent\Collection {#4338
           all: [],
         },
       },
     ],
   }


Article model에서 ->tags() method 호출

>>> $article
=> Illuminate\Database\Eloquent\Collection {#4316
     all: [
       App\Models\Article {#4327
         id: 1,
         user_id: 1,
         title: "Learn Laravel",
         excerpt: "Maxime occaecati voluptatem voluptatum atque atque.",
         body: "Exercitationem omnis doloribus magni quo inventore. Et aut quia natus velit. Modi atque repellat dolores quo ut.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4343
           all: [
             App\Models\Tag {#4345
               id: 1,
               name: "laravel",
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
               pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4348
                 article_id: 1,
                 tag_id: 1,
                 created_at: "2021-03-04 05:50:30",
                 updated_at: "2021-03-04 05:50:30",
               },
             },
             App\Models\Tag {#4346
               id: 2,
               name: "php",
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
               pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4344
                 article_id: 1,
                 tag_id: 2,
                 created_at: "2021-03-04 05:50:30",
                 updated_at: "2021-03-04 05:50:30",
               },
             },
             App\Models\Tag {#4349
               id: 3,
               name: "education",
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
               pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4341
                 article_id: 1,
                 tag_id: 3,
                 created_at: "2021-03-04 05:50:30",
                 updated_at: "2021-03-04 05:50:30",
               },
             },
           ],
         },
       },
       App\Models\Article {#4328
         id: 2,
         user_id: 1,
         title: "Illo rerum molestiae itaque et repellendus.",
         excerpt: "Officiis quia soluta quod perspiciatis.",
         body: "Et quisquam aliquam quaerat. Facere amet dolor rerum nesciunt. Qui asperiores est et recusandae sed.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4305
           all: [],
         },
       },
       App\Models\Article {#4329
         id: 3,
         user_id: 1,
         title: "Et et neque sit.",
         excerpt: "Et et corrupti voluptas dicta labore et in.",
         body: "Aspernatur quis hic porro. Eos et et quidem eius at. Placeat ut nisi porro illo et vel veniam sed. Officia quibusdam alias mollitia incidunt excepturi itaque. Ipsam sint quia quam ea.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4306
           all: [],
         },
       },
       App\Models\Article {#4330
         id: 4,
         user_id: 1,
         title: "In molestias ipsam vel non.",
         excerpt: "Cum et voluptate necessitatibus culpa vel necessitatibus amet.",
         body: "Omnis asperiores veritatis neque nihil. Nostrum quia ipsum eligendi dignissimos dolorem. Nihil omnis et voluptate magni qui ratione corrupti.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4317
           all: [],
         },
       },
       App\Models\Article {#4331
         id: 5,
         user_id: 1,
         title: "Libero natus enim ut quia.",
         excerpt: "Officiis nobis mollitia et unde eum minus dolor.",
         body: "Est quia vel inventore eveniet. Consequatur non quia qui labore aut. Dolore rem quisquam quam laborum voluptatum.",
         created_at: "2021-03-02 22:18:00",
         updated_at: "2021-03-02 22:18:00",
         tags: Illuminate\Database\Eloquent\Collection {#4244
           all: [],
         },
       },
       App\Models\Article {#4332
         id: 6,
         user_id: 2,
         title: "Asperiores quis culpa voluptates eius.",
         excerpt: "Labore id fuga architecto.",
         body: "Quod dicta eveniet voluptas. Laboriosam recusandae quisquam inventore in eveniet quia laboriosam. Ex ut fuga placeat enim hic cumque. Repellendus nulla dolorem quasi vel odit.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
         tags: Illuminate\Database\Eloquent\Collection {#4301
           all: [],
         },
       },
       App\Models\Article {#4333
         id: 7,
         user_id: 2,
         title: "Voluptatem nobis odio tempora.",
         excerpt: "Est laboriosam suscipit amet repellat illum ea illum aperiam.",
         body: "Blanditiis et vitae quam nihil dignissimos voluptatibus reprehenderit id. Architecto dolor dolor dolore aliquam eos saepe. Sunt qui atque et assumenda. Doloremque temporibus commodi est natus soluta tempore eligendi quaerat. Sed saepe quasi blanditiis.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
         tags: Illuminate\Database\Eloquent\Collection {#4309
           all: [],
         },
       },
       App\Models\Article {#4334
         id: 8,
         user_id: 2,
         title: "Commodi voluptatem vero corrupti nostrum omnis praesentium.",
         excerpt: "Culpa nihil asperiores in.",
         body: "Dolorum omnis culpa eius molestiae magnam alias. Aut et et quia consequatur itaque ea. Ut adipisci aut quam nam possimus. In aperiam voluptatem aliquid maiores.",
         created_at: "2021-03-02 22:18:14",
         updated_at: "2021-03-02 22:18:14",
         tags: Illuminate\Database\Eloquent\Collection {#4322
           all: [],
         },
       },
       App\Models\Article {#4335
         id: 9,
         user_id: 1,
         title: "test다시x테스트",
         excerpt: "test다시x테스트",
         body: "test다시x테스트",
         created_at: "2021-03-03 22:58:00",
         updated_at: "2021-03-03 22:58:00",
         tags: Illuminate\Database\Eloquent\Collection {#4337
           all: [],
         },
       },
       App\Models\Article {#4336
         id: 10,
         user_id: 1,
         title: "테스트테스트",
         excerpt: "테스트테스트",
         body: "테스트테스트",
         created_at: "2021-03-03 23:10:06",
         updated_at: "2021-03-03 23:10:06",
         tags: Illuminate\Database\Eloquent\Collection {#4338
           all: [],
         },
       },
     ],
   }

위의 긴 내용중에서 title로만 pluck  그룹화
new collection of only title

>>> $article->pluck('title');
=> Illuminate\Support\Collection {#4312
     all: [
       "Learn Laravel",
       "Illo rerum molestiae itaque et repellendus.",
       "Et et neque sit.",
       "In molestias ipsam vel non.",
       "Libero natus enim ut quia.",
       "Asperiores quis culpa voluptates eius.",
       "Voluptatem nobis odio tempora.",
       "Commodi voluptatem vero corrupti nostrum omnis praesentium.",
       "test다시x테스트",
       "테스트테스트",
     ],
   }

이번에는 'tags'만
>>> $article->pluck('tags');
=> Illuminate\Support\Collection {#4086
     all: [
       Illuminate\Database\Eloquent\Collection {#4343
         all: [
           App\Models\Tag {#4345
             id: 1,
             name: "laravel",
             created_at: "2021-03-04 05:50:30",
             updated_at: "2021-03-04 05:50:30",
             pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4348
               article_id: 1,
               tag_id: 1,
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
             },
           },
           App\Models\Tag {#4346
             id: 2,
             name: "php",
             created_at: "2021-03-04 05:50:30",
             updated_at: "2021-03-04 05:50:30",
             pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4344
               article_id: 1,
               tag_id: 2,
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
             },
           },
           App\Models\Tag {#4349
             id: 3,
             name: "education",
             created_at: "2021-03-04 05:50:30",
             updated_at: "2021-03-04 05:50:30",
             pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4341
               article_id: 1,
               tag_id: 3,
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
             },
           },
         ],
       },
       Illuminate\Database\Eloquent\Collection {#4305
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4306
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4317
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4244
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4301
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4309
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4322
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4337
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4338
         all: [],
       },
     ],
   }

이런거 할 수 있다고 하네,, 아래와 같이 적용가능할 수 있다고 함
which item has own collection so we could do is flunk the tag and flatten

'tags'로 묶고
>>> $article->pluck('tags');
=> Illuminate\Support\Collection {#4319
     all: [
       Illuminate\Database\Eloquent\Collection {#4343
         all: [
           App\Models\Tag {#4345
             id: 1,
             name: "laravel",
             created_at: "2021-03-04 05:50:30",
             updated_at: "2021-03-04 05:50:30",
             pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4348
               article_id: 1,
               tag_id: 1,
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
             },
           },
           App\Models\Tag {#4346
             id: 2,
             name: "php",
             created_at: "2021-03-04 05:50:30",
             updated_at: "2021-03-04 05:50:30",
             pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4344
               article_id: 1,
               tag_id: 2,
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
             },
           },
           App\Models\Tag {#4349
             id: 3,
             name: "education",
             created_at: "2021-03-04 05:50:30",
             updated_at: "2021-03-04 05:50:30",
             pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4341
               article_id: 1,
               tag_id: 3,
               created_at: "2021-03-04 05:50:30",
               updated_at: "2021-03-04 05:50:30",
             },
           },
         ],
       },
       Illuminate\Database\Eloquent\Collection {#4305
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4306
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4317
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4244
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4301
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4309
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4322
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4337
         all: [],
       },
       Illuminate\Database\Eloquent\Collection {#4338
         all: [],
       },
     ],
   }

그리고 collapse 하기 그러면 결과를 flatten 한 효과
flatten() 비슷하다고 함
>>> $article->pluck('tags')->collapse();
=> Illuminate\Support\Collection {#4304
     all: [
       App\Models\Tag {#4345
         id: 1,
         name: "laravel",
         created_at: "2021-03-04 05:50:30",
         updated_at: "2021-03-04 05:50:30",
         pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4348
           article_id: 1,
           tag_id: 1,
           created_at: "2021-03-04 05:50:30",
           updated_at: "2021-03-04 05:50:30",
         },
       },
       App\Models\Tag {#4346
         id: 2,
         name: "php",
         created_at: "2021-03-04 05:50:30",
         updated_at: "2021-03-04 05:50:30",
         pivot: Illuminate\Database\Eloquent\Relations\Pivot {#4344

그 결과에서 다시 그룹화 by name
>>> $article->pluck('tags')->collapse()->pluck('name');
=> Illuminate\Support\Collection {#4358
     all: [
       "laravel",
       "php",
       "education",
     ],
   }

위의 결과는 3개만 나왔지만 만약 여러개가 중복으로 나올 경우에는 중복제거, 즉 unique 한 놈들만 보이기
categorical 데이터만 보이기 (py.판다스??)
>>> $article->pluck('tags')->collapse()->pluck('name')->unique();
=> Illuminate\Support\Collection {#4314
     all: [
       "laravel",
       "php",
       "education",
     ],
   }

. 이면 라라벨에서 웹페이지를 보여줄 때 디렉토리로 구성이 될 수 있느데
이를 적용, tags.name 하면 null 값만 보임
>>> $article->pluck('tags.name');
=> Illuminate\Support\Collection {#4352
     all: [
       null,
       null,
       null,
       null,
       null,
       null,
       null,
       null,
       null,
       null,
     ],
   }

그 사이에 *을 넣어주면 위에서 했던 것과 비슷한 효관
>>> $article->pluck('tags.*.name');
=> Illuminate\Support\Collection {#4311
     all: [
       [
         "laravel",
         "php",
         "education",
       ],
       [],
       [],
       [],
       [],
       [],
       [],
       [],
       [],
       [],
     ],
   }

이거를 다시 collapse()
>>> $article->pluck('tags.*.name')->collapse();
=> Illuminate\Support\Collection {#4353
     all: [
       "laravel",
       "php",
       "education",
     ],
   }

중복이 있다면 unique()로만 보여주기
>>> $article->pluck('tags.*.name')->collapse()->unique();
=> Illuminate\Support\Collection {#4320
     all: [
       "laravel",
       "php",
       "education",
     ],
   }

이것도 저장해서 사용
>>> $relevantTags = $article->pluck('tags.*.name')->collapse()->unique();
=> Illuminate\Support\Collection {#4311
     all: [
       "laravel",
       "php",
       "education",
     ],
   }

이걸로 map()메소드로 묶음 , 또 ucwords 로 변환 소문자 뭐시기 인가? 무슨함수인지 찾아봐야겠다
이런 내용이라는데 map over each of the items and just return ucwords($item)

>>> $relevantTags = $article->pluck('tags.*.name')->collapse()->unique()->map(function ($item) { return ucwords($item); });
=> Illuminate\Support\Collection {#4355
     all: [
       "Laravel",
       "Php",
       "Education",
     ],
   }



