# Prompting cheat sheet

Choose a prompt for the task at hand. Replace bracketed text with your details.

Use Plan Mode in OpenCode or Codex while discussing changes. It is intended to avoid implementation, but may still allow read-only commands. Switch to execution when ready.

## 1. Find the biggest issues

Review [repo/file] for [focus]. Rank up to 10 issues by impact. Cite the relevant code, explain the consequence, and give an example where applicable.

## 2. Decide one issue at a time

Take the findings one at a time. Recommend a fix, explain the trade-off, then wait for my decision. Record each as accepted, deferred, or rejected. Build a plan from the accepted items.

## 3. Trace unfamiliar code

Trace [input] from its source to [output]. Name the functions it passes through and explain each transformation. Keep this pass read-only.

## 4. Clarify what matters

Read [files] first. If a missing requirement would change your implementation, ask me the most important question first. State any smaller assumptions.

## 5. Define an Agent Contract

Your goal is [goal]. Use [inputs]. Respect [constraints]. The task is complete when [acceptance criteria]. Verify the result before reporting completion.

## 6. Manage context

Identify the files, documentation and prior decisions relevant to [task]. Explain what information is missing. Avoid loading unrelated material.

## 7. Compare options

Compare [option A] and [option B] for [task]. Consider [constraints]. Explain the trade-offs and recommend an approach.

## 8. Reproduce a bug

With [input], [command] gives [actual result]. I expected [expected result]. Capture the mismatch in a failing test, apply the smallest fix, and rerun the test.

## 9. Bound the edit

Implement [change] in [component]. Preserve [interfaces and formats]. Follow [reference implementation]. List unrelated cleanup separately.

## 10. Verify the result

Check each acceptance criterion. Report the command you ran and what it showed. Identify anything you couldn't verify and explain why.

## Prompting guides

- [GitHub](https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-engineering)
- [Anthropic](https://www.anthropic.com/research/claude-code-best-practices)
- [OpenAI](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)
