"use strict";
(() => {
    const solution = (id_list, report, k) => {
        const answer = [];
        const reportUsers = report.map((usersStr) => usersStr.split(" ")); // 길이는 최대 200,000
        const reportedInfo = {};
        const reportInfo = {};
        for (const id of id_list) {
            reportedInfo[id] = { reportedCount: 0 };
            reportInfo[id] = new Set();
        }
        for (const [reportUser, reportedUser] of reportUsers) {
            if (reportInfo[reportUser].has(reportedUser))
                continue;
            // 이미 신고한 경우에 대해서는 counting하지 않음
            reportInfo[reportUser].add(reportedUser);
            // reportUser가 reportedUser를 report 하였기 때문에 reportedInfo에 정보 업데이트
            reportedInfo[reportedUser].reportedCount++;
            // reportedUser는 report 되었으므로 reportedInfo[reportedUser]의 reportedCount 증가
        }
        for (const id of id_list) {
            // id_list 길이 최대 1000
            let count = 0;
            // reportInfo[id]의 길이 최대 1000 - 1 = =~ 1000
            for (const reportUser of reportInfo[id])
                if (reportedInfo[reportUser].reportedCount >= k)
                    count++;
            answer.push(count);
        }
        // 위 이중for문의 최대 시간 복잡도는 O(1000 * 1000) 추정 => O(1,000,000) 이므로 충분하다고 판단
        return answer;
    };
})();
