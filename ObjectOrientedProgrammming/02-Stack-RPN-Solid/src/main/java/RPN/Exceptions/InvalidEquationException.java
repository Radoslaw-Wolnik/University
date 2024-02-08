package main.java.RPN.Exceptions;
// used in SolveRPN.java -- > RPN.java

public class InvalidEquationException extends Exception {
    public InvalidEquationException(String message) {
        super(message);
    }
    public InvalidEquationException() {
        super();
    }
}
