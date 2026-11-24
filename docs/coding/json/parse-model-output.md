# Parse a Model Response

**Time:** 15 min  
**Topic:** Structured output parsing  
**Language:** Python

## Prompt

Implement a function that extracts the first valid JSON object from a raw model response.

```python
def extract_json(raw: str) -> dict | None:
    ...
```

The response may be plain JSON, a fenced code block, or prose with a JSON object somewhere inside. Return the first valid JSON object, or `None` if there is no valid object.

## Constraints

- Do not use regular expressions.
- Do not assume the response starts with `{`.
- Ignore prose before and after the object.
- Accept only JSON objects. Arrays and scalars should return `None`.
- Do not validate the schema; that is a separate step.

## Starter

```python
def extract_json(raw: str) -> dict | None:
    ...
```

## Tests

```python
assert extract_json('{"ok": true}') == {"ok": True}
assert extract_json('```json\n{"a": 1}\n```') == {"a": 1}
assert extract_json('prefix {"a": {"b": 2}} suffix') == {"a": {"b": 2}}
assert extract_json('{"a": 1} then {"b": 2}') == {"a": 1}
assert extract_json('no json here') is None
assert extract_json('[1, 2, 3]') is None
assert extract_json('{"a": 1,}') is None
```

## Solution

```python
import json


def extract_json(raw: str) -> dict | None:
    decoder = json.JSONDecoder()

    for index, char in enumerate(raw):
        if char != "{":
            continue
        try:
            value, _ = decoder.raw_decode(raw[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value

    return None
```

## Notes

- **Why `raw_decode`:** it parses one JSON value from a string and stops, which is exactly the behaviour needed when prose follows the object.
- **Why not `json.loads` directly:** the response is often fenced or wrapped in explanation.
- **Why not `find("{")` plus `rfind("}")`:** that breaks when there is more than one object or when braces appear in prose.
- **Schema validation:** parse first, then validate with Pydantic or JSON Schema. Parsing does not make the content trustworthy.
- **Streaming:** partial JSON needs a different strategy. Do not treat a failed parse as a failed generation until the stream is complete.
- **Common mistakes:** accepting arrays, returning a stringified object, and silently repairing malformed JSON without reporting it.
