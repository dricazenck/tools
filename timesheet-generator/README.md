# Timesheet Generator

A Python script to generate professional PDF timesheets for employee time tracking.

## Features

- **Multi-language support**: Spanish, Portuguese, and English
- **Flexible date ranges**: Generate timesheets for any month with custom start dates
- **Automated weekday filtering**: Automatically includes only Monday-Friday entries
- **Professional formatting**: Clean, print-ready PDF output
- **Customizable**: Easy to modify employee and supervisor names

## Requirements

- Python 3.7+
- ReportLab library

## Installation

```bash
cd timesheet-generator
pip install -r requirements.txt
```

## Configuration

Before first use, create your personal configuration file:

```bash
# Copy the example config
cp config.example.json config.json

# Edit with your details
nano config.json  # or use your preferred editor
```

**config.json structure:**
```json
{
  "default_employee": "Your Full Name",
  "default_supervisor": "Supervisor Full Name",
  "language": "es"
}
```

**Language options:**
- `"es"` - Spanish (default)
- `"pt"` - Portuguese
- `"en"` - English

**Note:** `config.json` is excluded from git to protect your privacy. The script will use example names if this file is missing.

## Usage

### Basic Usage

```bash
python3 generate_timesheet.py
```

This will generate example timesheets using your config.json settings.

### Advanced Configuration

For advanced use cases, you can override config values by calling the function directly:

```python
from generate_timesheet import generate_timesheet

# Override default config for a specific timesheet
generate_timesheet(
    employee_name="Maria Elena Rodriguez Garcia",
    supervisor_name="Carlos Alberto Martinez Silva",
    month=12,
    year=2025,
    start_day=15,
    language="es",  # "es", "pt", or "en"
    output_filename="timesheet_december_2025.pdf"
)
```

### Parameters

- `employee_name` (str): Full name of the employee
- `supervisor_name` (str): Full name of the supervisor/manager
- `month` (int): Month number (1-12)
- `year` (int): Year (e.g., 2025)
- `start_day` (int, optional): Starting day of the month (default: 1)
- `language` (str): Language code - "es" for Spanish, "pt" for Portuguese, or "en" for English (default: from config)
- `output_filename` (str): Name of the output PDF file

## Output

The script generates a PDF file with:
- Employee and supervisor information
- Date column with day of the week
- Time entry columns (Entry Time, Exit Time)
- Calculated hours columns (Total Hours, Balance)
- Signature lines for both employee and supervisor

## Examples

See the `examples/` directory for sample outputs.

## Customization

You can easily customize:
- Page margins and layout (modify `topMargin`, `bottomMargin`, etc.)
- Table column widths
- Colors and styling
- Date formats
- Additional fields

## Notes

- Personal names are stored in config.json (not tracked in git)
- The script automatically filters for weekdays (Monday-Friday)
- Holidays are included but can be manually marked as such
- All dates and day names are localized based on the selected language
