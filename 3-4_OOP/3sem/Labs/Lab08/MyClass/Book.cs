using System;

namespace MyClass
{
    class Book : Item
    {
        private string author;
        private string title;
        private string publisher;
        private int pages;
        private int year;
        private bool returnSrok;

        private static double price = 9;

        static Book()
        {
            price = 10;
        }

        public Book() { }
        public Book(string author, string title, string publisher, int pages, int year, long invNumber, bool taken) : base(invNumber, taken)
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

        public double PriceBook(int s)
        {
            return s * price;
        }

        public override void Show()
        {
            Console.WriteLine(
                "\nКнига\n Автор: {0}\n Название: {1}\n Издатель: {2}\n Год издания: {3}\n {4} стр.\n Стоимость аренды: {5}",
                author, title, publisher, year, pages, price
            );
            base.Show();
        }

        public void ReturnSrok()
        {
            returnSrok = true;
        }

        public override void Return()
        {
            taken = returnSrok;
        }
    }
}
