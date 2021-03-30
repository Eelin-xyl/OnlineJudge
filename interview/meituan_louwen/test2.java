package com.xiaoyuyu.shixi_jishi.meituan_3_20;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

/**
 * @Description: 美团编程题2
 * @Author: Xiaoyuyu
 * @CreateDate: 2021/3/20 3:52 下午
 */

// 小团现在有两个等大的多重集合（与集合的区别仅是在可以在集合中出现重复元素）A 和 B。她现在想让 A 集合与 B 集合相等。她会先选择一个非负整数
// x，然后让 A 集合中的所有数都加上 x 并对 m 取模。也就是说，对于 A 中的全部元素 a，都把 a 变成 (a + x) mod m。
//
// 她想知道这个最小的 x 是多少，才能使经过变换后 A = B。并且她保证至少存在一个满足条件的 x。

// 6 8
// 1 1 4 5 1 4
// 3 0 4 0 3 0

// 7

// 得分 63 超时
public class test2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int len = scanner.nextInt();
        int m = scanner.nextInt();
        // System.out.println(Long.MAX_VALUE);
        Map<Integer, Integer> a_cnt = new HashMap<Integer, Integer>();
        Map<Integer, Integer> b_cnt = new HashMap<Integer, Integer>();
        int[] a = new int[len];
        for (int i = 0; i < len; i++) {
            int num = scanner.nextInt();
            a[i] = num;
            if (a_cnt.get(num) == null) {
                a_cnt.put(num, 1);
            } else {
                a_cnt.put(num, a_cnt.get(num) + 1);
            }
        }
        for (int i = 0; i < len; i++) {
            int num = scanner.nextInt();
            if (b_cnt.get(num) == null) {
                b_cnt.put(num, 1);
            } else {
                b_cnt.put(num, b_cnt.get(num) + 1);
            }
        }
        // 处理数据
        int x = 0;
        while (true) {
            a_cnt = new HashMap<Integer, Integer>();
            for (int i = 0; i < len; i++) {
                if (a_cnt.get(a[i]) == null) {
                    a_cnt.put(a[i], 1);
                } else {
                    a_cnt.put(a[i], a_cnt.get(a[i]) + 1);
                }
            }
            for (int i = 0; i < len; i++) {
                int num = a[i];
                int num2 = (a[i] + x) % m;
                if (a_cnt.get(num2) == null) {
                    a_cnt.put(num2, 1);
                } else
                    a_cnt.put(num2, a_cnt.get(num2) + 1);
                a_cnt.put(num, a_cnt.get(num) - 1);
                if (a_cnt.get(num) == 0)
                    a_cnt.remove(num);
            }
            if (a_cnt.size() != b_cnt.size()) {
                x++;
                continue;
            }
            int flag = 1;
            Set<Map.Entry<Integer, Integer>> entries = a_cnt.entrySet();
            for (Map.Entry<Integer, Integer> temp1 : entries) {
                Integer key = temp1.getKey();
                if (!a_cnt.get(key).equals(b_cnt.get(key))) {
                    flag = 0;
                    break;
                }
            }
            if (flag == 0) {
                x++;
            } else {
                System.out.println(x);
                break;
            }
        }
    }
}
