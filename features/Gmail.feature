Feature: Google Mail login
  Scenario: Login to mail account
    Given launch Chrome browser
    When I open Google homepage
    And click on GMAIL shortcut
    And click on login button
    And provide as username "username"
    And click Next
    And provide as password "password"
    And click login button
    Then login into mail is successful