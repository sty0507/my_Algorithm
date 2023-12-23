def solution(players, callings):
    # .index()는 loop를 돌게 됨
    # rank = {"mumu" : 0, "soe" : 1, "poe" : 2, "kai" : 3, "mine" : 4}
    rank = {player : int(idx) for idx, player in enumerate(players)}
    
    for call in callings:
        current = rank[call]
        rank[call] -= 1
        rank[players[current - 1]] += 1
        
        players[current - 1], players[current] = call, players[current - 1]
        
    return players