package Commands;

import Basket.Basket;
import Product.Product;
import Promotion.Promotion;

import java.util.HashMap;
import java.util.Map;

public class BasketApplyCodelessPromo implements Command{
    private final Basket basket;
    private final HashMap<Product, Integer> before;
    private final HashMap<Product, Integer> after;

    public BasketApplyCodelessPromo (Basket basket, Promotion promotion){
        this.basket = basket;
        before = new HashMap<>();
        after = new HashMap<>();
        HashMap <Product, Integer> noCode = promotion.getNoCodePromo();

        // dependencies <------------------------------------------------------------
        for (Map.Entry<Product, Integer> entry : basket.getBasket().entrySet()) {
            Product product = entry.getKey();
            if(noCode.containsKey(product)){
                double newDiscount = product.getPrice() * (100 - noCode.get(product)) / 100;
                Product discounted = product.cloneChangedDiscountPrice(newDiscount);
                after.put(discounted, entry.getValue());
                before.put(entry.getKey(), entry.getValue());
            }
        }
    }

    @Override
    public void execute() {
        basket.RemoveEntireSet(before);
        basket.AddEntireSet(after);
        //AddRemove(after, before);
    }

    @Override
    public void unexecute() {
        basket.RemoveEntireSet(after);
        basket.AddEntireSet(before);
        //AddRemove(before, after);
    }
/*
    private void AddRemove(HashMap<Product, Integer> addSet, HashMap<Product, Integer> removeSet) {
        for (Map.Entry<Product, Integer> entry : removeSet.entrySet()) {
            Product product = entry.getKey();
            int amount = entry.getValue();
            basket.Remove(product, amount);
        }
        for (Map.Entry<Product, Integer> entry : addSet.entrySet()) {
            Product product = entry.getKey();
            int amount = entry.getValue();
            basket.Add(product, amount);
        }
    }*/

}
