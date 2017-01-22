using System;
namespace HelloWorld
{
    class DataProcess 
    {

        double getBias(){
             List<int> data_stand = new List<int>();
            string[] words;
            string line;
            while ((line = Console.ReadLine()) != null && line != "") {
                string[] words = line.splt(" ");
                if(words.Length>=6 && words[1]=='/muse/acc') data_stand.append(int.Parse(words[4]));
            }
            return bias = data_stand.Take().Sum()/data_stand.Length;
        }


        static void Main() 
        {
           double bias = getBias();

        }
    }
}
