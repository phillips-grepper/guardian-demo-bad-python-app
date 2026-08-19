## Semgrep Guardian Demo / Lab - Bad Python App

### Requisites

* Claude Code (CLI)
* Semgrep Guardian Plugin
* Semgrep Auth TOken
* Python 3.7+

### Lab

#### Installing Plugins (in Claude Code)
```
 /plugin install semgrep@claude-plugins-official
```
#### Reload Plugins in Claude
```
/reload-plugins
```
#### Authentication
Each developer completes a one-time browser login when they first use the plugin. Once authentication is completed, an OAuth session is stored in ./semgrep/guardian.yml. Semgrep refreshes access tokens automatically, so developers rarely need to sign in again.


#### Clone this repo
You're ready to begin using Semgrep Guardian in claude but lets get started by practicing with this demo app.

```
git clone https://github.com/phillips-grepper/guardian-demo-bad-python-app/; cd guardian-demo-bad-python-app
```

Now lets launch claude

```
claude
```

Start your Session
```
SessionStart
```

Paste Prompt from DEMO_PROMPT.md
```

```
