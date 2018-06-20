using CSharpSolutions.Solutions;
using System;

namespace CSharpSolutions
{
    class Program
    {
        static void Main(string[] args)
        {
            ISolution problem = new pe002();
            problem.Run();

            Console.WriteLine("Execution Complete");
            Console.Read();
        }
    }
}
