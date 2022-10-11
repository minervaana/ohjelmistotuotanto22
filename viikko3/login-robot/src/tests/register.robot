*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kallehei123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  onjo  joujoujouu22
    Output Should Contain  User with username onjo already exists

Register With Too Short Username And Valid Password
    Input Credentials  o  joujoujouu222
    Output Should Contain  Username must be longer than 2 characters

Register With Valid Username And Too Short Password
    Input Credentials  ooe  jou1
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ulle  kahdeksanmerkkia

*** Keywords ***
Input New Command And Create User
    Create User  onjo  helloworld123
    Input New Command
