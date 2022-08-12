#include <stdio.h>
#define size 100
int f,r;
f = -1;
r= -1;
int q1[size];
int q2[size];

void printStack(){
    int i;
    for( i = f ; i<= r ; ++i){
        printf("%d ",q1[i]);
    }
}


void push(int x){
    int i;
    if(r== -1){
        q1[++r] = x;
        f++;
       
        
    }
    
    else{
       
        for(i = f ; i <= r ; ++i){
            q2[i] = q1[i];
        }
        q1[f] = x;
        for(i = f+1 ; i <= r+1 ; ++i){
            q1[i] = q2[i-1];
        }
        r++;
        printf("\n");
        }
    
}


void pop(){
    if(f==-1){
        printf("Error Popping");
        exit(0);
    }
    else{
        
        printf("Popped Element : %d\nRemaining Elements : ",q1[f++]);
        int i;
        printStack();
        if(f > r){
            f = r = -1;
        }
       
    }
}


int main()
{
    
    int n;
    //pop();
    printf("Enter n value : ");
    scanf("%d",&n);
    for(int i = 0 ; i < n ; ++i){
        int k;
        printf("\n\n1 to push \n2 to pop\n3 to view Stack : ");
        scanf("%d",&k);
        if(k == 1){
            int l;
            printf("\nEnter the element to be pushed : ");
            scanf("%d",&l);
            push(l);
        }
        else if(k == 2){
            pop();
        }
        else if(k == 3){
            printStack();
        }
        else{
            printf("\nInvalid Option\n");
            i = i -1;
        }
    }
    
    printf("\nFinal Contents Of The Stack:\n");
    printStack();
    

    return 0;
}
