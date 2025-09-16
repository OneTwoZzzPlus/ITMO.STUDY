using System;
namespace Utils
{
    class Utils
    {
        public static int Greater(int a, int b)
        {
            if (a >  b) 
                return a;
            else 
                return b;
        }
        
        public static void Swap(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }

        public static bool Factorial(int n, out int answer)
        {
            int f = 1;
            bool ok = true;
            try
            {
                checked
                {
                    for (int k = 2; k <= n; ++k)
                    {
                        f *= k;
                    }
                }
            }
            catch (Exception)
            {
                f = 0;
                ok = false;
            }
            answer = f;
            return ok;
        }
    }
}
