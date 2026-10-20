# Git and GitHub Flask workflow

This project demonstrates a Flask JSON API, a browser to-do form, a MongoDB POST endpoint, and the requested Git branch, merge, conflict, commit, reset, and rebase workflow.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Start MongoDB locally, or set `MONGODB_URI` and optionally `MONGODB_DATABASE`.
4. Run `python app.py` and open http://127.0.0.1:5000.

The `/api` route returns a JSON project status. Submit the form to `/submittodoitem`; successful submissions are stored in MongoDB. If MongoDB is unreachable, the API responds with HTTP 503 and an explanatory JSON error.

See `SUBMISSION_REPORT.docx` for the task walkthrough, commands, repository-history evidence, and the external publication steps that still require the owner's GitHub and portal access.
