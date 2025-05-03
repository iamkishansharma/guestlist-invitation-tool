# 🎉 Generate Invitation Cards from CSV

This project generates personalized invitation cards for a list of guests provided in a CSV file, using a designed template image.


---

## 📋 Requirements

1. **Install `uv`**  
   Make sure you have [`uv`](https://docs.astral.sh/uv/) installed on your system.

2. **Create a `guests.csv` File**  
   The CSV file should include a column named **`name`** containing guest names.

   Example `guests.csv`:

   | name   |
   |--------|
   | Kishan |
   | Kisha  |
   | ...    |

3. **Put invitation card with no guest names name**  
   Put a designed blank image with name `invitation_og.jpg` in the same directory as `main.py`. This image will be used as the base template for all invitation cards.
---

## 💻 Setup and Execution

### Step 1: Install Dependencies

Use `uv` to install project dependencies:

```bash
uv pip install .
```

### Step 2: Run program

```bash
uv run main.py
```

After running this command, you will see a new directory named **output_invitations** containing the generated invitation cards—one for each guest in your guests.csv
