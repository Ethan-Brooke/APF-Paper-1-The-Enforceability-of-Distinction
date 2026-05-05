# NEXT_STEPS — Push the refreshed Paper 1 repo to GitHub

The repo at `Codebase/APF-Paper-1-The-Enforceability-of-Distinction/` has been refreshed end-to-end (2026-05-04 LATER):

- Paper 1 main v5.0 → **v5.2**
- Paper 1 supplement v8.81 → **v8.31** (κ_int + R1-R4 closures)
- Codebase v7.3 → **v7.8** (with `apf/kappa_int_bounds.py` bundled)
- README, START_HERE, REVIEWERS_GUIDE, ai_context/* all template-regenerated
- Colab notebook `APF_Reviewer_Walkthrough.ipynb` regenerated
- `interactive_dag.html` regenerated
- `MANIFEST.custom` seeded for custom-content preservation discipline

The push to GitHub requires your local credentials. Two paths:

## Path A — Push from this Drive-synced directory directly

```bash
cd "C:\Users\EthanBrooke\My Drive\__APF Library\Codebase\APF-Paper-1-The-Enforceability-of-Distinction"
git init -b main
git remote add origin https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction.git
git add -A
git commit -m "Refresh: Paper 1 sup v8.31 + κ_int + R1-R4 + codebase v7.8"
git push -u origin main --force
```

## Path B — Pull from the pre-built zip on outputs/

A zip with a clean working .git/ directory is at `outputs/APF-Paper-1-refresh-with-git_2026-05-05.zip`:

1. Unzip somewhere outside Drive (to avoid Drive sync conflicts with .git/)
2. cd into the unzipped `paper1_repo_git/` directory
3. Verify: `git log --oneline | head -3` should show one commit
4. Push: `git push -u origin main --force`

The commit message documents what landed.

## Path C — Patch your existing local clone

If you have a local clone of the GitHub repo elsewhere on disk:

1. cd to your local clone
2. Mirror the Drive-synced state: `rsync -av --delete --exclude=.git "C:\path\to\Drive\Codebase\APF-Paper-1.../" .`
3. `git add -A && git commit -m "..." && git push --force`

---

After push, optionally mint a new Zenodo version on the existing concept DOI (10.5281/zenodo.18604678 for the main paper; 10.5281/zenodo.19714958 for the standalone supplement). The current zenodo.json carries the existing DOI as a `related_identifier`; minting a new version is a manual action via Zenodo's web UI after the GitHub push triggers the webhook.
