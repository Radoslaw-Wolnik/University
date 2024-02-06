package Commands;
import Product.Product;
import Promotion.Promotion;

public class AddPromotion implements Command{

    private final int percentage;
    private final String code;
    private final Promotion promotion;
    private final Product product;
    //private final Product discounted;

    public AddPromotion(Promotion promotion, Product product, Integer percentage, String code){
        this.promotion = promotion;
        this.percentage = percentage;
        this.code = code;
        this.product = product;
    }

    @Override
    public void execute() {
        promotion.AddPromotion(product, percentage, code);
    }

    @Override
    public void unexecute() {
        promotion.RemovePromotion(product);
        // here we could also delete this object mby
    }

}
