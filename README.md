# MoodPy teaching archive

This repository contains historical course material, Moodle question-bank exports, notebooks, and a small number of source scripts. The folders are organized by discipline and academic term to make the archive easier to browse.

## Browse the collection

- [Full collection catalog](CATALOG.md) lists each collection, its former folder name, and file counts by type.
- `courses/<discipline>/<term>/<collection>/` contains course materials and working notebooks.
- `question-banks/<term>/<subject>/` contains exported Moodle question banks.
- `courses/*/undated/` is used when the source did not identify an academic term.

Academic term labels use lowercase `YYYY-term` names, such as `2019-2`; Roman numerals in source semester labels are written in lowercase. Original filenames and the contents of all archived files are preserved. The catalog records the former folder names.

## Use with care

These files are historical references, not verified Moodle recipes. XML files are archived exports and have not all been checked for valid Moodle imports or answer correctness. Notebooks and scripts may rely on old package versions or local data. Review them before reuse, and do not execute archived Python or notebook code without inspecting it.

Editor checkpoints, compiled `.pyc` files, temporary outputs, and other historical artifacts remain alongside the course material so the archive stays complete; they are not runnable authoring inputs. For new agent-assisted quizzes in an enclosing MoodPy checkout, use `../examples/agent_workflow/` and follow `../docs/authoring-guide.md`.
