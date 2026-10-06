# The Archive

**Pair:** *Jed and Joyce* **Repository:** *https://github.com/Odiedo123/archive-Jed-Joyce*

> This file is Part E of the assignment — **15 marks**. Replace every placeholder below. Delete the instruction lines in italics as you go. Marks come from the reasoning, not the length.

---

## 1\. The record *(3 marks)*

*What one manuscript looks like in our system, and what we do when a field is unknown.*

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` | Return an error |
| title |string  | At Night All Blood is Black | Return an Error |
| city | string | "Dodoma | Return an Error |
| year | string | "1800" | Return an Error |
| condition | string | "good" | Return an Error |

---

## 2\. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id | Must start with "MS" followed by a 3 digit int not 0 | Ms000 |
| title | Must be 3 characters once stripped | "  vf" |
| city | Must be in the list of known cities | "nairobi" |
| year | Contains integers only in the range of 1900 and 1100 | 1000 |
| condition | Must be in the list of valid conditions | "subpar" |

### Who decided the year range?

*The brief gave you 1100–1900. That was a decision someone made, and it has costs. 1900 excludes a modern copy of an old text. 1100 excludes anything earlier. State whether you accept these bounds or would change them, and say what your choice throws away. An undefended range scores 1 of the 4 marks.*

To include more books we would change the lower bound of 1100 to 1000
---

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*

- **(a)** Reject it. Only exact years enter the catalogue.
- **(b)** Store the year as text, so anything can be recorded.
- **(c)** Store `1590` plus a separate `approximate` flag.

**Our choice:(c)**

**Why: To allow approximate years of books to be included and stored**

**What it costs us: It will add another table and space consumption**

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid | valid | Yes |
| Abnormal | "high" | not valid | not valid | No |
| Extreme (low) | 1100 | valid | valid | Yes |
| Extreme (high) | 1900 | valid | valid | Yes |
| Boundary (below) | 1099 | invalid | invalid | No |
| Boundary (above) | 1901 | invalid | invalid |  No|

### `_______________` *(one other field of your choice)*

| Test data | Value | Expected | Actual | Pass? |
| Empty | "" | not valid | not valid | No |

---

## 5\. Collaboration reflection *(2 marks)*

*One paragraph each, written separately and signed. Do not write these together — the point is two honest accounts.*

***(Joyce)*:** One thing my partner did that I will steal:(The way of writing the code using boolean instead of a lot of operations that takes more space) One thing I would do differently next time:(Code better)


***(Jed)*:** One thing my partner did that I will steal: The efficient code writting with her using a lot of python functions i've never used before, allowing me to not only finish the project but learn through the experience
 One thing I would do differently next time: Realize that pair programming is quicker and more efficient and communicating more

---

## 6\. Declaration

*Required. See the integrity section of the brief.*

- [ Yes ] Both of us can explain every line in this repository.

- [ Yes ] AI assistants used for explanation only, not to generate our implementation or our tests.

**If you used an AI assistant, say what you asked and what you did with the answer:**

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)