"""Percy Jackson's World - character lookup. Run: streamlit run app.py"""
import difflib
import streamlit as st

st.set_page_config(page_title="Percy Jackson's World", page_icon="🔱", layout="wide")

# name, type, category, status, parent, powers, affiliation, bio
D = [
("Percy Jackson","Demigod","Demigods","Alive","Poseidon (god) & Sally Jackson (mortal)","Hydrokinesis, water breathing, communicates with horses, earthquake control, Curse of Achilles","Cabin 3 (Poseidon), Camp Half-Blood","A twelve-year-old with ADHD and dyslexia who learns he is a son of Poseidon. He is accused of stealing Zeus's master bolt, then goes on to fight Kronos, save Olympus twice and survive Tartarus."),
("Annabeth Chase","Demigod","Demigods","Alive","Athena (goddess) & Frederick Chase (mortal)","Strategic genius, architecture, combat skill, ancient Greek fluency, Yankees cap of invisibility","Cabin 6 (Athena), Camp Half-Blood","Percy's closest friend and later partner. She ran away at seven, designed the rebuilt Olympus and retrieved the Athena Parthenos from Arachne's lair."),
("Grover Underwood","Satyr","Other","Alive","Satyr; Lord of the Wild","Nature magic, reed pipes, empathy link, tracking, plant growth","Council of Cloven Elders, Camp Half-Blood","Percy's protector and best friend. Grover dreams of finding Pan and later becomes a Lord of the Wild and Percy's empathy-linked friend."),
("Luke Castellan","Demigod","Demigods","Deceased","Hermes (god) & May Castellan (mortal)","Swordsmanship, thievery, Curse of Achilles (via Styx), Kronos's vessel","Cabin 11 (Hermes), Kronos's army","Counselor-turned-traitor who blamed the gods for neglect. He hosted Kronos, then sacrificed himself to stop the Titan during the Battle of Manhattan."),
("Thalia Grace","Demigod","Demigods","Alive","Zeus (god) & Beryl Grace (mortal)","Electrokinesis, flight, Aegis shield, archery, lightning","Cabin 1 (Zeus), Hunters of Artemis","Pine-tree guardian of Camp Half-Blood's border who was revived. She later joined Artemis's Hunters and became their lieutenant."),
("Nico di Angelo","Demigod","Demigods","Alive","Hades (god) & Maria di Angelo (mortal)","Shadow travel, necromancy, summoning the dead, geokinesis, sensing death","Cabin 13 (Hades), Camp Half-Blood","Born in the 1930s and kept in the Lotus Hotel for decades. Nico is a Ghost King, Bianca's brother, and one of the most powerful demigods alive."),
("Clarisse La Rue","Demigod","Demigods","Alive","Ares (god) & Mrs. La Rue (mortal)","Combat mastery, enhanced strength, electric spear Maimer","Cabin 5 (Ares), Camp Half-Blood","Tough and loyal daughter of Ares. She bullied Percy at first but became a trusted ally and a hero of the Battle of the Labyrinth."),
("Rachel Elizabeth Dare","Mortal","Other","Alive","Mortal (Mr. & Mrs. Dare)","The Oracle of Delphi: prophecy, sees through the Mist","Oracle of Delphi, Camp Half-Blood","A mortal artist who sees through the Mist. She guided the demigods through the Labyrinth and later became the Oracle."),
("Chiron","Centaur","Other","Alive","Kronos (Titan) & Philyra (nymph)","Master archer, immortal trainer, wise leader, healing","Camp Half-Blood (Activities Director)","Son of Kronos and a trainer of Greek heroes for 3,000 years. He runs Camp Half-Blood as its director."),
("Mr. D (Dionysus)","God","Gods","Active","Zeus & Semele","Wine, madness, vines, theater, revelry","Olympian Council, Camp Half-Blood","The god of wine, forced to supervise camp as punishment. He pretends not to remember the campers' names."),
("Zeus","God","Gods","Active","Kronos & Rhea (Titans)","Sky and lightning, thunder, weather control, kingship","Olympian Council (Big Three)","King of the gods and ruler of the sky. His master bolt's theft is the spark that starts the war."),
("Poseidon","God","Gods","Active","Kronos & Rhea (Titans)","Seas, earthquakes, horses, storms, shape-shifting","Olympian Council (Big Three), Cabin 3","Lord of the sea and Percy's father. He broke the Big Three oath by having a mortal child."),
("Hades","God","Gods","Active","Kronos & Rhea (Titans)","Underworld, riches, shadows, command of the dead","Olympian Council (honorary), Underworld","The brooding lord of the dead, misunderstood and mostly seen as a villain. He is father to Nico and Bianca."),
("Athena","God","Gods","Active","Zeus & Metis (Titaness)","Wisdom, strategy, war, crafts, owls","Olympian Council, Cabin 6","Born from Zeus's head. Goddess of wisdom and Annabeth's mother, in a long-standing rivalry with Poseidon."),
("Apollo","God","Gods","Active","Zeus & Leto (Titaness)","Sun, music, prophecy, archery, healing, poetry","Olympian Council, Cabin 7","God of the sun and Artemis's twin. Later in the series he is stripped of his powers and made mortal."),
("Artemis","God","Gods","Active","Zeus & Leto (Titaness)","Hunt, moon, archery, wilderness, eternal youth","Olympian Council, Hunters of Artemis","Eternal maiden goddess of the hunt who leads her band of immortal Hunters."),
("Ares","God","Gods","Active","Zeus & Hera","War, bloodshed, combat, violence, courage","Olympian Council, Cabin 5","Brutal god of war. He tricked Percy into retrieving Zeus's stolen bolt and cursed him afterwards."),
("Hermes","God","Gods","Active","Zeus & Maia (Pleiad nymph)","Travel, thieves, messages, speed, trickery","Olympian Council, Cabin 11","Messenger god, patron of travelers and thieves, and Luke's neglectful father."),
("Hephaestus","God","Gods","Active","Zeus & Hera","Forges, fire, metalwork, craftsmanship","Olympian Council, Cabin 9","The smith god of the Olympians, who builds automatons and the best weapons."),
("Aphrodite","God","Gods","Active","Born of sea foam and Uranus's blood","Love, beauty, charmspeak, desire","Olympian Council, Cabin 10","Goddess of love who delights in meddling with the campers' hearts."),
("Demeter","God","Gods","Active","Kronos & Rhea (Titans)","Agriculture, harvest, plant growth, seasons","Olympian Council, Cabin 4","Goddess of grain and cereal who rules the harvest, and mother of Persephone."),
("Kronos","Titan","Titans","Defeated (in Tartarus)","Ouranos & Gaea","Time manipulation, scythe, size change, soul corruption, dread","Titan Army, Mount Othrys","Lord of Time and king of the Titans. He rises from Tartarus using Luke as a vessel to destroy Olympus."),
("Atlas","Titan","Titans","Imprisoned","Iapetus & Clymene","Superhuman strength, defense, bearing the sky","Titan Army","The Titan general condemned to hold up the sky. Percy helps bear the burden temporarily when he is freed."),
("Prometheus","Titan","Titans","Free","Iapetus & Clymene","Foresight, fire-making, human creation","Titan (neutral)","The fire-stealing Titan who gave humanity fire and was tormented for it, and who aids the heroes."),
("Gaea","Primordial","Titans","Dormant, awakening","Primordial (Chaos, Chaos is origin)","Earth control, giants, rebirth, planting seeds","Giants' army, Earth","Mother Earth and the main antagonist of The Heroes of Olympus."),
("Medusa","Monster","Other","Slain","Phorcys & Ceto (sea deities)","Petrifying gaze, snake hair, immortal slither","Gorgons, Aunty Em's Garden Gnome Emporium","The Gorgon who runs a garden-statue shop. Percy beheads her using his reflection."),
("Minotaur","Monster","Other","Slain","Pasiphae & the Cretan Bull","Brute strength, charging, bull horns","Labyrinth, Monsters","The half-man, half-bull that hunted Percy's mother. He is Percy's first big monster kill."),
("Sally Jackson","Mortal","Other","Alive","Mortal","Clear sight through the Mist, courage, cooking","Mortal world","Percy's courageous mother who is kidnapped by Hades but returned after the quest."),
("Tyson","Cyclops","Other","Alive","Poseidon & a nymph","Super strength, forging, fire resistance, smithing","Cyclopes, Camp Half-Blood","Percy's Cyclops half-brother. Tyson becomes general of the Cyclopes and a forge-working hero."),
("Bianca di Angelo","Demigod","Demigods","Deceased","Hades (god) & Maria di Angelo (mortal)","Shadow resistance, combat training","Hunters of Artemis","Nico's elder sister who joined Artemis's Hunters and died on a quest."),
]
KEYS = ["name","type","cat","status","parent","powers","affil","bio"]
CH = {r[0].lower(): dict(zip(KEYS, r)) for r in D}
NAMES = [r[0] for r in D]
ICON = {"Gods":"⚡","Demigods":"🗡️","Titans":"⌛","Other":"🐚"}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Cormorant+Garamond:wght@400;500;600&display=swap');
:root{--ink:#0a0f1a;--abyss:#121b2e;--bronze:#c9954a;--sea:#3fb7b0;--bone:#e9e2d0}
.stApp{background:radial-gradient(1200px 500px at 50% -10%,#1a2a4a 0%,var(--ink) 60%);color:var(--bone);font-family:'Cormorant Garamond',serif;font-size:1.15rem}
header[data-testid="stHeader"]{background:transparent}
h1.t{font-family:'Cinzel',serif;font-size:3rem;text-align:center;color:var(--bronze);letter-spacing:.06em;margin:.2em 0 0}
p.s{text-align:center;color:#9fb0c8;margin-bottom:1.2rem}
.card{background:linear-gradient(160deg,#16223a,#0e1626);border:1px solid var(--bronze);border-radius:6px;padding:1.8rem 2rem;box-shadow:0 0 40px rgba(63,183,176,.12)}
.card h2{font-family:'Cinzel',serif;color:var(--bronze);margin:0 0 .3rem;font-size:2.2rem}
.badge{display:inline-block;border:1px solid var(--sea);color:var(--sea);padding:.1rem .8rem;border-radius:999px;margin-right:.5rem;font-size:1rem}
.row{display:grid;grid-template-columns:11rem 1fr;gap:.4rem 1rem;margin-top:1rem}
.row b{color:var(--bronze);font-family:'Cinzel',serif;font-weight:500;font-size:.95rem}
.mini{background:#101a2e;border:1px solid #2a3a5a;border-radius:6px;padding:.8rem 1rem;margin-bottom:.6rem}
.mini b{font-family:'Cinzel',serif;color:var(--bronze)}
.stTextInput input{background:#101a2e;color:var(--bone);border:1px solid var(--bronze);font-size:1.2rem}
.stButton button{background:#101a2e;color:var(--bone);border:1px solid var(--sea)}
.stButton button:hover{border-color:var(--bronze);color:var(--bronze)}
@media(max-width:700px){.row{grid-template-columns:1fr}h1.t{font-size:2rem}}
</style>
<h1 class="t">🔱 Percy Jackson's World</h1>
<p class="s">Search the gods, heroes and monsters of Camp Half-Blood.</p>
""", unsafe_allow_html=True)

st.session_state.setdefault("q", "")

def pick(n):
    st.session_state.q = n

def card(c):
    st.markdown(f"""<div class="card"><h2>{ICON[c['cat']]} {c['name']}</h2>
<span class="badge">{c['type']}</span><span class="badge">{c['status']}</span>
<div class="row"><b>Parentage</b><span>{c['parent']}</span>
<b>Powers &amp; abilities</b><span>{c['powers']}</span>
<b>Cabin / affiliation</b><span>{c['affil']}</span>
<b>Biography</b><span>{c['bio']}</span></div></div>""", unsafe_allow_html=True)

def suggest(q, pool):
    q = q.strip().lower()
    if not q:
        return []
    starts = [n for n in pool if n.lower().startswith(q)]
    subs = [n for n in pool if q in n.lower() and n not in starts]
    fuzzy = [n for n in difflib.get_close_matches(q, [p.lower() for p in pool], n=5, cutoff=0.5)]
    fz = [CH[f]["name"] for f in fuzzy if CH[f]["name"] in pool and CH[f]["name"] not in starts + subs]
    return (starts + subs + fz)[:6]

cat = st.radio("Filter", ["All", "Gods", "Demigods", "Titans", "Other"], horizontal=True, label_visibility="collapsed")
pool = [n for n in NAMES if cat == "All" or CH[n.lower()]["cat"] == cat]

q = st.text_input("Search", key="q", placeholder="Type a name, e.g. percy, athena, kronos...", label_visibility="collapsed")
hit = CH.get(q.strip().lower())

if hit and (cat == "All" or hit["cat"] == cat):
    card(hit)
elif q.strip():
    sug = suggest(q, pool)
    if sug:
        st.markdown("**Did you mean:**")
        cols = st.columns(len(sug))
        for col, n in zip(cols, sug):
            col.button(n, on_click=pick, args=(n,), key="s_" + n)
    else:
        st.warning(f"No character matching \"{q}\" in {cat}. Try another spelling or switch the filter.")
else:
    st.markdown(f"**{len(pool)} characters.** Pick one or start typing:")
    cols = st.columns(3)
    for i, n in enumerate(pool):
        c = CH[n.lower()]
        with cols[i % 3]:
            st.markdown(f'<div class="mini"><b>{ICON[c["cat"]]} {n}</b><br>{c["type"]}</div>', unsafe_allow_html=True)
            st.button("View profile", on_click=pick, args=(n,), key="v_" + n)
