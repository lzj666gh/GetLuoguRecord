#include<bits/stdc++.h>
#include<chrono>
using namespace std;
using namespace chrono;
using Clock = std::chrono::high_resolution_clock;
using TimePoint = std::chrono::time_point<Clock>;
int main() {
	freopen("time.in", "r", stdin);
	freopen("time.out", "w", stdout);
	long long tm;
	cin >> tm;
	system_clock::time_point tmp = system_clock::time_point(system_clock::duration(tm * 1000000000ll));
	std::time_t tt = std::chrono::system_clock::to_time_t(tmp);
	char Week[10], Month[10];
	int Day, H, M, S, Y;
	sscanf(asctime(std::localtime(&tt)), "%s %s %d %d:%d:%d %d", Week, Month, &Day, &H, &M, &S, &Y);
	map<string, int>mp;
	mp["Jan"] = 1;
	mp["Feb"] = 2;
	mp["Mar"] = 3;
	mp["Apr"] = 4;
	mp["May"] = 5;
	mp["Jun"] = 6;
	mp["Jul"] = 7;
	mp["Aug"] = 8;
	mp["Sep"] = 9;
	mp["Oct"] = 10;
	mp["Nov"] = 11;
	mp["Dec"] = 12;
	cout << Y << '/' << setw(2) << setfill('0') << mp[Month] << '/' << setw(2) << setfill('0') << Day << ' ' << setw(2) << setfill('0') << H << ':' << setw(2) << setfill('0') << M << ':' << setw(2) << setfill('0') << S << endl;
	return 0;
}
