package Commands;
import Product.Product;
import Basket.Basket;

import java.util.HashMap;
import java.util.Map;

public class BasketAllPromotion implements Command{

    private final Basket basket;
    private final HashMap<Product, Integer> before;
    private final HashMap<Product, Integer> after;

    public BasketAllPromotion (Basket basket, int percentage){
        this.basket = basket;
        before = new HashMap<>();
        after = new HashMap<>();

        for (Map.Entry<Product, Integer> entry : basket.getBasket().entrySet()) {
            Product product = entry.getKey();

            double newDiscount = product.getDiscountPrice() * (100 - percentage) / 100;
            Product discounted = product.cloneChangedDiscountPrice(newDiscount);
            after.put(discounted, entry.getValue());
            before.put(product, entry.getValue());
        }

    }

    @Override
    public void execute() {
        basket.RemoveEntireSet(before);
        basket.AddEntireSet(after);
    }

    @Override
    public void unexecute() {
        basket.RemoveEntireSet(after);
        basket.AddEntireSet(before);
    }

}
