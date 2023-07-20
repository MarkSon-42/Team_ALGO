// maxDia, maxIRon, maxStone내에서 개수 같은 거 있을 때 어떻게 처리할지 아직 구현 X
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *ftSort(int **arr, int order, int *tmp){
    int temp = 0;

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 2; j++){
            if (arr[j][order] > arr[j + 1][order]){
                temp = tmp[j];
                tmp[j] = tmp[j + 1];
                tmp[j + 1] = temp;
            }
        }
    }
    return tmp;
}

int lowestFatigue(int *picks, char **minerals){
    // 미네랄을 5개씩 쪼개 나눠 새로운 리스트들로 저장하며, 각 리스트에 각 종류의 광물들이 몇개씩 있는지 세기
    int arrNum = 0;
    while (minerals)
        arrNum++;
    arrNum /= 5 + 1;
    char ***div5 = (char ***)calloc(arrNum, sizeof(char *));
    int **mineralNum = (int **)calloc(arrNum, sizeof(int *));

    for(int i = 0; i < arrNum; i++){
        div5[i] = (char **)calloc(6, sizeof(char *));
        mineralNum[i] = (int *)calloc(3, sizeof(int));
    }

    int k = 0;
    for (int i = 0; i < arrNum; i++){
        for (int j = 0; j < 6; j++){
            if (minerals[k][0] == 'd') //단어 전체를 비교하는 방법은?
                mineralNum[i][0]++;
            else if (minerals[k][0] == 'i')
                mineralNum[i][1]++;
            else
                mineralNum[i][2]++;
            div5[i][j] = minerals[k++];
        }
    }

    // 규칙대로 광물 캐주기
    int tmp1[3] = {0, 1, 2}, tmp2[3] = {0, 1, 2}, tmp3[3] = {0, 1, 2}; // q. 이렇게 3개 안만들고 더 효율적으로 하는 방법 생각해보기
    int *maxDiamond = ftSort(mineralNum, 0, tmp1);
    int *maxIron = ftSort(mineralNum, 1, tmp2);
    int *maxStone = ftSort(mineralNum, 2, tmp3);

    // 최소 피로도 구하기
    int arrNumCnt = 0, fatigue = 0;
    while (arrNumCnt < arrNum){
        // 다이아몬드 곡괭이를 사용하는 경우
        for (int i = 0; i < picks[0]; i++){
            // div5[maxDiamond[i]]를 다 캐며 피로도 계산
            for(int k = 0; k < 5; k++){
                if (div5[maxIron[i]][k][0] == 'd' || div5[maxIron[i]][k][0] == 'i' || div5[maxIron[i]][k][0] == 's')
                    fatigue += 1;
            }
            for (int j = 0; j < 3; j++){
                if (maxIron[j] == maxDiamond[i])
                    maxIron[j] = -1;
            }
        }
        // 철 곡괭이를 사용하는 경우
        for (int i = 0; i < picks[1]; i++){
            if (maxIron[i] == -1)
                continue;
            // div5(maxIron[i])를 다 캐며 피로도 계산
            for(int k = 0; k < 5; k++){
                if (div5[maxIron[i]][k][0] == 'd')
                    fatigue += 5;
                else if (div5[maxIron[i]][k][0] == 'i' || div5[maxIron[i]][k][0] == 's')
                    fatigue += 1;
                else
                    fatigue += 1;
            }
            for (int j = 0; j < 3; j++){
                if (maxStone[j] == maxIron[i])
                    maxStone[j] = -1;
            }
        }
        // 돌 곡괭이를 사용하는 경우
        for (int i = 0; i < picks[2]; i++){
            if (maxStone[i] == -1)
                continue;
            // div5(maxStone[i])를 다 캐며 피로도 계산
            for(int k = 0; k < 5; k++){
                if (div5[maxStone[i]][k][0] == 'd')
                    fatigue += 25;
                else if (div5[maxStone[i]][k][0] == 'i')
                    fatigue += 5;
                else
                    fatigue += 1;
            }
        }
        arrNumCnt++;
    }

    return (fatigue);
}    

int main(){
    int picks[3] = {1, 3, 2};
    char *minerals[8] = {"diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"};

    printf("%d\n", lowestFatigue(picks, minerals));
    return 0;
}

// ftSort에서 local variable 반환하려 해서 에러 -> 반환하고자 하는 배열을 미리 만들어주고 파라미터로 받았다가 내보내주는걸로 하자
