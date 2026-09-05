// Studio Day — opportunities calendar data
// One entry per dated event. status: "verified" means the date was read on the
// organisation's own page on the date given; "expected" means it is projected
// from the previous cycle and must be confirmed when the call opens.
// kind: grant | prize | residency | open | window
// Dates are ISO (local). "opens" is optional.
window.STUDIO_CALENDAR = [
  {
    id: "vsc-2026-09",
    name: "Vermont Studio Center",
    kind: "residency",
    date: "2026-09-30",
    opens: "2026-08-15",
    status: "verified",
    verified: "2026-09-05",
    url: "https://vermontstudiocenter.org/apply",
    fit: "painting and work on paper; two to four week sessions July to December 2027",
    needs: "five images, $25 fee; all residents receive a partial fellowship, about a third a full one",
    check: "whether two weeks away from work is possible in that window"
  },
  {
    id: "bcac-pd-2026",
    name: "BC Arts Council · Professional Development",
    kind: "grant",
    date: "2026-10-15",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.bcartscouncil.ca/program/",
    fit: "short-term learning activities that advance a practice",
    needs: "registration in the grant system well ahead; CV; the activity named and costed",
    check: "the 2026/27 guidelines say next intake fall 2026, subject to change; date above is a placeholder"
  },
  {
    id: "hsfk-2027",
    name: "Herbert Smith Freehills Kramer Portrait Award",
    kind: "prize",
    date: "2027-01-06",
    opens: "2026-10-15",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.npg.org.uk/",
    fit: "painted portraits only, human figure predominant; open to all nationalities, 18+",
    needs: "one entry; digital first, then shortlisted paintings couriered to London for judging",
    check: "2026 call closed 6 January 2026; the 2027 call was not yet posted"
  },
  {
    id: "ssnap-2027-open",
    name: "Salt Spring National Art Prize · submissions open",
    kind: "window",
    date: "2027-01-03",
    status: "verified",
    verified: "2026-09-05",
    url: "https://saltspringartprize.ca/artists/submission-info/",
    fit: "any 2D work; Canadian citizens and permanent residents 18+",
    needs: "one entry form and $35 per work",
    check: ""
  },
  {
    id: "banff-bair-2027",
    name: "Banff Centre · BAiR Summer",
    kind: "residency",
    date: "2027-01-21",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.banffcentre.ca/visual-arts",
    fit: "faculty-mentored studio residency, individual studios, scholarships",
    needs: "images, statement, project description",
    check: "2026 deadline was 21 January 2026; 2027 date not confirmed"
  },
  {
    id: "rp-2027",
    name: "Royal Society of Portrait Painters · annual open",
    kind: "open",
    date: "2027-02-03",
    opens: "2026-11-03",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.mallgalleries.org.uk/open-calls/royal-society-portrait-painters",
    fit: "paintings and drawings from life; international entries selected online only",
    needs: "one image under 5MB per work, up to four works, fee per work; ship only if selected",
    check: "2026 window was 3 November to 3 February; 2027 dates to be announced"
  },
  {
    id: "psa-2027",
    name: "Portrait Society of America · The International",
    kind: "prize",
    date: "2027-02-10",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.portraitsociety.org/the-international-portrait",
    fit: "painting, drawing, sculpture; open to non-members",
    needs: "$55 for up to three entries; finalists ship the original and attend in Washington, 8 May 2027",
    check: "site shows a February 2027 date but the wording reads as carried over; confirm"
  },
  {
    id: "figurativas-2027",
    name: "Figurativas · MEAM Barcelona",
    kind: "prize",
    date: "2027-03-31",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.meam.es/",
    fit: "figurative painting; biennial, next edition 2027",
    needs: "selected works shipped to Barcelona for in-person jury",
    check: "2025 virtual jury closed 13 April 2025; 2027 dates not posted"
  },
  {
    id: "vsc-2027-03",
    name: "Vermont Studio Center",
    kind: "residency",
    date: "2027-03-31",
    opens: "2027-02-15",
    status: "verified",
    verified: "2026-09-05",
    url: "https://vermontstudiocenter.org/apply",
    fit: "sessions January to June 2028",
    needs: "five images, $25 fee",
    check: ""
  },
  {
    id: "kingston-2027-open",
    name: "Kingston Prize · entries open",
    kind: "window",
    date: "2027-04-15",
    status: "expected",
    verified: "2026-09-05",
    url: "https://kingstonprize.ca/how-to-enter-2/",
    fit: "portrait of a Canadian, painting or drawing, from a sitting",
    needs: "one jpg 1 to 4MB, one-page PDF with statement, bio and CV, $40",
    check: "2026 window was 15 April to 1 September; now annual"
  },
  {
    id: "ssnap-2027-close",
    name: "Salt Spring National Art Prize · deadline",
    kind: "prize",
    date: "2027-05-31",
    status: "verified",
    verified: "2026-09-05",
    url: "https://saltspringartprize.ca/artists/submission-info/",
    fit: "finalists announced week of 19 July 2027; exhibition opens 24 September 2027",
    needs: "8pm PDT close; $35 per entry; shipping support for finalists",
    check: ""
  },
  {
    id: "tbw-2027",
    name: "Trinity Buoy Wharf Drawing Prize",
    kind: "prize",
    date: "2027-06-09",
    status: "expected",
    verified: "2026-09-05",
    url: "https://trinitybuoywharfdrawingprize.org/",
    fit: "drawing, any medium; international; up to three drawings",
    needs: "online registration, then physical drawings to a UK collection centre before shortlisting",
    check: "2026 deadline was 9 June 2026"
  },
  {
    id: "kingston-2027-close",
    name: "Kingston Prize · deadline",
    kind: "prize",
    date: "2027-09-01",
    status: "expected",
    verified: "2026-09-05",
    url: "https://kingstonprize.ca/how-to-enter-2/",
    fit: "$25,000; thirty finalists shown in the Greater Toronto Area in November",
    needs: "the artist must have met the subject; the work made inside the competition window",
    check: ""
  },
  {
    id: "vsc-2027-09",
    name: "Vermont Studio Center",
    kind: "residency",
    date: "2027-09-30",
    opens: "2027-08-15",
    status: "verified",
    verified: "2026-09-05",
    url: "https://vermontstudiocenter.org/apply",
    fit: "sessions July to December 2028",
    needs: "five images, $25 fee",
    check: ""
  },
  {
    id: "bcac-va-2026",
    name: "BC Arts Council · Individual Arts Grants: Visual Artists",
    kind: "grant",
    date: "2026-12-09",
    opens: "2026-10-24",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.bcartscouncil.ca/program/visual-artists-crafts-artists-critics-curators/",
    fit: "creation of new work, up to $15,000; excludes arts education and therapeutic projects",
    needs: "registration a fortnight ahead; CV to three pages; up to 12 images; workplan; budget",
    check: "eligibility asks for two curated exhibitions with fees paid; last intake closed 9 December 2025, next expected fall 2026"
  },
  {
    id: "bcac-va-2027",
    name: "BC Arts Council · Individual Arts Grants: Visual Artists",
    kind: "grant",
    date: "2027-12-08",
    opens: "2027-10-22",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.bcartscouncil.ca/program/visual-artists-crafts-artists-critics-curators/",
    fit: "as above",
    needs: "as above",
    check: "projected from the annual pattern"
  }
];

// Rolling or undated. Shown in a separate list, never on the grid.
window.STUDIO_ROLLING = [
  {
    name: "Canada Council · Explore and Create: Artistic Creation",
    status: "verified",
    verified: "2026-09-05",
    url: "https://canadacouncil.ca/funding/grants/explore-and-create",
    note: "Apply any time before the project starts. Results take about five months. The portal profile has to be validated as a professional artist first, which takes weeks; do that now."
  },
  {
    name: "Elizabeth Greenshields Foundation",
    status: "unverified",
    verified: "",
    url: "https://www.elizabethgreenshieldsfoundation.org/",
    note: "Representational painting and drawing only; the research report puts the first-application age window at 18 to 41. Confirm the age rule on the foundation's site before anything else; it decides whether this is the best grant on the list or closed."
  },
  {
    name: "City of Surrey Cultural Grants",
    status: "verified",
    verified: "2026-09-05",
    url: "https://www.surrey.ca/arts-culture/cultural-grants",
    note: "Not paid to individuals. Only a route if partnered with an organisation such as Arts Umbrella."
  }
];
