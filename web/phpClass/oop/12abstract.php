<?php
include_once "abstract/paymenttypes.abstract.php";
include_once "classes/BuyProduct.cls.php";

//오브젝트 생성
$buyProduct = new BuyProduct();
//오브젝트의 getPayment()메소드 호출
echo $buyProduct->getPayment();

