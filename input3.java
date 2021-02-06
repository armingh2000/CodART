class Example extends Ex
{
    void printG(){
       print(this.g);
       printG();
       A.printG();
       A a = new A();
       Example c = new Example();
       c.printG();
       a.printG();
       a.g = 2;
       c.g = 3;
       l = A :: printG;
       d = c :: printG;
   }

}


abstract class Ex{
    void printG(){
        return;
    }
}