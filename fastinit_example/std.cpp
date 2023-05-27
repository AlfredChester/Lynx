#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
template <typename _Tp> 
inline void read(_Tp &x) {
    char c = getchar(); bool f = x = 0;
    while (c < '0' || c > '9') {
        f = (c == '-'), c = getchar();
    }
    while (c >= '0' && c <= '9') {
        x = (x << 1) + (x << 3) + (c ^ 48), c = getchar();
    }
    f ? x = -x : 0;
}

int main(int argc, char const *argv[]) {
    
    return 0;
}
