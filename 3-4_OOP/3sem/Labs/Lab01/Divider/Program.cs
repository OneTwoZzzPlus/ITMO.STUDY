using System;

namespace Divider
{
    internal class DivideIt
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Enter the 1st integer");
                string temp = Console.ReadLine();
                int i = Convert.ToInt32(temp);
                Console.WriteLine("Enter the 2nd integer");
                temp = Console.ReadLine();
                int j = Convert.ToInt32(temp);
                int k = i / j;
                Console.WriteLine("Result = {0}", k);
            }
            catch (FormatException e)
            {
                Console.WriteLine("An format exception was thrown: {0}", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("An exception was thrown: {0}", e.Message);
            }
        }   
    }
}
