*  TODO:
*   To change the location of the Git folder, you can use the git --git-dir option
*   All should be src/... not src/main/...
Next project realizes Observer pattern

Project realises the Command Design Pattern
invoker -> reciver
InvokerBasket -> Basket                        : Add/Remove Product to basket, Sort basket etc
InvokerPromotion -> Promotion                  : Add/Remove promotion
BasketPromotionInvoker -> Basket and Promotion : Apply Promotion on Product in Basket

ClientTest - client that uses invoker, creates all necessiary classes and invokes instructions
CLientTest - Free CompanyCup if TotalCost of product > 200; All products 5% off if TotalCost > 300; 3 products cheapest one for free

Product realises Comparable on Double Price
Product have comparators on String Name and Double Price

Product:
> String CodeID
> String Name
> Double Price
> Double DiscountPrice

Basket:
> {Product product : int amount}

Promotion:
> {Product product : int percentageOff) eg percentageOff = 10 => 10% off => price = 90% basePrice
> {Product product : String code} code - to get promotion; nullable; null if u dont need code to have product price off

CLientTest
@Test
public void name(){
  prepare set
  performe action
  check value assertion
}
