/* Before refactoring (Original version) */
class A
{
    public int f; /* printF , printF, */
    public int g; /* printF, printG */
    public string h; /* printH */

    // Method 1
    void printF(int i)
    {
        this.f = i * this.f;
    }

    // Method 2
    void printF(float i){
        this.f = (int) (i * this.f);
        this.g = (int) (i * this.g);
    }

    // Method 3
     void printg(){
        print(this.g);
        printg();
        A.printg();
        A a = new A();
        a.printg();
        var b =  A :: printG;
        var c = a :: printG;
    }

    // Method 4
    void printH(){
        print(this.h);
    }
}
