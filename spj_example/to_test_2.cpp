#include <bits/stdc++.h>
using namespace std;
long long a, b;
// input two numbers
// print two numbers that has a sum of a + b
int main(int argc, char const *argv[]) {
    scanf("%lld%lld", &a, &b);
    printf("1 %lld\n", a + b - 1);
    return 0;
}
