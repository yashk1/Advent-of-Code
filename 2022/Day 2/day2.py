with open("./input/day2.txt") as file:
    lines = [l.split(" ") for l in file.read().splitlines()]
    
    score = 0
    for i in lines:
        if i[1] == 'X':
            score +=1 
        if i[1] == 'Y':
            score +=2
        if i[1] == 'Z':
            score +=3  

        if i[0] == 'A':
            if i[1] == 'X':
                score+=3
            elif i[1] == 'Y':
                score += 6
            elif i[1] == 'Z':
                score +=0
        elif i[0] == 'B':
            if i[1] == 'X':
                score+= 0
            elif i[1] == 'Y':
                score += 3
            elif i[1] == 'Z':
                score +=6
        elif i[0] == 'C':
            if i[1] == 'X':
                score+= 6
            elif i[1] == 'Y':
                score += 0
            elif i[1] == 'Z':
                score +=3
                    
    print(score)


