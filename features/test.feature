Feature: ONET homepage opens
  Scenario: Logo of ONET is present on homepage
    Given launch Chrome browser
    When open onet.pl homepage
    Then verify logo is present on the homepage
    And close browser