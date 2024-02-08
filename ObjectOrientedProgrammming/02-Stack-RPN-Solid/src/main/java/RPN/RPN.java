package RPN;
//import SolveRPN.java
/* zgodnosc z solid*/
import RPN.SolveRPN;


import jdk.jshell.spi.ExecutionControl.NotImplementedException;
//import java.util.EmptyStackException;
import RPN.Exceptions.*;

public class RPN {
    private String Equation;


    public RPN(String equation) {
        this.Equation = equation;
    }

    public RPN() {
        this.Equation = null;
    }

    public void SetEquation(String Equation){
        this.Equation = Equation;
    }

    public String getEquation(){
        return Equation;
    }

    public int Value() throws main.java.RPN.Exceptions.UnknownOperationException, main.java.RPN.Exceptions.InvalidEquationException, NotImplementedException {
        SolveRPN result = new SolveRPN(Equation);
        return result.SolveItself();
    }

    // SolveRPN.SolveItself was here

}
