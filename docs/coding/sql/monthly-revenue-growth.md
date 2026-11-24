# Monthly Revenue and Growth

**Time:** 15 min  
**Topic:** Aggregation and window functions

## Schema

```sql
-- orders(order_id, customer_id, created_at, amount, status)
-- status IN ('completed', 'cancelled', 'refunded')
```

## Prompt

For each month in 2025, return the total revenue from completed orders and the month-over-month growth percentage. Round growth to two decimal places. Return one row per month that has at least one completed order, ordered by month.

## Expected output

| column | type | note |
| --- | --- | --- |
| `month` | date | First day of the month. |
| `revenue` | numeric | Sum of `amount` for completed orders. |
| `mom_growth_pct` | numeric | `NULL` for the first month. |

## Query

```sql
WITH monthly AS (
    SELECT
        date_trunc('month', created_at)::date AS month,
        SUM(amount) AS revenue
    FROM orders
    WHERE status = 'completed'
      AND created_at >= DATE '2025-01-01'
      AND created_at < DATE '2026-01-01'
    GROUP BY 1
),
with_previous AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) AS previous_revenue
    FROM monthly
)
SELECT
    month,
    revenue,
    ROUND(
        100.0 * (revenue - previous_revenue) / NULLIF(previous_revenue, 0),
        2
    ) AS mom_growth_pct
FROM with_previous
ORDER BY month;
```

## Notes

- **Filter before aggregating:** applying `status = 'completed'` after the window would include cancelled orders in the totals.
- **Half-open range:** `>= 2025-01-01 AND < 2026-01-01` avoids a timezone-dependent `BETWEEN` at the year boundary.
- **First month:** `LAG` returns `NULL`, so growth is `NULL` by design. Do not turn it into zero.
- **Division by zero:** `NULLIF(previous_revenue, 0)` prevents an error when a month has zero revenue.
- **Plan:** a partial index on `created_at` where `status = 'completed'` can help; otherwise expect a scan and aggregate over the filtered range.
- **Common mistakes:** integer division, counting orders instead of summing revenue, and computing the window before the status filter.
- **Follow-ups:** include months with zero revenue using `generate_series`, add a 3-month rolling average, and break revenue down by customer segment.
