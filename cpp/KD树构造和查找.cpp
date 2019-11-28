#include <iostream>
#include <cstring>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <string>
#include <sstream>
#define MAX (55555)
#define K (5)
#define INF (0x3f3f3f3f)
#define pow(x) ((x) * (x))

using namespace std;

int k, n, idx;

struct Point
{
    double x[K];
    bool operator<(const Point &u) const
    {
        return x[idx] < u.x[idx];
    }
} po[MAX];

typedef pair<double, Point> PDP;
priority_queue<PDP> nq;

struct Tree
{
    Point p[MAX << 2];
    int son[MAX << 2];

    void build(int l, int r, int u = 1, int dep = 0)
    {
        if (l > r)
            return;
        son[u] = r - l;
        son[u << 1] = son[u << 1 | 1] = -1;
        idx = dep % k;
        int mid = l + r >> 1;
        nth_element(po + l, po + mid, po + r + 1);
        p[u] = po[mid];
        build(l, mid - 1, u << 1, dep + 1);
        build(mid + 1, r, u << 1 | 1, dep + 1);
    }

    void query(Point a, int m, int u = 1, int dep = 0)
    {
        if (son[u] == -1)
            return;
        PDP nd(0, p[u]);
        for (int i = 0; i < k; i++)
            nd.first += pow(nd.second.x[i] - a.x[i]);
        int dim = dep % k, fg = 0;
        int x = u << 1, y = u << 1 | 1;
        if (a.x[dim] >= p[u].x[dim])
            swap(x, y);
        if (~son[x])
            query(a, m, x, dep + 1);
        if (nq.size() < m)
            nq.push(nd), fg = 1;
        else
        {
            if (nd.first < nq.top().first)
                nq.pop(), nq.push(nd);
            if (pow(a.x[dim] - p[u].x[dim]) < nq.top().first)
                fg = 1;
        }
        if (~son[y] && fg)
            query(a, m, y, dep + 1);
    }

} kd;

void print(Point a[], int m)
{
    string output = "";
    for (int j = m - 1; j >= 0; j--)
    {
        if (j != m - 1)
            output += ",";
        stringstream ss;
        ss << a[j].x[0] << " " << a[j].x[1];
        output += ss.str();
    }
    cout << output << endl;
}

int main()
{
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    while (T--)
    {
        getchar();
        k = 2;

        string line;
        getline(cin, line);
        stringstream ss1(line);

        n = 0;
        string coord;
        while (getline(ss1, coord, ','))
        {
            stringstream ss2(coord);
            ss2 >> po[n].x[0] >> po[n].x[1];
            n++;
        }
        kd.build(0, n - 1);

        Point ans;
        int m;
        scanf("%lf%lf%d", &ans.x[0], &ans.x[1], &m);
        kd.query(ans, m);

        Point pt[20];
        for (int j = 0; !nq.empty(); j++)
            pt[j] = nq.top().second,
            nq.pop();
        print(pt, m);
    }
}