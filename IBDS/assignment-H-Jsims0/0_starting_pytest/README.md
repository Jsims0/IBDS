# Introducing Software Testing
In this practical we are going to see how testing can be used to
aid software development. First watch this video:

* *"Software Testing"*
   First watch this presentation on Software testing
  * [Software testing introduction presentation (Travis video)](
https://canvas.anglia.ac.uk/courses/12178/external_tools/retrieve?display=borderless&url=https%3A%2F%2Fhierarchy.talis.com%2F1%2Fanglia%2Fintegrations%2Flti1%2F1%2Fassets%2Fplayerresource%2F5dc947e894073d95425cb8cb) (requires ARU Login.
  * ["Software Testing" Powerpoint slides](
   https://1drv.ms/p/s!AjeHBmwgk7Hto1USV9VWha1ny9jG)

## Using `pytest` for testing
In this practical you are going to start using 'Unit tests'
where individual 'units' of code are tested.
At this stage we will be testing individual functions
and the tests are a set of function input parameters
and expected return values.

Unit testing forms an important part of modern software development,
for more information see the Wikipedia page: 
https://en.wikipedia.org/wiki/Unit_testing

The Python standard library has a reasonable unit testing module called `unittest`
but using its syntax is difficult to use (there is a lot of 'boiler-plate'). So
we will be using `pytest` as it is easier to understand and use in practice. The
first thing to do is to check that you have pytest installed:

* From the OSX (or Linux) command prompt issue the command `pytest --version`.
  This should produce output showing the `pytest` command works and giving you
  version information:
  ```
  $ pytest --version
  This is pytest version 3.2.1, imported from /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest.py
  setuptools registered plugins:
    pytest-cov-2.6.0 at /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest_cov/plugin.py
  ```
  If instead of this you get a response like `-bash: pytest: command not found` then 
  pytest has not been installed. 
  To install pytest See https://docs.pytest.org/en/latest/getting-started.html#install-pytest 
  and if you continue to have problems ask for help, see
  [Help with programming (Module Canvas page)](
  https://canvas.anglia.ac.uk/courses/1490/pages/help-with-programming).

## Exercises: Using pytest to unit test code 

These are follow-me exercises to introduce `pytest` unit tests.

* First print out (or view) a reference card on pytest:
  *  [pytest_basic_usage_reference_card.pdf](
     ../.instructions/0_starting_pytest/pytest_basic_usage_reference_card.pdf)
     (PDF for printing)
  *  [pytest_basic_usage_reference_card.md](
     ../.instructions/0_starting_pytest/pytest_basic_usage_reference_card.md)
     (markdown for viewing)

* Then view and follow along the follow-me exercise videos:
  * *"Introducing pytest"*
    * [![ MyPlayer Introducing pytest Video](
      ../.instructions/0_starting_pytest/h0b_myplayer_screenshot.png?raw=true)](
      https://myplayer.anglia.ac.uk/Player/9848 "MyPlayer Run Thru Video")
      [*MyPlayer link*](https://myplayer.anglia.ac.uk/Play/9848)
    * GitHub links to the commits made in video 
      * [Fixed bug in test_add_one now passes all tests:](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/8296e7d333b6a64adf0386f6a920e5e20560be3e)
      * [fix up example test comparisons so all tests pass.](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/475dde0de1c60ecc57e33c01de440ef3986669c0)
  * *"Practical Example of pytest"*
    * [![MyPlayer Practical Example of pytest Video](
      ../.instructions/0_starting_pytest/h0c_myplayer_screenshot.png?raw=true)](
      https://myplayer.anglia.ac.uk/Player/9849 "MyPlayer Practical Example of pytest Video")
      [*MyPlayer link*](https://myplayer.anglia.ac.uk/Play/9849)
    * GitHub links to the commits made in video 
      * [pytests for count_vowels function](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/696db39b5ee4a503e8be435bcf218e4cbb3be415)
      * [First version of count_vowels function](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/3d0da4b94bf2e17467fe7c0eb366d17c52dc8d9f)
      * [count_vowels function, all pytests pass](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/a301fd3b7702fda38e619efec75f7078816d1b0f)

<hr>

*Back to:* [Instructions for Assignment H: Unit tests and File IO](../.instructions/README.md)
