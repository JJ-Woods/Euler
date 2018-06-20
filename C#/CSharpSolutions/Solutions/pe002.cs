using System;
using System.Collections.Generic;
using System.Text;

namespace CSharpSolutions.Solutions
{
    class pe002 : ISolution
    {
        const int LIMIT = 4000000;

        public void Run()
        {
            var fibNum1 = 1;
            var fibNum2 = 2;

            var sum = 0; //starting at two to include first matching number

            while (fibNum2 < LIMIT)
            {
                if (fibNum2 % 2 == 0)
                {
                    sum += fibNum2;
                }

                var temp = fibNum1 + fibNum2;
                fibNum1 = fibNum2;
                fibNum2 = temp;
            }

            Console.WriteLine($"The solution to problem 002 is {sum}");
        }
    }
}
