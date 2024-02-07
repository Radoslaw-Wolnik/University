import Commands.Command;

import java.util.LinkedList;
import java.util.Queue;

public class Invoker {

    private LinkedList<Command> history = new LinkedList<>(); // Stack represented as a linkedList

    private Command basketAddProduct; // done - adds product to basket
    private Command basketRemoveProduct; // done
    private Command promotionAddPromotion; // done - adds a promotion to promotion list
    private Command promotionRemovePromotion; // done
    private Command basketApplyPromotion; // done - applies promotion on product
    private Command basketAllPromotion; // done - applies promotion to all products in basket
    private Command basketApplyCodelessPromo; // done - applies promotion for all products in basket if promotion.code = null




    private final Command basketSortPriceName; // done : default
    private final Command basketSortRevPriceName; // done
    private final Command basketSortNamePrice; // done
    private final Command basketSortRevNamePrice; // done


    private Command BasketThirdProductFree; // if total product count = 3 then third -> gratis  Product.Product.DiscountPrice = 0 for cheapest


    // total cost is not in command as it returns a value


    Invoker(Command basketSortPriceName, Command basketSortRevPriceName, Command basketSortNamePrice, Command basketSortRevNamePrice){
        // if its mutable then not in constructor
        this.basketSortPriceName = basketSortPriceName;
        this.basketSortRevPriceName = basketSortRevPriceName;
        this.basketSortNamePrice = basketSortNamePrice;
        this.basketSortRevNamePrice = basketSortRevNamePrice;
    }

    // ------------- set --------------
    public void setBasketAddProduct(Command basketAddProduct) {
        this.basketAddProduct = basketAddProduct;
    }
    public void setBasketRemoveProduct(Command basketRemoveProduct) {
        this.basketRemoveProduct = basketRemoveProduct;
    }
    public void setPromotionAddPromotion(Command promotionAddPromotion) {
        this.promotionAddPromotion = promotionAddPromotion;
    }
    public void setPromotionRemovePromotion(Command promotionRemovePromotion) {
        this.promotionRemovePromotion = promotionRemovePromotion;
    }
    public void setBasketApplyPromotion(Command basketApplyPromotion) {
        this.basketApplyPromotion = basketApplyPromotion;
    }

    public void setBasketApplyCodelessPromo(Command basketApplyCodelessPromo) {
        this.basketApplyCodelessPromo = basketApplyCodelessPromo;
    }

    public void setBasketAllPromotion(Command basketAllPromotion) {
        this.basketAllPromotion = basketAllPromotion;
    }

    // --------- Commands.Command Interface -----------
    public void Undo(){
        Command last = history.pop();
        if(last != null){
            last.unexecute();
        }
    }

    // mby there is an easier way to do it?
    public void BasketAddProduct(){
        basketAddProduct.execute();
        history.push(basketAddProduct);
    }

    public void BasketRemoveProduct(){
        basketRemoveProduct.execute();
        history.push(basketRemoveProduct);
    }

    public void PromotionAddPromotion(){
        promotionAddPromotion.execute();
        history.push(promotionAddPromotion);
    }

    public void PromotionRemovePromotion(){
        promotionRemovePromotion.execute();
        history.push(promotionRemovePromotion);
    }

    public void BasketApplyPromotion(){
        basketApplyPromotion.execute();
        history.push(basketApplyPromotion);
    }

    public void BasketAllPromotion(){
        basketAllPromotion.execute();
        history.push(basketAllPromotion);
    }

    public void BasketApplyCodelessPromo(){
        basketApplyCodelessPromo.execute();
        history.push(basketApplyCodelessPromo);
    }


    // Sorts
    public void BasketSortPriceName(){
        basketSortPriceName.execute();
        history.push(basketSortPriceName);
    }
    public void BasketSortRevPriceName(){
        basketSortRevPriceName.execute();
        history.push(basketSortRevPriceName);
    }
    public void BasketSortNamePrice(){
        basketSortNamePrice.execute();
        history.push(basketSortNamePrice);
    }
    public void BasketSortRevNamePrice(){
        basketSortRevNamePrice.execute();
        history.push(basketSortRevNamePrice);
    }

}
