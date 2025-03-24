# Baseline for Web Testing in Selenium (Python)

### High-Level Architecture

pytest (runner and tests) -> tasks (interactions decoupled from page objects) -> page objects (locator tuples only)

### What is this? 

It's a baseline for Web Testing in Selenium (Python), intended to be extended. The tests have interactions which have been decoupled from traditional page objects, known here as **tasks**. **page** objects are fed into the tasks. This encourages a task-centric way of creating tests, rather than getting hung up on what interactions and waits to use with which page. This is loosely based on the Screenplay pattern - see: https://www.infoq.com/articles/Beyond-Page-Objects-Test-Automation-Serenity-Screenplay/

#### How to set this up and run it?

1. Git clone as usual
2. Assuming you have Python3 and pytest are on your PATH, run the tests `pytest test_about_page_renders.py`

#### ToDo

1. Make this runnable from the dashboard