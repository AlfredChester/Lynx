#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
mt19937_64 rnd(time(0));
inline ll randint(ll l, ll r) {
    return rnd() % (r - l + 1) + l;
}
int main(int argc, const char *argv[]) {
   printf("%lld %lld", randint(INT_MIN, INT_MAX), randint(INT_MIN, INT_MAX)); 
   return 0;
}
