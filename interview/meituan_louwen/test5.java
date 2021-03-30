package com.xiaoyuyu.shixi_jishi.meituan_3_20;

import java.util.Scanner;

/**
 * @Description: 美团编程题5
 * @Author: Xiaoyuyu
 * @CreateDate: 2021/3/20 5:56 下午
 */

// 本题为专项练习 可能不需要做，没给我额外的时间计算，前四题给了120分钟的时间
//小美在做化学实验，这个实验需要配置很多种浓度溶液，因此配溶液之前需要详细计算溶液浓度（用质量分数表示），避免误操作。
//
//实验初始溶液质量和质量分数分别为 m0 , ω0%。小美会进行如下两种操作：
//
//1、A(m, ω) 表示向目前的溶液中加入质量为 m 质量分数为 ω% 的溶液；
//
//2、B 表示撤销上一步 A 操作。
//
//对于每一步操作，小美都想知道当前溶液的质量与质量分数。
//
//质量分数 ω 按如下方式计算：设溶液中溶质质量为 x，溶液总质量为 y，则 w% = x/y*100%

//20 50
//4
//A 30 0
//B
//B
//A 80 14

//50 20.00000
//20 50.00000
//20 50.00000
//100 21.20000

public class test5 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();  //
        int w = scanner.nextInt();  // 想知道的天数
    }
}
