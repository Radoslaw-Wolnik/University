/*
 * Żołnierze posiadają:
 *     stopień wojskowy: szeregowy (wartość: 1), kapral (wartość: 2), kapitan (wartość: 3) i major (wartość: 4)
 *     doświadczenie
 *     siła żołnierza jest obliczana jako iloczyn jego stopnia i doświadczenia
 *     żołnierz ginie, gdy jego doświadczenie = 0
 *     jeżeli doświadczenie osiągnie pięciokrotność wartości stopnia, awansuje na kolejny stopień oraz jego doświadczenie = 1.
 * */

import java.util.ArrayList;

// it would be perfect to use Decorator design pattern and make different modifiers to soldiers
// eg HaveMachinegun, OperatesTank, MarineTraining
public class Soldier {
    // Idk if every soldier should have a dictionary or just a number
    // and dictionary would have a general
    // Whose responsility is to remember that and limit max stopien
    //
    // private Dictionary<String, Integer> DictionaryStopnie;
    // szeregowy : 1
    // kapral    : 2
    // kapitan   : 3
    // major     : 4


    private String name;
    private int stopien = 1;
    private int experience = 1;
    private boolean isAlive = true;
    private final int MAX_STOPIEN = 4;

    public Soldier(){

    }

    public Soldier(String[] load){
        if(load.length != 4){
            // error
            this.name = "Error";
            this.stopien = 0;
            this.experience = 0;
            this.isAlive = false;
        }
        else {
            this.name = load[0];
            this.stopien = Integer.valueOf(load[1]);
            this.experience = Integer.valueOf(load[2]);
            this.isAlive = Boolean.valueOf(load[3]);
        }
    }

    public Soldier(int stopien){
        this.stopien = stopien;
        this.name = "NoName";
    }

    public Soldier(String name, int stopien, int experience){
        this.name = name;
        this.stopien = stopien;
        this.experience = experience;
    }

    public void ChangeExperience(int ammount){
        if(experience + ammount <= 0){
            isAlive = false;
            experience = 0;
        }
        else if(experience + ammount == stopien * 5){
            if(stopien < MAX_STOPIEN){
                stopien += 1; // not if its max :
                experience = 1;
            }
            else{
                experience += ammount;
            }
        }
        else {
            experience += ammount;
        }
    }

    public int Strenght(){
        return experience * stopien;
    }

    public int GetStopien(){
        return stopien;
    }

    public boolean isAlive() {
        return isAlive;
    }

    private void death(){
        // kill or remove the soldier object
        // there is no dynamic memory alocation in java
        // so all that can be done is null ify all references
    }

    @Override
    public String toString() {
        return "Soldier "+ name +"{" +
                "stopien=" + stopien +
                ", experience=" + experience +
                ", isAlive=" + isAlive +
                '}';
    }

    public ArrayList<String> Save() {
        ArrayList<String> result = new ArrayList<>();
        result.add(name);
        result.add(String.valueOf(stopien));
        result.add(String.valueOf(experience));
        result.add(String.valueOf(isAlive));
        return result;
    }
}
