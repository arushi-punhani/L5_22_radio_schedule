# Lab 5 Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest fixes were the naming, docstring, and formatting issues because they were local changes that did not alter how the schedule worked. Removing `eval` was harder because it meant changing the function to accept two show intervals directly instead of accepting a string containing Python code. That made the function safer and gave it a clearer purpose, but also required updating its demonstration call.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

I did not identify a false positive in the current findings. Pylint gave a 10.00/10 score, and Bandit reported no issues. Flake8 still reports two formatting findings: a missing blank line before a function and a line that exceeds its default length limit. Pylint's first run also displayed a warning that it could not write its cache under the user profile; that was an environment permission warning, not a code finding. Running Pylint with `--persistent=n` produced the score without the cache warning.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would run the tools locally before committing, ideally through a pre-commit hook, and run them again in continuous integration for every pull request. I would keep their settings in the repository so that everyone gets the same results. Security findings such as unsafe evaluation or unsafe SQL construction should be reviewed before merging, while style findings can usually be fixed alongside the related code.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The SQL insert now binds values as parameters, so input text is handled as data rather than SQL syntax. The program no longer evaluates arbitrary Python input, and the overlap check states directly what it compares. Snake-case names, docstrings, and clearer formatting make the functions easier to read. Removing the global counter avoids maintaining a second source of schedule state, and removing the unused hardcoded password avoids leaving a credential in the source. Pylint now reports 10.00/10, and Bandit reports no issues; Flake8 still points out two formatting cleanups.
