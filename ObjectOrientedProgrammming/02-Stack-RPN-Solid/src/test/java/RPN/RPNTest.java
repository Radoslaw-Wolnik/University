// Package RPN

import jdk.jshell.spi.ExecutionControl.NotImplementedException;
import org.junit.Test;

import java.util.EmptyStackException;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

import RPN.RPN;

public class RPNTest {

    private RPN sut;

    // check creation

    @Test
    public void creation(){
        sut = new RPN("a");
        assertNotEquals("creation", null, sut);
    }

    @Test
    public void creationEquation(){
        sut = new RPN("2 7 + 3 / 14 3 - 4 × 2 / +");
        assertEquals("creation equation", "2 7 + 3 / 14 3 - 4 × 2 / +", sut.getEquation());
    }


    // Check Solutions
    private int TryCatch(RPN toCatch){ // better name
        int result = 0;
        try{
            result = toCatch.Value();
        }
        catch (UnknownOperationException u){
            System.out.println("Unknown operation solve");
        }
        catch (InvalidEquationException i){
            System.out.println("Invalid equation rpn");
        }
        catch (NotImplementedException n){
            System.out.println("not implemented in solve");
        }
        return result;
    }

    @Test
    public void testSolving0() {
        sut = new RPN("2 2 2 + *");
        int result;
        result = TryCatch(sut);
        assertEquals("solve 2 2 2 + *", 8, result);
    }

    @Test
    public void testSolving1(){
        sut = new RPN("2 7 + 3 / 14 3 - 4 × 2 / +");
        int result;
        result = TryCatch(sut);
        assertEquals("solve 2 7 + 3 / 14 3 - 4 × 2 / +", 25, result);
    }

    @Test
    public void testSolving2(){
        sut = new RPN("12 2 3 4 × 10 5 / + × +");
        int result;
        result = TryCatch(sut);
        assertEquals("solve 12 2 3 4 × 10 5 / + × +", 40, result);
    }

    @Test
    public void testSolving3(){
        sut = new RPN("5 1 2 + 4 × + 3 -");
        int result;
        result = TryCatch(sut);
        assertEquals("solve 5 1 2 + 4 × + 3 -", 14, result);  // did not count
    }

    @Test
    public void NegativeNum(){
        sut = new RPN("-2 2 * 2 +");
        int result;
        result = TryCatch(sut);
        assertEquals("solve eq with neg numbers", -2, result);
    }

    @Test
    public void NegativeNumbComplex(){
        sut = new RPN("2 -3 * 26 -14 7 / -5 * + +");
        int result;
        result = TryCatch(sut);
        assertEquals("solve eq 2 -3 * 26 -14 7 / -5 * + +", 30, result);
    }

    @Test
    public void NegativeNumberSolution(){
        sut = new RPN("13 2 + 26 -");
        int result;
        result = TryCatch(sut);
        assertEquals("Negative Number Solution", -11, result);
    }

    // Check Exceptions

    @Test
    public void MoreNumbersThenNeeded(){
        sut = new RPN("2 4 7 87 77 12 + - +");
        assertThrows(InvalidEquationException.class, () -> sut.Value());
    }

    @Test
    public void EmptyEquation(){
        sut = new RPN();
        assertThrows(InvalidEquationException.class, () -> sut.Value());
    }

    @Test
    public void TooMuchOperations(){
        sut = new RPN("2 -3 * 26 - 7 / -5 * + + - - - - -");
        assertThrows(EmptyStackException.class, () -> {
            sut.Value();
        });
    }

    @Test
    public void UnknownOperation(){
        sut = new RPN("4 2 ^");
        assertThrows(UnknownOperationException.class, () -> {
            sut.Value();
        });
    }

    @Test
    public void UnknownOperation2(){
        sut = new RPN("4 2 Aga");
        assertThrows(UnknownOperationException.class, () -> {
            sut.Value();
        });
    }


    @Test
    public void BrokenEquation(){
        sut = new RPN("2 - 2");
        assertThrows(EmptyStackException.class, () -> {
            sut.Value();
        });
    }


    @Test
    public void StackEmptyBrokenEquation(){
        sut = new RPN("13 2 + 26 - - 2");
        assertThrows(EmptyStackException.class, () -> {
            sut.Value();
        });
    }




}
