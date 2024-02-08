import Basket.*;
import Commands.*;
import Product.Product;
import Promotion.*;
import org.junit.*;
import NotUsed.*;

import static org.junit.Assert.assertEquals;

public class ClientTest {
    // aka tests
    Basket basket;
    Product cucumber;
    Product potato;
    Product tomato;
    Product slowCar;
    Product fastCar;
    Product banana;
    Product companyCup;
    Product fish;
    Product companionFish;
    Product lion;
    Promotion promotion;

    @Test
    public void Directly() {
        Product cucumber = new Product("WEG001", "cucumber", 1.23);
        Product tomato = new Product("WEG002", "tomato", 1.01);
        Product potato = new Product("WEG003", "potato", 0.99);
        Product fastCar = new Product("CAR001", "gepard", 99999);
        Product slowCar = new Product("CAR002", "turtle", 2929);
        Product banana = new Product("FRU001", "banana", 3.42);
        Product mandarine = new Product("FRU002", "mandarine", 3.24);
        Product teddy = new Product("TOY001", "teddy", 23.33);
        Product fish = new Product("FOOD01", "fish", 23.33);
        Product companionFish = new Product("PET001", "companionFish", 100);
        Product lion = new Product("PET002", "lion", 99);

        Basket basket = new Basket();
        Promotion promotion = new Promotion();

        //basket.Add(cucumber, 10);
        //basket.Add(slowCar, 1);
        //basket.Add(fish, 1);
        //basket.Add(companionFish, 1);
        //basket.Add(teddy, 2);

        BasketAddProduct addCucumber = new BasketAddProduct(basket, cucumber, 10);
        addCucumber.execute();
        BasketAddProduct addSlowCar = new BasketAddProduct(basket, slowCar, 1);
        addSlowCar.execute();
        BasketAddProduct addFish = new BasketAddProduct(basket, fish, 2);
        addFish.execute();
        BasketAddProduct addFriendFish = new BasketAddProduct(basket, companionFish, 1);
        addFriendFish.execute();
        BasketAddProduct addFriendLion = new BasketAddProduct(basket, lion, 1);
        addFriendLion.execute();
        BasketAddProduct addTeddy = new BasketAddProduct(basket, teddy, 1);
        addTeddy.execute();
        BasketAddProduct addPotato = new BasketAddProduct(basket, potato, 7);
        addPotato.execute();
        BasketAddProduct addMand = new BasketAddProduct(basket, mandarine, 2);
        addMand.execute();

        BasketRemoveProduct remMand = new BasketRemoveProduct(basket, mandarine, 2);
        remMand.execute();

        System.out.println(basket);


        AddPromotion addPromoFriendFish = new AddPromotion(promotion, companionFish, 30, null);
        addPromoFriendFish.execute();
        AddPromotion addPromoLion = new AddPromotion(promotion, lion, 100, "FeedLionLeon");
        addPromoLion.execute();
        AddPromotion addPromoPotato = new AddPromotion(promotion, potato, 40, null);
        addPromoPotato.execute();
        AddPromotion addPromoSlowCar = new AddPromotion(promotion, slowCar, 10, null);
        addPromoSlowCar.execute();
        AddPromotion addPromoTeddy = new AddPromotion(promotion, teddy, 20, null);
        addPromoTeddy.execute();
        AddPromotion addPromoFish = new AddPromotion(promotion, fish, 30, "DontEatFriends");
        addPromoFish.execute();

        RemovePromotion remPromoTeddy = new RemovePromotion(promotion, teddy);
        remPromoTeddy.execute();



        System.out.println(promotion);

        ApplyPromotion applyPromoLion = new ApplyPromotion(basket, promotion, lion, "FeedLionLeon");
        applyPromoLion.execute();
        ApplyPromotion applyPromoFish = new ApplyPromotion(basket, promotion, fish, "DontEatFriends");
        applyPromoFish.execute();

        ApplyPromotion applyPromoNull = new ApplyPromotion(basket, promotion, potato, null);
        applyPromoNull.execute();

        System.out.println(basket);

        BasketApplyCodelessPromo applyCodelessPromo = new BasketApplyCodelessPromo(basket, promotion);
        applyCodelessPromo.execute();

        System.out.println(basket);

        BasketAllPromotion allPromotion = new BasketAllPromotion(basket, 5);
        allPromotion.execute();


        System.out.println(basket);


        // sorts

        BasketSortNamePrice sortNamePrice = new BasketSortNamePrice(basket);
        sortNamePrice.execute();

        System.out.println(basket);

        BasketSortRevNamePrice sortRevNamePrice = new BasketSortRevNamePrice(basket);
        sortRevNamePrice.execute();

        System.out.println(basket);


        BasketSortRevPriceName sortRevPriceName = new BasketSortRevPriceName(basket);
        sortRevPriceName.execute();

        System.out.println(basket);


        assertEquals("direct", true, true);
    }

    @Test
    public void Invoker(){

        // Create basket
        Basket basket = new Basket();
        // Create promotion
        Promotion promotion = new Promotion();

        // Create Products
        Product cucumber = new Product("WEG001", "cucumber", 1.23);
        Product tomato = new Product("WEG002", "tomato", 1.01);
        Product potato = new Product("WEG003", "potato", 0.99);
        Product fastCar = new Product("CAR001", "gepard", 99999);
        Product slowCar = new Product("CAR002", "turtle", 2929);
        Product banana = new Product("FRU001", "banana", 3.42);
        Product mandarine = new Product("FRU002", "mandarine", 3.24);
        Product teddy = new Product("TOY001", "teddy", 23.33);
        Product fish = new Product("FOOD01", "fish", 23.33);
        Product companionFish = new Product("PET001", "companionFish", 100);
        Product lion = new Product("PET002", "lion", 99);

        // Create addProduct
        BasketAddProduct addCucumber = new BasketAddProduct(basket, cucumber, 10);
        BasketAddProduct addSlowCar = new BasketAddProduct(basket, slowCar, 1);
        BasketAddProduct addFish = new BasketAddProduct(basket, fish, 2);
        BasketAddProduct addFriendFish = new BasketAddProduct(basket, companionFish, 1);
        BasketAddProduct addFriendLion = new BasketAddProduct(basket, lion, 1);
        BasketAddProduct addTeddy = new BasketAddProduct(basket, teddy, 1);
        BasketAddProduct addPotato = new BasketAddProduct(basket, potato, 7);
        BasketAddProduct addMandarine = new BasketAddProduct(basket, mandarine, 2);
        // Create RemProduct
        BasketRemoveProduct remMandarine = new BasketRemoveProduct(basket, mandarine, 2);

        // Create AddPromotion
        AddPromotion addPromoFriendFish = new AddPromotion(promotion, companionFish, 30, null);
        AddPromotion addPromoLion = new AddPromotion(promotion, lion, 100, "FeedLionLeon");
        AddPromotion addPromoPotato = new AddPromotion(promotion, potato, 40, null);
        AddPromotion addPromoSlowCar = new AddPromotion(promotion, slowCar, 10, null);
        AddPromotion addPromoTeddy = new AddPromotion(promotion, teddy, 20, null);
        AddPromotion addPromoFish = new AddPromotion(promotion, fish, 30, "DontEatFriends");
        // Remove promotion
        RemovePromotion remPromoTeddy = new RemovePromotion(promotion, teddy);

        // To create apply promotions we first have to add them using invoker
        // So that our promotions that we pass actually have promotions
        // becouse rn promotions have nothing

        // Create OrderBasket
        BasketSortPriceName sortPriceName = new BasketSortPriceName(basket);
        BasketSortRevPriceName sortRevPriceName = new BasketSortRevPriceName(basket);
        BasketSortNamePrice sortNamePrice = new BasketSortNamePrice(basket);
        BasketSortRevNamePrice sortRevNamePrice = new BasketSortRevNamePrice(basket);


        // --------------- Create Invoker -----------------
        Invoker invoker = new Invoker(sortPriceName, sortRevPriceName, sortNamePrice, sortRevNamePrice);
        // invoker add products
        invoker.setBasketAddProduct(addCucumber);
        invoker.BasketAddProduct();
        invoker.setBasketAddProduct(addSlowCar);
        invoker.BasketAddProduct();
        invoker.setBasketAddProduct(addFish);
        invoker.BasketAddProduct();
        invoker.setBasketAddProduct(addFriendFish);
        invoker.BasketAddProduct();
        invoker.setBasketAddProduct(addFriendLion);
        invoker.BasketAddProduct();
        invoker.setBasketAddProduct(addTeddy);
        invoker.BasketAddProduct();
        invoker.setBasketAddProduct(addPotato);
        invoker.BasketAddProduct();
        invoker.setBasketAddProduct(addMandarine);
        invoker.BasketAddProduct();
        // remove products
        invoker.setBasketRemoveProduct(remMandarine);
        invoker.BasketRemoveProduct();

        // invoker add promotions
        invoker.setPromotionAddPromotion(addPromoFriendFish);
        invoker.PromotionAddPromotion();
        invoker.setPromotionAddPromotion(addPromoLion);
        invoker.PromotionAddPromotion();
        invoker.setPromotionAddPromotion(addPromoPotato);
        invoker.PromotionAddPromotion();
        invoker.setPromotionAddPromotion(addPromoSlowCar);
        invoker.PromotionAddPromotion();
        invoker.setPromotionAddPromotion(addPromoTeddy);
        invoker.PromotionAddPromotion();
        invoker.setPromotionAddPromotion(addPromoFish);
        invoker.PromotionAddPromotion();
        // invoker remove promotion
        invoker.setPromotionRemovePromotion(remPromoTeddy);
        invoker.PromotionRemovePromotion();
        System.out.println(promotion); // good

        // Create applyPromotion
        ApplyPromotion applyPromoLion = new ApplyPromotion(basket, promotion, lion, "FeedLionLeon");
        ApplyPromotion applyPromoFish = new ApplyPromotion(basket, promotion, fish, "DontEatFriends");
        ApplyPromotion applyPromoNull = new ApplyPromotion(basket, promotion, potato, null);


        System.out.println(basket);

        // Promotions have not been applied <[================================
        // invoker apply promotion to basket
        invoker.setBasketApplyPromotion(applyPromoLion);
        invoker.BasketApplyPromotion();
        invoker.setBasketApplyPromotion(applyPromoFish);
        invoker.BasketApplyPromotion();
        invoker.setBasketApplyPromotion(applyPromoNull);
        invoker.BasketApplyPromotion();

        // invoker do codeless promo
        BasketApplyCodelessPromo applyCodelessPromo = new BasketApplyCodelessPromo(basket, promotion);
        invoker.setBasketApplyCodelessPromo(applyCodelessPromo);
        invoker.BasketApplyCodelessPromo();
        // invoker do all promotion
        BasketAllPromotion allPromotion = new BasketAllPromotion(basket, 5);
        invoker.setBasketAllPromotion(allPromotion);
        invoker.BasketAllPromotion(); // we need to create that after we have products in basket !!!

        System.out.println(basket);
        // SORTS will also have a problem that basket dont have products so we can create new invoker after adding porducts? mby ? or also set them

        assertEquals("first Invoker", true, true);
    }


    @Before
    public void Setup(){
        // Create basket
        basket = new Basket();
        // Create products
        cucumber = new Product("WEG001", "cucumber", 1.22);
        potato = new Product("WEG002", "potato", 2.21);
        tomato = new Product("WEG003", "tomato", 5);
        slowCar = new Product("CAR002", "turtle", 2929);
        fastCar = new Product("CAR001", "gepard", 99999);
        banana = new Product("FRU001", "banana", 3.42);
        companyCup = new Product("MERCH001", "CompanyCup", 73.33);
        fish = new Product("FOOD01", "fish", 23.33);
        companionFish = new Product("PET001", "companionFish", 100);
        lion = new Product("PET002", "lion", 99);
        // Create promotion
        promotion = new Promotion();
    }

    @Test
    public void BasketAddProduct(){
        // Create Commands
        Command addCucumber = new BasketAddProduct(basket, cucumber, 10);
        Command remCucumber = new BasketRemoveProduct(basket, cucumber, 5);
        // Create Invoker
        InvokerBasket InsertProduct = new InvokerBasket(addCucumber, remCucumber);
        // DO command via invoker
        InsertProduct.DoBasketAddProduct();
        assertEquals("Add product to basket via InvokerBasket", cucumber, basket.getAllProducts().get(0));
    }

    @Test
    public void BasketRemoveProduct(){
        // Create Commands
        Command addCucumber = new BasketAddProduct(basket, cucumber, 10);
        Command remCucumber = new BasketRemoveProduct(basket, cucumber, 5);
        // Create Invoker
        InvokerBasket RemoveProduct = new InvokerBasket(addCucumber, remCucumber);
        // DO command via invoker
        RemoveProduct.DoBasketAddProduct();
        RemoveProduct.DoBasketRemoveProduct();
        RemoveProduct.DoBasketRemoveProduct();
        assertEquals("Remove product from basket via InvokerBasket", 0, basket.getAllProducts().size());
    }

    @Test
    public void PromotionAddPromotionNoCode(){
        // Create Commands
        Command addPromoPotato = new AddPromotion(promotion, potato, 50, null);
        Command remPromoPotato = new RemovePromotion(promotion, potato);
        // Create Invoker
        InvokerPromotion promoInvoker = new InvokerPromotion(addPromoPotato, remPromoPotato);
        // Use Invoker
        promoInvoker.DoAddPromotion();
        assertEquals("Add product to promotions", potato, promotion.getAllPromoted()[0]);
    }

    @Test
    public void PromotionAddPromotionWithCode(){
        // Create Commands
        Command addPromoPotato = new AddPromotion(promotion, potato, 50, "HalfPrice");
        Command remPromoPotato = new RemovePromotion(promotion, potato);
        // Create Invoker
        InvokerPromotion promoInvoker = new InvokerPromotion(addPromoPotato, remPromoPotato);
        // Use Invoker
        promoInvoker.DoAddPromotion();
        assertEquals("Add product to promotions and get percentage with code",
                50, promotion.getItemPromotion(potato, "HalfPrice"));
    }

    @Test
    public void PromotionAddPromotionWithCodeWrong(){
        // Create Commands
        Command addPromoPotato = new AddPromotion(promotion, potato, 50, "HalfPrice");
        Command remPromoPotato = new RemovePromotion(promotion, potato);
        // Create Invoker
        InvokerPromotion promoInvoker = new InvokerPromotion(addPromoPotato, remPromoPotato);
        // Use Invoker
        promoInvoker.DoAddPromotion();
        assertEquals("Add product to promotions and check percentage when code in wrong",
                0, promotion.getItemPromotion(potato, "noonononno"));
    }
    @Test
    public void PromotionRemovePromotion(){
        // Create Commands
        Command addPromoPotato = new AddPromotion(promotion, potato, 50, null);
        Command remPromoPotato = new RemovePromotion(promotion, potato);
        // Create Invoker
        InvokerPromotion promoInvoker = new InvokerPromotion(addPromoPotato, remPromoPotato);
        // Use Invoker
        promoInvoker.DoAddPromotion();
        promoInvoker.DoRemovePromotion();
        assertEquals("Remove product from promotions", 0, promotion.getAllPromoted().length);
    }


    @Test
    public void ApplyPromotionOnProduct(){
        // Create Commands
        Command addPromoCucumber = new AddPromotion(promotion, cucumber, 50, null);
        Command remPromoCucumber = new RemovePromotion(promotion, cucumber);
        Command addBasketCucumber = new BasketAddProduct(basket, cucumber, 10);
        Command remoBasketCucumber = new BasketRemoveProduct(basket, cucumber, 10);
        // Create Invokers
        InvokerPromotion promoInvoker = new InvokerPromotion(addPromoCucumber, remPromoCucumber);
        InvokerBasket basketInvoker = new InvokerBasket(addBasketCucumber, remoBasketCucumber);
        // Use Invokers
        promoInvoker.DoAddPromotion();
        basketInvoker.DoBasketAddProduct();
        // Create Commands operating on changed basket and changed promotion
        Command applyPromotion = new ApplyPromotion(basket, promotion, cucumber, null);
        //Create Invoker that uses Promotion and Basket
        BasketPromotionInvoker BothInvoker = new BasketPromotionInvoker(applyPromotion);
        BothInvoker.DoBasketApplyPromotion();
        assertEquals("Apply promotion on product in basket", 10*1.22/2, basket.TotalCost(), 0.001);
    }

    @Test
    public void ApplyPromotionOver300pln(){
        // Create Commands
        Command addPromoCucumber = new AddPromotion(promotion, cucumber, 50, null);
        Command remPromoCucumber = new RemovePromotion(promotion, cucumber);
        Command addBasketCucumber = new BasketAddProduct(basket, cucumber, 10);
        Command remoBasketCucumber = new BasketRemoveProduct(basket, cucumber, 10);
        Command addBasketSlowCar = new BasketAddProduct(basket, slowCar, 1);
        Command remoBasketSlowCar = new BasketRemoveProduct(basket, slowCar, 1);
        // Create Invokers
        InvokerPromotion promoInvoker = new InvokerPromotion(addPromoCucumber, remPromoCucumber);
        InvokerBasket basketInvoker = new InvokerBasket(addBasketCucumber, remoBasketCucumber);
        InvokerBasket basketInvokerCar = new InvokerBasket(addBasketSlowCar, remoBasketSlowCar);
        // Use Invokers
        promoInvoker.DoAddPromotion();
        basketInvoker.DoBasketAddProduct();
        basketInvokerCar.DoBasketAddProduct();
        if (basket.TotalCost() >= 300){
            // Create Commands operating on changed basket and changed promotion
            Command basketAllPromotion = new BasketAllPromotion(basket, 5);
            Command basketCodellesPromo = new BasketApplyCodelessPromo(basket, promotion);
            //Create Invoker that uses Promotion and Basket
            BasketPromotionInvoker BothInvoker = new BasketPromotionInvoker(basketAllPromotion, basketCodellesPromo);
            BothInvoker.DoBasketApplyCodelessPromo();
            BothInvoker.DoBasketAllPromotion();
        }
        assertEquals("Apply promotion on all products", 2794.14, basket.TotalCost(), 0.001);
    }

    @Test
    public void ApplyCompanyCupFree(){
        // Create Commands
        Command addPromoCompanyCup = new AddPromotion(promotion, companyCup, 100, "over200");
        Command remPromoCompanyCup = new RemovePromotion(promotion, companyCup);
        Command addBasketCucumber = new BasketAddProduct(basket, cucumber, 10);
        Command remoBasketCucumber = new BasketRemoveProduct(basket, cucumber, 10);
        Command addBasketLion = new BasketAddProduct(basket, lion, 2);
        Command remoBasketLion = new BasketRemoveProduct(basket, lion, 2);
        // Create Invokers
        InvokerPromotion promoInvoker = new InvokerPromotion(addPromoCompanyCup, remPromoCompanyCup);
        InvokerBasket basketInvoker = new InvokerBasket(addBasketCucumber, remoBasketCucumber);
        InvokerBasket basketInvokerLion = new InvokerBasket(addBasketLion, remoBasketLion);
        // Use Invokers
        promoInvoker.DoAddPromotion();
        basketInvoker.DoBasketAddProduct();
        basketInvokerLion.DoBasketAddProduct();
        basketInvokerLion.DoBasketAddProduct();
        // LOGIC
        double totalBefore = basket.TotalCost();
        if (basket.TotalCost() >= 200){
            // Create Commands operating on changed basket and changed promotion
            Command addBasketCompanyCup = new BasketAddProduct(basket, companyCup, 1);
            Command remoBasketCompanyCup = new BasketRemoveProduct(basket, companyCup, 1);
            Command applyPromCup = new ApplyPromotion(basket, promotion, companyCup, "over200");
            //Create Invoker that uses Promotion and Basket
            InvokerBasket basketCompanyCup = new InvokerBasket(addBasketCompanyCup, remoBasketCompanyCup);
            BasketPromotionInvoker BothInvoker = new BasketPromotionInvoker(applyPromCup);
            // Do things
            basketCompanyCup.DoBasketAddProduct();
            BothInvoker.DoBasketApplyPromotion();
        }
        double totalAfter = basket.TotalCost();
        //System.out.println(basket.getAllProducts());
        //System.out.println(totalBefore == totalAfter);
        assertEquals("Apply promotion on all products", companyCup, basket.getAllProducts().get(1));
    }


    @Test
    public void BuyThreeGetOneFree(){
        // Create Commands
        Command addBasketCucumber = new BasketAddProduct(basket, cucumber, 10);
        Command remoBasketCucumber = new BasketRemoveProduct(basket, cucumber, 10);
        Command addBasketLion = new BasketAddProduct(basket, lion, 2);
        Command remoBasketLion = new BasketRemoveProduct(basket, lion, 2);
        // Create Invokers
        InvokerBasket basketInvoker = new InvokerBasket(addBasketCucumber, remoBasketCucumber);
        InvokerBasket basketInvokerLion = new InvokerBasket(addBasketLion, remoBasketLion);
        // Use Invokers
        basketInvoker.DoBasketAddProduct();
        basketInvokerLion.DoBasketAddProduct();
        basketInvokerLion.DoBasketAddProduct();
        // LOGIC
        Product oldProduct = basket.cheapest();
        double totalBefore = basket.TotalCost();
        if (basket.TotalAmount() >= 3){
            System.out.println(basket.getAllProducts());
            Product old = basket.cheapest();
            Product freeOne = new Product("FREE3", old.getName(), old.getPrice(), 0);
            // Product freeOne = old.ColneDiscountedPrice(0) doesn't work but should
            Command addBasketfreeOne = new BasketAddProduct(basket, freeOne, 1);
            Command remoBasketfreeOne = new BasketRemoveProduct(basket, freeOne, 1);
            InvokerBasket basketInvokerFreeOne = new InvokerBasket(addBasketfreeOne, remoBasketfreeOne);

            Command addBasketCheapOne = new BasketAddProduct(basket, old, 1);
            Command remoBasketCheapOne = new BasketRemoveProduct(basket, old, 1);
            InvokerBasket basketInvokerOld = new InvokerBasket(addBasketCheapOne, remoBasketCheapOne);
            // Do things
            basketInvokerFreeOne.DoBasketAddProduct();
            basketInvokerOld.DoBasketRemoveProduct();
            System.out.println(basket.getAllProducts());
        }
        double totalAfter = basket.TotalCost();
        System.out.println(basket.getAllProducts());
        System.out.println(totalBefore == totalAfter);
        assertEquals("Apply promotion on all products", oldProduct.getPrice(), totalBefore-totalAfter, 0.001);
    }

    @Test
    public void Sorts(){
        BasketAddProduct addCucumber = new BasketAddProduct(basket, cucumber, 10);
        addCucumber.execute();
        BasketAddProduct addSlowCar = new BasketAddProduct(basket, slowCar, 1);
        addSlowCar.execute();
        BasketAddProduct addFish = new BasketAddProduct(basket, fish, 2);
        addFish.execute();
        BasketAddProduct addFriendFish = new BasketAddProduct(basket, companionFish, 1);
        addFriendFish.execute();
        BasketAddProduct addFriendLion = new BasketAddProduct(basket, lion, 1);
        addFriendLion.execute();
        BasketAddProduct addPotato = new BasketAddProduct(basket, potato, 7);
        addPotato.execute();

        BasketSortNamePrice sortNamePrice = new BasketSortNamePrice(basket);
        sortNamePrice.execute();

        System.out.println(basket);

        BasketSortRevNamePrice sortRevNamePrice = new BasketSortRevNamePrice(basket);
        sortRevNamePrice.execute();

        System.out.println(basket);


        BasketSortRevPriceName sortRevPriceName = new BasketSortRevPriceName(basket);
        sortRevPriceName.execute();

        System.out.println(basket);
        assertEquals("Sorts with prints", true, true);
    }


}
