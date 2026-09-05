#!/usr/bin/env python3
"""Inspirations — a reading and looking list for the current chapter.
Text only. No artwork is reproduced."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                HRFlowable, KeepTogether, PageBreak, Image as RLImage)
from reportlab.lib.utils import ImageReader

INK        = colors.HexColor("#5d5a5b")
INK_STRONG = colors.HexColor("#454344")
STONE      = colors.HexColor("#a29f9f")
HAIR       = colors.HexColor("#e6e4e2")

S = {}
S['title'] = ParagraphStyle('title', fontName='Helvetica', fontSize=30, leading=34,
                            textColor=INK_STRONG, spaceAfter=8)
S['sub']   = ParagraphStyle('sub', fontName='Helvetica-Oblique', fontSize=12, leading=17,
                            textColor=STONE, spaceAfter=26)
S['eyebrow'] = ParagraphStyle('eyebrow', fontName='Helvetica-Bold', fontSize=7.5, leading=11,
                              textColor=STONE, spaceAfter=4)
S['h2']    = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=8.5, leading=12,
                            textColor=STONE, spaceBefore=22, spaceAfter=10)
S['body']  = ParagraphStyle('body', fontName='Helvetica', fontSize=9.6, leading=14.6,
                            textColor=INK, spaceAfter=10)
S['note']  = ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=8.6, leading=13,
                            textColor=STONE, spaceAfter=10)
S['name']  = ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=10.6, leading=14,
                            textColor=INK_STRONG, spaceAfter=1)
S['work']  = ParagraphStyle('work', fontName='Helvetica-Oblique', fontSize=9, leading=13,
                            textColor=STONE, spaceAfter=5)
S['why']   = ParagraphStyle('why', fontName='Helvetica', fontSize=9.4, leading=14,
                            textColor=INK, spaceAfter=15)

def rule(w=1, c=HAIR, before=0, after=12):
    return HRFlowable(width="100%", thickness=w, color=c,
                      spaceBefore=before, spaceAfter=after)

def entry(name, work, why):
    return KeepTogether([Paragraph(name, S['name']),
                         Paragraph(work, S['work']),
                         Paragraph(why, S['why'])])

story = []

# cover photograph, sized to the text column
_cov = ImageReader('images/photo-portrait.jpg')
_cw, _ch = _cov.getSize()
_w = letter[0] - 1.8 * inch
_h = _w * 0.52                       # a wide crop of the portrait
story += [
    RLImage('images/photo-portrait.jpg', width=_w, height=_h, kind='proportional'),
    Spacer(1, 22),
    Paragraph("ANDREA ROBIN STUDIO", S['eyebrow']),
    Paragraph("Inspirations", S['title']),
    Paragraph("The practices this chapter of the studio is learning from. September 2026.", S['sub']),
    rule(after=18),
    Paragraph("HOW TO READ THIS", S['h2']),
    Paragraph("This is a list of practices rather than of works, and it is a reading and looking "
              "list rather than an image book. No artwork is reproduced here. Every entry names "
              "the person, the specific thing being taken from them, and what does not transfer.",
              S['body']),
    Paragraph("The people here are on the list because something about how they work changed a "
              "decision in this studio. Admiration on its own is not enough to be included. That "
              "is a higher bar and it keeps the list short enough to be read rather than filed.",
              S['body']),
    Paragraph("The artists studied in the Dear Ordinary essays are deliberately not here. That is "
              "a separate body of reference, held in the curriculum's own artist file, and mixing "
              "the two would make both harder to use.", S['body']),
    Paragraph("Dates, locations and representation change. Anything load-bearing should be checked "
              "against the source before it is quoted or carried into an application.", S['note']),
]

story.append(PageBreak())

story += [
    Paragraph("ONE", S['eyebrow']),
    Paragraph("A rhythm that can be kept", S['title']),
    Paragraph("Fixed formats, fixed decisions, and the removal of choices that would "
              "otherwise be made again every month.", S['sub']),
    rule(),
    entry("Jean Smith",
          "11 &times; 14 inch portraits, $100 USD, sold direct since 2016",
          "One format, one price, one rhythm, sold from an apartment, with the surplus funding "
          "something beyond the practice. More than fifteen hundred sold, mostly within minutes "
          "of posting, in named series to repeat collectors. What does not transfer: thirty-five "
          "years of standing through Mecca Normal, a New York Times Magazine feature, and "
          "fifteen-hour days at peak. What does: the fixed format, which removes every pricing "
          "decision before it is made."),
    entry("Florian Gadsby",
          "Three collections a year; a book a year; documenting online since 2014",
          "Every camera position, light and shot order decided once, so the choosing stops. That "
          "single decision is why a one-person studio in High Barnet can sustain both the making "
          "and the documentation, and it is the direct source of the six setups on the "
          "Documentation page. The annual book is assembled from material captured anyway rather "
          "than produced for the book."),
    entry("Ini Neumann",
          "We Are Studio Studio, Hamburg",
          "A series name with a code for each one-off piece, sold work left listed, and one plain "
          "line about variation in hand-made things. It solves the problem of selling unique work "
          "without the shop reading as depleted. The product photography on that shop, credited to "
          "Anna Haerlin, is the reference the whole documentation setup is built from."),
]

story += [
    Paragraph("TWO", S['eyebrow']),
    Paragraph("Showing the process", S['title']),
    Paragraph("What a process post actually needs, which is less than it appears.", S['sub']),
    rule(),
    entry("Nicol&aacute;s Uribe",
          "Four frames of one figure at an identical crop",
          "Gesture through to resolved painting, shot from the same position each time. The "
          "clearest demonstration that a process post needs no video and no commentary. The "
          "identical crop is the entire technique, and it is produced by the flat copy setup "
          "that has to exist anyway. Born in Wisconsin, based in Bogot&aacute; by choice, having "
          "gone home to paint full time."),
    entry("H&eacute;l&egrave;ne Delmaire",
          "Captions that name what is failing; crops rather than whole paintings",
          "Working from a studio in Lille. The caption names what cannot be touched yet, which is "
          "candid without being a performance of struggle. The posts are crops, so the frame lands "
          "where the paint is doing something. The whole piece is what the record shot is for; the "
          "feed can have the two inches that were difficult."),
    entry("Zbyn&#283;k Sedleck&yacute;",
          "The work photographed in the room, with the wall in frame",
          "A scale shot as the second image. It answers the question every online buyer has and "
          "few think to ask, and it costs one extra frame at the end of a session."),
]

story.append(PageBreak())

story += [
    Paragraph("THREE", S['eyebrow']),
    Paragraph("Writing beside the practice", S['title']),
    Paragraph("Writing as its own object rather than as documentation of the painting.", S['sub']),
    rule(),
    entry("Maria Popova",
          "The Marginalian",
          "The register Dear Ordinary reaches for: feeling before concept, ideas already in "
          "conversation with one another, the reach past the fact toward the truth behind it. What "
          "is borrowed is a relationship rather than a style. Popova writes from inside a question "
          "she has not finished with, holds several thinkers in the same room and lets them "
          "disagree, and trusts the reader to follow without being managed. Intimacy with the "
          "question is the standard every post is measured against."),
    entry("Emma Webster",
          "Lonescape (2021); Decimate (2026)",
          "Part of what prompted Dear Ordinary to start. Lonescape is collected reflection on "
          "landscape and image-making, standing beside the paintings as its own artifact rather "
          "than documenting them. Decimate, at $35, is a digital sketchbook published on the "
          "occasion of the 2026 Petzel show, carrying a title and an epigraph rather than a year. "
          "The sketchbook is the model for the annual book: the material that did not become the "
          "finished work is cheaper to make, better to read, and does not compete with selling the "
          "paintings. Her years in interactive advertising and set design are where the maquette "
          "method came from, which is the argument for treating a day job as the second half of an "
          "unusual pair rather than as time away from the practice."),
]

story += [
    Paragraph("FOUR", S['eyebrow']),
    Paragraph("Selling without a shopfront", S['title']),
    Paragraph("Release mechanisms, catalogue structures, and the removal of friction.", S['sub']),
    rule(),
    entry("Joy Kinna",
          "A print store and a PDF catalogue",
          "Prints in their own store; originals sold from a PDF catalogue by email rather than "
          "through a cart. This is the model already in use, and it is the reason no inventory "
          "system has to exist."),
    entry("Olivier Forgues",
          "A quarterly email with a forty-eight hour window",
          "Subscribers see new work two days before it goes public. The clearest argument for the "
          "mailing list being the only asset that survives a platform closing."),
    entry("H&eacute;l&egrave;ne Delmaire",
          "A print release on a named day and hour, stated in three time zones",
          "The fixed hour does the work that marketing would otherwise have to do. The time-zone "
          "courtesy makes an international buyer feel invited rather than incidental, and from "
          "Vancouver the same courtesy runs in reverse."),
    entry("Heather Day",
          "An inquiry link with the subject and first line pre-written",
          "A small removal of friction that costs nothing and does the work a cart would "
          "otherwise do."),
]

story.append(PageBreak())

story += [
    Paragraph("FIVE", S['eyebrow']),
    Paragraph("How a body of work is presented", S['title']),
    Paragraph("Two structural decisions about a portfolio, both free to copy.", S['sub']),
    rule(),
    entry("Samantha Haring",
          "Recent years listed flat; older work gathered into series named in hindsight",
          "It removes the need to decide what a series is while still in the middle of making it. "
          "The naming happens later, when the shape is actually visible."),
    entry("Flora Yukhnovich",
          "Studies given their own section level with the paintings",
          "Labelled by year and nothing else. Studies sit level with the finished work rather than "
          "beneath it, which is a structural argument about what a study is. Separately, and less "
          "usefully: an MA in 2017, a dealer who found her on Instagram, and seven-figure auction "
          "sales within four years. Held as the route that cannot be planned for and should not be "
          "treated as impossible either. What carries across is a singular visual language with "
          "real art-historical grounding, which is built rather than discovered."),
]

story += [
    Paragraph("SIX", S['eyebrow']),
    Paragraph("Teaching, after credibility", S['title']),
    Paragraph("Two practices where teaching is the income that follows a record "
              "rather than the thing that builds one.", S['sub']),
    rule(),
    entry("Zoey Frank",
          "Roughly one course a year, $185 to $350",
          "Taught live, recorded the same day, then sold afterwards at a lower price and launched "
          "to a mailing list. Four sessions of about two and a half hours, so around ten hours of "
          "delivery. Foundations runs eighteen against her ten, which is what supports the higher "
          "price. The risk is over-designing it; version one should sit closer to her format than "
          "to an institutional course."),
    entry("Caitlin Winner",
          "Teaching and coaching circles alongside weekend painting",
          "A painting practice built on weekends around a full-time job, with a visible arc from "
          "roughly 2021 to 2025: juried shows, a fund, a residency, press, then representation. "
          "The order is the lesson. Shows and grants first, press after, representation after that, "
          "teaching on top of the credibility rather than instead of it."),
]

story += [
    Paragraph("HOW THIS LIST IS MAINTAINED", S['h2']),
    Paragraph("Entries are added when a practice changes a decision in this studio rather than "
              "when it is admired. Each one has to name the specific thing being taken and the "
              "thing that does not transfer, because a list of people whose work is good is not "
              "usable and a list of borrowed decisions is.", S['body']),
    Paragraph("Every claim about someone's reception has to be one that can be documented with "
              "named critics or named positions. Where it cannot, the tension is described in the "
              "work itself rather than in the reception.", S['body']),
    Paragraph("Citations are checked character by character against the actual source. AI tools "
              "reliably produce confident, plausible and wrong citation details, including titles, "
              "years, journals and publishers, and a citation carried forward from a draft without "
              "checking is the failure most likely to reach print.", S['body']),
    rule(before=14, after=10),
    Paragraph("Compiled September 2026. No artwork is reproduced. The Dear Ordinary essay artists "
              "are held separately, in the curriculum's own artist reference.", S['note']),
]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(STONE)
    canvas.drawString(0.9 * inch, 0.6 * inch, "Inspirations \u00b7 Andrea Robin Studio")
    canvas.drawRightString(letter[0] - 0.9 * inch, 0.6 * inch, str(doc.page))
    canvas.setStrokeColor(HAIR)
    canvas.setLineWidth(0.5)
    canvas.line(0.9 * inch, 0.78 * inch, letter[0] - 0.9 * inch, 0.78 * inch)
    canvas.restoreState()

doc = SimpleDocTemplate("files/inspirations.pdf", pagesize=letter,
                        leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                        topMargin=0.85 * inch, bottomMargin=0.95 * inch,
                        title="Inspirations \u2014 Andrea Robin Studio",
                        author="Andrea Robin Studio",
                        subject="Works this chapter of the practice is in conversation with")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("built files/inspirations.pdf")
