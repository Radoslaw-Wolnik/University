/*
 * Generałowie posiadają początkową (ograniczoną) liczbę złotych monet.
 * Celem generała jest posiadanie największej i najlepiej wyszkolonej armii.0
 *
 * Generał może:
 *
 *     zarządzić manewry swojej armii (lub jej części), które powiększają doświadczenie uczestniczących w nich żołnierzy o 1;
 *     manewry kosztują: za każdego żołnierza biorącego udział w manewrach generał płaci wartość (liczbę monet) przypisaną do stopnia wojskowego
 *
 *     zaatakować drugiego generała:
 *     wygrywa generał, który posiada armię o większej łącznej sile;
 *     przegrany przekazuje 10% swojego złota wygrywającemu;
 *     każdy żołnierz z armii przegrywającej traci 1 punkt doświadczenia, a z wygrywającej zyskuje jeden;
 *     w przypadku remisu każdy generał musi rozstrzelać jednego swojego losowo wybranego żołnierza

 *     kupić żołnierzy;
 *     koszt żołnierza = 10 *(jego stopień);
 *     zakupieni żołnierze posiadają doświadczenie = 1
 * */

// Possible actions (to inform observers about) : battle; buySoldier; manoeuvre


import java.util.ArrayList;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Paths;
import java.nio.file.Files;

public class General {

    private int goldCoins = 0;
    private ArrayList<Soldier> army = new ArrayList<>();
    private ArrayList<Observer> observers = new ArrayList<>();

    public General(){

    }

    public General(int goldCoins){
        this.goldCoins = goldCoins;
    }

    public int TotalStrenght(){
        int result = 0;
        for (Soldier soldier : army){
            result += soldier.Strenght();
        }
        return result;
    }

    private void RemoveDead(){
        ArrayList <Soldier> dead = new ArrayList<Soldier>();
        for(int i = 0; i < army.size(); i++){
            if(!army.get(i).isAlive()){
                dead.add(army.get(i));
            }
        }
        for(Soldier soldier : dead){
            army.remove(soldier);
        }
    }

    private void KillRandSoldier(){
        int index = (int)(Math.random() * army.size());
        Soldier temp = army.get(index);
        army.remove(index);
    }

    private void ArmyExperienceChange(int experienceAmmount){
        for(Soldier soldier : army){
            soldier.ChangeExperience(experienceAmmount);
        }
    }

    private int GiveGold(int percentage){
        // percentage 0 - 100 ;; default 10
        int give = (int) Math.floor((double) goldCoins / percentage);

        goldCoins = goldCoins - give;

        return give;
    }

    public void Attack(General other){
        if(this.TotalStrenght() > other.TotalStrenght()){
            // other gives 10% zlota dla this
            this.goldCoins += other.GiveGold(10);
            // kazy zolniez armi this zyskuje 1 pkt doswiadczenia
            this.ArmyExperienceChange(1);
            // kazdy zolniez armi other traci 1 pkt doswiadczenia
            other.ArmyExperienceChange(-1);
            other.RemoveDead();

        } else if (this.TotalStrenght() < other.TotalStrenght()) {
            // this oddaje 10% zlota dla other
            other.goldCoins += this.GiveGold(10);
            // kazy zolniez armi other zyskuje 1 pkt doswiadczenia
            other.ArmyExperienceChange(1);
            // kazdy zolniez armi this traci 1 pkt doswiadczenia
            this.ArmyExperienceChange(-1);
            this.RemoveDead();
        } else {
            // losowy soilder z armii this ginie
            this.KillRandSoldier();
            // losowy soilder z armii other ginie
            other.KillRandSoldier();
        }
        this.NotifyObservers("battle");
        other.NotifyObservers("battle");
    }

    public void BuySoilder(int stopien){
        if(goldCoins - stopien * 10 >= 0){
            // add soilder to army
            Soldier temp = new Soldier(stopien);
            army.add(temp);
            temp = null; // <- deleting reference
            goldCoins -= stopien * 10;
            NotifyObservers("buySoldier");
        }
        else {
            // u have too little money to do this exception or sth
        }
    }

    // Manewry for specified soldiers
    public void Manewry(ArrayList<Soldier> SpecifiedSoldiers){
        for(Soldier soldier : SpecifiedSoldiers){
            if(goldCoins - soldier.GetStopien() < 0){
                continue; // or break
            }
            soldier.ChangeExperience(1);
            goldCoins -= soldier.GetStopien();
        }
        NotifyObservers("manoeuvre");
    }

    // Manewry for all soldiers
    public void Manewry(){
        for(Soldier soldier : army){
            if(goldCoins - soldier.GetStopien() < 0){
                continue; // or break
            }
            soldier.ChangeExperience(1);
            goldCoins -= soldier.GetStopien();
        }
        NotifyObservers("manoeuvre");
    }

    public void AddGold(int ammount){
        goldCoins += ammount;
    }

    public ArrayList<Soldier> getArmy() {
        return army;
    }

    public void AddSoldier(Soldier soldier){
        army.add(soldier);
    }

    @Override
    public String toString() {
        return army.toString();
    }

    public void SaveArmy(String filePath){
        // zapisuje stan armi do pliku
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            // Iterate through the array and write each element to the file
            for (Soldier soldier : army){
                String temp;
                temp = String.join(";", soldier.Save());
                writer.println(temp);
            }

            System.out.println("Army saved to file: " + filePath);
        } catch (IOException e) {
            // Handle exceptions, such as file not found or permission issues
            e.printStackTrace();
        }

    }
    public void LoadArmy(String filePath){
        // Delete all Soldiers  from army
        army.clear();
        // Try-with-resources to automatically close resources
        try {
            // Read all lines from the file into a List
            ArrayList<String> lines = (ArrayList<String>) Files.readAllLines(Paths.get(filePath));

            // Iterate through each line, split based on semicolon, and add to the army
            for (String line : lines) {
                String[] elements = line.split(";");
                Soldier tempSoldier = new Soldier(elements);
                army.add(tempSoldier);
            }
        } catch (IOException e) {
            // Handle exceptions, such as file not found or permission issues
            e.printStackTrace();
        }

    }

    // The Observer design pattern for secretaries
    public void AddObserver(Observer observer){
        observers.add(observer);
    }

    public void RemoveObserver(Observer observer){
        observers.remove(observer);
    }

    private void NotifyObservers(String action){
        for (Observer observer : observers){
            observer.update(action, army);
        }
    }

}
