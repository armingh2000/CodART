public class Main {
	public static void main(String[] people) {
        bool found = true;
		for(Person p : people){
			if (!found) {
				if (p == "Don") {
					sendAlert();
					found = true;
				}
				if (p == "John") {
					sendAlert();
					found = true;
				}
			}
        }

        bool found2 = true;
		for(Person p : people)
			if (!found2) {
				if (p == "Don") {
					sendAlert();
					found2 = true;
				}
				if (p == "John") {
					sendAlert();
					found2 = true;
				}
			}


        bool found3 = true;
		while(found3){
            if (p == "Don") {
                sendAlert();
                found3 = true;
            }
            if (p == "John") {
                sendAlert();
                found3 = true;
            }
        }

        bool found4 = false;
		while(!found4){
            if (p == "Don") {
                sendAlert();
                found4 = true;
            }
            if (p == "John") {
                sendAlert();
                found4 = true;
            }

        }
	}
}
