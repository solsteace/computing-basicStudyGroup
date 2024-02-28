#include <bits/stdc++.h>

using namespace std;

int max(int x, int y) {
    return (x > y) ? x : y;
}

int maximum_sum(int nums[], int low, int high)
{
    if (high <= low) {
        return nums[low];
    }

    int mid = (low + high) / 2;
 
    // Mencari maksimum subarray dibagian kiri
    int left_max = INT_MIN;
    int sum = 0;
    for (int i = mid; i >= low; i--)
    {
        sum += nums[i];
        if (sum > left_max) {
            left_max = sum;
        }
    }
 
    // Mencari maksimum subaarray dibagian kanan
    int right_max = INT_MIN;
    sum = 0; 
    for (int i = mid + 1; i <= high; i++)
    {
        sum += nums[i];
        if (sum > right_max) {
            right_max = sum;
        }
    }
 
    // Mencari maksimum pada bagian kiri dan kanan secara rekursif dan simpan nilai maksimum
    int max_left_right = max(maximum_sum(nums, low, mid),
                            maximum_sum(nums, mid + 1, high));
 
    return max(max_left_right, left_max + right_max);
}

int main(){
    int n;
    cin >> n;
    int nums[n];
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }

    cout << maximum_sum(nums, 0, n-1);
}