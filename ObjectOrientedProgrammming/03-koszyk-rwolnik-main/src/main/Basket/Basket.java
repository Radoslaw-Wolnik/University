package Basket;

import Product.Product;
import Product.ProductNameComparator;
import Product.ProductPriceComparator;

import java.util.*;


public class Basket {
    private HashMap<Product, Integer> basket = new HashMap<>(); // Product.Product : AmountOfIt
    private ArrayList<Product> list;
    private boolean change = false;
    public Basket(){
    }

    public void Add(Product product, int amount){
        if(basket.get(product) != null){
            int oldAmount = basket.get(product);
            basket.put(product, oldAmount + amount);
        }
        else {
            basket.put(product, amount);
        }
        change = true;
    }

    public void Remove(Product product, int amount){
        if(basket.get(product) != null) {
            if (basket.get(product) <= amount) {
                basket.remove(product);
            } else {
                int newAmount = basket.get(product) - amount;
                basket.put(product, newAmount);
            }
            change = true;
        }
    }

    public void RemoveEntireSet(HashMap<Product, Integer> removeSet) {
        for (Map.Entry<Product, Integer> entry : removeSet.entrySet()) {
            Product product = entry.getKey();
            basket.remove(product);
        }
        change = true;
    }
    public void AddEntireSet(HashMap<Product, Integer> addSet){
        for (Map.Entry<Product, Integer> entry : addSet.entrySet()) {
            Product product = entry.getKey();
            int amount = entry.getValue();
            basket.put(product, amount);
        }
        change = true;
    }


    public double TotalCost(){
        double totalPrice = 0;
        for (Map.Entry<Product, Integer> entry : basket.entrySet()) {
            double DiscountPrice = entry.getKey().getDiscountPrice();
            int amount = entry.getValue();
            totalPrice += DiscountPrice*amount;
        }
        return totalPrice;
    }

    public double TotalAmount(){
        int totalAmount = 0;
        for (Map.Entry<Product, Integer> entry : basket.entrySet()) {
            totalAmount += entry.getValue();
        }
        return totalAmount;
    }

    public ArrayList<Product> getAllProducts(){
        SortPriceName();
        return list;
    }

    public HashMap<Product, Integer> getBasket() {
        return basket;
    }

    public int getProductAmount(Product product){
        if (basket.get(product) == null){
            return 0;
        }
        return basket.get(product);
    }

    public ArrayList<Product> getNProducts(int n){
        SortPriceName();
        if(n < basket.size()){
            ArrayList<Product> res = new ArrayList<Product>();
            for(int i = 0; i < n; i++){
                res.add(list.get(i));
            }
            return res;
        }
        else{
            return list;
        }
    }

    public void SortPriceName(){ // default
        ArrayList<Product> temp = new ArrayList<>(basket.keySet());
        temp.sort(new ProductPriceComparator().thenComparing(new ProductNameComparator()));
        list = temp;
    }

    public void SortRevPriceName(){
        SortPriceName();
        Collections.reverse(list);
    }

    public void SortNamePrice(){
        ArrayList<Product> temp = new ArrayList<>(basket.keySet());
        //Collections.sort(temp, new Product.ProductNameComparator());
        temp.sort(new ProductNameComparator().thenComparing(new ProductPriceComparator()));
        list = temp;
    }

    public void SortRevNamePrice(){
        SortNamePrice();
        Collections.reverse(list);
    }

    @Override
    public String toString() {
        if(list == null || change){
            SortRevPriceName();
            change = false;
        }

        return "------ Basket: " + Arrays.toString(list.stream().map(Product::toString).toArray())
                + "\n"
                + Arrays.toString(basket.values().toArray(new Integer[0]))
                + "\n";
    }

    public Product mostExpensive(){
        return Collections.max(basket.keySet(), new ProductPriceComparator());
    }

    public Product cheapest(){
        return Collections.min(basket.keySet(), new ProductPriceComparator());
    }


    public void Swap(Product oldProduct, Product newProduct) {
        //System.out.println("Basket: Swap");
        if (oldProduct.equals(newProduct) && basket.containsKey(oldProduct)){
            //System.out.println("Basket if in");
            int amount = basket.get(oldProduct);
            basket.remove(oldProduct);
            basket.put(newProduct, amount);
            //System.out.println(toString());
        }
    }
}
