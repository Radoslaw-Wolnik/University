// Package RPN
// import Stack.java
// import SolveOperation

import jdk.jshell.spi.ExecutionControl;
import jdk.jshell.spi.ExecutionControl.NotImplementedException;

public class SolveRPN {
    private final String Equation;

    public SolveRPN(String equation) {
        this.Equation = equation;

    }

    public int SolveItself() throws UnknownOperationException, InvalidEquationException, ExecutionControl.NotImplementedException {
        if (Equation == null){
            throw new InvalidEquationException("Equation = null");
        }

        String[] table = Equation.split(" ");
        Stack stos = new Stack(table.length);

        for (int i = 0; i < table.length; i++) { // would be nice to use diff name then Temp
            String Element = table[i];
            //System.out.println("element: " + Element);
            int number;
            try {
                number = Integer.parseInt(Element);
                stos.push(number);
            } catch (NumberFormatException e) {
                // operation or sth
                SolveOperation S;
                S = new SolveOperation(stos, Element);
                number = S.Value();
                stos.push(number);
            }
        }

        int result;
        result = stos.pop();
        //System.out.println(result);
        if (stos.isEmpty()) {
            return result;
        } else {
            throw new InvalidEquationException(Equation);
        }

    }


}
