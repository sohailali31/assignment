
#include <iostream>
#include <cstdlib>
#include <string>
#include <bits/stdc++.h>
using namespace std;

const int MAX_ACCTS = 100;
const double INIT_BAL = 0.0;

struct Acct {
    string usr;
    string pwd;
    double bal;
};

Acct accts[MAX_ACCTS];

void printIntroMenu();
void printMainMenu();
void begin();
void userLogin();
void createNewAcct();
void withdrawFunds(Acct& a);
void depositFunds(Acct& a);
void checkBalance(Acct& a);

char menuSelection;

int main() {
    cout << "Welcome to Secure Bank ATM!" << endl;
    begin();
    return 0;
}

void printIntroMenu() {
    cout << "Please choose an option:" << endl;
    cout << "L -> Login" << endl;
    cout << "C -> Create Account" << endl;
    cout << "Q -> Quit" << endl;
    cout << "> ";
}

void printMainMenu() {
    cout << "D -> Deposit Funds" << endl;
    cout << "W -> Withdraw Funds" << endl;
    cout << "R -> Check Balance" << endl;
    cout << "Q -> Quit" << endl;
    cout << "> ";
}

void begin() {
    printIntroMenu();
    cin >> menuSelection;
    switch(menuSelection) {
        case 'L':
            userLogin();
            break;
        case 'C':
            createNewAcct();
            break;
        case 'Q':
            exit(0);
            break;
        default:
            cout << "Invalid input. Please try again." << endl;
            begin();
    }
}

void userLogin() {
    string usr, pwd;
    cout << "Enter your username: ";
    cin >> usr;
    cout << "Enter your password: ";
    cin >> pwd;

    bool loggedIn = false;
    for (const auto& a : accts) {
        if (a.usr == usr && a.pwd == pwd) {
            loggedIn = true;
            break;
        }
    }

    if (loggedIn) {
        cout << "Login successful!" << endl;
        Acct currentAcct;
        for (const auto& a : accts) {
            if (a.usr == usr) {
                currentAcct = a;
                break;
            }
        }
        printMainMenu();
        cin >> menuSelection;
        switch(menuSelection) {
            case 'D':
                depositFunds(currentAcct);
                break;
            case 'W':
                withdrawFunds(currentAcct);
                break;
            case 'R':
                checkBalance(currentAcct);
                break;
            case 'Q':
                exit(0);
                break;
            default:
                cout << "Invalid input. Returning to main menu." << endl;
                begin();
        }
    } else {
        cout << "Login failed. Invalid username or password." << endl;
        begin();
    }
}

void createNewAcct() {
    string usr, pwd;
    cout << "Enter a new username: ";
    cin >> usr;
    cout << "Enter a new password: ";
    cin >> pwd;

    for (const auto& a : accts) {
        if (a.usr == usr) {
            cout << "Account creation failed. Username already exists." << endl;
            begin();
        }
    }

    for (auto& a : accts) {
        if (a.usr.empty()) {
            a.usr = usr;
            a.pwd = pwd;
            a.bal = INIT_BAL;
            cout << "Account created successfully!" << endl;
            begin();
        }
    }

    cout << "Account creation failed. Maximum accounts reached." << endl;
    begin();
}

void depositFunds(Acct& a) {
    double amt;
    cout << "Enter the amount to deposit: $";
    cin >> amt;
    if (amt > 0) {
        a.bal += amt;
        cout << "Deposit successful. Current balance: $" << a.bal << endl;
    } else {
        cout << "Invalid amount. Please enter a positive value." << endl;
    }
    begin();
}

void withdrawFunds(Acct& a) {
    double amt;
    cout << "Enter the amount to withdraw: $";
    cin >> amt;
    if (amt > 0 && amt <= a.bal) {
        a.bal -= amt;
        cout << "Withdrawal successful. Current balance: $" << a.bal << endl;
    } else if (amt > a.bal) {
        cout << "Insufficient balance." << endl;
    } else {
        cout << "Invalid amount. Please enter a positive value." << endl;
    }
    begin();
}

void checkBalance(Acct& a) {
    cout << "Your current balance is: $" << a.bal << endl;
    begin();
}
