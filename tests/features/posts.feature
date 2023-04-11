@posts
Feature: Posts API Tests
  As a engineer I want to test the POST endpoints
  So that I am confident that all the CRUD operations work as expected

  @get_posts
  Scenario: User retrieves the list of posts
    When I send a GET request to /posts
    Then I get a 200 status code from GET request
    And I see all the posts in the response

  @get_post
  Scenario: User retrieves a single post information
    When I send a GET request to /posts/4
    Then I get a 200 status code from GET request
    And I post id from GET response is 4

  @create_post
  Scenario: User creates a new post
    When I send a POST request to /posts
    Then I get a 201 status code from POST request
    And I post id from POST response is 101

  @update_post
  Scenario: User updates an existing post
    When I send a PUT request to /posts/6
    Then I get a 201 status code from POST request
    And I post id from PUT response is 6

  @patch_post
  Scenario: User updates a title of a post
    When I send a PATCH request to /posts/6
    Then I get a 201 status code from POST request
    And I post id from PUT response is 6

 @delete_post
  Scenario: User deletes an existing post
    When I send a DELETE request to /posts/7
    Then I get a 200 status code from DELETE request

  @invalid_url
  Scenario: Invalid URL returns a not found error
    When I send a GET request to /post
    Then I get a 404 status code from GET request



