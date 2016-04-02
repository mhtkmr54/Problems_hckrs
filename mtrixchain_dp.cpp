#include<stdio.h>
#include<stdlib.h>
#include<limits.h>


int MatrixOrder(int p[], int n);
int verify(int row[],int col[],int no_of_mat);

int main()
{
    int no_of_mat;
    scanf("%d",&no_of_mat);
    
    int *row=(int*)malloc(sizeof(int)*no_of_mat);
    int *col=(int*)malloc(sizeof(int)*no_of_mat);
    int i,j;
    for (i=0;i<no_of_mat;i++)
    {
	scanf("%d",&row[i]);
	scanf("%d",&col[i]);
    }
    int ans=verify(row,col,no_of_mat);
    if(ans == -1 )
    printf("Error");
    else 
    {
	int size = no_of_mat+1;
    	int *arr=(int*)malloc(sizeof(int)*(size));
	    arr[0]=row[0];
	    for (j=1;j<no_of_mat+1;j++)
	    {
	    	arr[j]=col[j-1];
	    }
 		 printf("%d",MatrixOrder(arr, size));
      }
    return 0;
}
int MatrixOrder(int p[], int n)
{
    int m[n][n]; 
    int i, j, k, L, q;
    for (i = 1; i < n; i++)
        m[i][i] = 0;
     for (L=2; L<n; L++)   
    {
        for (i=1; i<=n-L+1; i++)
        {
            j = i+L-1;
            m[i][j] = INT_MAX;
            for (k=i; k<=j-1; k++)
            {
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
                if (q < m[i][j])
                    m[i][j] = q;
            }
        }
    }
 
    return m[1][n-1];
}

int verify(int row[],int col[],int no_of_mat){
    int ans=1;
    int i;
    for (i=0;i<no_of_mat-1;i++){
        if(col[i]==row[i+1])
            ans=1;
        else {
            ans=-1;
            return ans;
        }
    }
return ans;
}
