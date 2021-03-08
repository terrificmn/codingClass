install
composer require laravel-frontend-presets/tailwindcss --dev

php artisan ui tailwindcss

npm install && npm run dev

-------------
make model with migration
php artisan make:model Car -m

auto create methods such as index, show, .. and destory
php artisan make:controller CarsController --resource
