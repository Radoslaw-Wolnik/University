package Stack;
import java.util.EmptyStackException;

public class Stack {
    private int[] stacky;
    private int top = -1;

    // Construction site
    public Stack(){
        stacky = new int[11]; // Str stacky --> { null, null, ... , null } ; int stacky --> [I@adress ; int stacky = new int[11] --> [0 0 0 0 0 0 0 0 0 0 0 ...]
    }

    public Stack(int size){
        stacky = new int[size];
    }

    // private methods

    private void resize(){
        int[] Temp = new int[stacky.length*2];
        for (int i = 0; i < stacky.length; i++){  // System.arraycopy
            Temp[i] = stacky[i];
        }
        stacky = Temp;
    }

    // public methods

    public void push(int newEl){
        if (top < (stacky.length-1)){
            //System.out.println("top:" + top);
            //System.out.println("size:" + (size -1));
            top += 1;
            stacky[top] = newEl;
            //System.out.println("element: " + newEl + " on: " + top);
        }
        else{
            resize();
            //System.out.println("resized");
            push(newEl);
            //System.out.println("try again");
        }
    }

    public int pop() throws EmptyStackException {
        int result;
        if (top > -1){
            result = stacky[top];
            stacky[top] = 0; // default int is 0; Elements in primitive arrays can't be empty (null) so default int is inserted
            top -= 1;
        }
        else{
            throw new EmptyStackException();
        }
        return result;
    }

    public int peak(){ // Sneak Peak - get peak but don't pop it
        int result;
        if (top > -1){
            result = stacky[top];
        }
        else{
            throw new EmptyStackException();
        }
        return result;
    }
    public boolean isEmpty(){
        return top == -1;
    }



}
