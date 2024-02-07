package kalkulator;


import java.lang.Math;

import static java.lang.Integer.MAX_VALUE;
import static java.lang.Math.floor;

public class Calculator {
    private int state = 0;
    private int memory;

    public Calculator(){
        setState(0);
    }

    public Calculator(int state){
        setState(state);
    }

    public Calculator(double state){
        setState((int) floor(state));
    }

    public Calculator(String a) {
        setState(0);
    }



    private void setState(int state){
        this.state = state;
    }


    public int getState(){
        return state;
    }

    public void setMemory(){
        memory = state;
    }

    public int getMemory() {
        return memory;
    }


    public void add(int value){
        double res, max = MAX_VALUE, st = state, val = value;
        res = st + val;

        if (res < max){
            setState(state + value);
        }
    }
    public void add(int a, int b){
        setState(a);
        add(b);
    }

    public void multi(int value){
        double res, max = MAX_VALUE, st = state, val = value;
        res = st * val;
        if(res < max){
            setState(state * value);}
    }

    public void multi(int a, int b){
        setState(a);
        multi(b);
    }

    public int div(int value) {
        //float delta = 0.001F;
        //    if(!(value > 0 - delta && value < delta)){
        //        setState(state/value);}
        //}
        if (value == 0){
            return 0;
        }

        int result;
        result = state%value;
        setState(state/value);
        return result;
    }

    public void div(int a, int b){
        setState(a);
        div(b);
    }

}
