package com.company;

import java.util.Iterator;

public class Main {

    public static int countSyllables(String word)
    {
        //
        int count = 0;
        String vowels = "aeiouy";
        word = word.toLowerCase();
        int preIndex = -1;  // previous vowel index in the word
        int idxNext = -1; // next character index in the vowels
        for (int i = 0; i < word.length(); i++) {   // i is the current index
            char currChar = word.charAt(i);
            if ( i != word.length()-1 ) {
                char nextChar = word.charAt(i+1);
                idxNext = vowels.indexOf(nextChar);
            }
            int idx = vowels.indexOf(currChar);	    // check whether it is a vowel

            if (idx != -1) {    //count the syllable only if it is but with some exceptions
                // y exception: y in the first place
                if (currChar == 'y' && i == 0) {
                    // no change, next
                }
                // y exception:  y before the vowel
                else if (currChar == 'y' && i != word.length()-1 && idxNext != -1 ) {
                    // no change
                }
                // e exception: index = end and count!=0
                else if (currChar == 'e' && i == word.length()-1 && count!=0) {
                    //no change
                }
                // exception: if it is after the previous vowel, no count
                else if ( i!= 0 && i == preIndex + 1) {
                    // no change
                    preIndex = i;
                }
                // others count
                else {
                    count += 1;
                    preIndex = i;
                }
            }
        }

        return count;
    }

    // calculate the hourglass sum starting at (i,j)
    private static int calSum(int i, int j, int[][] arr){
        int sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1]+
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
        return sum;
    }

    public static void main(String[] args) {
        // write your code here
        String s = "Hacker";
        for (int i = 0; i < s.length(); i += 2) {
            System.out.print(s.charAt(i));
        }
        System.out.print(" ");
        for (int i = 1; i < s.length(); i += 2) {
            System.out.print(s.charAt(i));
        }

        // regular expression
        //String text = "words are what i write here:! 9976 yes just some random number. 0986.laq";
        String text = "Here is a series of test sentences. Your program should "
                + "find 3 sentences, 33 words, and 49 syllables. Not every word will have "
                + "the correct amount of syllables (example, for example), "
                + "but most of them will.";
        String[] words = text.split("[0-9,\\W]+");
        for (int i = 0; i < words.length; i++) {
            System.out.println(words[i]);
        }
        System.out.println(words.length);

        int numTotal = 0;
        for (int i = 0; i < words.length; i++) {
            System.out.println(words[i]);
            numTotal += countSyllables(words[i]);
            System.out.println(countSyllables(words[i]));
        }
        System.out.println("total syllables: " + numTotal);


        String[] sentences = text.split("[.!?]+");
        for (int i = 0; i < sentences.length; i++) {
            System.out.println(sentences[i]);
        }
        System.out.println(sentences.length);

        double result = (double) 2/3;
        System.out.println(result);



        /* Binary Numbers hackerrank
        *
        * the maximum number of consecutive 1s in the binary form.
        */
        System.out.println("Binary number task:");
        int n = 1;

        String binary = Integer.toBinaryString(n);
        int count = 0;
        if (binary.equals("0")) {
            System.out.println(count);
        }
        else {
            String[] con1 = binary.split("0+");
            if(con1 != null) {
                for (String str: con1) {
                    int size = str.length();
                    if(size > count) {
                        count = size;
                    }
                }
            }
        }
        System.out.println(count);

        // hourglass
        System.out.println("Hour Glass task");
        int[][] arr = new int[3][3];
        arr[0][0] = 2;
        arr[0][1] = 4;
        arr[0][2] = 4;
        arr[1][1] = 2;
        arr[2][0] = 1;
        arr[2][1] = 2;
        arr[2][2] = 4;
        int sum = calSum(0, 0, arr);

        System.out.println(sum);


    }

}
