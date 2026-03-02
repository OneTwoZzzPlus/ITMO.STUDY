using System;
using System.Collections.Generic;


namespace Tree
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 1 walking
            //Tree t = new Tree();
            //t.Fill(ref Tree.Node, new List<char>() { 'a', 'b', 'd', '.', '.', 'e', '.', '.', 'c', '.', 'f', '.', '.' });
            //t.PrintTree(Tree.Node);

            //Console.WriteLine("Direct order");
            //Tree.TreeWalkDirect(Tree.Node);
            //Console.WriteLine(string.Join(" ", Tree.list));
            //Tree.list.Clear();

            //Console.WriteLine("Reverse order");
            //Tree.TreeWalkReverse(Tree.Node);
            //Console.WriteLine(string.Join(" ", Tree.list));
            //Tree.list.Clear();

            //Console.WriteLine("The final order");
            //Tree.TreeWalkFinal(Tree.Node);
            //Console.WriteLine(string.Join(" ", Tree.list));
            //Tree.list.Clear();

            // 2 calculator
            Tree t = new Tree();
            t.Fill(ref Tree.Node, new List<char>() { 
                '/', '*', '+', '2', '.', '.', '3', '.', '.', '-', '7', 
                '.', '.', '4', '.', '.', '3', '.', '.' 
            });
            t.PrintTree(Tree.Node);

            Console.WriteLine("The final order");
            Tree.TreeWalkFinal(Tree.Node);
            Console.WriteLine(string.Join(" ", Tree.list));
            Tree.list.Clear();

            Console.WriteLine("The result of the expression is");
            Console.WriteLine(Tree.CalcTree(Tree.Node));
        }
    }
}
