// Значения элементов двумерного массива из m строк и n столбцов скопировать в одномерный массив размером  m * n. Копирование проводить:
// а) по строкам начиная с первой (а в ней — с крайнего левого элемента);
// б) по столбцам начиная с первого (а в нем — с самого верхнего элемента)
/*
void Zadacha()
{
    Console.Clear();
    int rows = int.Parse(Console.ReadLine());
    int columns = int.Parse(Console.ReadLine());
    Console.WriteLine();
    int[,] matrix = new int[rows, columns];
    int[] array = new int[rows * columns];

    FillMatrix(matrix, rows, columns);
    PrintMatrix(matrix, rows, columns);
    FillArrayRows(array, matrix, rows, columns);
    Console.WriteLine("Одномерный массив через строку: [" + string.Join(", ", array) + "]");
    FillArrayColumns(array, matrix, rows, columns);
    Console.WriteLine();
    Console.WriteLine("Одномерный массив через столбец: [" + string.Join(", ", array) + "]");
}

int[,] FillMatrix(int[,] matrix, int rows, int columns)
{
    Random rand = new Random();
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            matrix[i, j] = rand.Next(0, 10);
        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix, int rows, int columns)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            Console.Write(matrix[i, j] + "\t");
        }
        Console.WriteLine();
    }
}

int[] FillArrayRows(int[] array, int[,] matrix, int rows, int columns)
{
    int index = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            array[index] = matrix[i, j];
            index++;
        }
    }
    return array;
}

int [] FillArrayColumns(int[] array, int[,] matrix, int rows, int columns)
{
    int index = 0;
    for (int j = 0; j < columns; j++)
    {
        for (int i = 0; i < rows; i++)
        {
            array[index] = matrix[i, j];
            index++;
        }
    }
    return array;
}

Zadacha();
*/
// Дан двумерный массив размером n n Сформировать:
// а) одномерный массив из элементов заданного массива, расположенных над главной диагональю;
// б) одномерный массив из элементов заданного массива, расположенных под главной диагональю;
// в) одномерный массив из элементов заданного массива, расположенных над побочной диагональю;
// г) одномерный массив из элементов заданного массива, расположенных под побочной диагональю.


void Zadacha()
{
    Console.Clear();
    int rows = int.Parse(Console.ReadLine());
    int columns = int.Parse(Console.ReadLine());
    Console.WriteLine();
    int[,] matrix = new int[rows, columns];

    FillMatrix(matrix, rows, columns);
    PrintMatrix(matrix, rows, columns);
/*
    int[] array1 = new int[CountArray1(matrix, rows, columns)];
    FillArray1(array1, matrix, rows, columns);
    Console.WriteLine("Одномерный массив над главной диагональю: [" + string.Join(", ", array1) + "]");
    Console.WriteLine();
*/
    int[] array2 = new int[CountArray2(matrix, rows, columns)];
    FillArray2(array2, matrix, rows, columns);
    Console.WriteLine("Одномерный массив над побочной диагональю: [" + string.Join(", ", array2) + "]");
}

int[,] FillMatrix(int[,] matrix, int rows, int columns)
{
    Random rand = new Random();
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            matrix[i, j] = rand.Next(0, 10);
        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix, int rows, int columns)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            Console.Write(matrix[i, j] + "\t");
        }
        Console.WriteLine();
    }
}
/*
int CountArray1(int[,] matrix, int rows, int columns)
{
    int count = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (i < j) count++;
        }
    }
    return count;
}

int[] FillArray1(int[] array, int[,] matrix, int rows, int columns)
{
    int index = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (i < j)
            {
                array[index] = matrix[i, j];
                index++;
            }
        }
    }
    return array;
}
*/

int CountArray2(int[,] matrix, int rows, int columns)
{
    int count = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (i + j < columns - 1) count++;
        }
    }
    return count;
}

int[] FillArray2(int[] array, int[,] matrix, int rows, int columns)
{
    int index = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (i + j < columns - 1)
            {
                array[index] = matrix[i, j];
                index++;
            }
        }
    }
    return array;
}
Zadacha();