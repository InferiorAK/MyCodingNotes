// Author: InferiorAK
// 1² + 3² + 5² + 7² + ....... + N²
#include <stdio.h>

int main()
{
    int sum = 0, a, n;
    scanf("%d", &n);
    for (a = 1; a <= n; a += 2)
    {
        sum += a * a;
    }
    printf("%d", sum);
    return 0;
}
