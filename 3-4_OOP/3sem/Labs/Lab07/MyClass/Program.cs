using System;
namespace MyClass
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Lab06
            // Book b1 = new Book("Стивен Хокинг", "Краткая история времени", "АСТ МОСКВА", 320, 2022);
            // Book b2 = new Book("Джордж Оруэл", "1984", "АЗБУКА", 352, 2024);

            // Упражнение 1
            //Console.WriteLine("===== УПРАЖНЕНИЕ 1 =====\n");
            //Item item1 = new Item();
            //item1.Show();

            // Упражнение 2
            Console.WriteLine("\n===== УПРАЖНЕНИЕ 2 =====");
            Book b2 = new Book("Джордж Оруэл", "1984", "АЗБУКА", 352, 2024, 101, false);
            b2.TakeItem();
            b2.Show();
            Magazine mag1 = new Magazine("О природе", 5, "Земля и мы", 2014, 303, false);
            mag1.Show();

            // Упражнения 3 - 4
            Console.WriteLine("\n===== УПРАЖНЕНИЯ 3 - 4 =====\n");
            Console.WriteLine("Тестирование полиморфизма");
            Item it;

            it = b2;
            it.TakeItem();
            it.Return();
            it.Show();

            it = mag1;
            it.TakeItem();
            it.Return();
            it.Show();
        }
    }
}
