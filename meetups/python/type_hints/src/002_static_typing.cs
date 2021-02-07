using System;

public class Program
{
    public static void Main()
    {
        int c = 5;
        c = "string";  // Compilation error (line 8, col 7): Cannot implicitly convert type 'string' to 'int'
    }
}
