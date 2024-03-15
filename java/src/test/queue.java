package test;
import java.util.NoSuchElementException;
public class queue {

    private static int MAX_QUEUE_SIZE = 10;
    private int rear, front, size;
    private int[] data = new int[MAX_QUEUE_SIZE];

    public queue(){
        front=rear=size=0;
    }

    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size==0;
    }

    public void add(int item){
        rear=(rear+1) % data.length;
        data[rear] = item;
        size++;
    }

    public int pop(){
        if(isEmpty()) throw new NoSuchElementException();
        front=(front+1)%data.length;
        int item=data[front];
        data[front]=0;
        size--;
        return item;
    }

    public int peek(){
        if(isEmpty()) throw new NoSuchElementException();
        return data[front];
    }
}
