// Package RPN
// import Stack.java
// HashMap

import jdk.jshell.spi.ExecutionControl.NotImplementedException;
import java.util.HashMap;


public class SolveOperation {
    private final Stack stos;
    private final String operation;
    private final HashMap<String, Integer> dictionary = new HashMap<>(){{
        put("+", 1);
        put("-", 2);
        put("*", 3);
        put("×", 3);
        put("/", 4);
    }};

    public SolveOperation(Stack stos, String operation){
        this.stos = stos;
        this.operation = operation;
    }


    private int Addition() {
        int a, b;
        b = stos.pop();
        a = stos.pop();
        return a + b;
    }
    private int Subtraction() {
        int a, b;
        b = stos.pop();
        a = stos.pop();
        return a - b;
    }
    private int Multiplication() {
        int a, b;
        b = stos.pop();
        a = stos.pop();
        return a * b;
    }
    private int Division() {
        int a, b;
        b = stos.pop();
        a = stos.pop();
        return a / b;
    }



    public int Value() throws UnknownOperationException, NotImplementedException{
        return this.SolveItself();
    }

    private int SolveItself() throws UnknownOperationException, NotImplementedException {
        if (dictionary.containsKey(operation)) {
            return switch (dictionary.get(operation)) {
                case 1 -> Addition();
                case 2 -> Subtraction();
                case 3 -> Multiplication();
                case 4 -> Division();
                default -> throw new NotImplementedException("Unexpected operation: " + dictionary.get(operation));
            };
        }
        else {
            throw new UnknownOperationException();
        }
    }


}
