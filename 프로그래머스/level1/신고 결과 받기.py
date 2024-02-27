def solution(id_list, reports, k):
    user_list = {id:{"reported_me":set(),"mail":0} for id in id_list}
    for report in reports:
        report = report.split(" ")
        user_list[report[1]]["reported_me"].add(report[0])
    for key in user_list:
        if (len(user_list[key]["reported_me"]) >= k):
            for user in user_list[key]["reported_me"]:
                user_list[user]["mail"] += 1
    mail_values = [value["mail"] for value in user_list.values()]
    return mail_values
"""
나의 머리로는 풀기가 힘들었다. 그래서 걍 땟겼다.
코드 리뷰를 살짝 해보자면 일단 user_list를 만들었다. 간단하게 생각하면 json 형태로 관리를 하는 것이다.
id와 나를 신고한 사람, 신고 성공 횟수를 기록하는 변수를 만들어준다.
그리고 반복문을 돌면서 확인을 하는데 오는 값의 형태를 보면 사이에 공백이 있다. 그래서 그 공백으로 split해서 report[0]은 신고를 한 사람, report[1]은 신고를 당한 사람이 되는 거다.
그리고 user_list를 업데이트를 해준다.
user_list를 반복문을 통해서 돌면서 신고 당한 횟수가 k를 넘기면 신고 성공의 수를 1 추가한다.
그리고 그 신고 성공 횟수를 list로 바꿔서 return 하는 형식이다.

나도 처음에는 얼추 다 했었다. 근데 k개 이상 신고가 제대로 된 사람을 신고한 사람을 찾는 부분에서 막혔다. 그래서 결국 포기^^
일단 난 그 전 과정을 무지성 반복문을 여러개 썻는데 이 분은 user_list라는 변수, json과 비슷하게 생긴 변수를 만들어서 한다는게 굉장히 좋고 신박한 아이디어인것 같다.

참고 : https://1ets-just-do-it.tistory.com/9
"""