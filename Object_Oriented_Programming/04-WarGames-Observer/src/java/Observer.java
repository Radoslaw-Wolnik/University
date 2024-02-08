import java.util.ArrayList;

public interface Observer {
    void update (String action, ArrayList<Soldier> status);
}
