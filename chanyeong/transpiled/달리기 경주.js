"use strict";
(() => {
    const solution = (players_, callings) => {
        const hash = {};
        const players = players_.slice(0);
        // 파마리터의 immutable함을 유지하기 위해 새 배열 선언
        for (let i = 0; i < players.length; i++)
            hash[players[i]] = i;
        // player의 이름으로 index(등수)를 초기화
        const call = (player) => {
            const i = hash[player];
            const curI = hash[player];
            const prevI = curI - 1;
            // 현재 call 된 선수의 index값(등수)
            const nP = players[prevI];
            // 이전 등수 player
            [players[curI], players[prevI]] = [players[prevI], players[curI]];
            [hash[player], hash[nP]] = [prevI, curI];
            // 추월(두 플레이어와 각 hash값을 스왑)
        };
        for (const calledPlayer of callings)
            call(calledPlayer);
        return players;
    };
})();
