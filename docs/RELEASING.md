Releasing hnet

Prereqs
- Python 3.9+
- Tools: `pip install --upgrade build twine`
- PyPI credentials or token

Checklist
1) Bump version in `pyproject.toml` (project.version).
2) Update `CHANGELOG.md` with notable changes.
3) Clean old artifacts:
   - `rm -rf dist build *.egg-info`
4) Build sdist + wheel:
   - `python -m build`
5) Verify artifacts:
   - `twine check dist/*`
6) Test publish to TestPyPI (optional):
   - `twine upload --repository testpypi dist/*`
7) Publish to PyPI:
   - `twine upload dist/*`
8) Tag and push git tag:
   - `git tag vX.Y.Z && git push origin vX.Y.Z`

Tips
- Consider `pipx install .` for local, isolated testing of the CLI.
- For tokens: set `TWINE_USERNAME=__token__` and `TWINE_PASSWORD=<pypi-token>`.

