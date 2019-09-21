#include <cstring>
#include <iostream>

using namespace std;

int main(void)
{
    char word[] = "Hi man";
    char insult[] = "fxxking";
    char text[20];
    char copy[20];

    strcpy(text, word);
    strcat(text, insult);
    cout << text << endl;
    cout << word << endl;

    cout << strcmp(text, word) << endl;
    cout << strlen(text) << endl;


    // strcat(word, insult);
    // cout << word << endl;

    return 0;
}