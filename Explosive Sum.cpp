#include <iostream>
#include <set>
#include <vector>
using namespace std;
void find_summ(set<vector<int>>& a, const int number) {
    vector<int> new_one;
    int finding = 2;
    while (finding != number) {
        for (vector<int> x: a) {
            int check = count(x.begin(), x.end(), 1);
            if (check >= finding) {
                new_one = x;
                new_one.erase(new_one.begin(), new_one.begin() + finding);
                new_one.push_back(finding);
            }
            a.insert(new_one);
        }
        ++finding;
    }
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
    int number, summ, repeat;
    set <vector<int>> a;
    cin >> number;
    ready(a, number);
    find_summ(a, number);
    cout << a.size() + 1 << "\n";
    //out(a);
}
