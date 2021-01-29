class C
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
     void printG(){
        print(this.g);
        printG();
        A.printg();
        A a = new A();
        C c = new C();
        c.printG();
        C.printG();
        a.printg();
        var b =  A :: printg;
        var d = a :: printg;
    }

    // Method 4
    void printH(){
        print(this.h);
    }
}/* Before refactoring (Original version) */
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
        printG();
        A.printg();
        A a = new A();
        a.printg();
        var b =  A :: printg;
        var c = a :: printg;
    }

    // Method 4
    void printH(){
        print(this.h);
    }
}
