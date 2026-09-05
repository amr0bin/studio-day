#!/usr/bin/env python3
"""Assemble atlas.html, injecting the world-map paths extracted from the repo."""
import json

land   = open('_build/_land.txt').read()
sphere = open('_build/_sphere.txt').read()
coast  = open('_build/_coast.txt').read()

# projection fitted from the existing region coordinates (residual < 0.7px)
PY = [3.048e-07, 1.50911e-05, -3.1195183055, 267.6541000389]
PS = [-8.72e-08, -0.0001292801, 6.92595e-05, 2.6898377856]

def poly(p, v):
    r = 0.0
    for c in p:
        r = r * v + c
    return r

def project(lat, lng):
    return round(500 + lng * poly(PS, lat), 2), round(poly(PY, lat), 2)

# ---------------------------------------------------------------- entries
# kind: artist | grant | prize | residency | network
# certainty: "held" = stated in the project's own files or well established
#            "check" = base or details should be verified before relying on it
E = [
 # ── practices: how a working life was built ─────────────────────────────
 dict(id="jsmith", name="Jean Smith", kind="artist", place="Vancouver, British Columbia",
   lat=49.28, lng=-123.12, certainty="held",
   brief="11\u00d714 inch portraits at $100 USD, sold direct on Facebook since 2016. More than 1,500 sold. Left the day job; surplus income directed toward founding a free artist residency.",
   why="One format, one price, one rhythm, sold from an apartment, with the surplus funding something beyond the practice. The proof that small work is a different path rather than a lesser one, and priced for access as an explicitly political choice.",
   take="What does not transfer: thirty-five years of cultural standing through Mecca Normal, a New York Times Magazine feature in 2021, and fifteen-hour days at peak. What does: the fixed format, which removes every pricing decision before it is made.",
   src=["Covered by CBC, The Tyee, the New York Times Magazine and Democracy Now"]),

 dict(id="cwinner", name="Caitlin Winner", kind="artist", place="United States",
   lat=42.25, lng=-73.79, certainty="check",
   brief="Teaching and coaching circles running alongside a painting practice built on weekends around a full-time job.",
   why="The closest visible analogue to a practice run alongside a career. A visible arc from roughly 2021 to 2025: Manifest, the Royal Institute of Oil Painters, First Street Gallery, the Martha Boschen Porter Fund, a Vermont Studio Center residency, a cookbook commission, a Studio Visit cover, Hyperallergic, then Carrie Haddad and Galerie Mokum.",
   take="The order is the lesson. Juried shows and grants first, press after, representation after that, teaching on top of the credibility rather than instead of it.",
   src=["Base location on this map is approximate and should be verified"]),

 dict(id="zfrank", name="Zoey Frank", kind="artist", place="United States",
   lat=40.58, lng=-105.08, certainty="check",
   brief="Roughly one new course a year, taught live, recorded the same day, then sold afterwards at a lower price and launched to a mailing list.",
   why="The teaching model Foundations is built against. Four sessions of about two and a half hours, so around ten hours of delivery at $185 to $350. Students find her by searching for what they want to learn rather than because they were already collectors.",
   take="Foundations runs eighteen hours against her ten, which is what supports the higher price. The risk is over-designing. Version one should sit closer to her format than to an institutional course.",
   src=["Base location on this map is approximate and should be verified"]),

 dict(id="fyukh", name="Flora Yukhnovich", kind="artist", place="London, United Kingdom",
   lat=51.51, lng=-0.13, certainty="held",
   brief="MA in 2017, found on Instagram by a dealer, seven-figure auction sales within four years, now with Hauser & Wirth alongside Victoria Miro. Studies given their own section level with the paintings, labelled by year and nothing else.",
   why="Two separate reasons. The site structure, where studies sit level with the finished paintings instead of below them. And the route itself, held as the one that cannot be planned for and should not be treated as impossible either.",
   take="The site structure transfers directly and costs nothing. The career does not transfer. What carries across from it is a singular visual language with real art-historical grounding, which is built rather than discovered.",
   src=[]),

 dict(id="gadsby", name="Florian Gadsby", kind="artist", place="High Barnet, North London",
   lat=51.65, lng=-0.20, certainty="held",
   brief="A ceramicist working alone from a studio in High Barnet, releasing three collections a year that sell out in minutes. A book a year, made from work already documented.",
   why="Every camera position, light and shot order decided once, so the choosing stops. That single decision is the reason a one-person studio can sustain both the making and the documentation, and it is the direct source of the setups on the Documentation page.",
   take="The annual book is the closer parallel: assembled from a year of material that was captured anyway rather than produced for the book. Documenting online since 2014, which is the part that is not reproducible in a year.",
   src=["Born 1992; based in North London since childhood"]),

 dict(id="neumann", name="Ini Neumann", kind="artist", place="Hamburg, Germany",
   lat=53.55, lng=9.99, certainty="held",
   brief="We Are Studio Studio. Wheel-thrown stoneware, sold direct. A series name with a code for each one-off piece, sold work left listed, and one plain line about variation in hand-made things.",
   why="Two things at once. The listing convention, which handles the problem of selling unique pieces without the shop looking depleted. And the product photography, which is the reference for the whole Documentation page.",
   take="The captions are four silent lines and Delmaire's are candid about failure. Both are honest and they suit different things. The studies release probably wants the quiet register and the process video the candid one, though that is a guess rather than a finding.",
   src=["Photography on the shop appears to be credited to Anna Haerlin"]),

 dict(id="delmaire", name="H\u00e9l\u00e8ne Delmaire", kind="artist", place="Lille, France",
   lat=50.63, lng=3.06, certainty="held",
   brief="Oil painter working from a studio in Lille. A print release on a named day and hour, stated in three time zones. Captions that name what is failing and what cannot be touched yet.",
   why="The release mechanism and the time-zone courtesy, which makes an international buyer feel invited rather than incidental. From Vancouver the same courtesy runs in reverse.",
   take="Her posts are crops rather than whole paintings, so the frame lands where the paint is doing something. The whole piece is what the record shot is for, and the feed can have the two inches that were difficult. A fourth thing the overhead camera position gives for free.",
   src=["Painted the works seen in Portrait of a Lady on Fire"]),

 dict(id="uribe", name="Nicol\u00e1s Uribe", kind="artist", place="Bogot\u00e1, Colombia",
   lat=4.71, lng=-74.07, certainty="held",
   brief="Semi-abstract figurative painter. Four frames of one figure at an identical crop, running from gesture through to resolved painting.",
   why="The clearest demonstration that a process post needs no video and no commentary. An identical crop across four stages does the whole job, and it is produced by the flat copy setup that already has to exist.",
   take="Born in Wisconsin, based in Bogot\u00e1 by choice, having gone home to paint full time. The identical crop is the entire technique and it costs nothing beyond remembering to shoot at each stage.",
   src=[]),

 dict(id="popova", name="Maria Popova", kind="network", place="New York, United States",
   lat=40.68, lng=-73.94, certainty="held",
   brief="The Marginalian. The register Dear Ordinary reaches for: feeling before concept, ideas already in conversation, the reach past the fact toward the truth behind it.",
   why="What is borrowed is a relationship rather than a style. Popova writes from inside a question she has not finished with, holds several thinkers in the same room and lets them disagree, and trusts the reader to follow without being managed.",
   take="Intimacy with the question is the standard every post is measured against. Where the writing goes thin it is usually because it started explaining instead of staying inside the question.",
   src=[]),

 dict(id="webster", name="Emma Webster", kind="artist", place="Los Angeles, United States",
   lat=34.05, lng=-118.24, certainty="held",
   brief="Landscape paintings built through sketch, handmade maquette, VR and 3D modelling, theatrical lighting, then oil at large scale. Part of what prompted Dear Ordinary to start.",
   why="Writing standing beside the practice as its own object. Lonescape, published 2021, is reflection rather than documentation. Decimate, $35, is a digital sketchbook published on the occasion of the 2026 Petzel show, carrying a title and an epigraph rather than a year.",
   take="The sketchbook is the model for the annual book: the material that did not become the finished painting. Cheaper to make, better to read, and it does not compete with selling the work. Her years in interactive advertising and set design are where the maquette method came from, which is the argument for treating a day job as the second half of an unusual pair.",
   src=["Born 1989, Encinitas; Stanford 2011, Yale MFA 2018; Petzel, Perrotin, Deitch"]),

 dict(id="forgues", name="Olivier Forgues", kind="artist", place="Toronto, Ontario",
   lat=43.65, lng=-79.38, certainty="held",
   brief="Alla prima oil portraits on small panels, listed with medium, size and year, and left listed once sold. A quarterly email giving subscribers a forty-eight hour look at new work before it goes public.",
   why="The clearest argument for the mailing list being the only asset that survives a platform closing. Sold work staying visible also solves the problem of a shop that reads as depleted, which is the same solution Ini Neumann reaches by a different route.",
   take="The caption convention is worth copying exactly: title, medium, dimensions, year, and the word sold where it applies. It takes ten seconds and it is the difference between a feed and a catalogue.",
   src=["Base confirmed from his own posts"]),

 dict(id="sedlecky", name="Zbyn\u011bk Sedleck\u00fd", kind="artist", place="Prague, Czech Republic",
   lat=50.08, lng=14.44, certainty="held",
   brief="Contemporary painting photographed hanging on the studio wall, with the wall and its marks left in frame, and a scale shot as the second image in the carousel.",
   why="It answers the question every online viewer has and few ask. The comments on his own posts are the evidence: people thank him for the swipe that shows how big the work actually is, and others ask outright.",
   take="Captions are close to nothing, sometimes a single tag. The photograph carries the whole post. That only works because the second image does the explaining, which makes the scale shot the load-bearing part rather than a nicety.",
   src=["Base confirmed from his own post locations"]),

 dict(id="kinna", name="Joy Kinna", kind="artist", place="Victoria, British Columbia",
   lat=48.47, lng=-123.30, certainty="held",
   brief="Abstract painter, born 1997 in Langley and now living and working in Victoria. Prints in their own store; originals sold from a PDF catalogue by email rather than through a cart.",
   why="The selling model already in use here, and the reason no inventory system has to exist. The catalogue is a dated PDF listing available work in both currencies, updated as pieces sell, which does the job a shop would do without any of the software.",
   take="The nearest artist on this map, an hour by ferry. Represented in New York, Sydney, Des Moines and Norway while based on Vancouver Island, which is the practical answer to whether location limits reach. She also runs a separate print site rather than mixing prints into the portfolio.",
   src=["joykinna.com/bio \u00b7 born Langley 1997, based Victoria"]),

 dict(id="haring", name="Samantha Haring", kind="artist", place="Cincinnati, Ohio",
   lat=39.16, lng=-84.44, certainty="held",
   brief="Painter and educator, she/they, from Des Plaines, Illinois. Quiet paintings of packing materials, containers and the residue of studio life. Recent years listed flat; older work gathered into series named in hindsight.",
   why="The portfolio structure removes the need to decide what a series is while still in the middle of making it. The naming happens later, when the shape is actually visible. Her captions also do something the rest of this list does not: they say what a piece began as and what the observation turned into.",
   take="A studio practice run alongside teaching, at the University of Cincinnati since 2016. She was a 2015 to 2016 Artist-in-Residence at Manifest, which is already on this map as a juried route, so the two markers are one path rather than two.",
   src=["samharing.com \u00b7 MFA Northern Illinois, BFA School of the Art Institute of Chicago"]),

 dict(id="hday", name="Heather Day", kind="artist", place="Mojave Desert, California",
   lat=35.02, lng=-117.18, certainty="held",
   brief="Born 1989 in Honolulu, working from a studio in the Mojave Desert. Paintings built from vast inventories of painted forms taken apart, rearranged and sewn back together.",
   why="An inquiry link with the subject line and the first line already written for the sender. A small removal of friction that costs nothing and does the work a cart would otherwise do, and it is the detail most easily copied from anyone on this map.",
   take="She has also been a resident at the Vermont Studio Center, which is on this map already. The site itself is the wider lesson: exhibitions listed plainly by year, no shop, and a single email address for studio inquiries.",
   src=["heatherday.com \u00b7 BFA Maryland Institute College of Art, 2012"]),

 dict(id="haerlin", name="Anna H\u00e4rlin", kind="network", place="Berlin, Germany",
   lat=52.50, lng=13.43, certainty="held",
   brief="Berlin-based multidisciplinary designer and photographer, freelance since 2010, with a background in art direction and screen design including four years at the Schaub\u00fchne Berlin.",
   why="The photographer credited on the We Are Studio Studio images, which means the whole Documentation page is reasoning from her work. She is on the map because a reference should name the person who made the thing being learned from.",
   take="Her own framing is worth noting alongside the technique: the aim is documenting the core essence of people, moments and places rather than producing a product shot. That is the difference between the record shot and the presentation shot, stated from the other side.",
   src=["annahaerlin.de/about \u00b7 photography credited on wearestudiostudio.com"]),

 # ── opportunities: British Columbia ─────────────────────────────────────
 dict(id="bcac", name="BC Arts Council", kind="grant", place="Victoria, British Columbia",
   lat=48.43, lng=-123.37, certainty="held",
   brief="The provincial arts funder, with programs for individual artists including project assistance and professional development.",
   why="The closest significant funder geographically and the most natural first application. Provincial residency is met, and a professional practice with an exhibition and teaching record is the applicant profile these programs are built around.",
   take="Amounts, streams and deadlines change annually and none are recorded here. Check the current round before building any plan on it. Ranked first among funders by hours returned, because a grant buys studio time and a sale consumes it.",
   src=["Verify the current programs, eligibility and deadlines directly"]),

 dict(id="vanfound", name="Vancouver Foundation", kind="grant", place="Vancouver, British Columbia",
   lat=49.28, lng=-123.11, certainty="held",
   brief="A community foundation making grants across the region, including in arts and culture.",
   why="Regional rather than discipline-specific, which sometimes suits a practice sitting between art, disability studies and counselling psychology better than an arts-only stream does.",
   take="Read the current priorities before assuming fit. Community foundations shift focus more often than arts councils do.",
   src=["Verify current programs and eligibility directly"]),

 dict(id="cityvan", name="City of Vancouver cultural grants", kind="grant",
   place="Vancouver, British Columbia", lat=49.26, lng=-123.14, certainty="held",
   brief="Municipal cultural grant programs supporting artists and organisations in the city.",
   why="Municipal money is often the least contested and the most accessible early, and a municipal grant on the record strengthens the provincial and federal applications that follow.",
   take="Check residency and eligibility carefully. Municipal programs are usually tied to the city boundary rather than the metropolitan area.",
   src=["Verify current programs and eligibility directly"]),

 dict(id="artsumbrella", name="Arts Umbrella", kind="network", place="Vancouver, British Columbia",
   lat=49.27, lng=-123.13, certainty="held",
   brief="Vancouver arts education organisation for children and young people. Part of every studies sale goes here.",
   why="Held in the atlas because it is already part of the practice rather than a target for it. The studies series funds a social good, which is the structure read correctly from Jean Smith's model.",
   take="This is a commitment rather than an opportunity. It is on the map so the map is honest about where the money goes.",
   src=[]),

 dict(id="ecuad", name="Emily Carr University", kind="network", place="Vancouver, British Columbia",
   lat=49.27, lng=-123.09, certainty="held",
   brief="Where the foundation year happened, and where seven years of staff work across three roles followed.",
   why="The network most likely to fill a first Foundations cohort, and a much easier ask than anything else on the list. The premise of the course comes directly from this curriculum.",
   take="Keep the institution out of any marketing language implying affiliation or endorsement. Her own experience is hers to teach, and seven years on staff means she will know exactly how that reads from the inside.",
   src=[]),

 dict(id="ssnap", name="Salt Spring National Art Prize", kind="prize",
   place="Salt Spring Island, British Columbia", lat=48.82, lng=-123.50, certainty="held",
   brief="A national juried art prize and exhibition held on Salt Spring Island.",
   why="A juried national exhibition within the province. Juried shows are the first step in the route Winner took, and this one is close enough to attend.",
   take="Verify the current cycle, entry requirements and fees. Juried prize calendars move.",
   src=["Verify the current cycle directly"]),

 # ── opportunities: national ─────────────────────────────────────────────
 dict(id="cca", name="Canada Council for the Arts", kind="grant", place="Ottawa, Canada",
   lat=45.42, lng=-75.70, certainty="held",
   brief="The federal arts funder. Explore and Create is the stream most relevant to an individual visual artist developing a body of work.",
   why="The largest single source of funded studio hours available to a Canadian artist, and the one that most directly converts an application into time.",
   take="Competitive, and stronger with an exhibition and grant record behind it, which is the argument for applying provincially and municipally first. Amounts and deadlines are not recorded here and should be checked against the current round.",
   src=["Verify current programs, eligibility and deadlines directly"]),

 dict(id="hnat", name="Hnatyshyn Foundation", kind="prize", place="Ottawa, Canada",
   lat=45.41, lng=-75.68, certainty="held",
   brief="A national foundation supporting Canadian artists through awards and grants.",
   why="National recognition of the kind that compounds. An award on the record changes how every subsequent application reads.",
   take="Check which programs are currently open and whether any require nomination rather than application.",
   src=["Verify current programs and nomination requirements directly"]),

 dict(id="kingston", name="Kingston Prize", kind="prize", place="Kingston, Ontario",
   lat=44.23, lng=-76.49, certainty="held",
   brief="A national competition for Canadian portraiture, exhibited and toured.",
   why="Directly aligned with a figurative and narrative practice. Portraiture is the stated subject rather than a category the work has to be argued into.",
   take="Verify the current cycle and whether it runs annually or biennially before planning a year around it.",
   src=["Verify the current cycle directly"]),

 # ── opportunities: international ────────────────────────────────────────
 dict(id="vsc", name="Vermont Studio Center", kind="residency", place="Johnson, Vermont",
   lat=44.64, lng=-72.68, certainty="held",
   brief="A residency programme for visual artists and writers, with fellowships available.",
   why="On Caitlin Winner's route, and one of the few residencies a practice run alongside full-time work can realistically fit, because residencies are measured in weeks rather than months.",
   take="The constraint is not the application. It is finding a block of leave. Verify current session lengths and fellowship deadlines.",
   src=["Verify current sessions and fellowship deadlines directly"]),

 dict(id="manifest", name="Manifest", kind="prize", place="Cincinnati, Ohio",
   lat=39.10, lng=-84.51, certainty="held",
   brief="A gallery and drawing centre running international juried exhibitions and publications.",
   why="On Winner's route, and one of the more accessible international juried listings for an artist without representation. H\u00e9l\u00e8ne Delmaire has also been represented through it.",
   take="Verify current calls, fees and the shipping requirements for accepted work, which from British Columbia is a real cost.",
   src=["Verify current calls and requirements directly"]),

 dict(id="rioc", name="Royal Institute of Oil Painters", kind="prize", place="London, United Kingdom",
   lat=51.51, lng=-0.13, certainty="held",
   brief="An annual open exhibition at the Mall Galleries in London.",
   why="On Winner's route. An international open exhibition with a long history and a clear submission process.",
   take="Verify the current call, fees and whether digital submission is accepted at the first stage. Shipping accepted work internationally is the practical constraint.",
   src=["Verify the current call and requirements directly"]),

 dict(id="firstst", name="First Street Gallery", kind="network", place="New York, United States",
   lat=40.74, lng=-74.00, certainty="held",
   brief="A New York artist-run gallery that has held national juried exhibitions.",
   why="On Winner's route. Artist-run spaces are where an exhibition record usually begins, and they are considerably more open than commercial representation.",
   take="Verify what the gallery currently runs and whether juried opportunities are still part of it.",
   src=["Verify current programming directly"]),
]

for e in E:
    e['x'], e['y'] = project(e['lat'], e['lng'])

data_json = json.dumps(E, ensure_ascii=False, separators=(',', ':'))

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="robots" content="noai, noimageai" />
<title>Atlas &middot; Studio Day</title>
<meta name="description" content="The artists the practice is oriented toward, and the grants, prizes and residencies that return hours to it." />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Asap:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet" />
<link rel="stylesheet" href="style.css" />
<style>
  :root{--land:#ece5d8;--land-line:#ddd3c2;--coast:#c6bba7;}
  /* The stage sits inside the same 1080px column as every other page, so the
     map and its panel line up with the prose above them rather than breaking
     out wider than the rest of the site. */
  .stage{grid-template-columns:minmax(0,1.9fr) minmax(290px,1fr);gap:24px;align-items:start;}
  .stage > .panel{position:sticky;top:20px;max-height:calc(100vh - 40px);overflow-y:auto;}
  .map-hold{position:relative;background:var(--panel);border:1px solid var(--hair);
    border-radius:8px;overflow:hidden;}
  .map{display:block;width:100%;height:auto;touch-action:none;cursor:grab;}
  @media(max-width:1080px){
    .stage{grid-template-columns:1fr;}
    .stage > .panel{position:static;max-height:none;}
  }
  .map.dragging{cursor:grabbing;}
  .sphere{fill:#ffffff;stroke:var(--coast);stroke-width:1;vector-effect:non-scaling-stroke;}
  .land{fill:var(--land);stroke:none;}
  .coast{fill:none;stroke:var(--coast);stroke-width:.9;vector-effect:non-scaling-stroke;}
  .mk{cursor:pointer;outline:none;}
  .mk .hit{fill:transparent;}
  .mk .halo{fill:var(--c);opacity:0;transition:opacity .2s var(--ease);}
  .mk:hover .halo,.mk.is-sel .halo{opacity:.22;}
  .mk .core{fill:var(--c);stroke:#fff;stroke-width:1.1;vector-effect:non-scaling-stroke;}
  .mk.is-sel .core{stroke-width:2;}
  .mk.is-dim{opacity:.18;pointer-events:none;}
  .zoom-controls{position:absolute;right:12px;bottom:12px;display:flex;flex-direction:column;gap:6px;}
  .zoombtn{width:30px;height:30px;border-radius:6px;border:1px solid var(--hair);
    background:var(--paper);color:var(--ink);font-size:15px;line-height:1;cursor:pointer;
    font-family:inherit;transition:all .2s var(--ease);}
  .zoombtn:hover{border-color:var(--stone);color:var(--ink-strong);}
  .legend{display:flex;flex-wrap:wrap;gap:14px;margin:16px 0 0;}
  .lg{display:inline-flex;align-items:center;gap:7px;font-size:11.5px;color:var(--stone);}
  .lg .sw{width:9px;height:9px;border-radius:50%;}
  .lg .sw.sq{border-radius:2px;}
  .conns{display:flex;flex-wrap:wrap;gap:7px;margin:6px 0 0;}
  .cbtn{font-family:inherit;font-size:11.5px;color:var(--ink);background:var(--paper);
    border:1px solid var(--hair);border-radius:100px;padding:5px 12px;cursor:pointer;
    display:inline-flex;align-items:center;gap:7px;transition:all .2s var(--ease);}
  .cbtn:hover{border-color:var(--stone);}
  .cbtn .cd{width:7px;height:7px;border-radius:50%;background:var(--sw);}
  .certnote{font-size:12.5px;color:var(--stone);margin:10px 0 0;}
  .roster{border-top:1px solid var(--hair);padding-top:16px;}
  .roster summary{font-size:11px;letter-spacing:.16em;text-transform:uppercase;
    color:var(--stone);font-weight:600;cursor:pointer;padding:6px 0;}
  .roster h3{font-size:13px;font-weight:600;margin:22px 0 8px;letter-spacing:.02em;}
  .roster p{font-size:14.5px;margin:0 0 12px;}
  .roster .rn{font-weight:600;color:var(--ink-strong);}
</style>
</head>
<body>
  <div class="wrap">

    <nav class="topbar" aria-label="Studio Day">
      <a class="mark" href="index.html">Studio&nbsp;Day</a>
      <div class="navlinks">
        <a href="atlas.html" aria-current="page">Atlas</a>
        <a href="writing.html">Writing</a>
        <a href="documentation.html">Documentation</a>
        <a href="year.html">The Year</a>
        <a href="studies.html">Studies</a>
        <a href="teaching.html">Teaching</a>
      </div>
    </nav>

    <header class="hero">
      <p class="eyebrow"><span>Atlas</span><span class="status">One map, two layers</span></p>
      <h1>The people, and the <em>hours they make possible</em></h1>
      <p class="lede">Two things worth holding in the same view. The artists the work is in conversation with, and the funders, prizes and residencies that return hours to a practice run alongside a career. They sit on one map because the second follows the first. The route that Winner and Frank both took runs through juried shows, grants and residencies before it reaches anything else.</p>
    </header>

    <section class="stage" aria-label="The atlas">
      <div>
        <div class="controls">
          <div class="chips" id="kindfilter" role="group" aria-label="Filter the atlas"></div>
          <span class="count" id="count"></span>
        </div>
        <div class="map-hold">
          <svg class="map" id="map" viewBox="0 0 1000 536" role="group" aria-label="World map of artists and opportunities">
            <g id="viewport">
              <path class="sphere" d="__SPHERE__" />
              <path class="land" d="__LAND__" />
              <path class="coast" d="__COAST__" />
              <g id="markers"></g>
            </g>
          </svg>
          <div class="zoom-controls">
            <button class="zoombtn" id="zoom-in" aria-label="Zoom in">+</button>
            <button class="zoombtn" id="zoom-out" aria-label="Zoom out">&minus;</button>
            <button class="zoombtn" id="zoom-reset" aria-label="Reset view">&#8634;</button>
          </div>
        </div>
        <div class="legend" id="legend"></div>
        <p class="certnote">Drag to move, scroll to zoom. Every marker sits at its true coordinates, which means eight of them stack up around Vancouver at this scale. Zoom in to separate them, or open any one of them and use the list of everything else at that location. Entries marked <span class="flag">verify</span> hold a detail that has not been confirmed, usually a base location.</p>
      </div>

      <div class="panel" id="panel" aria-live="polite">
        <p class="panel-empty" id="panel-empty">Choose a marker. Artists open with why they are held here and what actually transfers to the studio. Opportunities open with what they are, whether they fit, and what has to be checked before anything is planned around them.</p>
        <div id="panel-content" hidden></div>
      </div>
    </section>

    <figure class="photo-hero">
      <img src="images/photo-two-rock.jpg" alt="Two women lie back on a warm rock, sunlit water breaking behind them." />
      <figcaption>The binding constraint is paid hours rather than audience or talent.</figcaption>
    </figure>

    <section class="essay">
      <h2>Why funders and artists share a map</h2>
      <p>The binding constraint on this practice is paid hours rather than audience or talent. Twenty-five thousand dollars of grant money and twenty-five thousand of print sales are not equivalent, because the grant returns hours and the sales consume them. Ranked by hours returned: grants, institutional commissioning, teaching priced to institutions rather than hobbyists, then retail.</p>
      <p>The artists on this map who built sustainable practices did it in a particular order. Juried shows, prizes, grants, residencies and press came first. Gallery representation followed. Teaching arrived as the income that follows credibility rather than as the thing that builds it. None of the first three built a career through an e-commerce funnel.</p>
      <p>Jean Smith took a genuinely different route to a real outcome, and it is on this map for that reason. Small work is not a lesser path.</p>

      <figure class="photo-inline">
        <img src="images/photo-back-silver.jpg" alt="Seen from behind, a woman in a silver swimsuit lifts both arms to her hair at the water line." />
        <figcaption>Disability studies, counselling psychology and the thesis are one inquiry from three directions.</figcaption>
      </figure>

      <h2>What is not available</h2>
      <p>A research-creation PhD or MFA is not on this map because it is not on the table. The education path runs from an MSc in Disability Studies to an MA in Counselling Psychology toward registration, and then a PhD. Academia will not fund studio time along the way. The practice is funded by a professional career and runs alongside years of part-time graduate study.</p>
      <p>The coherence is real even so. Disability studies, counselling psychology and a thesis on the body as the site of the sacred are one inquiry approached from three directions. Week one argues that you cannot sense another person's inner life if you were trained to ignore your own, which is a counselling claim, a disability studies claim and a painting claim at once.</p>

      <h2>How to use the opportunity layer</h2>
      <p>No amounts and no deadlines are recorded anywhere on this page. Both change every year, and a reference document holding stale figures is worse than one holding none, because stale figures get trusted.</p>
      <p>What is recorded is what each one is, whether it fits this practice, and what has to be verified before a year is planned around it. Apply municipally and provincially before federally, because a grant record makes every subsequent application read differently.</p>

      <h2>Everyone is placed</h2>
      <p>Every entry in this atlas now sits on the map, each one sourced to the person's own site or account. Nobody is held in a footnote for want of a location.</p>
      <p>Two of the placements come from the inspiration deck rather than from a bio. Olivier Forgues tags his own posts to Toronto, and Zbyn&#283;k Sedleck&yacute;'s carry Prague location tags.</p>
      <p>Three of them turn out to connect to markers already here. Samantha Haring was a 2015 to 2016 Artist-in-Residence at Manifest. Heather Day has been a resident at the Vermont Studio Center. Anna H&auml;rlin is the photographer behind the We Are Studio Studio images that the Documentation page reasons from. Those are not three artists and three opportunities. They are three paths.</p>
    </section>

    <section class="essay">
      <h2>Read it as a list</h2>
      <details class="roster">
        <summary>Open every entry as text</summary>
        <div id="rosterbody"></div>
      </details>
    </section>

    <footer>
      <span class="copy">&copy; 2026 Andrea Robin Studio</span>
      <div class="fnav">
        <a href="index.html">Studio Day</a>
        <a href="writing.html">Writing</a>
        <a href="year.html">The Year</a>
      </div>
    </footer>

  </div>

<script id="atlas-data" type="application/json">__DATA__</script>
<script>
(function(){
"use strict";

var KINDS = {
  artist:    {label:"Artists",            color:"#6f6456", shape:"circle"},
  network:   {label:"Network",            color:"#9a6b3d", shape:"circle"},
  grant:     {label:"Grants",             color:"#4f7a6a", shape:"square"},
  prize:     {label:"Prizes",             color:"#3d6382", shape:"square"},
  residency: {label:"Residencies",        color:"#5f5a72", shape:"square"}
};

var E = JSON.parse(document.getElementById("atlas-data").textContent);
var byId = {};
E.forEach(function(e){ byId[e.id] = e; });

var svg = document.getElementById("map");
var vp = document.getElementById("viewport");
var markers = document.getElementById("markers");
var panelEmpty = document.getElementById("panel-empty");
var panelContent = document.getElementById("panel-content");
var filterWrap = document.getElementById("kindfilter");
var legend = document.getElementById("legend");
var countEl = document.getElementById("count");

var view = {x:0, y:0, k:1};
var activeKind = "all";
var selectedId = null;

function apply(){
  vp.setAttribute("transform",
    "translate(" + view.x + "," + view.y + ") scale(" + view.k + ")");
}

function buildMarkers(){
  markers.innerHTML = E.map(function(e){
    var K = KINDS[e.kind];
    var shape = K.shape === "square"
      ? '<rect class="core" x="-4.2" y="-4.2" width="8.4" height="8.4" rx="1.4"/>'
      : '<circle class="core" r="4.6"/>';
    return '<g class="mk" data-id="' + e.id + '" transform="translate(' + e.x + ',' + e.y + ')" ' +
           'style="--c:' + K.color + '" tabindex="0" role="button" aria-label="' + e.name + '">' +
           '<circle class="halo" r="13"/>' + shape +
           '<circle class="hit" r="8"/></g>';
  }).join("");

  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){
    g.addEventListener("click", function(ev){ ev.stopPropagation(); select(g.getAttribute("data-id")); });
    g.addEventListener("keydown", function(ev){
      if (ev.key === "Enter" || ev.key === " "){ ev.preventDefault(); select(g.getAttribute("data-id")); }
    });
  });
}

function buildFilters(){
  var html = '<button class="chip is-active" data-kind="all" aria-pressed="true">Everything</button>';
  Object.keys(KINDS).forEach(function(k){
    html += '<button class="chip" data-kind="' + k + '" aria-pressed="false">' +
            '<span class="dot" style="background:' + KINDS[k].color + '"></span>' +
            KINDS[k].label + '</button>';
  });
  filterWrap.innerHTML = html;
  Array.prototype.forEach.call(filterWrap.querySelectorAll(".chip"), function(b){
    b.addEventListener("click", function(){
      activeKind = b.getAttribute("data-kind");
      Array.prototype.forEach.call(filterWrap.querySelectorAll(".chip"), function(o){
        var on = o === b;
        o.classList.toggle("is-active", on);
        o.setAttribute("aria-pressed", on ? "true" : "false");
      });
      applyFilter();
    });
  });

  legend.innerHTML = Object.keys(KINDS).map(function(k){
    return '<span class="lg"><span class="sw' + (KINDS[k].shape === "square" ? " sq" : "") +
           '" style="background:' + KINDS[k].color + '"></span>' + KINDS[k].label + '</span>';
  }).join("");
}

function applyFilter(){
  var n = 0;
  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){
    var e = byId[g.getAttribute("data-id")];
    var on = activeKind === "all" || e.kind === activeKind;
    g.classList.toggle("is-dim", !on);
    if (on) n++;
  });
  countEl.textContent = n + (n === 1 ? " entry" : " entries");
}

function select(id){
  selectedId = id;
  var e = byId[id];
  if (!e) return;
  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){
    g.classList.toggle("is-sel", g.getAttribute("data-id") === id);
  });

  var flag = e.certainty === "check" ? '<span class="flag">verify</span>' : "";

  // several entries share a city, so anything sitting under this marker is
  // listed as a chip. Nothing is displaced; the map stays geographically true.
  var here = E.filter(function(o){
    if (o.id === e.id) return false;
    var dx = o.x - e.x, dy = o.y - e.y;
    return Math.sqrt(dx * dx + dy * dy) < 7;
  });
  var alsoHere = here.length
    ? '<h3>Also at this location</h3><div class="conns">' + here.map(function(o){
        return '<button class="cbtn" data-go="' + o.id + '" style="--sw:' +
               KINDS[o.kind].color + '"><span class="cd"></span>' + o.name + '</button>';
      }).join("") + '</div>'
    : "";
  var src = e.src && e.src.length
    ? '<h3>Notes</h3><ul class="srclist">' +
      e.src.map(function(s){ return "<li>" + s + "</li>"; }).join("") + "</ul>"
    : "";
  var isArtist = e.kind === "artist" || e.kind === "network";

  panelEmpty.hidden = true;
  panelContent.hidden = false;
  panelContent.innerHTML =
    '<p class="p-eyebrow">' + KINDS[e.kind].label + " \\u00b7 " + e.place + "</p>" +
    '<h2 class="p-title">' + e.name + flag + "</h2>" +
    '<div class="tabs" role="tablist">' +
      '<button class="tab is-active" data-l="a" role="tab">In brief</button>' +
      '<button class="tab" data-l="b" role="tab">' + (isArtist ? "Why it is here" : "Fit") + "</button>" +
      '<button class="tab" data-l="c" role="tab">' + (isArtist ? "What transfers" : "Before applying") + "</button>" +
    "</div>" +
    '<div class="layer" data-l="a"><p>' + e.brief + "</p>" + src + "</div>" +
    '<div class="layer" data-l="b" hidden><p>' + e.why + "</p></div>" +
    '<div class="layer" data-l="c" hidden><p>' + e.take + "</p></div>" + alsoHere;

  Array.prototype.forEach.call(panelContent.querySelectorAll("[data-go]"), function(b){
    b.addEventListener("click", function(){ select(b.getAttribute("data-go")); });
  });

  var tabs = panelContent.querySelectorAll(".tab");
  Array.prototype.forEach.call(tabs, function(t){
    t.addEventListener("click", function(){
      Array.prototype.forEach.call(tabs, function(o){ o.classList.toggle("is-active", o === t); });
      Array.prototype.forEach.call(panelContent.querySelectorAll(".layer"), function(l){
        l.hidden = l.getAttribute("data-l") !== t.getAttribute("data-l");
      });
    });
  });
}

/* pan and zoom */
var dragging = false, last = null, moved = false;
function rel(ev){
  var r = svg.getBoundingClientRect();
  var t = ev.touches ? ev.touches[0] : ev;
  return {x:(t.clientX - r.left) / r.width * 1000, y:(t.clientY - r.top) / r.width * 1000};
}
svg.addEventListener("mousedown", function(ev){
  dragging = true; moved = false; last = rel(ev); svg.classList.add("dragging");
});
window.addEventListener("mouseup", function(){ dragging = false; svg.classList.remove("dragging"); });
svg.addEventListener("mousemove", function(ev){
  if (!dragging || !last) return;
  var p = rel(ev);
  view.x += p.x - last.x; view.y += p.y - last.y;
  last = p; moved = true; apply();
});
svg.addEventListener("wheel", function(ev){
  ev.preventDefault();
  var f = ev.deltaY < 0 ? 1.15 : 0.87;
  var p = rel(ev);
  var nk = Math.max(1, Math.min(9, view.k * f));
  view.x = p.x - (p.x - view.x) * (nk / view.k);
  view.y = p.y - (p.y - view.y) * (nk / view.k);
  view.k = nk; apply();
}, {passive:false});
svg.addEventListener("touchstart", function(ev){ dragging = true; last = rel(ev); }, {passive:true});
svg.addEventListener("touchmove", function(ev){
  if (!dragging || !last) return;
  var p = rel(ev);
  view.x += p.x - last.x; view.y += p.y - last.y;
  last = p; apply();
}, {passive:true});
svg.addEventListener("touchend", function(){ dragging = false; }, {passive:true});

function zoomBy(f){
  var nk = Math.max(1, Math.min(9, view.k * f));
  view.x = 500 - (500 - view.x) * (nk / view.k);
  view.y = 268 - (268 - view.y) * (nk / view.k);
  view.k = nk; apply();
}
document.getElementById("zoom-in").addEventListener("click", function(){ zoomBy(1.35); });
document.getElementById("zoom-out").addEventListener("click", function(){ zoomBy(0.74); });
document.getElementById("zoom-reset").addEventListener("click", function(){
  view = {x:0, y:0, k:1}; apply();
  selectedId = null;
  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){ g.classList.remove("is-sel"); });
  panelContent.hidden = true; panelEmpty.hidden = false;
});

function buildRoster(){
  var body = document.getElementById("rosterbody");
  body.innerHTML = Object.keys(KINDS).map(function(k){
    var list = E.filter(function(e){ return e.kind === k; });
    if (!list.length) return "";
    return '<h3 style="color:' + KINDS[k].color + '">' + KINDS[k].label + "</h3>" +
      list.map(function(e){
        return "<p><span class=\\"rn\\">" + e.name + ".</span> " + e.place + ". " +
               e.brief + " " + e.why + " " + e.take + "</p>";
      }).join("");
  }).join("");
}

buildMarkers();
buildFilters();
applyFilter();
buildRoster();
apply();
})();
</script>
</body>
</html>
'''

out = (HTML
       .replace('__SPHERE__', sphere)
       .replace('__LAND__', land)
       .replace('__COAST__', coast)
       .replace('__DATA__', data_json))
open('atlas.html', 'w').write(out)
print("atlas.html written:", len(out), "bytes,", len(E), "entries")
