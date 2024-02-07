package kalkulator;

import org.junit.*;

import static java.lang.Integer.MAX_VALUE;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

public class TestCalculator {

    public Calculator sut;
    //bigCalculator
    public BigCalculator tus;
    /*@Before
    public void initial(){
        sut = new Calculator();
    }*/


    // CHECK CONSTRUCTION
    @Test
    public void creationNotEmpty(){
        sut = new Calculator();
        assertNotEquals("created", null, sut);
    }

    @Test
    public void creationString(){
        sut = new Calculator("ala am kota");
        assertEquals("creation with str", 0, sut.getState());
    }

    @Test
    public void creationDouble(){
        sut = new Calculator(7.7);
        assertEquals("created with 7.7", 7, sut.getState());
    }

    @Test
    public void creationInt(){
        sut = new Calculator(4);
        int result = sut.getState();
        assertEquals("created with int", 4, result);
    }


    // CHECK ADDITION
    @Test
    public void testAddOne(){
        // Arrange
        sut = new Calculator();
        // Act
        sut.add(1);
        // Assert
        assertEquals("0+1 = 1", 1, sut.getState());
    }

    @Test
    public void testAddTwoNum(){
        sut = new Calculator();
        sut.add(56, 67);
        int result = 123;
        assertEquals("Addition 56+67", result, sut.getState());
    }

    // CHECK MULTIPLICATION
    @Test
    public void MultiplyTwoNum(){
        sut = new Calculator();
        sut.multi(3, 2);
        int result = 6;
        assertEquals("3*2 = 6", result, sut.getState());
    }

    @Test
    public void MultiplyOneNum(){
        sut = new Calculator(4);
        sut.multi(2);
        int result = 4 * 2;
        assertEquals("4 * 2 = 8", result, sut.getState());
    }

    // CHECK DIVISION
    @Test
    public void DivByOneNum(){
        sut = new Calculator(4);
        sut.div(2);
        assertEquals("Division 4/2", 2, sut.getState());
    }

    @Test
    public void DivOddNum(){
        sut = new Calculator(7);
        sut.div(2);
        assertEquals("Division 7/2", 3, sut.getState());
    }

    @Test
    public void RestDiv(){
        sut = new Calculator(24);
        int result;
        result = sut.div(5);
        assertEquals("Rest from division 23/5", 4, result);
    }

    @Test
    public void DivByTwoNum(){
        sut = new Calculator(4);
        sut.div(20,4);
        assertEquals("Division 20/4", 5, sut.getState());
    }

    @Test
    public void DivByZero(){
        sut = new Calculator(34);
        sut.div(0);
        assertEquals("Division by zero", 34, sut.getState());
    }


    // CHECK MEMORY
    @Test
    public void MemoryDiv(){
        sut = new Calculator(4);
        sut.setMemory();
        sut.div(sut.getMemory());
        assertEquals("Division memory", 1, sut.getState(), 0.00001);
    }

    @Test
    public void MemoryAdd(){
        sut = new Calculator(6);
        sut.setMemory();
        //System.out.println(sut.getMemory());
        sut.add(sut.getMemory());
        assertEquals("Add memory", 12, sut.getState());
    }

    @Test
    public void MemoryMulti(){
        sut = new Calculator(4);
        sut.setMemory();
        sut.multi(sut.getMemory());
        assertEquals("Division memory", 16, sut.getState());
    }


    // CHECK RANGE
    @Test
    public void OverRangeAdd(){
        String binary;
        binary = Integer.toBinaryString(MAX_VALUE);
        sut = new Calculator(MAX_VALUE);
        int result = sut.getState();
        sut.add(100000);
        assertEquals(result, sut.getState());
    }

    @Test
    public void OverRangeAdd2(){
        sut = new Calculator(MAX_VALUE/2 + 10);
        int result = sut.getState();
        sut.add(MAX_VALUE/2 + 10);
        assertEquals(result, sut.getState());
    }

    @Test
    public void OverRangeMulti(){
        sut = new Calculator(MAX_VALUE);
        int result = sut.getState();
        sut.multi(2);
        assertEquals( result, sut.getState());
    }

    @Test
    public void OverRangeMulti2(){
        sut = new Calculator(MAX_VALUE/2 + 10);
        int result = sut.getState();
        sut.multi(MAX_VALUE/2 + 10);
        assertEquals(result, sut.getState());
    }


    //bigCalculator tests
    @Test
    public void BigtestAddOne(){
        tus = new BigCalculator(12);
        tus.add(10);
        assertEquals("12 + 10 = 22", 22, tus.getState());
    }

    @Test
    public void BigOverRangeAdd2() {
        tus = new BigCalculator(MAX_VALUE / 2 + 10);
        int result = tus.getState();
        tus.add(MAX_VALUE / 2 + 10);
        assertEquals(result, tus.getState());
    }

    @Test
    public void BigOverRangeMulti2(){
        tus = new BigCalculator(MAX_VALUE/2 + 10);
        int result = tus.getState();
        tus.multi(MAX_VALUE/2 + 10);
        assertEquals(result, tus.getState());
    }


    /*
    public void UnderRangeAdd(){
        sut = new Calculator(-10);
        sut.add(-MAX_VALUE);
        assertEquals( -10, sut.getState());
    }*/


}
