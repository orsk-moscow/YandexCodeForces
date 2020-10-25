# D. Спортивный турнир
# number if strings
from collections import Counter

def log2(num):
    for i in range(1,17):
        if 2**i==num:
            return i
    return 0

def solve(file='input.txt'):
    set_games=set()
    f=open(file,'r')
    players=dict()
    n=int(f.readline())
    num_games=n
    candidates=[]
    max_games=int(log2(num_games+1))
    if max_games==0:
        return 'NO SOLUTION'
    while n:
        s=f.readline()
        pair=s.split()
        if pair==[]:
            continue
        n-=1
        check = max(pair)+" "+min(pair)
        if check in set_games:
            return 'NO SOLUTION'
        else:
            set_games|=set([check])
        for player in pair:
            if player in players.keys():
                players[player]+=1
                if players[player] == max_games:
                    candidates.append(player)
            else:
                players[player]=1
    if candidates.__len__()!=2:
        return 'NO SOLUTION'
    list_players=players.items()
    dict_num_games=(Counter([games for player,games in list_players]))
    cnt=(num_games+1)/2
    for num in range(1,max_games):
        if num not in dict_num_games.keys():
            return 'NO SOLUTION'
        if dict_num_games[num] != cnt:
            return 'NO SOLUTION'
        cnt/=2
    return " ".join(candidates)

def main():
	res=(solve('input.txt'))
	with open('output.txt','w') as f:
		f.write(res)

if __name__ == '__main__':
	main()