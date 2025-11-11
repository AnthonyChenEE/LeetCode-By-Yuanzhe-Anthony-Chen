# include <iostream>
using namespace std;	
int fun(int n) {
	if (n == 1)
		return 1;
	else if (n == 2) {
		return 1;
	}
	else {
		return fun(n - 1) + fun(n - 2);
	}
}
int main() {
	int n;
	cin >> n;
	cout << endl;
	int i = 0;
	for (i=1; i<=n; i++) {
		cout << fun(i) << endl;
	}
	return 0;
}