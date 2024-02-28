#include <bits/stdc++.h>

using namespace std;

int maximum_sum(int nums[], int n)
{
    int max_sum = INT_MIN;
    int sum = 0;

    for (int i = 0; i < n; i++){
        sum = 0;
        for (int j = i; j < n; j++){
            sum += nums[j];
            if (sum > max_sum) {
                max_sum = sum;
            }
        }
    }
    return max_sum;
}

int main(){
    int n;
    cin >> n;
    int nums[n];
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }

    cout << maximum_sum(nums, n);
}