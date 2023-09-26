package backjoon.Implementation.Silver_1_2002;

import java.io.*;
import java.util.*;

/**
 * 문제 : 추월
 * 링크 : https://www.acmicpc.net/problem/2002
 * 소요시간 :
 */

public class Solved {
    static HashMap<String, Integer> in = new HashMap<>();
    static HashMap<String, Integer> out = new HashMap<>();
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int i = 0; i < N; i++) {
            String car = br.readLine().toString();
            in.put(car, i);
        }

        for (int i = 0; i < N; i++) {
            String car = br.readLine().toString();
            out.put(car, i);
        }

        // 출구쪽 map을 순회하면서 해당 차량이 진입 순서보다 일찍 나오면 추월차량으로 간주.
        for (Map.Entry<String, Integer> entry : out.entrySet()) {
            String car = entry.getKey();
            int num = entry.getValue();

            // 진입했을 때보다 먼저 나왔으면 추월차량 처리
            if (in.get(car) > num) {
                answer++;
            }
        }

        System.out.println(answer);
        br.close();
    }
}
