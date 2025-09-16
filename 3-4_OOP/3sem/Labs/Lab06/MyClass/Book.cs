using System;

namespace MyClass
{
    internal class Book
    {
        private string author;
        private string title;
        private string publisher;
        private int pages;
        private int year;

        private static double price = 9;

        static Book()
        {
            price = 10;
        }

        public Book() { }
        public Book(string author, string title, string publisher, int pages, int year)
        {
            this.author = author;
            this.title = title;
            this.publisher = publisher;
            this.pages = pages;
            this.year = year;
        }
        public Book(string author, string title)
        {
            this.author = author;
            this.title = title;
        }

        public void SetBook(string author, string title, string publisher, int pages, int year)
        {
            this.author = author;
            this.title = title;
            this.publisher = publisher;
            this.pages = pages;
            this.year = year;
        }

        public static void SetPrice(double price)
        {
            Book.price = price;
        }

        public void Show()
        {
            Console.WriteLine(
                "\nКнига\n Автор: {0}\n Название: {1}\n Издатель: {2}\n Год издания: {3}\n {4} стр.\n Стоимость аренды: {5}\n",
                this.author, this.title, this.publisher, this.year, this.pages, Book.price
            );
        }

        public double PriceBook(int s)
        {
            return s * price;
        }
    }
}
