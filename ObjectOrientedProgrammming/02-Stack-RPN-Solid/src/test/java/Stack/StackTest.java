// package Stack

import org.junit.*;


import java.util.Arrays; // .toString()
import java.util.EmptyStackException;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertThrows;
public class StackTest {

    Stack sut;

    @Before
    public void setup(){
        sut = new Stack();
    }

    @Test
    public void creationEmpty(){
        assertNotEquals("creation without arg", null, sut);
    }


    @Test
    public void creationInt(){
        sut = new Stack(7);
        assertNotEquals("created with defined size", null, sut);
    }


    // CHECK
    @Test
    public void testPushPop(){
        sut.push(1);
        int result;
        result = sut.pop();
        assertEquals("push pop", 1, result);
    }

    @Test
    public void PopEmpty(){
        sut = new Stack(7);
        assertThrows(EmptyStackException.class, () -> {
            sut.pop();
        });
    }

    @Test
    public void JustPush4(){
        int[] src = {12, 2, 3, 4};
        int[] result = new int[4];
        for(int i = 0; i < 4; i++){
            sut.push(src[i]);
        }
        for(int i = 0; i < 4; i++){
            result[i] = sut.pop();
        }
        assertEquals("Push 4 elements", "[4, 3, 2, 12]", Arrays.toString(result));
    }

    @Test
    public void PushOver(){
        sut = new Stack(3);
        int[] src = {12, 2, 3, 44, 20};
        int[] result = new int[5];
        for(int i = 0; i < 5; i++){
            sut.push(src[i]);
        }
        for(int i = 0; i < 5; i++){
            result[i] = sut.pop();
        }

        String check = "[20, 44, 3, 2, 12]";
        assertEquals("Push over the size", check, Arrays.toString(result));
    }

    @Test
    public void SneakPeak(){
        int[] src = {12, 2, 3, 44, 20};
        for(int i = 0; i < 5; i++){
            sut.push(src[i]);
        }
        int result;
        result = sut.peak();
        assertEquals("Push over the size", sut.pop(), result);
    }




}
