import java.util.Arrays;

import org.graalvm.compiler.java.LargeLocalLiveness;

import sun.security.util.Length;

class Solution {
    public int largestPerimeter(int[] A) {
        if (A.length < 3) {
            return 0;
        }
        Arrays.sort(A);
        for (int i = A.length - 1; i >= 2; i--) {
            if (A[i] < A[i - 1] + A[i - 2]) {
                return A[i] + A[i - 1] + A[i - 2];
            }
        }
        return 0;
    }

    public void main(String[] args) {
        int data[] = null; 
		data = new int[3]; /*开辟了一个长度为3的数组*/
		data[0] = 10; // 第一个元素
		data[1] = 20; // 第二个元素
		data[2] = 30; // 第三个元素
        int ans = largestPerimeter(data);
        System.out.println(ans);
    }
}