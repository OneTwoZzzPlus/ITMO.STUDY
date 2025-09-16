using System;

namespace MyClass
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book();
            b1.SetBook("Стивен Хокинг", "Краткая история времени", "АСТ МОСКВА", 320, 2022);
            Book.SetPrice(12);
            b1.Show();
            Console.WriteLine("Итоговая стоимость аренды: {0} р.", b1.PriceBook(3));

            Book b2 = new Book("Джордж Оруэл", "1984", "АЗБУКА", 352, 2024);
            b2.Show();

            Book b3 = new Book("Бруно Латур", "Наука в действии");
            b3.Show();
        }
    }
}
