Feature: Create Quiz
  As a teacher, I should be able create multiple quizzes with questions

  Scenario: Create quiz without questions
    Given I fill in the details of the quiz without questions
    When I click the submit button
    Then I expect to see an error message

  Scenario: Create quiz with all the required fields
    Given I fill in all the details of the quiz
    When I click the submit button
    Then I expect to see a success message

  Scenario: Create quiz without filling any field
    Given I don't fill in any of the details of the quiz
    When I click the submit button
    Then I expect to see an error message

Feature: Assign Quiz
  As a teacher, I should be able to assign quizzes to students

  Scenario: Assign quiz to a student
    Given I am on the quiz details page
    When I click the assign quiz button
    And I select the student to assign a quiz in the popup menu
    Then I expect to see a success message

Feature: Solve questions in the quiz
  As a student, I should be able to solve the questions in the
  quiz by clicking on the preferred choice or choices

  Scenario: No questions answered
    Given I am on the quiz questions page
    Then I expect the submit button to be disabled

  Scenario: One or more questions answered
    Given I am on the quiz questions page
    When I answer one or more questions
    Then I expect the submit button to active
    And The button text should remind that this is a partial submission

  Scenario: All questions anwsered
    Given I am on the quiz questions page
    When I answer all questions
    Then I expect the submit button to active
    And The button text should remind that this is a final submission

  Scenario: Returning to quiz after a partial submission
    Given I return to a partial completed quiz
    Then I expect the previously answered questions to be disabled

Feature: Grading quizzes
  As a student, I should be able to see my total score
  after fully completing the quiz

  Scenario: Making a complete submission
    Given I am on the quiz questions page
    When I answer all questions
    And I make a complete submission
    Then I should be redirected to a page with my total score

Feature: Total grade accumulated
  As a teacher, I should be able to compute
  my students accumulated grade

  Scenario: Making a complete submission
    Given I am on the student list page
    When I click on a student
    Then I should see a modal with the button for calculating the accumulated grade
    When I click on the button
    Then The student accumulated score should be displayed

  Scenario: Students dashboard
    Given I am on the student dashboard
    Then I should see the accumulated score widget

