#include<iostream>
using namespace std;

int main()
{
    int t;
    cout<<"Target value: ";
    cin>>t;
    int a[] ={1,1,3,2,1};
    int n= sizeof(a)/sizeof(a[0]);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(a[j]==t){
                for(int k =j;k<n;k++)
                {
                   a[k]=a[k+1];
                }
                a[n-1]=t;
            }
        }
    }
    for(int i =0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
}