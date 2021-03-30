package com.xiaoyuyu.shixi_jishi.meituan_3_20;

import java.util.Scanner;

/**
 * @Description: 美团编程题4
 * @Author: Xiaoyuyu
 * @CreateDate: 2021/3/20 5:27 下午
 */

//小美和小团的班上有 n 个人，分别编号为 1 到 n。其中小美的编号为 1，小团的编号为 2。
//
//班上有个值日表 ai,j。第一天由小美值日，第二天由小团值日。接下来的每一天，如果今天是 i 值日，昨天是 j 值日，那么明天就是 ai,j 值日。值日表是已经规划好的，保证今天值日的同学明天一定不值日。
//
//小美想知道，第 m 天值日的同学的编号。

//3 7
//0 3 2
//3 0 3
//2 1 0

// 1

// 得分 45 超时
public class test4 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();  // 人数
        int m = scanner.nextInt();  // 想知道的天数
        if(m==1){
            System.out.println(1);
            return;
        }
        if(m==2){
            System.out.println(2);
            return;
        }
        int[][] table = new int[n][n];
        for(int i = 0;i<n;i++) {
            for(int j=0;j<n;j++) {
                table[i][j] = scanner.nextInt();
            }
        }
        // 处理数据
        int start1 = 1;
        int start2 = 2;
        for(int i = 0;i<m-2;i++) {
            int temp = table[start2-1][start1-1];
            start1 = start2;
            start2 = temp;
        }
//        System.out.println(start1);
        System.out.println(start2);
    }
}
