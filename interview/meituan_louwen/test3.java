package com.xiaoyuyu.shixi_jishi.meituan_3_20;

import java.util.Map;
import java.util.Scanner;

/**
 * @Description: 美团编程题3
 * @Author: Xiaoyuyu
 * @CreateDate: 2021/3/20 5:14 下午
 */
//
// 学校正在举行喝奶茶比赛。这次比赛准备了 n 杯奶茶（为了比赛公平，奶茶里没有珍珠，椰果等各种小料，也就是纯奶茶），编号为 1 到 n。第 i 杯奶茶有
// ai 毫升，这 n 杯奶茶准备的吸管都是一样的，每秒最多能吸上来 C 毫升奶茶，选手只能通过吸管吸奶茶，不能捅破包装把奶茶倒进嘴里，这样对其他选手不公平。
//
// 选手按队伍参赛，小团所在的队伍有 m
// 个人，比赛要求队内的每个人选取编号在一个连续区间的奶茶喝，当然参赛选手也可以不喝任何奶茶。但是选定一杯奶茶喝就一定要喝完，不然的话这杯奶茶就被浪费了。
//
// 如果小团所在队打破了校记录，那么她们队的每个人都将获得一年的奶茶畅饮卷，所以她想知道所有奶茶都被喝完的最短用时。
//

// 5 3 4
// 5 8 3 10 7

// 4

// 得分 63 答案错误
public class test3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // 奶茶杯数
        int m = scanner.nextInt(); // 参与人数
        int c = scanner.nextInt(); // 喝的速度
        int[] cups = new int[n];
        int sum = 0; // 总共多少奶茶
        for (int i = 0; i < n; i++) {
            int num = scanner.nextInt();
            cups[i] = num;
            sum += num;
        }
        // 处理数据
        int ans = Integer.MAX_VALUE;
        int ave = (int) Math.ceil(sum * 1.0 / m); // 平均每个人喝多少
        int temp = 0;
        for (int i = 0; i < n; i++) {
            temp += cups[i];
            if (temp >= ave) {
                ans = Math.min(ans, (int) Math.ceil(temp * 1.0 / c));
                temp = 0;
            }
        }
        System.out.println(ans);
    }
}
