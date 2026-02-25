Releasing hnet

Prereqs
- Python 3.9+
- Tools: `pip install --upgrade build twine`
- PyPI credentials or token (optional)

Checklist
1) Bump version in `pyproject.toml` (project.version).
2) Update `CHANGELOG.md` with notable changes.
3) Merge to `main`.
4) GitHub Actions will auto-tag `vX.Y.Z`, build artifacts, and create a GitHub Release.
5) Optional: publishing to PyPI happens if `PYPI_API_TOKEN` is configured in repo secrets.

Manual build/publish (optional)
- Clean old artifacts: `rm -rf dist build *.egg-info`
- Build: `python -m build`
- Verify: `twine check dist/*`
- Upload (TestPyPI): `twine upload --repository testpypi dist/*`
- Upload (PyPI): `twine upload dist/*`

Tips
- CI creates releases only if the version in `pyproject.toml` is new (no existing tag with that version).
- Prefer merge commits for releases; squash/rebase changes history but CI tags after merge, so it’s safe.
- Consider `pipx install .` for local, isolated testing of the CLI.
- For tokens: set `TWINE_USERNAME=__token__` and `TWINE_PASSWORD=<pypi-token>`.
