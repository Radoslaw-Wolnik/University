package Commands;
import Basket.Basket;

public class BasketSortPriceName implements Command{
    final private Basket basket;

    public BasketSortPriceName(Basket basket){
        this.basket = basket;
    }

    @Override
    public void execute() {
        basket.SortPriceName();
    }

    @Override
    public void unexecute() {
        basket.SortPriceName(); //its default so not much to undo here
    }

}


