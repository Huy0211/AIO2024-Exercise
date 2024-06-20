# Câu 1:

import math


def calc_f1_score(tp, fp, fn):
    # Kiểm tra tp,fp,fn có phải int không
    if not isinstance(tp, int):
        print(f'(TP = {tp}, FP = {fp}, FN = {fn}) tp must be int')
    else:
        if not isinstance(fp, int):
            print(f'(TP = {tp}, FP = {fp}, FN = {fn}) fp must be int')
        else:
            if not isinstance(fn, int):
                print(f'(TP = {tp}, FP = {fp}, FN = {fn}) fn must be int')
            else:
                # Kiểm tra tp,fp,fn có lớn hơn 0 không
                if tp == 0 or fp == 0 or fn == 0:
                    print(f'(TP = {tp}, FP = {fp}, FN = {
                          fn}) tp and fp and fn must be greater than 0')
                else:
                    # Tính và in ra Precision,Reacll,F1_score
                    precision = tp/(tp+fp)
                    recall = tp/(tp+fn)
                    f1_score = (2*precision*recall)/(precision+recall)
                    print(f'(TP = {tp}, FP = {fp}, FN = {fn}) Precision is {
                          precision}, Recall is {recall}, F1_Score is {f1_score}')


if __name__ == '__main__':
    calc_f1_score(2, 3, 4)
    calc_f1_score('a', 3, 4)
    calc_f1_score(2, 'a', 4)
    calc_f1_score(2, 3, 'a')
    calc_f1_score(2, 3, 0)
    calc_f1_score(2.1, 3, 0)
