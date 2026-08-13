# What was added / fixed

All changes are additive or corrective; none of your module code was altered.

| File | Change |
|------|--------|
| `.github/workflows/ci.yml` | **Fixed the broken CI.** The old workflow had no steps (it did nothing). This one installs pytest and runs your `tests/` suite on Python 3.11 & 3.12 — fast, cloud-free, always green on valid code. |
| `LICENSE` | Added MIT license (matches the README badge). |
| `README.md` | Polished with badges + a Mermaid flow diagram. Fixed the "two stages" wording to correctly say **three** modules (01/02/03). **Kept your DeepLearning.AI course disclaimer** — that honesty is exactly right. |

## Recommended: ignore Snowflake secrets

Make sure your `.gitignore` contains this (so credentials never get committed):

```
.streamlit/secrets.toml
__pycache__/
*.pyc
```

## Push it

```powershell
git add -A
git commit -m "Fix CI, add LICENSE, polish README (3 modules, badges)"
git push
```
