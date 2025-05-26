import os
import pickle

def input_scores():
    i = 1
    scrlist = []
    while i > 0:
        scr = int(input(f'#{i}? '))
        if scr < 0:
            return scrlist
            break
        scrlist.append(scr)
        i += 1
    return scrlist

def get_average(scrlist):
    total = 0
    cnt = len(scrlist)
    for i in range(cnt):
        total = total + scrlist[i]
    avg = total / len(scrlist)
    return avg

def show_score(scrlist):
    cnt = len(scrlist)
    print('[점수 출력]')
    print('개인점수: ')
    for i in range(cnt):
        print(scrlist[i], end=' ')

def save_file(scr, avg):
    with open('score.bin', 'wb') as file:
        pickle.dump(scr, file)
        pickle.dump(avg, file)

def load_file():
    with open('score.bin', 'rb') as file:
        scr = pickle.load(file)
        avg = pickle.load(file)
        show_score(scr)
        print()
        print(f'평균: {avg}')


if os.path.exists('score.bin'):
    load_file()
else:
    print('[점수 입력]')
    result = input_scores()
    result2 = get_average(result)
    show_score(result)
    print()
    print(f'평균: {result2}')
    save_file(result, result2)
