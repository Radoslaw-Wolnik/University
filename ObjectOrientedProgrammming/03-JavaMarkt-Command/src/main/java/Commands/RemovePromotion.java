package Commands;

import Product.Product;
import Promotion.Promotion;

public class RemovePromotion implements Command{
    private final Promotion promotion;
    private final Product product;
    private final int percentage;
    private final String code;

    public RemovePromotion(Promotion promotion, Product product){
        this.promotion = promotion;
        this.product = product;
        this.code = promotion.getItemCode(product);
        this.percentage = promotion.getItemPromotion(product, code);
    }

    @Override
    public void execute() {
        promotion.RemovePromotion(product);
    }

    @Override
    public void unexecute() {
        promotion.AddPromotion(product, percentage, code);
    }

}
