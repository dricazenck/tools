#!/usr/bin/env python3
"""
Timesheet Generator
Generates professional PDF timesheets for employee time tracking.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
from datetime import datetime, timedelta
import json
import os
from pathlib import Path


def load_config():
    """
    Load configuration from config.json file.

    Returns:
        dict: Configuration dictionary with default_employee, default_supervisor, and language.
              If config.json doesn't exist, returns defaults with a warning message.
    """
    config_path = Path(__file__).parent / "config.json"

    # Default fallback values
    default_config = {
        "default_employee": "Maria Elena Rodriguez Garcia",
        "default_supervisor": "Carlos Alberto Martinez Silva",
        "language": "es"
    }

    if not config_path.exists():
        print("⚠ Warning: config.json not found. Using example names.")
        print("  To customize: Copy config.example.json to config.json and edit with your details.")
        return default_config

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            # Merge with defaults to ensure all keys exist
            return {**default_config, **config}
    except json.JSONDecodeError as e:
        print(f"⚠ Warning: config.json is invalid ({e}). Using example names.")
        return default_config
    except Exception as e:
        print(f"⚠ Warning: Could not load config.json ({e}). Using example names.")
        return default_config


def generate_timesheet(
    employee_name,
    supervisor_name,
    month,
    year,
    start_day=1,
    language="es",
    output_filename=None
):
    """
    Generate a PDF timesheet for an employee.

    Args:
        employee_name (str): Full name of the employee
        supervisor_name (str): Full name of the supervisor
        month (int): Month number (1-12)
        year (int): Year
        start_day (int): Starting day of the month (default: 1)
        language (str): Language code - "es" (Spanish), "pt" (Portuguese), or "en" (English)
        output_filename (str): Output PDF filename (optional)

    Returns:
        str: The filename of the generated PDF
    """

    # Language-specific translations
    translations = {
        "es": {
            "title": "HOJA DE CONTROL DE ASISTENCIA",
            "name": "Nombre:",
            "month_year": "Mes/Año:",
            "date": "Fecha",
            "day": "Día",
            "entry_time": "Hora Entrada",
            "exit_time": "Hora Salida",
            "total_hours": "Total Horas",
            "balance": "Saldo",
            "total": "TOTAL",
            "employee_signature": "Firma del Empleado",
            "supervisor_signature": "Firma del Responsable",
            "months": [
                "", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
            ],
            "weekdays": {
                0: "Lunes",
                1: "Martes",
                2: "Miérc.",
                3: "Jueves",
                4: "Viernes"
            }
        },
        "pt": {
            "title": "FOLHA DE PONTO",
            "name": "Nome:",
            "month_year": "Mês/Ano:",
            "date": "Data",
            "day": "Dia",
            "entry_time": "Hora Entrada",
            "exit_time": "Hora Saída",
            "total_hours": "Total Horas",
            "balance": "Saldo",
            "total": "TOTAL",
            "employee_signature": "Assinatura do Funcionário",
            "supervisor_signature": "Assinatura do Responsável",
            "months": [
                "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
            ],
            "weekdays": {
                0: "Segunda",
                1: "Terça",
                2: "Quarta",
                3: "Quinta",
                4: "Sexta"
            }
        },
        "en": {
            "title": "ATTENDANCE CONTROL SHEET",
            "name": "Name:",
            "month_year": "Month/Year:",
            "date": "Date",
            "day": "Day",
            "entry_time": "Entry Time",
            "exit_time": "Exit Time",
            "total_hours": "Total Hours",
            "balance": "Balance",
            "total": "TOTAL",
            "employee_signature": "Employee Signature",
            "supervisor_signature": "Supervisor Signature",
            "months": [
                "", "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            "weekdays": {
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday"
            }
        }
    }

    # Get translations for selected language
    t = translations.get(language, translations["es"])

    # Generate default filename if not provided
    if output_filename is None:
        month_name = t["months"][month].lower()
        output_filename = f"timesheet_{employee_name.split()[0].lower()}_{month_name}_{year}.pdf"

    # Create PDF
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        topMargin=3*cm,
        bottomMargin=1*cm,
        leftMargin=0.8*cm,
        rightMargin=0.8*cm
    )

    elements = []

    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.black,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Title
    title = Paragraph(f'<b>{t["title"]}</b>', title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.5*cm))

    # Create main table
    data = []

    # Row 1: Employee name
    data.append([t["name"], employee_name, '', '', '', ''])

    # Row 2: Month/Year
    data.append([t["month_year"], f'{t["months"][month]}/{year}', '', '', '', ''])

    # Row 3: Header
    data.append([
        t["date"],
        t["day"],
        t["entry_time"],
        t["exit_time"],
        t["total_hours"],
        t["balance"]
    ])

    # Calculate weekdays (Monday-Friday)
    # Get the last day of the month
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    last_day = (next_month - timedelta(days=1)).day

    # Generate date rows
    current_date = datetime(year, month, start_day)
    end_date = datetime(year, month, last_day)

    while current_date <= end_date:
        weekday = current_date.weekday()
        # Only include Monday-Friday (0-4)
        if weekday <= 4:
            date_formatted = current_date.strftime('%d/%m/%Y')
            day_name = t["weekdays"][weekday]
            data.append([date_formatted, day_name, '', '', '', ''])
        current_date += timedelta(days=1)

    # Total row
    data.append([t["total"], '', '', '', '', ''])

    # Create table
    col_widths = [3*cm, 2.5*cm, 3*cm, 3*cm, 3*cm, 3*cm]

    # Row heights
    row_heights = []
    row_heights.append(0.7*cm)  # Name row
    row_heights.append(0.7*cm)  # Month/Year row
    row_heights.append(0.7*cm)  # Header row
    for i in range(3, len(data)):  # Data and total rows
        row_heights.append(0.65*cm)

    table = Table(data, colWidths=col_widths, rowHeights=row_heights)

    # Table style
    table_style = [
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        # Info rows (Name and Month/Year)
        ('FONTNAME', (0, 0), (0, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 1), 10),
        ('SPAN', (1, 0), (5, 0)),  # Merge cells for name
        ('SPAN', (1, 1), (5, 1)),  # Merge cells for month/year
        # Header row
        ('FONTNAME', (0, 2), (-1, 2), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 2), (-1, 2), colors.Color(0.85, 0.89, 0.95)),
        ('FONTSIZE', (0, 2), (-1, 2), 9),
        # Total row
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, -1), (-1, -1), colors.Color(0.91, 0.90, 0.90)),
        # General
        ('FONTSIZE', (0, 3), (-1, -2), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]

    table.setStyle(TableStyle(table_style))
    elements.append(table)

    # Spacing
    elements.append(Spacer(1, 1*cm))

    # Signature table
    signature_data = [
        ['', ''],
        ['_' * 40, '_' * 40],
        [employee_name, supervisor_name],
        [t["employee_signature"], t["supervisor_signature"]]
    ]

    signature_table = Table(signature_data, colWidths=[9*cm, 9*cm])
    signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 1), (-1, 1), 0),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 2),
        ('TOPPADDING', (0, 2), (-1, 2), 2),
    ]))

    elements.append(signature_table)

    # Generate PDF
    doc.build(elements)

    return output_filename


if __name__ == "__main__":
    # Load configuration
    config = load_config()

    # Example usage

    # Generate December 2025 timesheet (starting from day 15)
    filename_dec = generate_timesheet(
        employee_name=config["default_employee"],
        supervisor_name=config["default_supervisor"],
        month=12,
        year=2025,
        start_day=15,
        language=config["language"],
        output_filename="timesheet_december_2025.pdf"
    )
    print(f"✓ Generated: {filename_dec}")

    # Generate January 2026 timesheet
    filename_jan = generate_timesheet(
        employee_name=config["default_employee"],
        supervisor_name=config["default_supervisor"],
        month=1,
        year=2026,
        start_day=1,
        language=config["language"],
        output_filename="timesheet_january_2026.pdf"
    )
    print(f"✓ Generated: {filename_jan}")
