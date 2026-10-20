# Workflow commands

GitHub repository: https://github.com/adityakittad1/Git_and_GitHub_Adity

SSH authentication succeeded from WSL. The repository was pushed and GitHub confirmed branches `main`, `Adity`, `Adity_new`, `master_1`, and `master_2`.

```bash
git remote add origin git@github.com:adityakittad1/Git_and_GitHub_Adity.git
git push -u origin main
git push origin Adity Adity_new master_1 master_2
git ls-remote --heads origin
```

The assignment also asks for a fresh SSH clone. The existing local history was pushed over SSH; a separate fresh clone has not been captured. To demonstrate it, run from the parent directory:

```bash
git clone git@github.com:adityakittad1/Git_and_GitHub_Adity.git Git_and_GitHub_Adity_clone
```

The ZIP is ready for the submission portal. The portal URL was not included in the supplied guidelines, so the upload remains outstanding.
