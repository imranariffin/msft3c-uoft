import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		while (in.hasNext()) {
			String[] names = in.nextLine().split(", ");
			System.out.println(names);
			String name1 = names[0];
			String name2 = names[1];
			
			System.out.println(name1);
			System.out.println(name2);
			System.out.println(isPottery(name1, name2));
		}
	}


	private static String isPottery(String name1, String name2) {
		int[] counter1 = new int[26];
		int[] counter2 = new int[26];

		char[] chars1 = name1.toLowerCase().toCharArray();
		char[] chars2 = name2.toLowerCase().toCharArray();

		for (char c: chars1) {
			if (c != '\"') {
				counter1[c - 'a']++;
			}
		}
		for (char c: chars2) {
			if (c != '\"') {
				counter2[c - 'a']++;
			}
		}
		
		for (int i = 0; i < 26; i++) {
			if (counter1[i] != counter2[i]) {
				return "Invalid Pattern";
			}
		}
		return "Valid Pattern";
	}
}
