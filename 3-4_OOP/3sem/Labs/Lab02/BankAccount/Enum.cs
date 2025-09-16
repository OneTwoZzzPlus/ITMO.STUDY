using System;

namespace BankAccount
{
    public enum AccountType { Checking, Deposit }

    internal class Enum
    {
        static void Main(string[] args)
        {
            AccountType goldAccount, platinumAccount;
            goldAccount = AccountType.Checking;
            platinumAccount = AccountType.Deposit;

            Console.WriteLine("The Customer Account Type is {0}", goldAccount);
            Console.WriteLine("The Customer Account Type is {0}", platinumAccount);

        }
    }
}
