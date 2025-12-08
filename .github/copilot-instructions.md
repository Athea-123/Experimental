**Standardizer Component (pyclense/standardizer.py)**

- **Purpose:**: The `Standardizer` class implements a collection of in-place dataframe normalization helpers (dates, casing, whitespace, boolean normalization, special-character removal). It is designed to be used as a fluent API that mutates `self._df` and returns `self` for chaining.
- **Location:**: `pyclense/standardizer.py`

**Key Methods & Behavior**
- **`standardize_dates`**: Converts listed columns to datetime then formats with `strftime`. Default format is `'%m/%d/%Y'`.
- **`capitalize_names`**: Title-cases text in specified columns (`.str.title()`).
- **`convert_to_lowercase`**: Lowercases specified text columns.
- **`fix_whitespace`**: If `columns=None`, operates on all object dtype columns; strips outer whitespace and collapses internal runs of whitespace (`r'\\s+'`). Logs a simple metric of how many multi-space occurrences were found before fix.
- **`remove_special_chars`**: Removes non-alphanumeric characters via regex `r'[^a-zA-Z0-9\\s]'` (note: this removes diacritics and non-Latin characters, and will drop emojis).
- **`standardize_booleans`**: Maps common string representations (`yes/no/y/n/true/false/1/0`) to Python booleans using a `bool_map`.

**Patterns & Conventions for AI Agents**
- **Fluent, in-place API**: Each method returns `self` so allow chaining (e.g. `s.standardize_dates(['dob']).convert_to_lowercase(['name'])`). Use this pattern when adding new transformations.
- **Data storage**: The `DataFrame` is stored on `self._df` (set by `BaseCleaner.__init__`). Use and update that attribute rather than returning new DataFrames.
- **Logging changes**: The `Standardizer` calls a logging helper (`self._log_change(...)`) to record operations and small metadata. Inspect `pyclense/base.py` to align with the project's logging API before adding or calling log helpers.

**Discovered Inconsistencies / Bugs (important)**
- **Logging API mismatch**: `Standardizer` calls `self._log_change(...)`, but `BaseCleaner` (in `pyclense/base.py`) exposes `record_change(...)` and `get_log()`; there is no `_log_change` defined. Agents should prefer editing `Standardizer` to call `record_change` or add a compatible `_log_change` shim in `BaseCleaner`.
- **Getter naming mismatch**: `BaseCleaner` provides `get_data()` while `standardizer.py` defines a `get_dataframe` function (but it is currently defined at module level rather than as a class method). Either use `get_data()` or move/rename the helper into `Standardizer` to match expectations.
- **Indentation / method placement bug**: `clean` and `get_dataframe` in `pyclense/standardizer.py` are defined at module scope (not as methods on `Standardizer`). Agents editing code should move them into the `Standardizer` class and implement `clean(self)` to satisfy `BaseCleaner`'s abstract method.
- **`standardize_dates` reliability**: `pd.to_datetime(..., errors='coerce')` produces `NaT` for invalid dates; calling `.dt.strftime(...)` may yield `NaT` or raise in some pandas versions. Consider using `.dt.strftime(format).fillna('')` or applying `lambda` with try/except for robust behavior.
- **`standardize_booleans` mapping gaps**: Values not in `bool_map` become `NaN`. If the project expects `False`/`True` only, add a `.fillna(False)` or expand the map; otherwise preserve `NaN` intentionally and document it.

**Examples**
- Basic usage (intended):

```py
from pyclense.standardizer import Standardizer

st = Standardizer(df)
st.standardize_dates(['dob'])\\
  .fix_whitespace(['name', 'address'])\\
  .convert_to_lowercase(['email'])
clean_df = st.get_data()  # preferred BaseCleaner API
```

- If you change the code to expose `get_dataframe()` on the class, update callers accordingly.

**When making edits**
- **Prefer minimal, focused changes**: fix the logging/ getter naming mismatch and move `clean`/`get_dataframe` into the class first. This keeps the public API stable and prevents widespread ripple fixes.
- **Unit tests**: Update or add tests in `test_standardizer.py` to assert both happy-path and edge cases (invalid dates, unseen boolean strings, presence of NaN after mappings).
- **Document behavioral decisions**: If you choose to coerce unknown boolean strings to `False` or to remove diacritics in `remove_special_chars`, add a short comment in the method and update this file.

**Files to inspect when changing Standardizer**
- `pyclense/standardizer.py` — implementation and current bugs.
- `pyclense/base.py` — base APIs: `__init__`, `get_data()`, `record_change()`, `get_log()`, and abstract `clean()`.
- `test_standardizer.py` and `test.py` — existing tests and usage examples to update.

If any part of the `Standardizer` behavior should be changed (for example, how NaNs are handled after boolean mapping), tell me which option you prefer and I can implement and update tests accordingly.

---
Request: Please confirm whether you'd like me to (A) patch `pyclense/standardizer.py` to fix the method placement and logging name mismatch, or (B) instead update `pyclense/base.py` to add a `_log_change` shim and `get_dataframe()` alias. I can implement either and update tests.
