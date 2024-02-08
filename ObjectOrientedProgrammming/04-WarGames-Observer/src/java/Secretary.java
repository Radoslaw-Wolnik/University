// Implementing observer pattern
/*
 * Walczącym generałom przygląda się sekretarz prezydenta.
 * Pisze on raporty dotyczące danej armii.
 * Opisuje wszelkie akcje podjęte przez generałów oraz zmiany poszczególnych żołnierzy.
 *
 * */

import java.util.ArrayList;

public class Secretary implements Observer{
    public Secretary(){
    }

    @Override
    public void update(String action, ArrayList<Soldier> status) {
        String result = "";
        for(Soldier soldier : status){
            result += soldier.toString() + "\n";
        }

        System.out.println("Our general performed action: " + action + "\n" +
                "Current army status: " + "\n" + result + "\n");
    }
}
