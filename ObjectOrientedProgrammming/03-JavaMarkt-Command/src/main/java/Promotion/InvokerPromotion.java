package Promotion;
import Commands.Command;
import java.util.LinkedList;

public class InvokerPromotion {
    // Target: Promotion
    private LinkedList<Command> history = new LinkedList<>(); // Stack represented as a linkedList
    private final Command promotionAddPromotion;
    private final Command promotionRemovePromotion;

    public InvokerPromotion(Command promotionAddPromotion, Command promotionRemovePromotion){
        this.promotionAddPromotion = promotionAddPromotion;
        this.promotionRemovePromotion =promotionRemovePromotion;
    }



    // --------- Command Interface -----------
    private boolean checkCommand(Command check){
        return check != null;
    }
    public void Undo(){
        Command last = history.pop();
        if(last != null){
            last.unexecute();
        }
    }
    private void executeCommand(Command command){
        command.execute();
        history.push(command);
    }

    public void DoAddPromotion(){
        executeCommand(promotionAddPromotion);
    }
    public void DoRemovePromotion(){
        executeCommand(promotionRemovePromotion);
    }

}
