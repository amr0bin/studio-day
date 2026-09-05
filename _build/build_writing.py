#!/usr/bin/env python3
"""Build writing.html for Studio Day, reusing the Dear Ordinary star-chart engine
with entirely new content about writing inside the studio practice."""

src = open('_build/star-chart.html').read()

def swap(old, new, s):
    assert old in s, "NOT FOUND: " + old[:90]
    return s.replace(old, new, 1)

s = src

# ── head ────────────────────────────────────────────────────────────────
s = swap('<title>Dear Ordinary · A Star Chart for Queering Contemplative Spirituality</title>',
         '<title>Writing · Studio Day</title>', s)
s = swap('An interactive star chart mapping paths to goodness through queering contemplative spirituality. Eight constellations of equal dignity — explore it in two dimensions or three, with a scholarly anchor and sources for every star.',
         'What writing does inside the studio practice: where it comes from, how it is made, where it lives, and what forms it takes. Seven constellations, in two dimensions or three.', s)

# ── topbar styling, appended to the existing sheet ───────────────────────
s = swap('  @media (max-width:680px){.wrap{padding:0 20px;}}',
'''  .topbar{display:flex;align-items:baseline;justify-content:space-between;gap:16px 28px;
    flex-wrap:wrap;padding:26px 0 18px;border-bottom:1px solid var(--hair);}
  .mark{font-weight:600;font-size:15px;letter-spacing:.02em;color:var(--ink-strong);text-decoration:none;}
  .navlinks{display:flex;flex-wrap:wrap;gap:20px;}
  .navlinks a{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--stone);
    font-weight:600;text-decoration:none;transition:color .2s var(--ease);}
  .navlinks a:hover{color:var(--ink);}
  .navlinks a[aria-current="page"]{color:var(--ink-strong);}
  .outlink{display:block;background:var(--panel);border:1px solid var(--hair);border-radius:8px;
    padding:18px 20px;margin:0 0 8px;text-decoration:none;transition:border-color .2s var(--ease);}
  .outlink:hover{border-color:var(--stone);}
  .outlink .ol-k{font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;
    color:var(--stone);font-weight:600;display:block;margin:0 0 5px;}
  .outlink .ol-t{font-size:16px;color:var(--ink-strong);font-weight:500;display:block;margin:0 0 5px;}
  .outlink .ol-d{font-size:13.5px;color:var(--ink);display:block;}
  .standard-list{list-style:none;padding:0;margin:0;}
  .standard-list li{padding:12px 0;border-bottom:1px solid var(--hair-soft);font-size:14.5px;}
  .standard-list li:last-child{border-bottom:none;}
  .standard-list b{color:var(--ink-strong);font-weight:600;}
  @media (max-width:680px){.wrap{padding:0 20px;}}''', s)

# ── nav + hero ──────────────────────────────────────────────────────────
s = swap('''  <div class="wrap">
    <header class="hero">
      <p class="eyebrow"><span>Dear Ordinary</span><span class="status">Interactive</span></p>
      <h1>Dear <em>Ordinary</em></h1>
      <p class="lede">A star chart for navigating queering contemplative spirituality — eight constellations of equal dignity, no hierarchy, all threads. Each star carries its scholarly anchor and its sources; explore it as a flat map in two dimensions, or turn it in three.</p>
    </header>''',
'''  <div class="wrap">
    <nav class="topbar" aria-label="Studio Day">
      <a class="mark" href="index.html">Studio&nbsp;Day</a>
      <div class="navlinks">
        <a href="atlas.html">Atlas</a>
        <a href="writing.html" aria-current="page">Writing</a>
        <a href="documentation.html">Documentation</a>
        <a href="year.html">The Year</a>
        <a href="studies.html">Studies</a>
        <a href="teaching.html">Teaching</a>
        <a href="support.html">Support</a>
      </div>
    </nav>

    <header class="hero">
      <p class="eyebrow"><span>Writing</span><span class="status">Interactive</span></p>
      <h1>What the writing <em>is doing</em></h1>
      <p class="lede">Seven constellations covering where the writing comes from, how a sentence is made, where the archive lives, what forms the writing takes, what it owes to the people it cites, when it happens, and who it reaches. Some stars are settled and running. Others are open, and are here because they are the ones a practice like this eventually has to decide.</p>
    </header>

    <a class="outlink" href="https://andrearobinstudio.github.io/dear-ordinary/star-chart.html" target="_blank" rel="noopener">
      <span class="ol-k">The subject of the writing lives elsewhere</span>
      <span class="ol-t">Dear Ordinary &middot; A Star Chart for Queering Contemplative Spirituality</span>
      <span class="ol-d">Eight constellations, thirty-five stars, each with its scholarly anchor and sources. That chart holds what the writing is about. This one holds what the writing does.</span>
    </a>''', s)

# ── panel empty state ───────────────────────────────────────────────────
s = swap('<div class="empty" id="empty"><strong>Select a star</strong>Tap any star to read its anchor, description, and sources. Larger stars hold more depth; colour marks the constellation. In 2D, drag to move and scroll to zoom; in 3D, drag to rotate.</div>',
         '<div class="empty" id="empty"><strong>Select a star</strong>Tap any star to read what it holds and where it stands. Each one is marked either <em>running</em>, meaning the decision is made and in use, or <em>open</em>, meaning it is a real question this practice has not answered yet. Larger stars carry more weight; colour marks the constellation.</div>', s)

# ── legend tiers ────────────────────────────────────────────────────────
s = swap('<span class="lt">Star size · depth of attention</span>',
         '<span class="lt">Star size · how much rests on it</span>', s)
s = swap('''          <span class="li"><span class="sz" style="width:16px;height:16px"></span>Anchor</span>
          <span class="li"><span class="sz" style="width:12px;height:12px"></span>Major</span>
          <span class="li"><span class="sz" style="width:9px;height:9px"></span>Core</span>
          <span class="li"><span class="sz" style="width:6px;height:6px"></span>Opening</span>''',
'''          <span class="li"><span class="sz" style="width:16px;height:16px"></span>Load-bearing</span>
          <span class="li"><span class="sz" style="width:12px;height:12px"></span>Structural</span>
          <span class="li"><span class="sz" style="width:9px;height:9px"></span>Working</span>
          <span class="li"><span class="sz" style="width:6px;height:6px"></span>Detail</span>''', s)

# ── how to read ─────────────────────────────────────────────────────────
s = swap('<div class="note"><strong>How to read this.</strong> Drag to move; scroll to zoom. Switch between a flat <strong>2D</strong> view — where the horizontal axis runs inward to outward and the vertical runs dissolution to integration — and a <strong>3D</strong> view you can rotate through all three dimensions. Colour marks the constellation; larger stars hold more depth. Click any star to read its anchor, description, and sources; the same content is written out in full below. Where the chart touches trauma and systemic harm, it names the system rather than the person who carries its wound.</div>',
         '<div class="note"><strong>How to read this.</strong> Drag to move; scroll to zoom. Switch between a flat <strong>2D</strong> view, where the horizontal axis runs private to public and the vertical runs recording to generating, and a <strong>3D</strong> view you can rotate through all three dimensions. Colour marks the constellation; larger stars carry more weight. Every star is marked <em>running</em> or <em>open</em>, and the open ones are not gaps to be embarrassed about. They are the questions a writing practice arrives at once the first ones are settled.</div>', s)

s = swap('<summary>Every star, in full, with its anchors and references</summary>',
         '<summary>Every star, in full, with its status and references</summary>', s)

# ── axes table ──────────────────────────────────────────────────────────
s = swap('''          <tr><td>X — Inward ↔ Outward</td><td>Interior life toward the relational, political, and ecological</td></tr>
          <tr><td>Y — Dissolution ↔ Integration</td><td>Grief and dark night upward toward wholeness and purpose</td></tr>
          <tr><td>Z — Embodied ↔ Transpersonal</td><td>Somatic sensation toward the cosmic and mystical</td></tr>''',
'''          <tr><td>X — Private ↔ Public</td><td>The notebook and the repository toward the page anyone can read</td></tr>
          <tr><td>Y — Recording ↔ Generating</td><td>Writing that holds what happened, up toward writing that decides what gets made next</td></tr>
          <tr><td>Z — Sentence ↔ Structure</td><td>The line, the clause and the word toward the architecture of a year</td></tr>''', s)

# ── replace the poem section with the craft standard ────────────────────
poem_start = s.index('    <div class="section">\n      <h2>The Asking</h2>')
poem_end   = s.index('    <div class="section">\n      <h2>The foundational principle</h2>')
STANDARD = '''    <div class="section">
      <h2>What the writing is held to</h2>
      <p>Checked before publishing rather than felt for. The list exists because these are failures that read as competent prose, so they survive a reread and get caught only by counting.</p>
      <ul class="standard-list">
        <li><b>No bridging by geometry.</b> No claim that two things occupy the same territory, sit at another end of something, or approach from a different angle. A spatial phrase asserts a relation instead of producing one, and there is usually no territory and no angle.</li>
        <li><b>No reversal family.</b> This covers the not-this-but-that construction and the stripped conjunction pair, where two sentences are run in sequence to do the work of one.</li>
        <li><b>Em dashes under five per thousand words.</b> A count rather than a feeling, because the em dash is the punctuation that hides a sentence which has not decided what it is.</li>
        <li><b>No self-description.</b> The writing does not announce what it is about to do, and it does not tell the reader how to receive it.</li>
        <li><b>Star to ground under one in eight.</b> Most of what is on the page has to be load-bearing. A memorable line surrounded by more memorable lines stops being memorable.</li>
        <li><b>A 1,500 word floor, and 700 to 1,000 of body.</b> The artists get space. The theory gets compressed. If it runs long, the framework is cut before the artists are.</li>
        <li><b>Anchors checked character by character.</b> Against the actual source, every time. AI tools produce confident, plausible and wrong citation details, and a citation carried forward from a draft is the failure most likely to reach print.</li>
        <li><b>Contested reception named, not smoothed.</b> If a debate can be documented with named critics and named positions, it goes in and stays unresolved. If it cannot be documented, the tension is described in the work rather than in the reception.</li>
      </ul>
    </div>

'''
s = s[:poem_start] + STANDARD + s[poem_end:]

# ── principle + credit + footer ─────────────────────────────────────────
s = swap('<p class="principle">To queer contemplative spirituality is to notice that many of the core insights of contemplative traditions — the dissolution of fixed identity, the transgression of boundaries between self and other, the destabilisation of normative categories, the insistence that the sacred exceeds all human attempts to contain it — are themselves profoundly queer in their logic.</p>',
         '<p class="principle">The writing is where the thinking happens. It is not a record of the paintings and it is not an argument for them; the two act on the same premise through different materials, which is why neither one has to explain the other. What the writing is for is the reach past the fact toward the truth behind it, and what it demonstrates is the thinking the work came out of.</p>', s)

s = swap('    <footer>Andrea Robin Studio · Dear Ordinary</footer>',
         '    <footer>Andrea Robin Studio · Studio Day · Writing</footer>', s)

# ── data: constellations, stars, lines ──────────────────────────────────
d_start = s.index('const CATS = {')
d_end   = s.index('/* ── build adjacency (connects) from LINES ── */')

DATA = '''const CATS = {
  source:  {label:"The Reading",       color:"#8496a0"},
  method:  {label:"The Sentence",      color:"#7d7469"},
  keeping: {label:"The Archive",       color:"#7f938c"},
  forms:   {label:"The Forms",         color:"#a2917a"},
  owed:    {label:"What It Owes",      color:"#a5867c"},
  rhythm:  {label:"The Rhythm",        color:"#8f8798"},
  reach:   {label:"The Reach",         color:"#9d7f92"},
};
const CAT_ORDER = ["source","method","keeping","forms","owed","rhythm","reach"];

const STARS = [
  /* ── THE READING ── */
  { id:"question", cat:"source", r:9.5, x:-0.10, y:0.42, z:0.10, name:"Intimacy with the question", anchor:"Running \\u00b7 Maria Popova, The Marginalian", desc:"The mentor for the writing, and what is borrowed is a relationship rather than a manner. Popova writes from inside a question she has not finished with, holds several thinkers in the same room and lets them disagree, and trusts the reader to follow without being managed. This is the north star. Where a post goes thin it is almost always because it began explaining instead of staying inside the question.", refs:"The Marginalian \\u00b7 the register named in the post template, versions one and two" },
  { id:"beside", cat:"source", r:7, x:0.30, y:0.30, z:0.55, name:"Writing standing beside the work", anchor:"Running \\u00b7 Emma Webster, Lonescape (2021), Decimate (2026)", desc:"Lonescape is collected reflection on landscape and image-making, standing next to the paintings as its own artifact rather than documenting them. Decimate is a digital sketchbook published on the occasion of a show, carrying a title and an epigraph instead of a year. Both make the case that the writing is a second body of work rather than an appendix to the first.", refs:"Petzel, New York \\u00b7 part of what prompted Dear Ordinary to start" },
  { id:"already", cat:"source", r:6, x:0.10, y:-0.35, z:0.68, name:"A book from work already documented", anchor:"Running \\u00b7 Florian Gadsby", desc:"A book a year, assembled from material captured because the practice captures material, rather than produced for the book. It is the reason an annual volume is affordable inside thirty-five studio hours a month. Nothing in it is made for it.", refs:"By My Hands (2024) \\u00b7 documenting online since 2014" },
  { id:"beginner", cat:"source", r:6.5, x:-0.42, y:0.55, z:-0.20, name:"Beginner's mind", anchor:"Running \\u00b7 Shunryu Suzuki", desc:"In the beginner's mind there are many possibilities; in the expert's mind there are few. This is what keeps the writing honest and what makes it inviting, because a reader can feel when someone is seeking alongside them rather than delivering from above. It is also the permission to publish a question rather than a conclusion.", refs:"Suzuki (1970) Zen Mind, Beginner's Mind" },
  { id:"chart", cat:"source", r:5.5, x:0.20, y:0.12, z:0.82, name:"The star chart as the subject", anchor:"Running \\u00b7 Dear Ordinary star chart", desc:"Eight constellations and thirty-five stars, held as a separate document and linked rather than duplicated. That chart is what the writing is about. This one is what the writing does. Keeping them apart is what stops either from becoming a summary of the other.", refs:"andrearobinstudio.github.io/dear-ordinary/star-chart.html" },
  { id:"readinglog", cat:"source", r:5, x:-0.62, y:0.20, z:-0.10, name:"A record of what was read", anchor:"Open \\u00b7 no system in place", desc:"A writing practice runs on a reading practice, and the reading is currently untracked. A dated log of what was read and what it changed would make the influences visible to the writer as well as the reader, and would remove the annual scramble to remember where a thought came from.", refs:"Would sit in the Monday block \\u00b7 low cost, no decision made" },
  { id:"otherfields", cat:"source", r:5, x:-0.48, y:0.34, z:0.34, name:"Reading outside the field", anchor:"Open \\u00b7 partly happening, not deliberate", desc:"The learning design decade is already the second half of an unusual pair, and it is the reason the inquiry has a methodology under it rather than an intuition. Reading deliberately outside painting is what keeps that pairing productive instead of incidental.", refs:"Compare Webster's years in set design and interactive advertising" },

  /* ── THE SENTENCE ── */
  { id:"standard", cat:"method", r:8.5, x:-0.35, y:-0.05, z:-0.72, name:"The craft standard", anchor:"Running \\u00b7 written, counted, checked", desc:"A list of constructions that read as competent prose and are therefore invisible on a reread. Because they survive editing by feel, they are caught by counting instead. The standard is applied before publishing rather than aspired to.", refs:"Set out in full further down this page" },
  { id:"geometry", cat:"method", r:6, x:-0.52, y:-0.22, z:-0.85, name:"No bridging by geometry", anchor:"Running \\u00b7 zero tolerance", desc:"No claim that two things occupy the same territory, sit at another end of something, or arrive from a different angle. A spatial phrase asserts a relation instead of producing one, and there is generally no territory and no angle. The fix is always to state the actual cause.", refs:"Named in the Week 17 entry" },
  { id:"reversal", cat:"method", r:6, x:-0.68, y:-0.10, z:-0.72, name:"The reversal family", anchor:"Running \\u00b7 zero tolerance", desc:"Covers the not-this-but-that construction and the stripped conjunction pair, where two sentences run in sequence to do the work of one. Both produce a rhythm that feels like emphasis and delivers no additional information.", refs:"Checked by pattern count before publishing" },
  { id:"ratio", cat:"method", r:6.5, x:-0.44, y:0.08, z:-0.55, name:"Star to ground", anchor:"Running \\u00b7 under one in eight", desc:"Most of what is on the page has to be load-bearing. A memorable line surrounded by other memorable lines stops being memorable, and the reader loses the ability to tell what matters. This is the one part of the standard that cannot be counted mechanically and needs reading.", refs:"The essay pages are the ones worth checking by eye" },
  { id:"template", cat:"method", r:6.5, x:-0.20, y:-0.12, z:0.48, name:"The shape of a post", anchor:"Running \\u00b7 post template, versions one and two", desc:"Eight sections: the opening, the framework, the first artist, the second, the connection, the invitation, the keywords, the anchors. The shape means the writing starts from a question about content rather than a question about structure, every week, for fifty-six weeks.", refs:"Template v2 incorporates the Week 09 register shift" },
  { id:"exemplar", cat:"method", r:5.5, x:-0.30, y:0.22, z:-0.34, name:"A held example of the voice", anchor:"Running \\u00b7 Week 06 exemplar, Week 09 shift", desc:"One entry kept as the measure of the register, and one that marks where the register changed. When a draft is running lush, it is measured against the restraint of the exemplar rather than against a rule.", refs:"voice-exemplar-week-06 \\u00b7 week-09-rupture-marginalian" },
  { id:"editor", cat:"method", r:5, x:0.28, y:-0.30, z:-0.40, name:"A reader before it goes out", anchor:"Open \\u00b7 currently nobody", desc:"Every post is currently written, checked and published by the same person. A standing reader who sees a draft before it publishes would catch what a self-check structurally cannot, and would change what the writing is willing to risk. It also introduces a dependency into a weekly rhythm, which is the reason it has not happened.", refs:"No decision made \\u00b7 would need to survive the weekly cadence" },

  /* ── THE ARCHIVE ── */
  { id:"archive", cat:"keeping", r:8, x:-0.78, y:-0.18, z:0.62, name:"The archive of record", anchor:"Running \\u00b7 markdown repository, git history", desc:"The repository is the archive; the platform is only distribution. Git gives dated version history, which matters as evidence of authorship and as a record of how a thought changed. Publishing happens from the archive and never inside a platform, and at least one copy is kept outside the host.", refs:"Canadian copyright exists automatically from the moment of writing" },
  { id:"distribution", cat:"keeping", r:6, x:-0.30, y:-0.42, z:0.40, name:"Distribution is not a home", anchor:"Running \\u00b7 Patreon", desc:"The login gate keeps the writing out of the open crawl, which handles being taken about as well as anything can. Being lost is the likelier risk and the platform does nothing about it. Separating the two meanings of safe is what makes the arrangement legible.", refs:"Moved from Substack \\u00b7 the archive handles permanence" },
  { id:"licence", cat:"keeping", r:6, x:-0.55, y:-0.60, z:0.30, name:"Refusing a training licence", anchor:"Running \\u00b7 YouTube rejected as a writing home", desc:"Uploading grants a worldwide, sublicensable, transferable licence, and Google has confirmed it trains on the material. The third-party training setting, off by default, does not cover Google's own models. The essays stay off it. A narrated video made from an essay is a different question and is treated as one.", refs:"Google to CNBC and to a federal court, June 2026" },
  { id:"rights", cat:"keeping", r:5, x:-0.62, y:-0.48, z:0.72, name:"Licensing your own text", anchor:"Open \\u00b7 nothing stated anywhere", desc:"No licence is currently declared on any of the writing. The default is all rights reserved, which is workable, but it leaves a reader who wants to quote or teach from it with no answer. A stated position, however restrictive, is more useful than silence.", refs:"noai and noimageai tags are in place; a text licence is not" },
  { id:"deposit", cat:"keeping", r:5, x:-0.35, y:-0.72, z:0.85, name:"ISBN and legal deposit", anchor:"Open \\u00b7 raised, not decided", desc:"Whether the annual book carries an ISBN and is deposited with Library and Archives Canada. An ISBN makes it findable and orderable; deposit places it in the national collection. Both are administrative rather than creative, and both are much easier to do at the first volume than retroactively at the fifth.", refs:"Still open alongside trim size, page count and print method" },

  /* ── THE FORMS ── */
  { id:"essay", cat:"forms", r:8, x:0.42, y:0.05, z:0.20, name:"The weekly essay", anchor:"Running \\u00b7 one a week, fifty-six weeks", desc:"The primary form and the one everything else is drawn from. Seven hundred to a thousand words of body, three artists, a framework compressed, an invitation offered peer to peer. Because it is committed to the archive as written, everything downstream of it is selection rather than production.", refs:"All fifty-six week files exist \\u00b7 the curriculum is drafted" },
  { id:"book", cat:"forms", r:7.5, x:0.58, y:-0.30, z:0.80, name:"The annual book", anchor:"Running \\u00b7 completed every November", desc:"The writing, the process documentation and the year's works gathered into one volume, and the volume is sold. Closing the chapter is what it is for; selling it is how it reaches anyone. The November deadline exists so that December is genuinely clear.", refs:"Compilation sits in Monday blocks through October and November" },
  { id:"sketchbook", cat:"forms", r:6.5, x:0.32, y:0.20, z:0.62, name:"What did not become the work", anchor:"Running \\u00b7 the Decimate principle", desc:"The book holds the false starts, the abandoned pieces, the studies that were never released, and the studio log with the hours and materials in it. The finished work is available elsewhere. A sketchbook is cheaper to make, better to read, and does not compete with selling the paintings.", refs:"Webster's Decimate, $35, a digital sketchbook rather than a catalogue" },
  { id:"video", cat:"forms", r:6, x:0.72, y:0.10, z:-0.10, name:"The essay as a doorway", anchor:"Running \\u00b7 one essay a month becomes a narrated video", desc:"The essay is the source and the video is the doorway, with the full piece linked for anyone who wants to read it. This is what YouTube is for in the arrangement: search-based discovery, no posting schedule, and no writing living there.", refs:"Deferred until the Monday block can carry the editing" },
  { id:"statement", cat:"forms", r:5.5, x:0.80, y:-0.20, z:0.10, name:"The artist statement", anchor:"Open \\u00b7 no current version held to the standard", desc:"The statement is the one piece of writing that every application, gallery and studio visit asks for, and it is the one most often written under time pressure in a register the writer would not otherwise use. Writing it deliberately, to the same standard as an essay, would make it the shortest and hardest thing on this map.", refs:"Required by most of the funders on the Atlas" },
  { id:"titles", cat:"forms", r:5, x:0.55, y:0.48, z:-0.62, name:"Titles as the smallest unit", anchor:"Open \\u00b7 no convention decided", desc:"A title is the only writing that arrives attached to the work and travels with it everywhere. The studies series currently numbers rather than names. Whether a piece gets a title, and whether the title is descriptive or does its own work, is undecided and will be decided by default if it is not decided deliberately.", refs:"Flora Yukhnovich labels studies by year and nothing else" },
  { id:"walltext", cat:"forms", r:5, x:0.86, y:-0.05, z:0.42, name:"Wall text and exhibition writing", anchor:"Open \\u00b7 not yet needed", desc:"Writing that has to work standing up, in a room, next to the thing it describes, read by someone who did not choose to read it. A different constraint from the essay, and the form where the compression practised in the framework sections would pay off most.", refs:"Becomes live at the first juried or solo exhibition" },
  { id:"grantwriting", cat:"reach", r:6, x:0.66, y:0.30, z:0.34, name:"The grant register", anchor:"Open \\u00b7 the highest-value writing not yet being done", desc:"A different register from the essay: a panel reading quickly, against criteria, with no obligation to be persuaded. It is also the writing that returns the most hours to the practice, because a grant buys studio time and a sale consumes it. Practising it is a use of the Monday block that competes directly with everything else there.", refs:"Ranked first by hours returned on the Atlas" },

  /* ── WHAT IT OWES ── */
  { id:"anchors", cat:"owed", r:7, x:0.05, y:-0.55, z:0.05, name:"Anchors checked character by character", anchor:"Running \\u00b7 against the actual source, every time", desc:"AI tools reliably produce confident, plausible and wrong citation details, including titles, years, journals and publishers. A citation carried forward from a draft without checking is the single failure most likely to reach print, and the one that would do the most damage to everything around it.", refs:"The fact-checking instructions held with the project" },
  { id:"contested", cat:"owed", r:6, x:0.24, y:-0.42, z:0.24, name:"Contested reception, left contested", anchor:"Running \\u00b7 named or not raised", desc:"Where an artist's reception sits inside a live debate, the debate is named with its critics and its positions, woven into the description of the work rather than appended to it, and left unresolved. Where it cannot be documented, the tension is described in the work instead. No invented controversy, and no invented resolution.", refs:"Post template, section four" },
  { id:"three", cat:"owed", r:5.5, x:-0.05, y:-0.28, z:-0.15, name:"Three artists a week", anchor:"Running \\u00b7 historical, contemporary, emerging", desc:"Meeting the territory across time rather than illustrating it with one example. The emerging artist is the one most often needing verification, since exhibition histories and representation change and a claim true at drafting may be false at publishing.", refs:"One hundred and sixty-eight entries across fifty-six weeks" },
  { id:"permission", cat:"owed", r:5, x:0.34, y:-0.62, z:-0.05, name:"Quoting, and the right to", anchor:"Open \\u00b7 no working rule", desc:"How much of someone else's text can be quoted, when permission is required rather than courteous, and what changes when the writing moves from a free post into a book that is sold. The answer differs between those two cases, and the book is the case where getting it wrong is expensive.", refs:"Becomes live at the first volume" },
  { id:"access", cat:"owed", r:5, x:0.46, y:-0.50, z:-0.42, name:"Alt text and plain language", anchor:"Open \\u00b7 practised, not systematic", desc:"Alt text has been written carefully for individual posts. Whether every image across every surface carries it, and whether the essays offer a plainer entry point for readers the register does not serve, is undecided. This is the part of the writing where fifteen years of accessibility work is most directly applicable and least applied.", refs:"Screen readers announce alt text in full \\u00b7 order matters" },

  /* ── THE RHYTHM ── */
  { id:"monday", cat:"rhythm", r:6.5, x:-0.70, y:0.15, z:-0.35, name:"Where the writing sits", anchor:"Running \\u00b7 and the least protected block", desc:"Eight hours on Sunday for making, two to four on Monday evening for everything else. If each week is revised before it goes out, that is a weekly session with no slot in either block, and it is the thing most likely to quietly eat a Sunday. Publishing a finished piece from the archive is a twenty-minute task; revising one is not.", refs:"The capacity arithmetic \\u00b7 nine to seventeen hours a month for all admin" },
  { id:"november", cat:"rhythm", r:6, x:-0.20, y:-0.78, z:0.55, name:"Completed in November", anchor:"Running \\u00b7 the one hard deadline", desc:"The book is finished and sent to print in November so that December is genuinely clear. December holds a birthday and the anniversary of a significant loss and is kept as a retreat. December is also a strong month for art sales, and the decision stands anyway.", refs:"Nothing in December should require her" },
  { id:"log", cat:"rhythm", r:5, x:-0.85, y:-0.30, z:-0.12, name:"The studio log", anchor:"Open \\u00b7 named as book material, not yet kept", desc:"Hours, materials, and what shifted. Private, undated in the sense of never published, and distinct from the essays. It is already listed as one of the three layers the annual book draws on, which means it is currently a promise rather than a practice.", refs:"Named in the documentation plan as a book input" },
  { id:"unwritten", cat:"rhythm", r:5.5, x:-0.55, y:0.40, z:-0.60, name:"What is left unwritten", anchor:"Open \\u00b7 no rule, and it needs one", desc:"A weekly public practice built on a body of work about wounding will produce material that should not be published, and the decision about which is which is currently made in the moment, weekly, by a tired person. A rule made in advance is worth more than a judgement made at the point of publishing.", refs:"The curriculum touches trauma and systemic harm throughout" },

  /* ── THE REACH ── */
  { id:"peer", cat:"reach", r:7, x:0.62, y:0.55, z:-0.30, name:"Offered peer to peer", anchor:"Running \\u00b7 the closing move of every post", desc:"The invitation describes where the writer is starting and leaves space for the reader to find their own, then releases them from obligation. Genuinely open rather than performatively humble. The reader's experience is not being managed.", refs:"Post template, section six" },
  { id:"onevoice", cat:"reach", r:5.5, x:0.78, y:0.38, z:-0.55, name:"One voice across every surface", anchor:"Open \\u00b7 currently drifting", desc:"The essays are held to a standard. The captions, the listing descriptions, the emails and the site copy are not. A reader who arrives through a caption and stays for an essay meets two different writers, and the caption is the one they met first.", refs:"Delmaire's captions are candid; Neumann's are four silent lines" },
  { id:"generative", cat:"reach", r:6.5, x:0.35, y:0.85, z:0.15, name:"Writing that decides the next work", anchor:"Open \\u00b7 the largest unclaimed use", desc:"Currently the writing follows the studio week and reflects on it. The practice invitation at the end of each entry is already an instruction for making, addressed to a reader. Turning it inward, so that the week's question sets what happens on Sunday, would make the writing generative rather than reflective and would close the loop the whole project assumes.", refs:"The art practice does not illustrate the thesis; it acts on the same premise" },
  { id:"talk", cat:"reach", r:5, x:0.90, y:0.20, z:-0.20, name:"Writing for the voice", anchor:"Open \\u00b7 no version exists", desc:"An artist talk is written to be heard once, without rereading, by people who cannot scroll back. Sentence length, repetition and signposting all invert. It is also the form that a taught session, a studio visit and a narrated video all quietly depend on.", refs:"The narrated video already needs this and is using essay prose" },
];

const LINES = [
  ['question','beside'],['question','beginner'],['question','standard'],['question','peer'],
  ['question','exemplar'],['question','otherfields'],
  ['beside','book'],['beside','sketchbook'],['beside','chart'],
  ['already','book'],['already','sketchbook'],['already','log'],
  ['beginner','peer'],['beginner','unwritten'],['beginner','generative'],
  ['chart','essay'],['chart','archive'],
  ['readinglog','otherfields'],['readinglog','log'],['readinglog','anchors'],
  ['otherfields','generative'],
  ['standard','geometry'],['standard','reversal'],['standard','ratio'],
  ['standard','exemplar'],['standard','editor'],['standard','onevoice'],
  ['template','essay'],['template','three'],['template','peer'],['template','contested'],
  ['exemplar','ratio'],['editor','unwritten'],
  ['archive','distribution'],['archive','licence'],['archive','rights'],
  ['archive','book'],['archive','essay'],['archive','monday'],
  ['distribution','licence'],['distribution','rights'],
  ['licence','video'],['rights','deposit'],['deposit','book'],
  ['essay','video'],['essay','book'],['essay','monday'],['essay','three'],
  ['book','sketchbook'],['book','november'],['book','permission'],['book','log'],
  ['sketchbook','log'],['video','talk'],['video','monday'],
  ['statement','grantwriting'],['statement','walltext'],['statement','onevoice'],
  ['titles','onevoice'],['titles','generative'],
  ['walltext','talk'],['grantwriting','monday'],['grantwriting','peer'],
  ['anchors','contested'],['anchors','three'],['anchors','permission'],
  ['contested','three'],['permission','book'],
  ['access','onevoice'],['access','walltext'],['access','peer'],
  ['monday','november'],['monday','log'],['monday','unwritten'],
  ['november','log'],['unwritten','peer'],
  ['peer','generative'],['peer','onevoice'],['generative','essay'],
  ['generative','titles'],['onevoice','talk'],
];

'''
s = s[:d_start] + DATA + s[d_end:]

# ── stale social/accessibility metadata from the source chart ───────────
s = swap('<meta property="og:title" content="Dear Ordinary" />',
         '<meta property="og:title" content="Writing \u00b7 Studio Day" />', s)
s = swap('<meta property="og:description" content="An interactive star chart for navigating queering contemplative spirituality. Eight constellations: The Body\'s Wisdom, The Hearthstone, The Mystical Thread, The Engaged Path, The Wide Waters, The Dark Night, The Queer Path, The Making." />',
         '<meta property="og:description" content="What writing does inside the studio practice. Seven constellations: The Reading, The Sentence, The Archive, The Forms, What It Owes, The Rhythm, The Reach." />', s)
s = swap('aria-label="Star chart of queering contemplative spirituality. Interactive; a readable list of every star follows below."',
         'aria-label="A map of what writing does inside the studio practice. Interactive; a readable list of every star follows below."', s)

open('/home/claude/studio-day/writing.html', 'w').write(s)
print("writing.html rebuilt:", len(s), "bytes")
