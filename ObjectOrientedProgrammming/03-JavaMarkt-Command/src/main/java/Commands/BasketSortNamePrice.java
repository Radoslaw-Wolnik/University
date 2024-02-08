package Commands;

import Basket.Basket;

public class BasketSortNamePrice implements Command{
    final private Basket basket;

    public BasketSortNamePrice(Basket basket){
        this.basket = basket;
    }

    @Override
    public void execute() {
        basket.SortNamePrice();
    }

    @Override
    public void unexecute() {
        basket.SortPriceName();
    }

}



