int memo[100];
int f(int n){
  if (memo[n] != 0) return memo[n];
  if (n == 1 || n == 2) return 1;
  memo[n] = f(n - 1) + f(n - 2);
  return memo[n];
}