package Commands;
import Product.Product;
import Basket.Basket;

public class BasketAddProduct implements Command{

    final private Basket basket;
    final private Product product;
    final private int amount;

    public BasketAddProduct(Basket basket, Product product, Integer amount){
        this.basket = basket;
        this.product = product;
        this.amount = amount;
    }

    @Override
    public void execute() {
        basket.Add(product, amount);
    }

    @Override
    public void unexecute() {
        basket.Remove(product, amount);
    }

}
