#include <iostream>
#include <cstdlib>   //for exit 
#include <cmath>
#include <complex>

using namespace std;
 
int addition(int num1,int num2);
int substraction(int num1,int num2);
int multiplication(int num1,int num2);
int division(int num1,int num2);
int factorial(int num1,char operation);
double power(double base, int exponent);
int square(int num1);
int cube(int num1);
int squareroot(int num1);
int permutation(int arr[]);   // to print all
int combination(int arr[]);
void quadraticRoots(double a, double b, double c);
void disign();


void quadraticRoots(double a, double b, double c) {
    // Calculate the discriminant
    double discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        // Two real roots
        double root1 = (-b + sqrt(discriminant)) / (2 * a);
        double root2 = (-b - sqrt(discriminant)) / (2 * a);
        cout << "Real roots: " << root1 << " and " << root2 << endl;
    } else if (discriminant == 0) {
        // One real root (repeated)
        double root = -b / (2 * a);
        cout << "Repeated real root: " << root << endl;
    } else {
        // Complex roots
        complex<double> root1 = (-b + sqrt(-discriminant)*1i) / (2 * a);
        complex<double> root2 = (-b - sqrt(-discriminant)*1i) / (2 * a);
        cout << "Complex roots: " << root1 << " and " << root2 << endl;
    }
}

int addition(int num1,int num2){
    return num1+num2;
}
int substraction(int num1,int num2){
    return num1-num2;
}

int multiplication(int num1,int num2){
    return num1*num2;
}

int division(int num1,int num2){
    return num1/num2;
}


int factorial(int num1,char operation){
   int result = 1;
    if (num1 == 0) {
        return 1; // Factorial of 0 is 1
    } else {
        for (int i = 1; i <= num1; i++) {
            result *= i;
        }
    }
    return result;
}

int squareroot(int num1){
    float squar_root= sqrt(num1);

    return squar_root;
}

double power(double base, int exponent) {
    double result = 1.0;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

int square(int num1){
    return (num1*num1);
}

int cube(int num1){
    return (num1*num1*num1);
}


void disign(){
     
cout<<"-----------------------------------------------------------------------------------------------\n\n";
}




int main(){

   
    int n;
    int num1,num2;
    char operation;
    disign();  
    cout<<"                              Scientific calculator\n\n";

    disign();     
    
    while(1){
    cout<<"\nEnter chioce\n\n";
    
    cout<<"1.Addition           2.Substraction         3.Multiplication\n";
    cout<<"4.Division           5.factorial            6.power\n";
    cout<<"7.square             8.cube                 9.squareroot\n";
    cout<<"10.permutation       11.combination         12.quadraticRoots\n";
    cout<<"0.quit program.\n";
    // cout<<"00.ToContinue"
    cin>>n;
    disign();
   switch (n)
   {

    case 1:
    int add;
        cout<<"Enter operation\n";
        cin>>num1>>operation>>num2;
        cout<<addition(num1, num2);
        
    
        break;

    case 2:
        int sub;
        cout<<"Enter operation\n";
        cin>>num1>>operation>>num2;
        cout<<substraction(num1,num2);
       
        break;

    case 3:
        int mul;
        cout<<"Enter operation\n";
        cin>>num1>>operation>>num2;
        cout<<multiplication(num1,num2);
        
        break;

    case 4:
        int div;
        cout<<"Enter operation\n";
        cin>>num1>>operation>>num2;
        cout<<division(num1,num2);
        
        break;

    case 5:
        num1;
        char operation;
        cout<<"Enter num! (eg. 8!)";
        cin>>num1>>operation;
        cout<< factorial(num1,operation);
        break;


    case 6:
          double base;
          int exponent;
          cout<<"Enter base: ";
          cin>>base;
          cout<<"Enter exponent";
          cin>>exponent;
          cout<<power(base, exponent);
        break;

    case 7:
          num1;
          cout<<"Enter number: ";
          cin>>num1;
          cout<<square(num1);
        break;

    case 8:
         cout<<"Enter number: ";
         cin>>num1;
         cout<<cube(num1);
        break;

    case 9:
    
           cout<<"Enter number: ";
           cin>>num1;
           cout<<squareroot(num1);
           break;
    case 10:
           break;
    case 11:
           break;
    case 12:
          double a;
          double b;
          double c;
          cout<<"Enter values/n a:";
          cin>>a;
          cout<<"b: ";
          cin>>b;
          cout<<"c: ";
          cin>>c;
    quadraticRoots(a,b,c);
            break;
    case 0:
          exit(0);
          break;

   default:
          cout<<"Invalid input";
          break;
   }
}
   


    return 0;
}
