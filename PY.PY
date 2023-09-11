Def distract_soldiers(A):
    countRight = sum(A)
    countLeft = 0
    distractedSoldiers = 0
    
    for i in range(len(A)):
        if A[i] == 0:
            if countLeft < countRight:
                countLeft += 1
                distractedSoldiers += 1
            else:
                break
    
    return distractedSoldiers