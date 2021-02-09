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
			else
			{
				c += 0;
				b = 1;
			}
        }

        
		for(Person p : people)
			{
				if (p == "Don") {
					sendAlert();
					break;
				}
				if (p == "John") {
					sendAlert();
					break;
				}
			}


        
		while(true){
            if (p == "Don") {
                sendAlert();
                break;
            }
            if (p == "John") {
                sendAlert();
                break;
            }
        }

        
		while(true){
            if (p == "Don") {
                sendAlert();
                break;
            }
            if (p == "John") {
                sendAlert();
                break;
            }

        }
	}
}
