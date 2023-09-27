package backjoon.Implementation.Silver_2_2477;

import java.util.*;
import java.io.*;
/**
 * 문제 : 참외밭
 * 링크 : https://www.acmicpc.net/problem/2477
 * 소요시간 : failed(풀이 참조)
 */
public class Solved {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int K = Integer.parseInt(br.readLine());

        int hMax = 0, wMax = 0; //각 가로 세로의 최대 길이 저장
        int hMaxIdx = -1, wMaxIdx = -1; //가로 세로의 최대 길이의 인덱스 저장

        int[] dirs = new int[6]; //순서대로 방향 저장
        int[] dist = new int[6]; //변의 길이 저장

        for (int i = 0; i < 6; i++) {
            st = new StringTokenizer(br.readLine());
            dirs[i] = Integer.parseInt(st.nextToken());
            dist[i] = Integer.parseInt(st.nextToken());
            if (dirs[i] == 1 || dirs[i] == 2) { //가로 방향이면
                if (hMax < dist[i]) { //가로에 해당하는 변수들에 최대값, 인덱스 저장
                    hMax = dist[i];
                    hMaxIdx = i;
                }
            } else {//세로에 해당하는 변수들에 최대값, 인덱스 저장
                if (wMax < dist[i]) {
                    wMax = dist[i];
                    wMaxIdx = i;
                }
            }
        }
        int maxSquare = wMax * hMax; //전체 사각형의 넓이
        //각 인덱스의 +3을 하면 안에 있는 사각형의 길이를 가지고 있는 인덱스임
        int minSquare = dist[(wMaxIdx + 3) % 6] * dist[(hMaxIdx + 3) % 6];

        System.out.println((maxSquare-minSquare)*K);

        // 1, 2 중의 긴거랑
        // 3, 4 중의 긴거 둘이 합쳐서 전체 사각형 밭의 크기를 구한다.

        // 전체 사각형 밭의 크기 - 모자란 밭의 크기 하면 정답

        // ㄱ - 4, 2, 3, 1, 3, 1 - 1중 가장 큰값이 가로, 4중 가장 큰값이 세로 - 첫 1다음에 오는 3이 가짜 세로 길이 첫번째 1이 가짜 가로 길이
        // ㄴ - 3, 1, 4, 2, 4, 2 - 3이 가로 1이 세로 - 첫 4다음에 오는 2가 가짜 가로, 첫 2다음에 오는 4가 가짜 세로
        // 『 - 3, 1, 4, 1, 4, 2 - 2가 가로, 3이 세로 - 첫 4가 가짜 세로, 첫 4다음에 오는 1이 가짜 가로
        // 』 - 3, 1, 4, 2, 3, 2 - 1이 가로, 4가 세로 - 4다음에 오는 3이

        // 이 친구들 정렬
    }

}
