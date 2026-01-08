# Kids Educational Projects

Educational materials generator for school projects. Currently includes materials about artists and other educational topics suitable for elementary school children.

## Projects

### Piet Mondrian Educational PDF

An interactive and educational PDF about the artist Piet Mondrian, designed for 3rd grade elementary school students (ages 8-9).

#### Features

- **Biographical information** adapted for children
- **Fun facts** with emojis to maintain engagement
- **Timeline** of the artist's life with visual table
- **Famous works** description
- **Interactive activities** including:
  - Coloring grid in Mondrian's style
  - Drawing exercises
  - Creative writing prompts
  - Real-world observation tasks

#### Content Structure

The PDF includes:
1. Cover page with Mondrian-style grid example
2. Introduction to Piet Mondrian
3. 6 fun curiosities about the artist
4. Timeline with 5 key moments in his life
5. Description of famous artworks
6. Hands-on coloring activity
7. Additional creative activities

#### Usage

```bash
python create_mondrian_pdf.py
```

The script generates a PDF file named `piet_mondrian.pdf` in the `outputs/` directory.

#### Requirements

```bash
pip install reportlab
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

#### Customization

The script uses Mondrian's signature colors:
- Red: `#E03C31`
- Blue: `#0C5DA5`
- Yellow: `#FFC300`
- Black: `#1a1a1a`

You can modify the content by editing:
- `intro_text` - Main introduction section
- `facts` - List of fun facts
- `timeline_data` - Timeline entries
- `famous_works` - Description of artworks
- `activity_instructions` - Activity guidelines

#### Output

The generated PDF is:
- **A4 format** ready for printing
- **Colorful and engaging** with Mondrian's color palette
- **5 pages** of content
- **Spanish language** (can be adapted to other languages)

## Future Projects

This directory can be expanded with other educational materials:
- Other artist profiles
- Science topics for kids
- Historical figures
- Geography materials
- Math exercise generators

## File Structure

```
kids-project/
├── create_mondrian_pdf.py    # Piet Mondrian PDF generator
├── example_output.pdf         # Example of generated PDF
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── outputs/                   # Generated PDF files (created automatically)
    └── piet_mondrian.pdf
```

## Contributing

When adding new educational projects:
1. Keep content age-appropriate
2. Use engaging visual elements
3. Include interactive activities
4. Document the target age group
5. Provide clear usage instructions

## Notes

- All PDFs are generated in the `outputs/` directory (created automatically if it doesn't exist)
- Content language can be easily modified by updating text variables
- Color schemes follow the theme of each educational topic
- Generated files are ready for printing on standard A4 paper

## License

Educational materials for personal and school use.
