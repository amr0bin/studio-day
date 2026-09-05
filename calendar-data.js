// Studio Day — opportunities calendar data
// One entry per dated event. status: "verified" means the date was read on the
// organisation's own page on the date given; "expected" means it is projected
// from the previous cycle and must be confirmed when the call opens.
// kind: grant | prize | residency | open | window
// Dates are ISO (local). "opens" is optional.
window.STUDIO_CALENDAR = [
  {
    id: "fca-crit-2026-09",
    name: "Federation · Peer Critique, Community Open Studio",
    kind: "window",
    date: "2026-09-25",
    opens: "2026-08-18",
    status: "verified",
    verified: "2026-09-05",
    url: "https://artists.ca/courses/view/id/2945",
    fit: "Friday 6 to 9pm at the FCA Flex Space, 1310 Johnston Street, Granville Island; bring one artwork; by donation; open to all levels; a senior member and juror leads it",
    needs: "register online before the 25th; bring one piece and stay the whole evening to critique others' work",
    check: "the first Critique session of the Curriculum; bring the best recent sheet, whatever it is"
  },
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
    id: "casc-2026-10",
    name: "City of Vancouver · CASC (through a sponsor)",
    kind: "grant",
    date: "2026-10-07",
    opens: "2026-08-26",
    status: "verified",
    verified: "2026-09-05",
    url: "https://vancouver.ca/people-programs/cultural-grants-program.aspx",
    fit: "project grants $2,500 to $15,000 for 2027 activity in Vancouver; individuals from equity-denied communities apply through a sponsor organisation",
    needs: "a sponsor organisation willing to apply on the project's behalf, a project with cash expenses to cover up to 75%, VanApply submission",
    check: "whether the series qualifies for the sponsored route, and whether Arts Umbrella would sponsor; this cycle is probably too soon"
  },
  {
    id: "macdowell-2026-09",
    name: "MacDowell · Spring–Summer 2027",
    kind: "residency",
    date: "2026-09-10",
    opens: "2026-08-17",
    status: "verified",
    verified: "2026-09-05",
    url: "https://www.macdowell.org/apply/apply-for-fellowship",
    fit: "two to eight weeks, private studio, no fee, need-based stipend; residencies 1 March to 31 August 2027",
    needs: "work samples by discipline; one application every 24 months",
    check: "five days away and it locks out the February round; probably let this one pass"
  },
  {
    id: "skowhegan-2026-10",
    name: "Skowhegan · 2027 program",
    kind: "residency",
    date: "2026-10-16",
    opens: "2026-09-01",
    status: "verified",
    verified: "2026-09-05",
    url: "https://skowheganart.org/school/",
    fit: "nine weeks, 5 June to 7 August 2027, emerging artists, scholarships",
    needs: "ten images or six minutes of video, brief notes, a short video narrative; no CV",
    check: "whether nine weeks of leave is conceivable; the interview comes in December"
  },
  {
    id: "fawc-2027-02",
    name: "Fine Arts Work Center · 2027–28 fellowship",
    kind: "residency",
    date: "2027-02-05",
    opens: "2026-10-20",
    status: "expected",
    verified: "2026-09-05",
    url: "https://fawc.org/apply/",
    fit: "seven months in Provincetown, October to April, $1,250 a month, studio and apartment",
    needs: "images, statement; tiered fee from $40",
    check: "2026–27 round closed 6 February 2026; 2027–28 dates to confirm when posted"
  },
  {
    id: "macdowell-2027-02",
    name: "MacDowell · Fall–Winter 2027–28",
    kind: "residency",
    date: "2027-02-10",
    opens: "2027-01-15",
    status: "verified",
    verified: "2026-09-05",
    url: "https://www.macdowell.org/apply/apply-for-fellowship",
    fit: "residencies 1 September 2027 to 29 February 2028; two weeks is a normal stay",
    needs: "work samples; the studies log as the record",
    check: "the round to aim for, with a year of studies behind it"
  },
  {
    id: "ahva-2027",
    name: "UBC AHVA · MFA, MA Art History, MA Critical & Curatorial Studies, PhD Art History",
    kind: "window",
    date: "2027-01-08",
    opens: "2026-10-15",
    status: "verified",
    verified: "2026-09-05",
    url: "https://ahva.ubc.ca/graduate/admissions/",
    fit: "one September intake a year, every program on the same date; three references, writing sample, statement; the art-history PhD wants an art-history MA and a second language",
    needs: "not an application this year; recorded so the date is known. The Diploma in Art History, the bridge from a BFA, has a separate 1 August deadline through Enrolment Services",
    check: "the date recurs each January; reread in October 2029 for the term-four decision"
  },
  {
    id: "siat-2027",
    name: "SFU SIAT · MA, MSc and PhD",
    kind: "window",
    date: "2027-01-15",
    opens: "2026-11-01",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.sfu.ca/siat/programs/graduate/admissions.html",
    fit: "September intake; thesis applicants are expected to have a supervisor agreed before applying; portfolio or interview possible at the later stage",
    needs: "not an application this year; recorded so the date is known",
    check: "the 2026 intake ran 1 November to 15 January; confirm the 2027 window when posted"
  },
  {
    id: "lind-biennial-2026",
    name: "The Polygon · Lind Biennial opens",
    kind: "window",
    date: "2026-12-04",
    status: "verified",
    verified: "2026-09-05",
    url: "https://thepolygon.ca/the-lind-biennial/",
    fit: "five nominated finalists in film, photography and video, on view to 7 February 2027; winner announced 21 January 2027; by donation",
    needs: "nothing to enter; a SeaBus ticket. The prize is nomination-only and lens-based, so this is a room to see, not a door",
    check: "go on a weekday in December before wintering; it is a Seminar-course afternoon, not an application"
  },
  {
    id: "leeds-2027",
    name: "Leeds · MSc Disability Studies, Rights and Inclusion, application target",
    kind: "window",
    date: "2027-05-31",
    status: "expected",
    verified: "2026-09-05",
    url: "https://courses.leeds.ac.uk/d326/disability-studies-rights-and-inclusion-online-msc",
    fit: "online, part-time, 24 months from September 2027; £12,750 payable by module; entry on a degree plus relevant experience; a self-set target, since the course page prints no closing date",
    needs: "the online application form with proof of identity; transcripts; a statement; a possible online interview. The one-page statement from the readiness kit is the same document with the field changed",
    check: "email onlineadmissions@leeds.ac.uk when the 2027/28 portal opens for the actual closing date, and move this entry to it. Not SSHRC-eligible: a UK university"
  },
  {
    id: "cullman-2026-09",
    name: "Cullman Center, NYPL · 2027–28 fellowship",
    kind: "residency",
    date: "2026-09-25",
    status: "verified",
    verified: "2026-09-05",
    url: "https://nypl.onlineapplicationportal.com/misc/guidelines/default.aspx",
    fit: "nine months in New York, September 2027 to May 2028, $90,000, private office; visual artists at work on a book project that needs the Library's collections",
    needs: "research proposal, CV, new letters of recommendation, art or writing sample; 5 pm Eastern",
    check: "let this one pass: twenty days out, and the book that would justify it does not yet exist. The date recurs each late September"
  },
  {
    id: "cullman-2027-09",
    name: "Cullman Center, NYPL · 2028–29 fellowship",
    kind: "residency",
    date: "2027-09-24",
    status: "expected",
    verified: "2026-09-05",
    url: "https://www.nypl.org/about/fellowships-institutes/cullman-center-scholars-writers",
    fit: "as above, for September 2028 to May 2029; the first round where an annual book exists to show",
    needs: "as above; two referees lined up by July",
    check: "a life decision: it cannot be held beside Leeds's second year or a job. Read the guidelines in July 2027 and decide by August whether 2028–29 is a year that can be given to it"
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
    id: "ars-2027",
    name: "Art Rental & Sales · Vancouver Art Gallery open call",
    kind: "open",
    date: "2027-04-30",
    opens: "2027-04-01",
    status: "expected",
    verified: "2026-09-05",
    url: "https://artrentalandsales.com/pages/submissions",
    fit: "juried consignment program for BC-based artists, rental and sale, ten minutes from home",
    needs: "the application package posted in April; recent work; one application a year; rental exclusivity; D-rings and wire",
    check: "the 2026 call closed and the page says check back April 2027; the 30 April deadline is the standing one"
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
    name: "City of Vancouver and Park Board · Artist opportunities page",
    status: "verified",
    verified: "2026-09-05",
    url: "https://vancouver.ca/parks-recreation-culture/opportunities-for-artists.aspx",
    note: "Fieldhouse residencies, studio awards, community-centre residencies and public-art calls are posted here as they arise, not on a cycle. The Stanley Park A-Frame is reserved for artists of the three host Nations. Read the page on the first Monday of each month; move anything open onto the grid."
  },
  {
    name: "SSHRC · Canada Graduate Research Scholarship, Master's: for the UBC counselling MA, not for Leeds",
    status: "verified",
    verified: "2026-09-05",
    url: "https://sshrc-crsh.canada.ca/en/funding/opportunities/canada-graduate-research-scholarships/masters-program.aspx",
    note: "$27,000 for one year of a research master's at a Canadian university; 1 December, 8 pm Eastern, for the following September. The Leeds MSc does not qualify. The UBC MA in Counselling Psychology does, and its own application closes the same day, so the earliest date on the route is 1 December 2030. Recorded here so the date is known; it moves to the grid when that year's Calendar is built."
  },
  {
    name: "SFU School for the Contemporary Arts · 611 Talks, Desire Line Sessions, and the autumn graduate information sessions",
    status: "verified",
    verified: "2026-09-05",
    url: "https://www.sfu.ca/sca/events---news/events.html",
    note: "Free, downtown, twenty minutes' walk. The 611 Talks are visiting artists; Desire Line Sessions are alumni and faculty in conversation; a graduate-programs information session is posted each autumn ahead of the 1 October PhD opening and the 15 February MFA/MA deadline. These are where the doctoral cohort is met: in a room, years before an application. One a term is enough."
  },
  {
    name: "UBC AHVA and the Belkin · department talks and openings",
    status: "verified",
    verified: "2026-09-05",
    url: "https://ahva.ubc.ca/news-events/",
    note: "The events page lists talks, visiting artists and Belkin openings. Two a year keeps the department a known room rather than a name on a form."
  },
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
    name: "City of Vancouver · Communities and Artists Shifting Culture (CASC)",
    status: "verified",
    verified: "2026-09-05",
    url: "https://vancouver.ca/people-programs/cultural-grants-program.aspx",
    note: "Project grants of $2,500 to $15,000 for organisations. Individual artists from equity-denied communities may apply through a sponsor organisation; Arts Umbrella is the obvious sponsor if the series qualifies. 2027 projects: opens 26 August 2026, closes 7 October 2026, with a second 2027 intake to be announced. Not a door on your own."
  }
];
