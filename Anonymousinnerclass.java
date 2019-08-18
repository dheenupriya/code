/*has no name
can be instantiated only once
is usually declared inside a method or a code block ,a curly braces ending with semicolon.
is accessible only at the point where it is defined.
does not have a constructor simply because it does not have a name
cannot be static
 */
abstract class B
{
    public abstract void fun();
}
public class Anonymousinnerclass{
    public static void main(String args[])
    {
        B a=new B(){
            public void fun()
            {System.out.println("Anonymous");
            }
        };
        a.fun();
    }
}