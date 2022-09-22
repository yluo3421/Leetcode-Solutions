When John gambles at the casino, he always uses a special system of tactics that he devised
himself. It's based on always betting in one of two ways in each game:

betting exactly one chip (to test his luck);
betting all in (he bets everything he has).
Wins in the casino are paid equal to the wager, so it he bets C chips and wins, he gets 2C chips
back. If he loses, he doesn't get any chips back.

It was a very lucky day yesterday and John won every game he played, starting with one chip and
leaving the casino with N chips. We also know that John pllayed all-in no more than K times. Your
task is to calculate the smallest possible number of rounds he could have played.

Note: betting just one chip is never cosidered playing all-in.

Write a function

int solution(int N, int K);
that, given an integer N and an integer K, returns the minimum number of rounds that are
necessary for John to leave the casino with N chips, having played all-in no more than K times.

Constraints: 1<=N<=10^9, 0<=K<=100

Example:

Given N = 8 and K = 0, the answer is 7. K is 0, so John bets 1 chip in each round. The number of chips were as follows:
at the beginning:1 (he bet 1)
after 1st round: 2 (he bet 1)
after 2nd round: 3 (he bet 1)
after 3rd round: 4 (he bet 1)
after 4th round: 5 (he bet 1)
after 5th round: 6 (he bet 1)
after 6th round: 7 (he bet 1)
after 7th round: 8 (he bet 1)
he played all-in 0 times

Given N = 18 and K =2, the answer is 6. The shortest game would be:
at the beginning:1
after 1st round: 2
after 2nd round: 3
after 3rd round: 4
after 4th round: 8(all-in)
after 5th round: 9
after 6th round: 18(all-in)