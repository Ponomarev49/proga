int[] num = { 3, -1, 2, 5, -100, 0 };
var highZero = from p in num where p > 0 select p;
Console.WriteLine("Числа больше нуля");
foreach(int number in highZero)
{
    Console.Write($"{number}\t");
}
Console.WriteLine();
var lessZero = from p in num where p < 0 select p;
Console.WriteLine("Числа меньше нуля");
foreach(int number in lessZero)
{
    Console.Write($"{number}\t");
}
Console.WriteLine();

Console.WriteLine("Произведение ненулевых");
var proiz= from p in num where p !=0 select p;
int otv = 1;
foreach(int number in proiz)
{
    otv*=number;
}
Console.WriteLine(otv);

Console.WriteLine("Сумма четных");
var sum= (from p in num where p%2==0 select p);
Console.WriteLine(sum.Sum());
