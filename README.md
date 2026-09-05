# Studio Day

The working repository for a painting practice run alongside a full-time career.
Four projects, the year they run in, and the map of people and opportunities the
practice is oriented toward.

Nothing here is a shop front. It holds decisions already made, written down so they
do not have to be made again.

---

## Pages

| File | What it holds |
|---|---|
| `index.html` | **The studio day.** The landing page, and the one to open on a Sunday morning. The four projects, the two frames that hold them, and the inspiration download. |
| `studies.html` | **The studies series.** An hour a piece, one size, one price, released monthly, with part of every sale to Arts Umbrella. |
| `teaching.html` | **Foundations.** Foundation year at Emily Carr, reconsidered. One recorded module a year. |
| `writing.html` | **Writing.** What the writing does in the practice: where it comes from, how a sentence is made, where the archive lives, what forms it takes. Forty stars across seven constellations, in 2D or 3D. |
| `documentation.html` | **The capture setup, decided once.** Six rigs that between them feed the website, grant applications, the annual book, video and teaching. Filter by what you need. |
| `year.html` | **The year.** Twelve months on a wheel, each with what runs, what pauses, the milestone, and how the Monday block is spent. |
| `atlas.html` | **The atlas.** The artists the practice is in conversation with, and the funders, prizes and residencies that return hours to it. One world map, two layers. |

## Assets

| Path | What it holds |
|---|---|
| `style.css` | Shared styling for every page. `atlas.html`, `writing.html`, `year.html` and `documentation.html` each add a small page-scoped `<style>` block on top of it. |
| `images/` | Photographs. See the card photographs note below. |
| `images/card-documentation.jpg` | The only photograph here that belongs to the practice. |
| `files/studio-day-inspiration.pdf` | The inspiration deck. Twenty-eight pages of work being looked at while this chapter is made. **11 MB, and it reproduces other artists' work.** See the note below before publishing. |
| `files/inspirations.pdf` | The same influences as text: what each practice contributes and what does not transfer. Reproduces nothing. |

## Build sources

Three pages are generated rather than hand-edited, because their content is
easier to maintain as data than as markup. Run any of these from the repository
root; each overwrites its page in place.

| Command | Rebuilds | Edit this to change |
|---|---|---|
| `python3 _build/build_atlas.py` | `atlas.html` | The 25 atlas entries, as plain Python dictionaries |
| `python3 _build/build_writing.py` | `writing.html` | The 40 stars and their connecting lines |
| `python3 _build/build_pdf.py` | `files/inspirations.pdf` | The text influence list |

`_build/` also holds `_land.txt`, `_sphere.txt` and `_coast.txt`, the world map
geometry the atlas draws, and `star-chart.html`, the Dear Ordinary chart whose
engine the writing page reuses. None of these are served; the underscore keeps
GitHub Pages from publishing the folder.

**Editing `atlas.html` or `writing.html` by hand will be overwritten** the next
time their build script runs. Change the script instead.

---

## Card photographs on the index

The six cards on `index.html` each look for a photograph in `images/`:

| File | Card |
|---|---|
| `card-studies.jpg` | Studies |
| `card-teaching.jpg` | Teaching |
| `card-writing.jpg` | Writing |
| `card-documentation.jpg` | Documentation |
| `card-atlas.jpg` | Atlas |
| `card-year.jpg` | The Year |

`card-documentation.jpg` is filled: coloured pencil shavings on a white plate,
photographed overhead, from an Instagram post of September 2019. It is the only
photograph in this repository that belongs to the practice.

Add any of the others and that card fills with the photograph under a dark gradient,
with the text sitting over it. Leave one out and the slot is removed on load, so
the card shows as a plain dark tile. Nothing renders as a broken image either way,
and they can be added one at a time.

Landscape crops around 1200 x 1600 for the four project cards and 1600 x 900 for
the two wide ones are plenty; they are displayed small and darkened.

---

## A note on Support

`support.html` was linked from the nav on every page and had nothing to say. It is
out of the nav now, in the pages and in the two build scripts, so it will not
return on the next rebuild. The file itself is untouched, wherever it lives.

If it comes back, the two things it could hold that nothing else does are: how
someone actually buys work, since the originals are sold by PDF catalogue and
email rather than through a cart and that is not written down anywhere public;
and what the practice supports, since part of every studies sale goes to Arts
Umbrella and that is currently only recorded on the Atlas.

---

## Printing

This is a working reference, so every page is set up to print. Paper drops the
navigation, the photographs and every control, and reveals what the interactions
normally hide.

| Page | On paper |
|---|---|
| The Year | All twelve months written out flat, each with its milestone, what runs, what pauses and how the Monday block is spent |
| Documentation | All six setups with rig, steps, what each feeds, and the pre-shoot checks |
| Writing | The full list of forty stars, not the map |
| Atlas | The full roster, not the map |
| Studies, Teaching | The settled rows and the checklist, laid out plainly |

The Year also opens on whatever month it currently is, rather than waiting for a
click.

---

## The palette

Every colour is sampled from the twenty photographs, clustered across all of
them rather than picked from one. The five dominant families are warm umber
shadow, dry sand, wet rock, sea green and the deep blue of the towel and water.

| Token | Value | Role | Contrast on paper |
|---|---|---|---|
| `--paper` | `#fdfcfa` | Background | — |
| `--ink-strong` | `#2b2219` | Headings | 15.2:1 |
| `--ink` | `#4e453c` | Body text | 9.1:1 |
| `--stone` | `#7d7164` | Captions, labels | 4.6:1 |
| `--accent` | `#1a4a78` | Links, focus, checkboxes | 8.9:1 |
| `--accent-warm` | `#9a6b3d` | Warm highlight | 4.5:1 |

The colour-coded legends on the Atlas, the Writing chart and the Year wheel are
drawn from the same families. Nothing on any page falls below 4.5:1, so colour
carries meaning without carrying it alone.

The previous palette was a cool neutral grey. The captions in it sat at 2.6:1,
which was below AA; the warm set is both closer to the photographs and easier
to read.

---

## Conventions

**Verification.** Atlas entries carry a status. Anything marked `verify` holds a
detail that has not been confirmed, usually a base location or a current funding
round. No grant amounts and no deadlines appear anywhere, because both change
annually and stale figures get trusted.

**The writing page marks each star `running` or `open`.** Running means the
decision is made and in use. Open means it is a real question the practice has not
answered yet.

**Prose is held to the Dear Ordinary craft standard.** No bridging by geometry,
no reversal family, em dashes under five per thousand words, no self-description,
star to ground under one in eight. Set out in full on `writing.html`.

**`noai` and `noimageai` meta tags** are on every page.

---

## Before publishing

The inspiration deck is twenty-eight pages of other artists' paintings and
drawings, screenshotted from Instagram with their captions, and with commenters'
names and profile photographs still in frame. As a private working file that is
ordinary practice. As a download on a public site it republishes a great deal of
copyrighted work, and a number of people's names and faces, without asking any of
them.

Three ways through it:

1. Keep the repository private and change nothing.
2. Publish the deck with each screenshot cropped to the artwork and the artist's
   handle, dropping the comment threads.
3. Keep the deck private and let `files/inspirations.pdf` be the public version,
   since it names everyone and reproduces nothing.

The deck is also 11 MB, which is most of the repository's weight.

---

## Still open

- Two atlas entries are flagged `verify`: Caitlin Winner's and Zoey Frank's base
  locations.
- Four people are held in the atlas but not placed on the map, because their base
  is not recorded anywhere: Joy Kinna, Samantha Haring, Heather Day, Anna Haerlin.
- The inspiration deck holds artists who are not in the atlas at all, among them
  Anthony Cudahy, Pierre Knop, Raffael Bader, Helen Ward, Maryam Gohar,
  Jesse Dstern and Xu Wangjun.

---

*Andrea Robin Studio · September 2026*
