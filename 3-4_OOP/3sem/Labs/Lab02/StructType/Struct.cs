using System;

namespace StructType
{
    public enum AccountType { Checking, Deposite }
    public struct BankAccount
    {
        public long accNo;
        public decimal accBal;
        public AccountType accType;
    }
    internal class Struct
    {
        static void Main(string[] args)
        {
            BankAccount goldAccount;
            Console.Write("Enter account number: ");
            goldAccount.accNo = long.Parse(Console.ReadLine());
            //goldAccount.accNo = 333;
            goldAccount.accBal = (decimal)3400.00;
            goldAccount.accType = AccountType.Checking;

            Console.WriteLine("*** Account Summary ***");
            Console.WriteLine("Acct Number {0}", goldAccount.accNo);
            Console.WriteLine("Acct Type {0}", goldAccount.accType);
            Console.WriteLine("Acct Balance ${0}", goldAccount.accBal);
        }
    }
}
