using System;
namespace MyClass
{
    class Operation
    {
        public static void PrintTitle(Book book)
        {
            book.Show();
        }

        public static void MethodHandler(Book book)
        {
            Console.WriteLine("Книга {0} сдана в срок.", book.ToString());
        }

    }
}
