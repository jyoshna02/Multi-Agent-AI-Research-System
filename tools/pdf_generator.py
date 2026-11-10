from io import BytesIO
from datetime import datetime
from xml.sax.saxutils import escape
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    HRFlowable
)


def add_page_number(canvas, document):

    canvas.saveState()

    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.grey)

    canvas.drawString(
        0.7 * inch,
        0.45 * inch,
        "Multi-Agent AI Research System"
    )

    canvas.drawRightString(
        7.8 * inch,
        0.45 * inch,
        f"Page {document.page}"
    )

    canvas.restoreState()


def generate_pdf(report_text, topic="Research Report"):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.8 * inch,
        bottomMargin=0.8 * inch
    )

    styles = getSampleStyleSheet()

    cover_title = ParagraphStyle(
        "CoverTitle",
        parent=styles["Title"],
        fontSize=25,
        leading=32,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#17365D"),
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#17365D"),
        spaceBefore=14,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["BodyText"],
        fontSize=10,
        leading=16,
        spaceAfter=8
    )

    story = []

    # Cover page
    story.append(Spacer(1, 1.7 * inch))

    story.append(
        Paragraph(
            "MULTI-AGENT AI<br/>RESEARCH SYSTEM",
            cover_title
        )
    )

    story.append(
        HRFlowable(
            width="70%",
            thickness=2,
            color=colors.HexColor("#2874A6"),
            hAlign="CENTER"
        )
    )

    story.append(Spacer(1, 0.5 * inch))

    story.append(
        Paragraph(
            "Research Report",
            ParagraphStyle(
                "Subtitle",
                parent=styles["Heading2"],
                alignment=TA_CENTER,
                textColor=colors.HexColor("#2874A6")
            )
        )
    )

    story.append(Spacer(1, 0.3 * inch))

    story.append(
        Paragraph(
            f"<b>Research Topic:</b> {escape(topic)}",
            ParagraphStyle(
                "Topic",
                parent=body_style,
                alignment=TA_CENTER
            )
        )
    )

    report_date = datetime.now().strftime(
        "%d %B %Y, %I:%M %p"
    )

    story.append(
        Paragraph(
            f"<b>Generated On:</b> {report_date}",
            ParagraphStyle(
                "Date",
                parent=body_style,
                alignment=TA_CENTER
            )
        )
    )

    story.append(Spacer(1, 2 * inch))

    story.append(
        Paragraph(
            "Generated using an AI-powered multi-agent research workflow",
            ParagraphStyle(
                "FooterText",
                parent=body_style,
                alignment=TA_CENTER,
                textColor=colors.grey
            )
        )
    )

    # Start report content on a new page
    story.append(PageBreak())

    story.append(
        Paragraph("Research Findings", heading_style)
    )

    # Process report content
    for line in report_text.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 6))
            continue

        if line.startswith("# "):
            text = escape(line[2:])
            story.append(Paragraph(text, cover_title))

        elif line.startswith("## "):
            text = escape(line[3:])
            story.append(Paragraph(text, heading_style))

        elif line.startswith("### "):
            text = escape(line[4:])
            story.append(Paragraph(text, styles["Heading3"]))

        elif line.startswith("- ") or line.startswith("* "):
            text = escape(line[2:])
            story.append(
                Paragraph(f"&bull; {text}", body_style)
            )

        else:
            text = escape(line)

            text = re.sub(
                r"\*\*(.*?)\*\*",
                r"<b>\1</b>",
                text
            )

            story.append(
                Paragraph(text, body_style)
            )

    document.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data