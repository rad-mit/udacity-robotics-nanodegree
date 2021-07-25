#include <iostream>

using namespace std;

double w[] = { 0.6, 1.2, 2.4, 0.6, 1.2 };//You can also change this to a vector

//TODO: Define a  ComputeProb function and compute the Probabilities
double ComputeProb(double x, double y){
    return x/y;
}

int main()
{
    //TODO: Print Probabilites each on a single line:
    //P1=Value
    //:
    //P5=Value
    double W=0.0;
    for (int i=0; i<5; i++)  W+=w[i];
    for (int i=0; i<5; i++){
        cout << ComputeProb(w[i], W) << "\n";
    }
    return 0;
}
