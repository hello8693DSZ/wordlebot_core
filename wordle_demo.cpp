#include<bits/stdc++.h>
#include<conio.h>
using namespace std;
#define int long long
#define endl '\n'
const int green=1;
const int grey=0;
const int yellow=-1;
int len;
void printgreen(char c){
    printf("\033[42m\033[31m %c ",c);
}
void printgrey(char c){
    printf("\033[47m\033[30m %c ",c);
}
void printyellow(char c){
    printf("\033[43m\033[30m %c ",c);
}
void printendl(){
    printf("\033[0m\n");
}
void printwordle(string ans,string guess){
    vector<int>color(len);
    map<char,int>mp;
    for(int i=0;i<len;i++){
        if(ans[i]==guess[i]){
            color[i]=green;
        }
        else{
            mp[ans[i]]++;
        }
    }
    for(int i=0;i<len;i++){
        if(color[i]==0){
            if(mp[guess[i]]){
                color[i]=yellow;
                mp[guess[i]]--;
            }
            else{
                color[i]=grey;
            }
        }
    }
    for(int i=0;i<len;i++){
        if(color[i]==green){
            printgreen(guess[i]);
        }
        else if(color[i]==yellow){
            printyellow(guess[i]);
        }
        else{
            printgrey(guess[i]);
        }
    }
    printendl();
}
vector<string>mem;
signed main(){
    int cnt=0;
    string word;
    cin>>word;
    len=word.size();
    system("cls");
    while(1){
        string guess;
        cin>>guess;
        guess.resize(len,' ');
        cnt++;
        mem.push_back(guess);
        system("cls");
        for(int i=0;i<mem.size();i++){
            printwordle(word,mem[i]);
        }
        if(guess==word){
            cout<<mem.size()<<" tries"<<endl;
            return 0;
        }
        if(guess[0]=='*'){
            cout<<"You gave up. What a loser."<<endl;
            cout<<"The word was "<<word<<endl;
        }
    }
    return 0;
}
