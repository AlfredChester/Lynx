// �����������������Ե�����
#include <bits/stdc++.h>
using namespace std;
mt19937_64 rnd(time(0));
inline long long randint(long long l, long long r) {
	// ������[l, r]���е������
	return rnd() % (r - l + 1) + l; 
}
int main() {
	printf("%lld %lld\n", randint(INT_MIN, INT_MAX), randint(INT_MIN, INT_MAX));
	return 0;
}
