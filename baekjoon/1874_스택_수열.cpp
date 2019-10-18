#include <stdio.h>

int seq[100001];
int seq_idx = 0;
char op[200001];
int op_idx = 0;
int stack[100001];
int stack_idx = 0;

int main(void)
{
    int n;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++)
        scanf("%d", &seq[i]);

    for(int i = 1; i <= n; i++)
    {
        op[op_idx++] = '+';
        stack[stack_idx++] = i;
        while(stack_idx > 0 && seq_idx < n && stack[stack_idx - 1] == seq[seq_idx])
        {
            op[op_idx++] = '-';
            stack_idx--;
            seq_idx++;
        }
    }

    if(seq_idx < n)
    {
        printf("NO");
        return 0;
    }

    for(int i = 0; i < op_idx; i++)
    {
        printf("%c\n", op[i]);
    }
}