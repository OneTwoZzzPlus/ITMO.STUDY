using System;
using System.Collections.Generic;
using System.Linq;

namespace Genetic
{
    class Generation
    {
        public int min_arg_value = 1;
        public int max_arg_value = 30;

        public static Random r = new Random();
        public Func<int[], int> f;
        public int[] args;
        public int ex_res;
        private int? real_res;

        public Generation(Func<int[], int> f, int[] args, int ex_res)
        {
            this.f = f;
            this.args = args;
            this.ex_res = ex_res;
        }

        public int RealResult
        {
            get
            {
                if (real_res == null)
                {
                    real_res = f(args);
                }
                return (int)real_res;
            }
        }

        public static Generation NewGen(Generation p1, Generation p2)
        {
            int n = p1.args.Count();
            int[] newArgs = new int[n];

            int x = r.Next(1, 4);

            for (int i = 0; i < n; i++)
            {
                newArgs[i] = i < x ? p1.args[i] : p2.args[i];
            }

            return new Generation(p1.f, newArgs, p1.ex_res);
        }

        public static Generation operator +(Generation p1, Generation p2)
        {
            return NewGen(p1, p2);
        }

        public void Mutation()
        {
            int n = args.Count();
            int imposter = r.Next(1, n);
            args[imposter] = r.Next(min_arg_value, max_arg_value + 1);

        }

        public int GetAc()
        {
            return Math.Abs((int)(ex_res - RealResult));
        }


        public static double SurvivalKoef(List<Generation> generations)
        {
            double sum = 0;
            foreach (Generation gen in generations)
            {
                sum += gen.GetAc();
            }
            return sum / generations.Count();
        }
    }
}
