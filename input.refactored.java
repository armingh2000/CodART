public class Main {
	public static void main(String[] people) {
        bool found = false;
		for(Person p : people){
			if (!found) {
				if (p == "Don") {
					sendAlert();
					found = true;
				}
				else if (p == "John") {
					sendAlert();
					found = true;
				}
			}
			else {
			    x = 1;
			    c = 2;
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
            else if (p == "John") {
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
