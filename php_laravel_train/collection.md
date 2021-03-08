>>> $customer = \App\Models\Customer::where('id', 1)->get();
=> Illuminate\Database\Eloquent\Collection {#4245
     all: [
       App\Models\Customer {#4155
         id: 1,
         name: "mike",
         email: "mike@naver.com",
         active: 1,
         created_at: "2021-03-08 04:55:30",
         updated_at: "2021-03-08 04:55:30",
       },
     ],
   }
>>> $customer = \App\Models\Customer::where('id', 1)->first();
=> App\Models\Customer {#4298
     id: 1,
     name: "mike",
     email: "mike@naver.com",
     active: 1,
     created_at: "2021-03-08 04:55:30",
     updated_at: "2021-03-08 04:55:30",
   }
>>> 


the difference

get() method is from Collection
first() method is from Model class( DB)

