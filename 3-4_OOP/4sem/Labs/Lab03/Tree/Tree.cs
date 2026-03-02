using System;
using System.Collections.Generic;

namespace Tree
{
    public class Tree
    {
        public Tree Left;
        public Tree Right;
        public char Value;
        public bool flag = false;
        public static List<char> list = new List<char>();
        public static Tree Node;
        
        public Tree()
        {
            Node = null;
        }

        public Tree(Tree left, Tree right, char value)
        {
            Left = left;
            Right = right;
            Value = value;
        }

        public void Add(ref Tree node, char value)
        {
            if (node == null) {
                node = new Tree(null, null, value);
                flag = false;
            } 
            else if (node.Value != '.' && !flag)
            {
                if (node.Left != null)
                {
                    Add(ref node.Left, value);
                    if (!flag)
                    {
                        if (node.Right != null)
                        {
                            Add(ref node.Right, value);
                        }
                        else
                        {
                            node.Right = new Tree(null, null, value);
                            flag = true;        
                        }
                    }
                }
                else
                {
                    node.Left = new Tree(null, null, value);
                    flag = true;                
                }
            }
        }

        public void Fill(ref Tree node, List<char> chars)
        {
            for (int i = 0; i < chars.Count; i++)
            {
                flag = false;
                Add(ref node, chars[i]);
            }
        }

        public void PrintTree(Tree node)
        {
            if (node == null) return;
            if (node.Value != '.')
            {
                Console.WriteLine("value: {0}, left: {1}, right: {2}", node.Value, node.Left.Value, node.Right.Value);
            }
            PrintTree(node.Left);
            PrintTree(node.Right);
        }

        public static List<char> TreeWalkDirect(Tree node)
        {
            /* NLR */
            if (node.Value == '.') return new List<char>();
            
            list.Add(node.Value);
            TreeWalkDirect(node.Left);
            TreeWalkDirect(node.Right);

            return list;
        }

        public static List<char> TreeWalkFinal(Tree node)
        {
            /* LRN */
            if (node.Value == '.') return new List<char>();
            
            TreeWalkFinal(node.Left);
            TreeWalkFinal(node.Right);
            list.Add(node.Value);

            return list;
        }

        public static List<char> TreeWalkReverse(Tree node)
        {
            /* LNR */
            if (node.Value == '.') return new List<char>();
            var result = TreeWalkReverse(node.Left);
            result.Add(node.Value);
            result.AddRange(TreeWalkReverse(node.Right));
            list = result;
            return result;
        }

        public static int CalcTree(Tree node)
        {
            if (char.IsDigit(node.Value)) return node.Value;
            int a = CalcTree(node.Left);
            int b = CalcTree(node.Right);
            switch (node.Value)
            {
                case '+': return a + b;
                case '-': return a - b;
                case '*': return a * b;
                case '/': return a / b;
                default: return 0;
            }
        }

    }
}
