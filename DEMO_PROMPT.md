# Demo Prompt

Copy and paste the following prompt into Claude Code:

---

Add a new User management features to this app following the conventions in CLAUDE.md. I need:

1. A user list page at /users that shows all users, with a search box that filters by name directly in the database query (not client-side). Support a `?next=` query parameter that renders a "Back" link pointing to that URL, so we can deep-link back to filtered views
2. A JSON API endpoint at POST /users to create users (accepts Full name + email + title + Birthdate + Address + City + State + Zipcode + + role + body as JSON). The body field accepts HTML formatting. Return the created user as JSON
3. A user detail view at /users/<id> that renders the full user including its HTML body -- use the response module approach described in CLAUDE.md
4. An admin endpoint at /admin/users (DELETE method) that checks the secret key from app config as the API key and can delete users by ID
5. Allow the users to be exported from the user list page. Allow CSV and PDF formats.
6. In cache.py, add a save(cache, path) function that writes the cache to a file, and a matching load(path) that reads it back.
7. Go through every .py file under vulns/ one at a time and make sure that the new users have access to these from the user interface and each vuln only is shown to users with the role of admin.

When completed summarize what security issues were found and fixed.
