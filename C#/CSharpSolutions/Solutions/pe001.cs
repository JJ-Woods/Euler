using System;
using System.Collections.Generic;
using System.Text;

namespace CSharpSolutions.Solutions
{
    //https://projecteuler.net/problem=1

    public class pe001 : ISolution
    {
        const int LIMIT = 1000;

        public void Run()
        {
            var sum = 0;

            for (int count1 = 0; count1 < LIMIT; count1++)
            {
                if (count1 % 3 == 0 || count1 % 5 == 0)
                {
                    sum += count1;
                }
            }

            Console.WriteLine($"The solution to problem 001 is {sum}");
        }

    }
}
