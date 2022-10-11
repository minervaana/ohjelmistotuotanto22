*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kallehei123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kalle  kalle124
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  nonexistent  nopassword
    Output Should Contain  Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kallehei123
    Input Login Command