import Commands.Command;
import java.util.LinkedList;

public class BasketPromotionInvoker {
    // Target Basket with Promotion
    private LinkedList<Command> history = new LinkedList<>(); // Stack represented as a linkedList
    private final Command basketApplyPromotion; // done - applies promotion on product
    private final Command basketAllPromotion; // done - applies promotion to all products in basket
    private final Command basketApplyCodelessPromo; // done - applies promotion for all products in basket if promotion.code = null

    public BasketPromotionInvoker(Command basketApplyPromotion, Command basketAllPromotion, Command basketApplyCodelessPromo){
        this.basketApplyPromotion = basketApplyPromotion;
        this.basketAllPromotion = basketAllPromotion;
        this.basketApplyCodelessPromo = basketApplyCodelessPromo;
    }

    public BasketPromotionInvoker(Command basketApplyPromotion){
        this.basketApplyPromotion = basketApplyPromotion;
        this.basketAllPromotion = null;
        this.basketApplyCodelessPromo = null;
    }

    public BasketPromotionInvoker(Command basketAllPromotion, Command basketApplyCodelessPromo){
        this.basketApplyPromotion = null;
        this.basketAllPromotion = basketAllPromotion;
        this.basketApplyCodelessPromo = basketApplyCodelessPromo;
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


    public void DoBasketApplyPromotion(){
        executeCommand(basketApplyPromotion);
    }

    public void DoBasketAllPromotion(){
        executeCommand(basketAllPromotion);
    }

    public void DoBasketApplyCodelessPromo(){
        executeCommand(basketApplyCodelessPromo);
    }


}
