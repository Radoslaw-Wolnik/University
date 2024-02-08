package Product;

import java.util.Comparator;

public class ProductNameComparator implements Comparator<Product> {
    @Override
    public int compare(Product a, Product b) {
        return a.getName().compareToIgnoreCase(b.getName());
    }
}
