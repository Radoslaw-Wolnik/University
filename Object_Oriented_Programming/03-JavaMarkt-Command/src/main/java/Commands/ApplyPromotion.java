package Commands;
import Product.Product;
import Basket.Basket;
import Promotion.Promotion;

public class ApplyPromotion implements Command{

    private final Basket basket;
    private final Product product;
    private final Product discProduct;

    public ApplyPromotion(Basket basket, Promotion promotion, Product product, String promotionCode){
        this.basket = basket;
        this.product = product;
        int percentage = promotion.getItemPromotion(product, promotionCode);
        double discPrice = product.getPrice() * (100 - percentage) / 100;
        discProduct = product.cloneChangedDiscountPrice(discPrice);
    }

    @Override
    public void execute() {
        basket.Swap(product, discProduct);
        //System.out.println("Swapped");
        //basket.Remove(product, amount);
        //basket.Add(discProduct, amount);
    }

    @Override
    public void unexecute() {
        basket.Swap(discProduct, product);
        //basket.Remove(discProduct, amount);
        //basket.Add(product, amount);
    }
}
