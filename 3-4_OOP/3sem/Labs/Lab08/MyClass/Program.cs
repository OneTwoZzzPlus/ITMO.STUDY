using System;
namespace MyClass
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book("Стивен Хокинг", "Краткая история времени", "АСТ МОСКВА", 320, 2022, 101, false);
            Book b2 = new Book("Джордж Оруэл", "1984", "АЗБУКА", 352, 2024, 202, false);
            Book b3 = new Book("Бруно Латур", "Наука в действии", "ЕУ в СПб", 414, 2013, 303, false);
            Magazine mag1 = new Magazine("О природе", 5, "Земля и мы", 2014, 404, false);

            Item[] items = new Item[4];
            items[0] = b1;
            items[1] = b2;
            items[2] = b3;
            items[3] = mag1;

            Array.Sort(items);

            Console.WriteLine("Сортировка по инвертарному номеру");
            foreach (Item item in items) item.Show();
        }
    }
}
