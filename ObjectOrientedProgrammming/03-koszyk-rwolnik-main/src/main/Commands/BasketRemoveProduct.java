package Commands;

import Basket.Basket;
import Product.Product;

public class BasketRemoveProduct implements Command {
    final private Basket basket;
    final private Product product;
    final private int amount;

    public BasketRemoveProduct(Basket basket, Product product, Integer amount){
        this.basket = basket;
        this.product = product;
        this.amount = amount;
    }

    @Override
    public void execute() {
        basket.Remove(product, amount);
    }

    @Override
    public void unexecute() {
        basket.Add(product, amount);
    }

}
