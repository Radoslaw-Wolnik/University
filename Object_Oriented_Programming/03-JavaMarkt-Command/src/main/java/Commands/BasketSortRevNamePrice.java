package Commands;

import Basket.Basket;
public class BasketSortRevNamePrice implements Command{
    final private Basket basket;

    public BasketSortRevNamePrice(Basket basket){
        this.basket = basket;
    }

    @Override
    public void execute() {
        basket.SortRevNamePrice();
    }

    @Override
    public void unexecute() {
        basket.SortPriceName();
    }

}




