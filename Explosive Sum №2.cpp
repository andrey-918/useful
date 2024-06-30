#include <iostream>
#include <set>
#include <vector>
using namespace std;
using ull = unsigned long long;
ull find_summ(set<vector<int>>& a, const int number) {
    vector<int> new_one;
    int finding = 2;
    ull answer = 1;
    while (finding <= number) {
        for (vector<int> x: a) {
            if (x.size() > finding - 1 && x[finding - 1] == 1) {
                new_one = {x.begin() + finding, x.end()};
                new_one.push_back(finding);
                ++answer;
                a.insert(new_one);
            }
            else continue;
        }
        ++finding;
    }
    return answer;
}
void ready(set<vector<int>>& a, int number){
    vector <int> line;
    for (int i = 0; i != number; ++i) {
        line.push_back(1);
    }
    a.insert(line);

}
void out(const set<vector<int>>& a){
    for (const vector<int>& x: a){
        for (int y: x) cout << y << " ";
        cout << '\n';
    }
}
int main() {
    int number;
    set <vector<int>> a;
    cin >> number;
    ready(a, number);
    cout << find_summ(a, number) << '\n';
    //out(a);
}
