def unique(*x):
    return len(x) == len(set(x))


for q in [6,9]:

    V = [1, 2, 3, 4, 5, q] #
    D = [1, 2, 3, 4, 5, q] #
    C = [1, 2, 3, 4, 5, q] #
    R = [7, 8, q] #
    E = [1, 2, 3, 4, 5, 7, 8, q] 
    A = [1, 2, 3, 4, 5, 7, 8, q] #
    U = [1, 2, 3, 4, 5, 7, 8, q] #
    G = [1, 2, 3, 4, 5, 7, 8, q] #

    # VVD
    # Dzz
    # CDA
    #  CU
    # REG

    count = checks = 0
    dots1 = dots2 = 0

    # V + D + C = R dus minimaal  1 + 2 + 3
    # V + D + C + 1 == R
    R = [7, 8]
    if q == 9:
        R.append(9)
    
    for v in V:
        for d in D:
            if not unique(v,d): continue # 1
            for c in C:
                if not unique(v,d,c): continue # 1
                if v + d + c + 1 > 10: continue # 2
                for r in R:
                    if not unique(v,d,c,r): continue # 1
                    if (v + d + c + 1) % 10 != r: continue # 3
                    for e in E:
                        if not unique(v,d,c,r,e): continue # 1
                        if (v + 6 + d + c +1) % 10 != e and (v + 6 + d + c +2) % 10 != e: continue
                        for a in A:
                            if not unique(v,d,c,r,e,a): continue # 1
                            for u in U:
                                if not unique(v,d,c,r,e,a,u): continue # 1
                                for g in G:
                                    if not unique(v,d,c,r,e,a,u,g): continue # 1
                                    if (d + 6 + a + u) % 10 != g: continue
                                    text = "{}{}{} + {}66 + {}{}{} + {}{} == {}{}{}".format(v,v,d, d, c,d,a, c,u, r,e,g)

                                    dots = ""
                                    if eval("{}+6+{}+{}+{}".format(d,a,u,g)):
                                        dots = "."
                                        dots1 += 1
                                    elif eval("{}+6+{}+{}+{}".format(v,d,c,e)):
                                        dots = ".."
                                        dots2 += 1

                                    if eval(text):
                                        print(text, True, v,d,c,r,e,a,u,g, " - ", dots)
                                        count += 1
                                    else:
                                        print(text, "....", v,d,c,r,e,a,u,g, " - ", dots)
                                    checks += 1

    print("\n\n")
    print("{}/{}".format(count, checks))
    print("{} {}".format(dots1, dots2))



# 1: All values maust be unique

# 2: V + D + C < 10 Is makkelijk te zien
#    V + D + C +1 < 10 TODO

# 3: V + D + C +1 == R Nu we dit hebben kunnen we dit uitbreiden naar een verdie met E

# 3: (v + 6 + d + c +1) % 10 != e and (v + 6 + d + c +2) % 10 != e TODO





# 114 + 466 + 247 + 26 == 853
# 114 + 466 + 246 + 27 == 853
# 224 + 466 + 147 + 16 == 853
# 224 + 466 + 146 + 17 == 853

# 112 + 266 + 328 + 39 == 745
# 112 + 266 + 329 + 38 == 745
# 113 + 366 + 432 + 47 == 958
# 113 + 366 + 437 + 42 == 958
# 221 + 166 + 417 + 49 == 853
# 221 + 166 + 419 + 47 == 853
# 331 + 166 + 412 + 48 == 957
# 331 + 166 + 418 + 42 == 957
# 332 + 266 + 128 + 19 == 745
# 332 + 266 + 129 + 18 == 745
# 441 + 166 + 217 + 29 == 853
# 441 + 166 + 219 + 27 == 853
# 441 + 166 + 312 + 38 == 957
# 441 + 166 + 318 + 32 == 957
# 443 + 366 + 132 + 17 == 958
# 443 + 366 + 137 + 12 == 958



# 112 + 266 + 324 + 36 == 738 	1,2,3,7,3,4,6,8
# 112 + 266 + 326 + 34 == 738 	1,2,3,7,3,6,4,8
# 112 + 266 + 423 + 45 == 846 	1,2,4,8,4,3,5,6
# 112 + 266 + 423 + 46 == 847 	1,2,4,8,4,3,6,7
# 112 + 266 + 425 + 43 == 846 	1,2,4,8,4,5,3,6
# 112 + 266 + 426 + 43 == 847 	1,2,4,8,4,6,3,7
# 112 + 266 + 523 + 56 == 957 	1,2,5,9,5,3,6,7
# 112 + 266 + 523 + 57 == 958 	1,2,5,9,5,3,7,8
# 112 + 266 + 524 + 56 == 958 	1,2,5,9,5,4,6,8
# 112 + 266 + 526 + 53 == 957 	1,2,5,9,5,6,3,7
# 112 + 266 + 526 + 54 == 958 	1,2,5,9,5,6,4,8
# 112 + 266 + 527 + 53 == 958 	1,2,5,9,5,7,3,8
# 112 + 266 + 527 + 58 == 963 	1,2,5,9,6,7,8,3
# 112 + 266 + 528 + 57 == 963 	1,2,5,9,6,8,7,3
# 113 + 366 + 234 + 25 == 738 	1,3,2,7,3,4,5,8
# 113 + 366 + 235 + 24 == 738 	1,3,2,7,3,5,4,8
# 113 + 366 + 432 + 45 == 956 	1,3,4,9,5,2,5,6
# 113 + 366 + 432 + 46 == 957 	1,3,4,9,5,2,6,7
# 113 + 366 + 432 + 47 == 958 	1,3,4,9,5,2,7,8
# 113 + 366 + 435 + 42 == 956 	1,3,4,9,5,5,2,6
# 113 + 366 + 435 + 48 == 962 	1,3,4,9,6,5,8,2
# 113 + 366 + 436 + 42 == 957 	1,3,4,9,5,6,2,7
# 113 + 366 + 436 + 47 == 962 	1,3,4,9,6,6,7,2
# 113 + 366 + 437 + 42 == 958 	1,3,4,9,5,7,2,8
# 113 + 366 + 437 + 46 == 962 	1,3,4,9,6,7,6,2
# 113 + 366 + 438 + 45 == 962 	1,3,4,9,6,8,5,2
# 114 + 466 + 246 + 27 == 853 	1,4,2,8,5,6,7,3
# 114 + 466 + 247 + 26 == 853 	1,4,2,8,5,7,6,3
# 114 + 466 + 342 + 35 == 957 	1,4,3,9,5,2,5,7
# 114 + 466 + 342 + 36 == 958 	1,4,3,9,5,2,6,8
# 114 + 466 + 345 + 32 == 957 	1,4,3,9,5,5,2,7
# 114 + 466 + 345 + 37 == 962 	1,4,3,9,6,5,7,2
# 114 + 466 + 346 + 32 == 958 	1,4,3,9,5,6,2,8
# 114 + 466 + 347 + 35 == 962 	1,4,3,9,6,7,5,2
# 114 + 466 + 347 + 38 == 965 	1,4,3,9,6,7,8,5
# 114 + 466 + 348 + 37 == 965 	1,4,3,9,6,8,7,5
# 115 + 566 + 253 + 24 == 958 	1,5,2,9,5,3,4,8
# 115 + 566 + 254 + 23 == 958 	1,5,2,9,5,4,3,8
# 115 + 566 + 254 + 28 == 963 	1,5,2,9,6,4,8,3
# 115 + 566 + 256 + 27 == 964 	1,5,2,9,6,6,7,4
# 115 + 566 + 257 + 26 == 964 	1,5,2,9,6,7,6,4
# 115 + 566 + 257 + 28 == 966 	1,5,2,9,6,7,8,6
# 115 + 566 + 258 + 24 == 963 	1,5,2,9,6,8,4,3
# 115 + 566 + 258 + 27 == 966 	1,5,2,9,6,8,7,6
# 221 + 166 + 314 + 35 == 736 	2,1,3,7,3,4,5,6
# 221 + 166 + 315 + 34 == 736 	2,1,3,7,3,5,4,6
# 221 + 166 + 315 + 36 == 738 	2,1,3,7,3,5,6,8
# 221 + 166 + 316 + 35 == 738 	2,1,3,7,3,6,5,8
# 221 + 166 + 514 + 56 == 957 	2,1,5,9,5,4,6,7
# 221 + 166 + 514 + 57 == 958 	2,1,5,9,5,4,7,8
# 221 + 166 + 516 + 54 == 957 	2,1,5,9,5,6,4,7
# 221 + 166 + 517 + 54 == 958 	2,1,5,9,5,7,4,8
# 223 + 366 + 134 + 15 == 738 	2,3,1,7,3,4,5,8
# 223 + 366 + 135 + 14 == 738 	2,3,1,7,3,5,4,8
# 224 + 466 + 146 + 17 == 853 	2,4,1,8,5,6,7,3
# 224 + 466 + 147 + 16 == 853 	2,4,1,8,5,7,6,3
# 225 + 566 + 153 + 14 == 958 	2,5,1,9,5,3,4,8
# 225 + 566 + 154 + 13 == 958 	2,5,1,9,5,4,3,8
# 225 + 566 + 154 + 18 == 963 	2,5,1,9,6,4,8,3
# 225 + 566 + 156 + 17 == 964 	2,5,1,9,6,6,7,4
# 225 + 566 + 157 + 16 == 964 	2,5,1,9,6,7,6,4
# 225 + 566 + 157 + 18 == 966 	2,5,1,9,6,7,8,6
# 225 + 566 + 158 + 14 == 963 	2,5,1,9,6,8,4,3
# 225 + 566 + 158 + 17 == 966 	2,5,1,9,6,8,7,6
# 331 + 166 + 214 + 25 == 736 	3,1,2,7,3,4,5,6
# 331 + 166 + 215 + 24 == 736 	3,1,2,7,3,5,4,6
# 331 + 166 + 215 + 26 == 738 	3,1,2,7,3,5,6,8
# 331 + 166 + 216 + 25 == 738 	3,1,2,7,3,6,5,8
# 331 + 166 + 412 + 46 == 955 	3,1,4,9,5,2,6,5
# 331 + 166 + 412 + 47 == 956 	3,1,4,9,5,2,7,6
# 331 + 166 + 412 + 48 == 957 	3,1,4,9,5,2,8,7
# 331 + 166 + 415 + 46 == 958 	3,1,4,9,5,5,6,8
# 331 + 166 + 416 + 42 == 955 	3,1,4,9,5,6,2,5
# 331 + 166 + 416 + 45 == 958 	3,1,4,9,5,6,5,8
# 331 + 166 + 417 + 42 == 956 	3,1,4,9,5,7,2,6
# 331 + 166 + 417 + 48 == 962 	3,1,4,9,6,7,8,2
# 331 + 166 + 418 + 42 == 957 	3,1,4,9,5,8,2,7
# 331 + 166 + 418 + 47 == 962 	3,1,4,9,6,8,7,2
# 332 + 266 + 124 + 16 == 738 	3,2,1,7,3,4,6,8
# 332 + 266 + 126 + 14 == 738 	3,2,1,7,3,6,4,8
# 334 + 466 + 142 + 15 == 957 	3,4,1,9,5,2,5,7
# 334 + 466 + 142 + 16 == 958 	3,4,1,9,5,2,6,8
# 334 + 466 + 145 + 12 == 957 	3,4,1,9,5,5,2,7
# 334 + 466 + 145 + 17 == 962 	3,4,1,9,6,5,7,2
# 334 + 466 + 146 + 12 == 958 	3,4,1,9,5,6,2,8
# 334 + 466 + 147 + 15 == 962 	3,4,1,9,6,7,5,2
# 334 + 466 + 147 + 18 == 965 	3,4,1,9,6,7,8,5
# 334 + 466 + 148 + 17 == 965 	3,4,1,9,6,8,7,5
# 441 + 166 + 312 + 36 == 955 	4,1,3,9,5,2,6,5
# 441 + 166 + 312 + 37 == 956 	4,1,3,9,5,2,7,6
# 441 + 166 + 312 + 38 == 957 	4,1,3,9,5,2,8,7
# 441 + 166 + 315 + 36 == 958 	4,1,3,9,5,5,6,8
# 441 + 166 + 316 + 32 == 955 	4,1,3,9,5,6,2,5
# 441 + 166 + 316 + 35 == 958 	4,1,3,9,5,6,5,8
# 441 + 166 + 317 + 32 == 956 	4,1,3,9,5,7,2,6
# 441 + 166 + 317 + 38 == 962 	4,1,3,9,6,7,8,2
# 441 + 166 + 318 + 32 == 957 	4,1,3,9,5,8,2,7
# 441 + 166 + 318 + 37 == 962 	4,1,3,9,6,8,7,2
# 442 + 266 + 123 + 15 == 846 	4,2,1,8,4,3,5,6
# 442 + 266 + 123 + 16 == 847 	4,2,1,8,4,3,6,7
# 442 + 266 + 125 + 13 == 846 	4,2,1,8,4,5,3,6
# 442 + 266 + 126 + 13 == 847 	4,2,1,8,4,6,3,7
# 443 + 366 + 132 + 15 == 956 	4,3,1,9,5,2,5,6
# 443 + 366 + 132 + 16 == 957 	4,3,1,9,5,2,6,7
# 443 + 366 + 132 + 17 == 958 	4,3,1,9,5,2,7,8
# 443 + 366 + 135 + 12 == 956 	4,3,1,9,5,5,2,6
# 443 + 366 + 135 + 18 == 962 	4,3,1,9,6,5,8,2
# 443 + 366 + 136 + 12 == 957 	4,3,1,9,5,6,2,7
# 443 + 366 + 136 + 17 == 962 	4,3,1,9,6,6,7,2
# 443 + 366 + 137 + 12 == 958 	4,3,1,9,5,7,2,8
# 443 + 366 + 137 + 16 == 962 	4,3,1,9,6,7,6,2
# 443 + 366 + 138 + 15 == 962 	4,3,1,9,6,8,5,2
# 551 + 166 + 214 + 26 == 957 	5,1,2,9,5,4,6,7
# 551 + 166 + 214 + 27 == 958 	5,1,2,9,5,4,7,8
# 551 + 166 + 216 + 24 == 957 	5,1,2,9,5,6,4,7
# 551 + 166 + 217 + 24 == 958 	5,1,2,9,5,7,4,8
# 552 + 266 + 123 + 16 == 957 	5,2,1,9,5,3,6,7
# 552 + 266 + 123 + 17 == 958 	5,2,1,9,5,3,7,8
# 552 + 266 + 124 + 16 == 958 	5,2,1,9,5,4,6,8
# 552 + 266 + 126 + 13 == 957 	5,2,1,9,5,6,3,7
# 552 + 266 + 126 + 14 == 958 	5,2,1,9,5,6,4,8
# 552 + 266 + 127 + 13 == 958 	5,2,1,9,5,7,3,8
# 552 + 266 + 127 + 18 == 963 	5,2,1,9,6,7,8,3
# 552 + 266 + 128 + 17 == 963 	5,2,1,9,6,8,7,3
