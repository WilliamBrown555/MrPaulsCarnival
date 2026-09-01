# Carnival Bar menus — build source

`build_menu_pdf.py` builds `../Carnival Website/carnival-bar-menus.pdf`, the
single PDF that the **Carnival Bar Menu** button on lnk.bio/CarnivalBar
points at. Three pages: cocktails, food, wine & beer.

```
python3 build_menu_pdf.py
```

Needs `pypdf`.

## Where the pages come from

The print files one folder up are letter sheets carrying the same menu
**twice, side by side**, with a second page of elephant marks for the back.
The script takes page 1 of each and crops it to the left half, so the PDF is
one readable menu per page with no backs — built for a phone, not a printer.

When the season changes, drop the new print PDFs in the folder above, update
`SOURCES` at the top of the script, re-run it, then commit and push. The push
is the deploy.

## Publishing

This folder is a git repo. Netlify serves `Carnival Website/` with an empty
build command — the PDF is committed built, exactly like the HTML menus.
