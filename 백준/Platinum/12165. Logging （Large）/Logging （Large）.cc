#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;
        vector<long long> X(N), Y(N);
        for (int i = 0; i < N; i++) cin >> X[i] >> Y[i];

        cout << "Case #" << tc << ":\n";
        if (N <= 3) {
            for (int i = 0; i < N; i++) cout << 0 << "\n";
            continue;
        }

        const double PI = acos(-1.0);
        const double TWOPI = 2.0 * PI;
        const double EPS = 1e-12;

        for (int i = 0; i < N; i++) {
            vector<double> ang;
            ang.reserve(N - 1);
            for (int j = 0; j < N; j++) {
                if (i == j) continue;
                long long dx = X[j] - X[i];
                long long dy = Y[j] - Y[i];
                ang.push_back(atan2((double)dy, (double)dx));
            }
            sort(ang.begin(), ang.end());

            int m = N - 1;
            vector<double> ext(2 * m);
            for (int k = 0; k < m; k++) {
                ext[k] = ang[k];
                ext[k + m] = ang[k] + TWOPI;
            }

            int best = 0;
            int r = 0;
            for (int l = 0; l < m; l++) {
                if (r < l) r = l;
                while (r < l + m && ext[r] - ext[l] <= PI + EPS) r++;
                best = max(best, r - l);
            }

            cout << (m - best) << "\n";
        }
    }
    return 0;
}
