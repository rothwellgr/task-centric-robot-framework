# task-centric-robot-framework

### High-Level Architecture

pytest at the moment (runner and tests) -> tasks (interactions decoupled from page objects) -> page objects (locator tuples only)

### What is this? 

It's a minimal (MVP if you like) task-centric Selenium test in Python, intended to be extended. I am
to add Robot Framework and more tests to this asap. The tests have interactions which have been decoupled from traditional page objects, known here as **tasks**. **page** objects are fed into the tasks. This encourages a task-centric way of creating tests, rather than getting hung up on what interactions and waits to use with which page. This is (very) loosely based on the Screenplay pattern - see: https://www.infoq.com/articles/Beyond-Page-Objects-Test-Automation-Serenity-Screenplay/

#### How to set this up and run it?

1. Git clone as usual
2. Assuming you have Python3 and pip3 on your PATH, install Robot Framework first `pip install robotframework`
3. Then install Robot Framework's Selenium library `pip install --upgrade robotframework-seleniumlibrary`
4. Run the tests `pytest test_about_page_renders.py`