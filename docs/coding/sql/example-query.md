# Example SQL Drill

> Format placeholder. Replace this page with a real drill, or keep it as a template.

**Time:** 15 min  
**Topic:** [e.g. joins, window functions, incremental loads]

## Schema

```sql
-- orders(order_id, customer_id, created_at, amount, status)
-- customers(customer_id, country, segment)
```

## Prompt

[State the question in one sentence, including the grain of the result.]

## Expected output

| column | type | note |
| --- | --- | --- |
| [name] | [type] | [grain or ordering] |

## Query

```sql
-- Write the query here.
```

## Notes

- **Approach:** [Join strategy, filtering, and why.]
- **Plan:** [Which index or scan the database should use.]
- **Common mistakes:** [Fan-out, duplicate rows, NULL handling, timezone boundaries.]
