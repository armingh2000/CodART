public class Main {
	public static void main(String[] people) {
		boolean found = false;
		for (i = 0; i < count(people); i++) {
			if (!found) {
				if (people[i] == "Don") {
					sendAlert();
					found = true;
				}
				if (people[i] == "John") {
					sendAlert();
					found = true;
				}
			}
		}
	}
}
