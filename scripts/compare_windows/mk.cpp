// 他负责生成用来测试的数据
#include <bits/stdc++.h>
using namespace std;
mt19937_64 rnd(time(0));
inline long long randint(long long l, long long r) {
	// 生成在[l, r]当中的随机数
	return rnd() % (r - l + 1) + l; 
}
int main() {
	printf("%lld %lld\n", randint(INT_MIN, INT_MAX), randint(INT_MIN, INT_MAX));
	return 0;
}
