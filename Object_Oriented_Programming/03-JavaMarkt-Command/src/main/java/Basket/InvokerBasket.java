package Basket;
import Commands.Command;
import java.util.LinkedList;

public class InvokerBasket {
    // Target: Basket
    private LinkedList<Command> history = new LinkedList<>(); // Stack represented as a linkedList

    private final Command basketAddProduct;
    private final Command basketRemoveProduct;
    private final Command basketSortPriceName;
    private final Command basketSortRevPriceName;
    private final Command basketSortNamePrice;
    private final Command basketSortRevNamePrice;


    public InvokerBasket(Command basketAddProduct, Command basketRemoveProduct,
            Command basketSortPriceName, Command basketSortRevPriceName, Command basketSortNamePrice, Command basketSortRevNamePrice){
        this.basketAddProduct = basketAddProduct;
        this.basketRemoveProduct = basketRemoveProduct;
        this.basketSortPriceName = basketSortPriceName;
        this.basketSortRevPriceName = basketSortRevPriceName;
        this.basketSortNamePrice = basketSortNamePrice;
        this.basketSortRevNamePrice = basketSortRevNamePrice;
    }

    public InvokerBasket(Command basketAddProduct, Command basketRemoveProduct){
        this.basketAddProduct = basketAddProduct;
        this.basketRemoveProduct = basketRemoveProduct;
        this.basketSortPriceName = null;
        this.basketSortRevPriceName = null;
        this.basketSortNamePrice = null;
        this.basketSortRevNamePrice = null;
    }

    public InvokerBasket(Command basketSortPriceName, Command basketSortRevPriceName, Command basketSortNamePrice, Command basketSortRevNamePrice){
        this.basketAddProduct = null;
        this.basketRemoveProduct = null;
        this.basketSortPriceName = basketSortPriceName;
        this.basketSortRevPriceName = basketSortRevPriceName;
        this.basketSortNamePrice = basketSortNamePrice;
        this.basketSortRevNamePrice = basketSortRevNamePrice;
    }



    // --------- Command Interface -----------
    public void Undo(){
        Command last = history.pop();
        if(last != null){
            last.unexecute();
        }
    }
    private void executeCommand(Command command){
        if(command != null){
            command.execute();
            history.push(command);
        }
    }

    public void DoBasketAddProduct(){
        executeCommand(basketAddProduct);
    }

    public void DoBasketRemoveProduct(){
        executeCommand(basketRemoveProduct);
    }

    // Sorts
    public void DoBasketSortPriceName(){
        executeCommand(basketSortPriceName);
    }
    public void DoBasketSortRevPriceName(){
        executeCommand(basketSortRevPriceName);
    }
    public void DoBasketSortNamePrice(){
        executeCommand(basketSortNamePrice);
    }
    public void DoBasketSortRevNamePrice(){
        executeCommand(basketSortRevNamePrice);
    }

}
