*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Input Text  username  jaakko
    Input Password  password  jaakko123
    Input Password  password_confirmation  jaakko123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Input Text  username  p
    Input Password  password  pertti123
    Input Password  password_confirmation  pertti123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Input Text  username  elisa
    Input Password  password  e
    Input Password  password_confirmation  e
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Input Text  username  eeva
    Input Password  password  eevaeeva
    Input Password  password_confirmation  eevaeeva
    Submit Credentials
    Register Should Fail With Message  Password shouldn't only contain a-z

Register With Nonmatching Password And Password Confirmation
    Input Text  username  jaakko
    Input Password  password  jaakko123
    Input Password  password_confirmation  jaakko234
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Input Text  username  kalle
    Input Password  password  kalle123
    Input Password  password_confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username already taken

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
