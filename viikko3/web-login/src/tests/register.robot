*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  jaakko
    Set Password  jaakko123
    Set Confirmation Password  jaakko123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  p
    Set Password  pertti123
    Set Confirmation Password  pertti123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  elisa
    Set Password  e
    Set Confirmation Password  e
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  eeva
    Set Password  eevaeeva
    Set Confirmation Password  eevaeeva
    Submit Credentials
    Register Should Fail With Message  Password shouldn't only contain a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  jaakko
    Set Password  jaakko123
    Set Confirmation Password  jaakko234
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Username already taken

Login After Successful Registration
    Set Username  jaakko
    Set Password  jaakko123
    Set Confirmation Password  jaakko123
    Submit Credentials
    Go To Login Page
    Set Username  jaakko
    Set Password  jaakko123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  jaakko
    Set Password  jaakko123
    Set Confirmation Password  jaakko234
    Submit Credentials
    Register Should Fail With Message  Passwords don't match
    Go To Login Page
    Set Username  jaakko
    Set Password  jaakko123
    Click Button  Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password
# ...

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
