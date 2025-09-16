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
            Book b4 = new Book("Эндрю Таненбаум", "Компьютерные сети", "Питер", 992, 2023, 404, false);
            Book b5 = new Book("Уильям Шоттс", "Командная строка Linux", "Питер", 480, 2017, 505, false);
            Magazine mag1 = new Magazine("О природе", 5, "Земля и мы", 2014, 1010, false);

            Book.RetSrok += new Book.ProcessBookDelegate(Operation.MethodHandler);

            b4.ReturnSrok = true;
            b5.ReturnSrok = true;

            Console.WriteLine("Книги возвращены в срок:");
            b4.ProcessPaperbackBooks(Operation.PrintTitle);
            b5.ProcessPaperbackBooks(Operation.PrintTitle);
        }
    }
}
