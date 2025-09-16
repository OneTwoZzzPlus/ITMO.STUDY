using System;

namespace ArrayAnalizer
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] arr = Input();
            Output(arr);
            Help();
            char op; bool ok;
            while (true)
            {
                Console.Write("Введите команду: ");
                ok = char.TryParse(Console.ReadLine(), out op);
                if (!ok)
                {
                    Console.WriteLine("Неизвестная операция");
                    continue;
                }
                switch (op)
                {
                    case 'a': Console.WriteLine("Сумма всех элементов = {0}", Sum(arr)); break;
                    case 'b': Console.WriteLine("Среднее значение элементов = {0}", Medium(arr)); break;
                    case 'c': Console.WriteLine("Сумма положительных элементов = {0}", SumPositive(arr)); break;                        
                    case 'd': Console.WriteLine("Сумма отрицательных элементов = {0}", SumNegative(arr)); break;
                    case 'e': Console.WriteLine("Сумма элементов с нечетными номерами = {0}", SumOdd(arr)); break;
                    case 'f': Console.WriteLine("Сумма элементов с четными номерами = {0}", SumEven(arr)); break;
                    case 'g': Console.WriteLine("Индекс максимального элемента = {0}", MaxIndex(arr)); break;
                    case 'h': Console.WriteLine("Индекс минимального элемента = {0}", MinIndex(arr)); break;
                    case 'i': Console.WriteLine("Произведение = {0}", MinMaxProd(arr)); break;
                    case '?': Help(); break;
                    case '+': Output(arr); break;
                    case '0': return;
                    default: Console.WriteLine("Неизвестная операция"); break;
                }
            }
            
        }
        
        private static int[] Input()
        {
            int n = 0;
            bool ok = false;
            do
            {
                Console.Write("Введите длину массива: ");
                ok = int.TryParse(Console.ReadLine(), out n);
                if (!ok || n <= 0) Console.WriteLine("Должно быть положительное целое число!");
            }
            while (!ok || n <= 0);
            int[] arr = new int[n];
            Console.WriteLine("Построчно введите элементы массива.");
            int i = 0;
            while (i < arr.Length)
            {
                Console.Write("arr[{0}] = ", i);
                ok = int.TryParse(Console.ReadLine(), out int a);
                if (!ok)
                {
                    Console.WriteLine("Должно быть целое число!");
                    continue;
                }
                arr[i] = a;
                i++;
            }

            return arr;
        }

        private static void Help()
        {
            Console.WriteLine("Операции с массивом");
            Console.WriteLine("a - сумма всех элементов");
            Console.WriteLine("b - среднее значение элементов");
            Console.WriteLine("с - сумма положительных элементов");
            Console.WriteLine("d - сумма отрицательных элементов");
            Console.WriteLine("e - сумма элементов с нечетными номерами");
            Console.WriteLine("f - сумма элементов с четными номерами");
            Console.WriteLine("g - индекс максимального элемента");
            Console.WriteLine("h - индекс минимального элемента");
            Console.WriteLine("i - произведение всех элементов между max и min");
            Console.WriteLine("? - справка");
            Console.WriteLine("+ - вывод массива на экран");
            Console.WriteLine("0 - выход");
        }

        private static void Output(int[] arr)
        {
            foreach (int x in arr) Console.Write("{0} ", x);
            Console.WriteLine();
        }

        private static int Sum(int[] arr)
        {
            int sum = 0;
            foreach (int x in arr) sum += x;
            return sum;
        }

        private static double Medium(int[] arr)
        {
            return (double)Sum(arr) / arr.Length;
        }

        private static int SumPositive(int[] arr)
        {
            int sum = 0;
            foreach (int x in arr) if (x > 0) sum += x;
            return sum;
        }

        private static int SumNegative(int[] arr)
        {
            int sum = 0;
            foreach (int x in arr) if (x < 0) sum += x;
            return sum;
        }

        private static int SumEven(int[] arr)
        {
            int sum = 0;
            foreach (int x in arr) if (x % 2 == 0) sum += x;
            return sum;
        }

        private static int SumOdd(int[] arr)
        {
            int sum = 0;
            foreach (int x in arr) if (x % 2 == 1) sum += x;
            return sum;
        }

        private static int MaxIndex(int[] arr)
        {
            int max = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] > arr[max]) max = i;
            }
            return max;
        }

        private static int MinIndex(int[] arr)
        {
            int min = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] < arr[min]) min = i;
            }
            return min;
        }

        private static int MinMaxProd(int[] arr)
        {
            int min = MinIndex(arr);
            int max = MaxIndex(arr);
            int prod = 1;
            for (int i = min; i <= max; i++) prod *= arr[i];
            return prod;
        }
    }
}
