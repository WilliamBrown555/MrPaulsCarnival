#!/usr/bin/env python3
"""Builds ../Carnival Website/carnival-bar-menus.pdf - the one PDF the link
tree points at, carrying every Carnival Bar menu.

Each print PDF in the folder above is a letter sheet with the SAME menu
printed twice side by side, plus a second page of elephant marks for the
back. For reading on a phone we want one copy and no backs, so this takes
page 1 of each and crops it to the left half.

    python3 build_menu_pdf.py

Order is cocktails, food, wine & beer - the order a guest reads them in.
Update SOURCES when the season changes and the print files are renamed.
"""
import os
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "..")
OUT  = os.path.join(HERE, "..", "Carnival Website", "carnival-bar-menus.pdf")

SOURCES = [
    ("Cocktails",   "Carnival Bar - Cocktails - SUMMER 2026.pdf"),
    ("Food",        "Carnival Bar - Food - SUMMER 2026.pdf"),
    ("Wine & Beer", "Carnival Bar - Wine & Beer - SUMMER 2026 (even spacing).pdf"),
]

def main():
    writer = PdfWriter()
    for title, name in SOURCES:
        page = PdfReader(os.path.join(SRC, name)).pages[0]
        box = page.mediabox
        left, bottom = float(box.left), float(box.bottom)
        right, top   = float(box.right), float(box.top)
        middle = (left + right) / 2
        page.mediabox.upper_right = (middle, top)
        page.cropbox.lower_left   = (left, bottom)
        page.cropbox.upper_right  = (middle, top)
        writer.add_page(page)
        writer.add_outline_item(title, len(writer.pages) - 1)
    writer.add_metadata({"/Title": "Carnival Bar \u2014 Menus, Summer 2026",
                         "/Author": "Mr. Paul's Supper Club"})
    with open(OUT, "wb") as fh:
        writer.write(fh)
    print("%d pages -> %s" % (len(writer.pages), os.path.normpath(OUT)))

if __name__ == "__main__":
    main()
