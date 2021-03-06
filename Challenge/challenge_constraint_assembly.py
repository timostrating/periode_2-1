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

if eval("({}+6+{}+{})%10 == {}".format(d,a,u,g)):
    dots = "."
    dots1 += 1
if eval("({}+6+{}+{}+ 1)%10  == {}".format(v,d,c,e)):
    dots = ".."
    dots2 += 1
if eval("({}+6+{}+{}+ 2)%10  == {}".format(v,d,c,e)):



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



# 112 + 266 + 324 + 36 == 738 	12373468
# 112 + 266 + 326 + 34 == 738 	12373648
# 112 + 266 + 423 + 45 == 846 	12484356
# 112 + 266 + 423 + 46 == 847 	12484367
# 112 + 266 + 425 + 43 == 846 	12484536
# 112 + 266 + 426 + 43 == 847 	12484637
# 112 + 266 + 523 + 56 == 957 	12595367
# 112 + 266 + 523 + 57 == 958 	12595378
# 112 + 266 + 524 + 56 == 958 	12595468
# 112 + 266 + 526 + 53 == 957 	12595637
# 112 + 266 + 526 + 54 == 958 	12595648
# 112 + 266 + 527 + 53 == 958 	12595738
# 112 + 266 + 527 + 58 == 963 	12596783
# 112 + 266 + 528 + 57 == 963 	12596873
# 113 + 366 + 234 + 25 == 738 	13273458
# 113 + 366 + 235 + 24 == 738 	13273548
# 113 + 366 + 432 + 45 == 956 	13495256
# 113 + 366 + 432 + 46 == 957 	13495267
# 113 + 366 + 432 + 47 == 958 	13495278
# 113 + 366 + 435 + 42 == 956 	13495526
# 113 + 366 + 435 + 48 == 962 	13496582
# 113 + 366 + 436 + 42 == 957 	13495627
# 113 + 366 + 436 + 47 == 962 	13496672
# 113 + 366 + 437 + 42 == 958 	13495728
# 113 + 366 + 437 + 46 == 962 	13496762
# 113 + 366 + 438 + 45 == 962 	13496852
# 114 + 466 + 246 + 27 == 853 	14285673
# 114 + 466 + 247 + 26 == 853 	14285763
# 114 + 466 + 342 + 35 == 957 	14395257
# 114 + 466 + 342 + 36 == 958 	14395268
# 114 + 466 + 345 + 32 == 957 	14395527
# 114 + 466 + 345 + 37 == 962 	14396572
# 114 + 466 + 346 + 32 == 958 	14395628
# 114 + 466 + 347 + 35 == 962 	14396752
# 114 + 466 + 347 + 38 == 965 	14396785
# 114 + 466 + 348 + 37 == 965 	14396875
# 115 + 566 + 253 + 24 == 958 	15295348
# 115 + 566 + 254 + 23 == 958 	15295438
# 115 + 566 + 254 + 28 == 963 	15296483
# 115 + 566 + 256 + 27 == 964 	15296674
# 115 + 566 + 257 + 26 == 964 	15296764
# 115 + 566 + 257 + 28 == 966 	15296786
# 115 + 566 + 258 + 24 == 963 	15296843
# 115 + 566 + 258 + 27 == 966 	15296876
# 221 + 166 + 314 + 35 == 736 	21373456
# 221 + 166 + 315 + 34 == 736 	21373546
# 221 + 166 + 315 + 36 == 738 	21373568
# 221 + 166 + 316 + 35 == 738 	21373658
# 221 + 166 + 514 + 56 == 957 	21595467
# 221 + 166 + 514 + 57 == 958 	21595478
# 221 + 166 + 516 + 54 == 957 	21595647
# 221 + 166 + 517 + 54 == 958 	21595748
# 223 + 366 + 134 + 15 == 738 	23173458
# 223 + 366 + 135 + 14 == 738 	23173548
# 224 + 466 + 146 + 17 == 853 	24185673
# 224 + 466 + 147 + 16 == 853 	24185763
# 225 + 566 + 153 + 14 == 958 	25195348
# 225 + 566 + 154 + 13 == 958 	25195438
# 225 + 566 + 154 + 18 == 963 	25196483
# 225 + 566 + 156 + 17 == 964 	25196674
# 225 + 566 + 157 + 16 == 964 	25196764
# 225 + 566 + 157 + 18 == 966 	25196786
# 225 + 566 + 158 + 14 == 963 	25196843
# 225 + 566 + 158 + 17 == 966 	25196876
# 331 + 166 + 214 + 25 == 736 	31273456
# 331 + 166 + 215 + 24 == 736 	31273546
# 331 + 166 + 215 + 26 == 738 	31273568
# 331 + 166 + 216 + 25 == 738 	31273658
# 331 + 166 + 412 + 46 == 955 	31495265
# 331 + 166 + 412 + 47 == 956 	31495276
# 331 + 166 + 412 + 48 == 957 	31495287
# 331 + 166 + 415 + 46 == 958 	31495568
# 331 + 166 + 416 + 42 == 955 	31495625
# 331 + 166 + 416 + 45 == 958 	31495658
# 331 + 166 + 417 + 42 == 956 	31495726
# 331 + 166 + 417 + 48 == 962 	31496782
# 331 + 166 + 418 + 42 == 957 	31495827
# 331 + 166 + 418 + 47 == 962 	31496872
# 332 + 266 + 124 + 16 == 738 	32173468
# 332 + 266 + 126 + 14 == 738 	32173648
# 334 + 466 + 142 + 15 == 957 	34195257
# 334 + 466 + 142 + 16 == 958 	34195268
# 334 + 466 + 145 + 12 == 957 	34195527
# 334 + 466 + 145 + 17 == 962 	34196572
# 334 + 466 + 146 + 12 == 958 	34195628
# 334 + 466 + 147 + 15 == 962 	34196752
# 334 + 466 + 147 + 18 == 965 	34196785
# 334 + 466 + 148 + 17 == 965 	34196875
# 441 + 166 + 312 + 36 == 955 	41395265
# 441 + 166 + 312 + 37 == 956 	41395276
# 441 + 166 + 312 + 38 == 957 	41395287
# 441 + 166 + 315 + 36 == 958 	41395568
# 441 + 166 + 316 + 32 == 955 	41395625
# 441 + 166 + 316 + 35 == 958 	41395658
# 441 + 166 + 317 + 32 == 956 	41395726
# 441 + 166 + 317 + 38 == 962 	41396782
# 441 + 166 + 318 + 32 == 957 	41395827
# 441 + 166 + 318 + 37 == 962 	41396872
# 442 + 266 + 123 + 15 == 846 	42184356
# 442 + 266 + 123 + 16 == 847 	42184367
# 442 + 266 + 125 + 13 == 846 	42184536
# 442 + 266 + 126 + 13 == 847 	42184637
# 443 + 366 + 132 + 15 == 956 	43195256
# 443 + 366 + 132 + 16 == 957 	43195267
# 443 + 366 + 132 + 17 == 958 	43195278
# 443 + 366 + 135 + 12 == 956 	43195526
# 443 + 366 + 135 + 18 == 962 	43196582
# 443 + 366 + 136 + 12 == 957 	43195627
# 443 + 366 + 136 + 17 == 962 	43196672
# 443 + 366 + 137 + 12 == 958 	43195728
# 443 + 366 + 137 + 16 == 962 	43196762
# 443 + 366 + 138 + 15 == 962 	43196852
# 551 + 166 + 214 + 26 == 957 	51295467
# 551 + 166 + 214 + 27 == 958 	51295478
# 551 + 166 + 216 + 24 == 957 	51295647
# 551 + 166 + 217 + 24 == 958 	51295748
# 552 + 266 + 123 + 16 == 957 	52195367
# 552 + 266 + 123 + 17 == 958 	52195378
# 552 + 266 + 124 + 16 == 958 	52195468
# 552 + 266 + 126 + 13 == 957 	52195637
# 552 + 266 + 126 + 14 == 958 	52195648
# 552 + 266 + 127 + 13 == 958 	52195738
# 552 + 266 + 127 + 18 == 963 	52196783
# 552 + 266 + 128 + 17 == 963 	52196873

