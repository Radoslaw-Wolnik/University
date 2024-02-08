package Product;

import java.util.Comparator;

public class ProductPriceComparator implements Comparator<Product> {
    @Override
    public int compare(Product a, Product b) {
        return Double.compare(a.getPrice(), b.getPrice());
    }
}
