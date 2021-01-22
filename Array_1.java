public class Array_1 {
    public static void main(String[] args) {
        int[] intArray = new int[30];

        for (int i = 0; i < intArray.length; i++) {
            intArray[i] = 1001 + i;
        }

        String[] remainders = new String[4];
        remainders[0] = "Zero";
        remainders[1] = "One";
        remainders[2] = "Two";
        remainders[3] = "Three";

        for (int i : intArray) {
            System.out.println(remainders[i % 4]);
        }
    }
}
