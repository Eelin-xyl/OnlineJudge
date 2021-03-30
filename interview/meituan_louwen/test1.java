package com.xiaoyuyu.shixi_jishi.meituan_3_20;

import java.util.Scanner;

/**
 * @Description: 美团编程题1
 * @Author: Xiaoyuyu
 * @CreateDate: 2021/3/20 3:52 下午
 */

//小美最近在学习操作系统。
//
//流是操作系统中一个重要的概念。在 Linux 操作系统中，/dev/random 和 /dev/urandom 是两个重要的设备，它们可以提供永不为空的随机字节数据流。
//
//小美自己也实现了一个类似于 /dev/random 的设备 /dev/crandom，但是它只能提供预先设定好但循环不断的某个小写字母排列。例如预先设定的字符串为 abcdefgh...xyz，那么这个设备会提供永不为空的字符串流 abcdefgh...xyzabcdefg...xyzabc...。
//
//小美想利用这个设备生成一段文字，但她想知道恰好生成完这段文字时，浪费了这个流的多少个字符。
//
//样例说明
//
//拿取生成流中字母的情况如下，拿取的字母用下划线表示。
//
//abcde...lmn...def...hij...stu..zab...mno...
//
//在生成好最后一个 n 的时候，浪费了没有标下划线的 59 个字符。

//abcdefghijklmnopqrstuvwxyz
//meituan

// 59

// 得分 100
public class test1 {


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        String output = scanner.next();

        int sum = 0;

        int idx =0;
        int len = input.length();
        int i = 0;
        for(;i<len;i++) {
            if(idx==output.length()) break;
            char c = output.charAt(idx);
            char c1 = input.charAt(i);
            if(c==c1) {
                idx++;
            } else sum++;
            if(i==len-1) i=-1;
        }
        System.out.println(sum);
    }
}
