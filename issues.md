# Static Analysis Issues

The high and medium severity items below were identified in the original version of `radio_schedule.py`. The current status reflects the cleaned version.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL built by string interpolation — fixed | Security, high (manual review) | 11 | Show and host text were inserted directly into SQL. Quotes could break the query, and crafted input could alter it. | Use SQLite placeholders (`?`) and pass values separately to `execute`. |
| `eval` on caller input — fixed | Security, high (Pylint W0123) | 21 | `eval` can execute arbitrary Python expressions rather than just checking schedule times. | Replace formula evaluation with an explicit interval comparison using start times and durations. |
| Hardcoded studio password — fixed | Security, medium (manual review) | 5 | A password was embedded in source and was unused by the program. | Remove the unused credential instead of keeping a secret in source code. |
| Catching every exception — fixed | Robustness, medium (Pylint W0718) | 22 | A broad `except Exception` hid unrelated programming errors and returned the same result for all failures. | Remove the catch-all along with `eval`; the explicit overlap calculation has no broad exception handler. |
| Global booking counter — fixed | Maintainability, low (Pylint W0603) | 6, 10 | `addSlot` mutated module-level state to track minutes even though the database already stores the slots. | Remove the counter and query the database directly for morning shows. |
| Module-level definitions too close together — outstanding | Style, low (Flake8 E302) | 11 (current) | There is no two-blank-line separation before `add_slot`. | Add the required blank lines between the module setup and function definition. |
| SQL statement exceeds the Flake8 line limit — outstanding | Style, low (Flake8 E501) | 14 (current) | The parameterized `INSERT` statement is longer than Flake8's 79-character default. | Split the SQL string across adjacent string literals or otherwise format it below the configured limit. |

## Current analysis results

- Pylint: **10.00/10** (`.venv\Scripts\pylint.exe --persistent=n radio_schedule.py`)
- Bandit: **No issues identified** (`.venv\Scripts\bandit.exe -r radio_schedule.py`)
- Flake8: two style findings remain: E302 and E501 above (`.venv\Scripts\flake8.exe radio_schedule.py`)
