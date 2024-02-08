package Commands;

import Basket.Basket;
public class BasketSortRevPriceName implements Command{
    final private Basket basket;

    public BasketSortRevPriceName(Basket basket){
        this.basket = basket;
    }

    @Override
    public void execute() {
        basket.SortRevPriceName();
    }

    @Override
    public void unexecute() {
        basket.SortPriceName();
    }

}



