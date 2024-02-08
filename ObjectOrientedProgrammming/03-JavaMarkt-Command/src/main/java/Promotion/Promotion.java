package Promotion;

import Product.Product;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Promotion {
    private HashMap<Product, Integer> promotions = new HashMap<>();  // ItemID : Promotion.Promotion in % eg 100 => 100%off => price = 0
    private HashMap<Product, String> codes = new HashMap<>();        // ItemID : Code // if it dont require a code then ItemID "null"

    public Promotion(){

    }

    public void AddPromotion(Product product, Integer percentage, String code){
        promotions.put(product, percentage);
        codes.put(product, code);
    }

    public void RemovePromotion(Product product){
        if(promotions.containsKey(product)){
            promotions.remove(product);
            codes.remove(product);
        }
    }


    // val: int % 0-100 where 100% = 0pln
    public int getItemPromotion(Product product, String code){
        // hashmap uses .equals and .hashCode to find key so if the product equals key (id's are the same) it should return value
        if(promotions.containsKey(product)){
            if(codes.get(product) == null && code == null) {
                return promotions.get(product);
            }
            else if (codes.get(product).equals(code)) {
                return promotions.get(product);
            }
        }
        return 0;
    }

    @Override
    public String toString() {
        return "---- Promotion ---- Product.Product : Percentage ----"
                + promotions.toString()
                + "\n---- Promotion ---- Product.Product : Code ----"
                + codes.toString()
                + "\n";
    }


    // useless ------------------------------------------------------------------------------
    public Product[] getAllPromoted(){
        return promotions.keySet().toArray(new Product[0]);
    }

    public HashMap<Product, Integer> getNoCodePromo(){
        HashMap<Product, Integer>  result = new HashMap<>();
        for (Map.Entry<Product, String> entry : codes.entrySet()) {
            if(entry.getValue() == null){
                result.put(entry.getKey(), promotions.get(entry.getKey()));
            }
        }
        return result;
    }


    public String getItemCode(Product product) {
        return codes.get(product);
    }
}
