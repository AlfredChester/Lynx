#include <bits/stdc++.h>
#define OK_EXIT    0
#define WRONG_EXIT 1
#define ERROR_EXIT 2
#define lowbit(x)  (x & (-x))
typedef long long ll;
using namespace std;

const int e5 = 100000;
const int e6 = 1000000;
const int e8 = 100000000;
const ll e18 = 1000000000000000000ll;

template <class valTp, class rangeTp>
inline bool inRange(valTp x, rangeTp l, rangeTp r) {
    return l <= x && x <= r;
}

inline int judge(void) {
    // complete the function yourself
    return OK_EXIT;
}

int main(int argc, char const *argv[]) {
    // read input file from argv
    if (argc != 2) {
        puts("Invalid argument(s) given");
        return ERROR_EXIT;
    }
    try {
        freopen(argv[1], "r", stdin);
    } catch (const std::exception &e) {
        std::cerr << "Error captured when redirecting input "
                  << "to input file" << e.what() << '\n';
        return ERROR_EXIT;
    }
    return judge();
}
