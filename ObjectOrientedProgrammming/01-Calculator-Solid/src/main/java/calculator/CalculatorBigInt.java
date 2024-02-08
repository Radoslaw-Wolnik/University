package calculator;

import static java.lang.Integer.MAX_VALUE;
import static java.lang.Math.floor;

import java.math.BigInteger;

public class CalculatorBigInt extends Calculator {


    private int state = 0;
    private int memory;

    public CalculatorBigInt(){
        setState(0);
    }

    public CalculatorBigInt(int state){
        setState(state);
    }

    public CalculatorBigInt(double state){
        setState((int) floor(state));
    }

    public CalculatorBigInt(String a) {
        setState(0);
    }

    public void add(int value){
        BigInteger val = new BigInteger(String.valueOf(value));
        BigInteger st = new BigInteger(String.valueOf(getState()));
        BigInteger res;
        res = st.add(val);
        BigInteger max = new BigInteger(String.valueOf(MAX_VALUE));
        int compare = max.compareTo(res); // 0 - equal; 1 if max is bigger then res; -1 otherwise
        //System.out.println("Biggy");
        if (1 == compare){
            setState(getState() + value);
        }
    }

    public void multi(int value){
        BigInteger val = new BigInteger(String.valueOf(value));
        BigInteger st = new BigInteger(String.valueOf(getState()));
        BigInteger res;
        res = st.multiply(val);
        BigInteger max = new BigInteger(String.valueOf(MAX_VALUE));
        int compare = max.compareTo(res);
        //System.out.println("Biggy");
        if(1 == compare){
            setState(getState() * value);
        }
    }


}
