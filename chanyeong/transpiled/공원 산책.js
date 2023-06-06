"use strict";
(() => {
    const solution = (park, routes) => {
        const row = park.length;
        const col = park[0].length;
        // 시작 지점이 반드시 하나 존재하므로 position는 [number,number] 임이 자명
        const position = (() => {
            for (let i = 0; i < row; i++)
                for (let j = 0; j < col; j++)
                    if (park[i][j] === "S")
                        return [i, j];
        })();
        // x, y 좌표가 이동 가능한 좌표인지 확인하는 함수
        const isValidPosition = ([r, c]) => 0 <= c && c < col && 0 <= r && r < row && park[r][c] !== "X";
        // command에 따라 현재 좌표 기준 이동 좌표들을 구하는 함수
        const getNextPosition = (direction, dist, [curY, curX]) => {
            switch (direction) {
                case "N":
                    return Array.from(Array(dist), (_, i) => [curY - (i + 1), curX]);
                case "S":
                    return Array.from(Array(dist), (_, i) => [curY + (i + 1), curX]);
                case "W":
                    return Array.from(Array(dist), (_, i) => [curY, curX - (i + 1)]);
                case "E":
                    return Array.from(Array(dist), (_, i) => [curY, curX + (i + 1)]);
            }
        };
        // routes를 순회
        for (const route of routes) {
            const [direction, distance] = route.split(" ");
            const dist = Number(distance);
            const nextPositions = getNextPosition(direction, dist, position);
            let flag = true;
            for (const nextPosition of nextPositions)
                if (!isValidPosition(nextPosition)) {
                    // invalid한 포지션이 하나라도 있다면 flag를 false로 하여 break;
                    // (바깥 for문을 outer로 잡고 continue도 가능)
                    flag = false;
                    break;
                }
            // flag가 true라면 이동 경로가 모두 valid하다는 뜻 이므로 포지션을 업데이트
            if (flag)
                [position[0], position[1]] = nextPositions.at(-1);
        }
        return position;
    };
})();
