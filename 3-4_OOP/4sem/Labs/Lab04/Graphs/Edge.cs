using System.Collections.Generic;

namespace Graphs
{
    public class Edge
    {
        public int I { get; set; }
        public int J { get; set; }
        public int Weight { get; set; }

        public Edge(int i, int j, int weight)
        {
            I = i; 
            J = j; 
            Weight = weight;
        }

        public override string ToString()
        {
            return "Edge (" + I + ", " + J + "): weight = " + Weight;
        }

        public bool Check(List<HashSet<int>> components)
        {
            HashSet<int> compI = null;
            HashSet<int> compJ = null;

            foreach (var comp in components)
            {
                if (comp.Contains(I)) compI = comp;
                if (comp.Contains(J)) compJ = comp;
            }

            // Случай 1: обе вершины ещё не входят ни в одну компоненту
            if (compI == null && compJ == null)
            {
                components.Add(new HashSet<int> { I, J });
                return true;
            }
            // Случай 2: только I уже в какой-то компоненте
            else if (compI != null && compJ == null)
            {
                compI.Add(J);
                return true;
            }
            // Случай 3: только J уже в компоненте
            else if (compI == null && compJ != null)
            {
                compJ.Add(I);
                return true;
            }
            // Случай 4: обе вершины уже в компонентах
            else // compI != null && compJ != null
            {
                if (compI == compJ)
                {
                    // Ребро замыкает цикл
                    return false;
                }
                else
                {
                    // Объединяем две разные компоненты
                    compI.UnionWith(compJ);
                    components.Remove(compJ);
                    return true;
                }
            }
        }
    }
}
