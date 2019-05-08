#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <time.h>


/////////////////////////////////////
// Run the code by using           //
// gcc challenge_with_lookup.c -lm //
/////////////////////////////////////


#define IGNORE 6    // enter 6 or 9


// long factorial(int n) 
// {
//     // printf("%d \n", n);
//     if (n == 0)
//         return 1;
//     else
//         return(n * factorial(n-1));
// }
uint32_t factorials[] = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600}; // list of all factorials that fit in an Integer

uint64_t power(uint32_t value, uint32_t power) 
{
    uint64_t out = 1;
    for(int i=0; i < power; i++)
        out *= value;

    return out;
}

uint32_t get_pos(uint64_t p, uint32_t index) 
{
    return( ((uint64_t)(p / power(10, floor(log10(p))-index))) % 10 ); // magic number 7
}

/*
    # https://medium.com/@aiswaryamathur/find-the-n-th-permutation-of-an-ordered-string-using-factorial-number-system-9c81e34ab0c8
*/
uint32_t get_nth_permutation(long in) 
{
    uint32_t out = 0;
    uint32_t length = floor(log10(in)) + 1;

    for(int i=0; i<length; i++) {
        out += get_pos(in, i) * factorials[length - i];
    }
    return out;
}

// See The python file to see how i get to these numbers
//   112 + 266 + 328 + 39 == 745	True    34072202110                          SOLUTION B
//   112 + 266 + 329 + 38 == 745	True    34072241110      <--                 SOLUTION B
//   112 + 266 + 426 + 49 == 853	True    34352120210 
//   112 + 266 + 429 + 46 == 853	True    34352331210 
//   112 + 266 + 527 + 58 == 963	True    34632303210 
//   112 + 266 + 528 + 57 == 963	True    34632342210      <--
//   113 + 366 + 238 + 29 == 746	True    36516202200 
//   113 + 366 + 239 + 28 == 746	True    36516241200      <--
//   113 + 366 + 432 + 47 == 958	True    37154231000                          SOLUTION B
//   113 + 366 + 432 + 46 == 957	True    37154223010 
//   113 + 366 + 437 + 42 == 958	True    37155020000           |              SOLUTION B
//   113 + 366 + 436 + 42 == 957	True    37154523010 
//   113 + 366 + 435 + 48 == 962	True    37156122100 
//   113 + 366 + 438 + 45 == 962	True    37156333100 
//   114 + 466 + 247 + 26 == 853	True    39323200110              SOLUTION A
//   114 + 466 + 247 + 29 == 856	True    39323212000 
//   114 + 466 + 246 + 27 == 853	True    39323111110       -      SOLUTION A
//   114 + 466 + 249 + 27 == 856	True    39323340000 
//   114 + 466 + 342 + 36 == 958	True    39601223100 
//   114 + 466 + 346 + 32 == 958	True    39601523100 
//   114 + 466 + 345 + 37 == 962	True    39603120200 
//   114 + 466 + 347 + 35 == 962	True    39603242200 
//   114 + 466 + 347 + 38 == 965	True    39603310010 
//   114 + 466 + 348 + 37 == 965	True    39603343010 
//   115 + 566 + 254 + 28 == 963	True    42130031210 
//   115 + 566 + 258 + 24 == 963	True    42130331210 
//   221 + 166 + 417 + 49 == 853	True    59170211110                          SOLUTION B
//   221 + 166 + 419 + 47 == 853	True    59170333110       __                 SOLUTION B
//   223 + 366 + 138 + 19 == 746	True    63761202200 
//   223 + 366 + 139 + 18 == 746	True    63761241200      <--
//   224 + 466 + 147 + 16 == 853	True    66565200110              SOLUTION A
//   224 + 466 + 147 + 19 == 856	True    66565212000 
//   224 + 466 + 146 + 17 == 853	True    66565111110       -      SOLUTION A
//   224 + 466 + 149 + 17 == 856	True    66565340000 
//   225 + 566 + 154 + 18 == 963	True    69372031210 
//   225 + 566 + 158 + 14 == 963	True    69372331210 
//   331 + 166 + 412 + 47 == 956	True    86710230200 
//   331 + 166 + 412 + 48 == 957	True    86710232110           /              SOLUTION B
//   331 + 166 + 417 + 42 == 956	True    86711013200 
//   331 + 166 + 418 + 42 == 957	True    86711110110                          SOLUTION B
//   331 + 166 + 417 + 48 == 962	True    86712303200 
//   331 + 166 + 418 + 47 == 962	True    86712342200      <--
//   332 + 266 + 128 + 19 == 745	True    88576202110                          SOLUTION B
//   332 + 266 + 129 + 18 == 745	True    88576241110      <--                 SOLUTION B
//   334 + 466 + 142 + 16 == 958	True    94205223100 
//   334 + 466 + 146 + 12 == 958	True    94205523100 
//   334 + 466 + 145 + 17 == 962	True    94210120200 
//   334 + 466 + 147 + 15 == 962	True    94210242200 
//   334 + 466 + 147 + 18 == 965	True    94210310010 
//   334 + 466 + 148 + 17 == 965	True    94210343010 
//   441 + 166 + 217 + 29 == 853	True    103674211110                         SOLUTION B
//   441 + 166 + 219 + 27 == 853	True    103674333110     __                  SOLUTION B
//   441 + 166 + 312 + 37 == 956	True    104052230200
//   441 + 166 + 312 + 38 == 957	True    104052232110          /              SOLUTION B
//   441 + 166 + 317 + 32 == 956	True    104053013200
//   441 + 166 + 318 + 32 == 957	True    104053110110                         SOLUTION B
//   441 + 166 + 317 + 38 == 962	True    104054303200
//   441 + 166 + 318 + 37 == 962	True    104054342200     <--
//   442 + 266 + 126 + 19 == 853	True    106221120210
//   442 + 266 + 129 + 16 == 853	True    106221331210
//   443 + 366 + 132 + 17 == 958	True    109023231000                         SOLUTION B
//   443 + 366 + 132 + 16 == 957	True    109023223010
//   443 + 366 + 137 + 12 == 958	True    109024020000          |              SOLUTION B
//   443 + 366 + 136 + 12 == 957	True    109023523010
//   443 + 366 + 135 + 18 == 962	True    109025122100
//   443 + 366 + 138 + 15 == 962	True    109025333100
//   552 + 266 + 127 + 18 == 963	True    133743303210 
//   552 + 266 + 128 + 17 == 963	True    133743342210     <--

int get_time() {
    uint64_t t;
    __asm volatile ("rdtsc" : "=A"(t));
    return t;
}

int main() {
    clock_t start_t = clock(); // returns the number of clock ticks elapsed since the program was launched

    uint64_t lookup_table[]={3407220211,3407224111,3435212021,3435233121,3463230321,3463234221,3651620220,3651624120,3715423100,3715422301,3715502000,3715452301,3715612210,3715633310,3932320011,3932321200,3932311111,3932334000,3960122310,3960152310,3960312020,3960324220,3960331001,3960334301,4213003121,4213033121,5917021111,5917033311,6376120220,6376124120,6656520011,6656521200,6656511111,6656534000,6937203121,6937233121,8671023020,8671023211,8671101320,8671111011,8671230320,8671234220,8857620211,8857624111,9420522310,9420552310,9421012020,9421024220,9421031001,9421034301,10367421111,10367433311,10405223020,10405223211,10405301320,10405311011,10405430320,10405434220,10622112021,10622133121,10902323100,10902322301,10902402000,10902352301,10902512210,10902533310,13374330321,13374334221};
    uint64_t *p;
    uint32_t out[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    uint32_t number, i = 0;

    for(p=lookup_table; p<(&lookup_table)[1]; p++) {
        number = get_nth_permutation(*p);
        // printf("%d \n", number);
        // We know for shure that there wil not be a 6 or 9 in the first 3 digits
        if(get_pos(number, 3) != IGNORE && get_pos(number, 4) != IGNORE && get_pos(number, 5) != IGNORE && get_pos(number, 6) != IGNORE && get_pos(number, 7) != IGNORE)
            out[i++] = number;
    }
    
    // while (i > 0)
    //     printf("%d \n", out[--i]);

    // printf("%ld \n", start_time);
    // printf("%ld \n", end_time);

    printf("Total time taken by CPU: %f ms\n", ((double) (clock() - start_t)) / CLOCKS_PER_SEC * 1000);

    return 0;   
}
