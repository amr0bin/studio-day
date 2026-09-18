# ORCID and Zenodo

*Working note, 18 September 2026. How to make the work citable and permanently identified, years before any institution is behind it. All facts below were read on ORCID's, Zenodo's and CERN's own pages on 18 September 2026, and should be re-read before the first deposit, because interfaces change.*

---

## The short answer to the question that prompted this

**Yes. Deposit the work, not the system.** Zenodo deposits are per object. Each essay, each annual book, each exposition, each conference paper, each documented body of work gets its own record and its own DOI. The Studio Day repository does not have to be deposited at all, and probably should not be. It is working infrastructure rather than a research output, and depositing it would confuse the record.

What goes in is what a reader would cite.

---

## What these two things are

**ORCID** is a free, permanent identifier for a person who makes research outputs. It is issued at no cost by a non-profit, individual researchers always have free access to their own records, and it is not tied to any institution. It is a sixteen-digit number, usually written as a URL. Its purpose is that everything you make stays attached to you across every change of name, institution and country for the rest of your life.

**Zenodo** is a free, general-purpose open repository operated by CERN with OpenAIRE. It accepts any output type, mints a DataCite DOI for every deposit, supports versioning, and is the standard recommendation for researchers with no institutional repository. Data and metadata are retained for the lifetime of the repository, which CERN states as as long as CERN exists. A personal email registration stays valid whatever happens to your affiliations.

Together they do one thing: they turn work that currently exists only on a website and a login-gated platform into objects with permanent identifiers, gathered under one profile, that a grant officer, an admissions committee or a curator can find and cite.

---

## The part that needs thinking about before the first deposit

This practice carries `noai` and `noimageai` tags, left Substack, and rejected YouTube as a writing home over training rights. Open-access deposit runs against that posture, and the default licence would grant worldwide reuse. So read this section before the first upload.

**Metadata is always public.** Title, description, authors, date and keywords are visible on every record regardless of what you do with the files, and Zenodo licenses metadata under CC0 and exports it for harvesting. Write descriptions knowing they are open, permanent and machine-readable.

**Files are a separate decision.** Visibility is set per record: public, or restricted. A restricted record still gets a DOI, still has a public citable page, and still appears on your ORCID profile. People can request access and you decide individually. Embargo is available if you want files to open automatically on a future date.

**This is the useful combination.** Citability without release. A restricted deposit of a body of paintings gives you a permanent, checkable, dated record that a committee can see exists and can ask to see, while the image files stay under your control. For text you may well want public, because writing that cannot be read does not do the work you want it to do; for images, restricted is the sensible default until you decide otherwise.

**A licence is required for public files.** The default is Creative Commons Attribution, which permits commercial reuse. For text, a more restrictive Creative Commons option may suit better; Zenodo offers a list. For restricted files the licence can be stated in the description instead.

**Files are permanent once published.** Metadata can be edited afterwards, but files cannot be swapped. A correction means publishing a new version, which gets its own DOI while a concept DOI continues to point at the latest. This is a feature for an annual book and a hazard for anything uploaded in a hurry.

**Two things to check before depositing.** Whether a journal you intend to submit to treats a prior deposit as prior publication, which varies. And whether anyone appears in the work who has not signed the image-use release. Nobody's face goes into a permanent international repository without written consent.

---

## Setting it up, once

1. **Register at orcid.org** with a personal email you will keep. Free, no institution required. Record the iD in `identifiers.md` beside this file.
2. **Fill the ORCID profile properly.** Employment, education, and a biography written for a reader who does not know you. This page will be read by admissions committees; treat it as a public document rather than a form.
3. **Register at zenodo.org** and sign in with the ORCID iD, so the two are linked from the start.
4. **In Zenodo, link the ORCID account** under linked accounts, so deposits carry the iD. To have deposits appear automatically on the ORCID profile, set up the synchronisation between ORCID and DataCite, since Zenodo mints through DataCite. Otherwise add each record to ORCID by hand, which takes a minute and is fine at this volume.
5. **Put the ORCID URL** on the artist CV, the grant applications, the email signature, and the Studio Day footer.

---

## Depositing a work

1. New upload. Choose the resource type honestly: publication, image, presentation, poster, video, or other.
2. **Reserve the DOI** before publishing. A reserved DOI can be quoted in an application or an article before the record goes live, which is occasionally very useful.
3. Title, authors with the ORCID iD, publication date, and a description written as though for a stranger.
4. Set visibility. Public for text you want read; restricted for image files; embargo if a date is known.
5. Choose the licence for anything public.
6. Add related identifiers where they exist, linking an essay to the exhibition it accompanied, or a version to the one before it.
7. Publish. Record the DOI in `submissions.md` and in the catalogue row for the work.

---

## What to deposit, and when

| Object | Visibility | When |
|---|---|---|
| **The annual book**, each November | Restricted, or public with low-resolution plates | From the first one. Versioned annually under one concept DOI. |
| **Dear Ordinary**, as a completed sequence or in gathered parts | Public for the text | Once a section is finished and will not change. Patreon remains the place it is read; this is the place it is citable. |
| **A conference paper or talk** | Public | Immediately after giving it. This is the cheapest citable item available and almost nobody deposits them. |
| **A catalogue essay** | Depends on the publisher | Check the agreement first. |
| **A documented body of work**, with the catalogue extract | Restricted | At the close of a phase, not piece by piece. |
| **The commission in care**, with its report | Public for the text, restricted for images, and only with consent | On delivery. This is the deposit that will matter most. |
| **A dated version of the question paragraph** | Public | Optional, and worth considering once there are five of them. |

Not deposited: the Studio Day repository itself, work in progress, anything with an unresolved consent question, and anything a publisher has an exclusive claim on.

---

## Why this is worth an afternoon

SSHRC defines a record of research achievement as any identifiable contribution to the advancement, development and mobilization of knowledge. The word doing the work there is **identifiable**. A Patreon essay is a contribution and is not identifiable in that sense. The same essay with a DOI, attached to an ORCID profile, is.

For the next five years there will be no institution behind this practice. That is the condition this pair of tools was designed for, and it is the one almost no artist uses. It costs nothing, it takes an afternoon to set up, and it means that in 2034 the scholarly ledger is not an assertion about a decade of writing. It is a list of permanent identifiers that anyone can check.

---

## To verify before the first deposit

1. Whether the *Journal for Artistic Research* and the Research Catalogue treat a Zenodo deposit as prior publication. **Unverified.**
2. Zenodo's current licence list, and which option best matches the intention for text. **Unverified.**
3. Whether the ORCID to DataCite synchronisation still works as described, since the integration has changed before. **Unverified.**
