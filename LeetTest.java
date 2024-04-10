import java.util.LinkedList;

import java.util.*;
class LeetTest{
    public static void main(String [] args){
        System.out.println("did those work ");
        //creating the linked list 
        LinkedList <Integer> l1 = new LinkedList<>();
        LinkedList <Integer> l2 = new LinkedList<>();
        int firstNum = 0 ; 


        l1.add(2);
        l1.add(4);
        l1.add(3);
        System.out.println(l1);

        l2.add(5);
        l2.add(6);
        l2.add(4);

        System.out.println(l2);

        System.out.println(makeReverse(l1) + " this is 1l REVERSE");
        

        System.out.println(makeReverse(l2) + " this is l2 REVERSE");
        

        int finalAnswer = linkToNum(l1) + linkToNum(l2);
        System.out.println(finalAnswer + " Final answer");

    

    }
    public static int linkToNum(LinkedList<Integer> l1){
        int firstNum = 0 ; 
        for ( int i = 0 ; i < l1.size() ; i++){   
            firstNum = firstNum * 10 + (int)l1.get(i);
        }
        return firstNum;
    }
    public static LinkedList makeReverse(LinkedList<Integer> l1){
        int size = l1.size();
        for (int i = 0 ; i < size/2; i++){
            int temp = l1.get(i);
            l1.set(i, l1.get(size - i -1 ));
            l1.set(size -i -1, temp);
            
        }
        return l1;
        
    }
}