# Git and GitHub Flask workflow

This commit adds the complete Flask project guide on the Adity branch. The project demonstrates a JSON API, a MongoDB-backed to-do POST route, and the requested Git branching workflow.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Start MongoDB locally, or set `MONGODB_URI` and optionally `MONGODB_DATABASE`.
4. Run `python app.py` and open http://127.0.0.1:5000.

The `/api` route returns the project's JSON data. Submit the browser form to `/submittodoitem`; successful submissions are saved in MongoDB. If MongoDB is unreachable, the API responds with HTTP 503 and a JSON error.

See `SUBMISSION_REPORT.docx` for the task walkthrough, command evidence, and remote publication checklist.
