using System;

namespace MyClass
{
    internal abstract class Item
    {
        protected long invNumber;
        protected bool taken;

        public Item(long invNumber, bool taken)
        {
            this.invNumber = invNumber;
            this.taken = taken;
        }

        public Item()
        {
            taken = false;
        }

        public long GetInvNumber()
        {
            return invNumber;
        }

        public bool IsAvailable()
        {
            return !taken;
        }

        private void Take()
        {
            taken = true;
        }
        public bool TakeItem()
        {
            if (IsAvailable())
            {
                Take();
                return true;
            }
            return false;

        }

        abstract public void Return();

        public virtual void Show()
        {
            Console.WriteLine(
                "Состояние единицы хранения\n Инвентарный номер: {0}\n Наличие: {1}",
                invNumber, !taken
            );
        }
    }
}
