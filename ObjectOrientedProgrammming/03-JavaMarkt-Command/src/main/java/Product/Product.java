package Product;

import java.util.Objects;

// product extens/implements comparable <---------------------------
public class Product implements Comparable<Product>{
    private final String code;          // kod produktu
    private final String name;          // nazwa produktu
    private final double price;         // cena produktu
    private final double discountPrice; // cena produktu po uwzględnieniu promocji


    public Product(String code, String name, double price){
        this.code = code;
        this.name = name;
        this.price = price;
        this.discountPrice = price;
    }

    public Product(String code, String name, double price, double discountPrice){
        this.code = code;
        this.name = name;
        this.price = price;
        this.discountPrice = discountPrice;
    }

    public String getCode() {
        return code;
    }

    public String getName(){
        return name;
    }

    public double getPrice() {
        return price;
    }

    public double getDiscountPrice() {
        return discountPrice;
    }

    public Product cloneChangedDiscountPrice(double newDiscountPrice){
        return new Product(code, name, price, newDiscountPrice);
    }

    public Product clone(){
        return this;
    }

    @Override
    public String toString() {
        return "\nProduct.Product{" +
                "code='" + code + '\'' +
                ", name='" + name + '\'' +
                ", price=" + price +
                ", discountPrice=" + discountPrice +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Product product = (Product) o;
        return Objects.equals(code, product.code);
    }

    @Override
    public int hashCode() {
        return Objects.hash(code);
    }

    // Could be used in Price comparisons in Comparators
    @Override
    public int compareTo(Product o) { // true : 0; lower then curr : -1; bigger then curr : 1
        if (this == o) return 0;
        if (o == null) throw new NullPointerException();
        if (getClass() != o.getClass()) throw new UnsupportedOperationException(); // not comparable objects
        return Double.compare(o.price, price); // not sure witch order mby: Double.compare(price, o.price);
    }
}
