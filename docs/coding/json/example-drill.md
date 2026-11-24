# Example Drill

> Format placeholder. Replace this page with a real drill, or keep it as a template.

**Time:** 15 min  
**Topic:** Structured output parsing  
**Language:** Python

## Prompt

[Write a function that accepts a raw model response and returns either a validated object or a structured error. Include the expected input and output types.]

## Constraints

- [Handle a fenced code block and plain JSON.]
- [Return an error instead of raising on invalid input.]
- [Do not lose unknown fields.]

## Starter

```python
def parse_response(raw: str) -> dict | None:
    ...
```

## Tests

```python
assert parse_response('{"ok": true}') == {"ok": True}
assert parse_response("not json") is None
```

## Notes

- **Approach:** [One paragraph.]
- **Failure modes:** [Fences, partial JSON, wrong types, duplicate keys.]
- **Common mistakes:** [Assuming the first `{` is the start of the payload.]
