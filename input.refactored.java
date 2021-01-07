/* Before refactoring (Original version) */
class A
{
    public int f; /* printF , printF, */
    public int gg; /* printF, printG */
    public string h; /* printH */

    // Method 1
    void printF(int i)
    {
        this.f = i * this.f;
    }

    // Method 2
    void printF(float i){
        this.f = (int) (i * this.f);
        this.gg = (int) (i * this.gg);
    }

    // Method 3
    void printG(){
        print(this.gg);
    }

    // Method 4
    void printH(){
        print(this.h);
    }
}
