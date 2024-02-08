package main.java.RPN.Exceptions;

// Package RPN
// used in SolveOperation.java -- > SolveRPN.java -- > RPN.java
public class UnknownOperationException extends Exception {
    public UnknownOperationException(String message) {
        super(message);
    }
    public UnknownOperationException() {
        super();
    }
}
