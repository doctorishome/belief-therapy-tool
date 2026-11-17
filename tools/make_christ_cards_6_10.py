"""Christ-topic cards 6–10, same structure as the God cards.

Every chapter-and-verse citation is written out from the Berean Standard Bible
beside the reference. Run: python3 tools/make_christ_cards_6_10.py
"""
import make_god_cards_2_5 as g

for book in ("1 Timothy", "2 Timothy", "Galatians", "Ephesians", "Luke"):
    if book not in g.BOOKS:
        g.BOOKS.append(book)

cite = g.cite

C6 = dict(
    num=6, file="I-Need-Someone-Else-To-Bring-My-Prayers-To-God",
    belief="I need a priest, a saint, or Mary to bring my prayers to God.",
    key="1 Timothy 2:5",
    also=["Hebrews 4:14–16", "Hebrews 7:25", "Ephesians 2:18", "John 14:13–14", "Luke 1:48"],
    pearls=["prayer-how-to", "christ-identity-of", "salvation", "christ-mission-of", "grace"],
    reading="prayer-how-to", gc=[22, 8, 7],
    songs=[
        ("messiah", "Jesus the Messiah is the one who stands between us and the Father."),
        ("forever", "The risen Christ lives, and a living Savior can carry your prayer."),
        ("worthy", "He is worthy of the direct worship and prayer of His people."),
        ("friend", "What a friend we have in Jesus: we are invited to carry every care to Him."),
    ],
    origins="Many Christians, including Catholic and Orthodox believers, have been taught with real reverence to ask Mary, a saint, or a priest to carry their prayers. That teaching often comes from love for the church and from a humble fear of approaching God on our own. Pastors and friends may pray with us, and that is a gift. Mary is honored in Scripture. The belief that God will not hear us unless a human or a saint stands in between is a different claim.",
    self=[
        "God will not listen if I come by myself.",
        "I am not holy enough to speak to the Father.",
        "My prayer counts only if a priest, a saint, or Mary delivers it.",
        "Jesus is too far above me to bother with my request.",
        "I should be afraid to use His name directly.",
        "Asking someone else is safer than coming to God.",
    ],
    errors=[
        ("All-or-nothing thinking", "If I am not holy enough in myself, I cannot come to God at all."),
        ("Discounting the positive", "Ignoring the mediator Scripture already gives: the man Christ Jesus."),
        ("Mind reading", "Deciding God will not hear a prayer that comes in Jesus’ name."),
        ("Emotional reasoning", "Feeling unworthy and treating that feeling as a closed door."),
    ],
    prompt="When I thought I could not pray unless someone else carried it",
    moment="I held back from God because I thought I needed another mediator",
    example="I have one mediator, the man Christ Jesus, and I may come to the Father in His name.",
    tracker="A prayer I brought to the Father in Jesus’ name",
)
C6["teaches"] = (
    "Scripture honors Mary and welcomes the prayers of the church. It also names one mediator. "
    + cite("1 Timothy 2:5") + " "
    + cite("Hebrews 4:14–16") + " "
    + cite("Hebrews 7:25") + " "
    + cite("Ephesians 2:18") + " "
    + cite("John 14:13–14") + " "
    "Luke records Mary’s own words: " + cite("Luke 1:48") + " "
    "Calling her blessed is not the same as needing her to carry our prayers. "
    "We may ask others to pray with us. We do not have to wait for a priest, a saint, or Mary before we speak to the Father. Jesus the Son of God is the great high priest, and He lives to intercede."
)
C6["questions"] = [
    "Am I grateful for people who pray with me, or am I treating them as a required bridge?",
    "Who does %s name as the one mediator between God and men?" % cite("1 Timothy 2:5"),
    "What does %s invite me to do at the throne of grace?" % cite("Hebrews 4:14–16"),
    "Does feeling unworthy cancel what %s says about drawing near through Jesus?" % cite("Hebrews 7:25"),
    "What did Jesus say about asking in His name, in %s?" % cite("John 14:13–14"),
    "Can I thank God for Mary, and still come to the Father through Christ alone?",
]
C6["truths"] = [
    "There is one mediator between God and men, the man Christ Jesus.",
    "I may approach the throne of grace with confidence.",
    "Jesus always lives to intercede for those who draw near through Him.",
    "Through Him I have access to the Father.",
    "I can ask in His name.",
    "Other people may pray with me. They do not replace Him.",
]
C6["replacement"] = (
    "I do not need a priest, a saint, or Mary to make God hear me. There is one mediator, the man Christ Jesus. "
    "I may approach the throne of grace with confidence, and I may ask the Father in His name."
)
C6["actions"] = [
    "<strong>Pray one request in Jesus’ name today,</strong> with no one else carrying it for you, and read %s first." % cite("1 Timothy 2:5"),
    "<strong>Read %s aloud</strong> and write the words “with confidence” next to a need you have been afraid to bring." % cite("Hebrews 4:14–16"),
    "<strong>Thank one person who prays with you,</strong> and tell them Christ is still the mediator.",
    "<strong>If you have avoided speaking to the Father directly,</strong> say one honest sentence to Him today.",
]
C6["prayer"] = (
    "Father, I have been afraid to come to You on my own. Thank You for what %s says. "
    "I come in the name of Jesus, my mediator, and I ask You to hear me. Amen."
) % cite("1 Timothy 2:5")

C7 = dict(
    num=7, file="Now-Its-Up-To-Me-To-Stay-Acceptable",
    belief="Jesus saved me, but now it’s up to me to stay acceptable.",
    key="Ephesians 2:8–9",
    also=["Romans 5:1", "Romans 8:1", "Philippians 1:6", "Galatians 3:3"],
    pearls=["grace", "salvation", "forgiveness", "christ-sacrifice-of", "mercy"],
    reading="grace", gc=[7, 26, 29],
    songs=[
        ("grace", "The grace that saved you is not a starter kit you have to finish alone."),
        ("wins", "Grace wins over the project of keeping yourself acceptable."),
        ("chains", "You do not keep your freedom by rebuilding the chains."),
        ("amazing", "Amazing grace does not hand the rest of the work back to you."),
    ],
    origins="After a real turning to Christ, the first relief can fade. A strict home, a sermon that only counts failures, or a relapse can make grace feel like the front door only. Then staying loved looks like a job: pray enough, slip less, and maybe God will still want you. Obedience matters. It is not the payment that keeps you acceptable.",
    self=[
        "Jesus started this. I have to keep it going.",
        "One bad week and I am unacceptable again.",
        "Grace got me in. Performance keeps me in.",
        "God is patient at conversion and strict after that.",
        "If I cannot hold the line, I will lose His welcome.",
        "I should hide until I have cleaned this up.",
    ],
    errors=[
        ("All-or-nothing thinking", "If I am not impressive this week, I am no longer accepted."),
        ("Discounting the positive", "Forgetting that justification and no condemnation are gifts, not wages."),
        ("Emotional reasoning", "Feeling unacceptable and calling that feeling God’s verdict."),
        ("Fortune telling", "Deciding a failure today means God will drop the work He began."),
    ],
    prompt="When staying saved felt like my job",
    moment="a failure made me think I had to earn my welcome back",
    example="I was saved by grace through faith. Jesus will carry to completion the work He began.",
    tracker="A failure I stopped treating as the loss of God’s acceptance",
)
C7["teaches"] = (
    "Salvation is not a down payment we finish with our own goodness. "
    + cite("Ephesians 2:8–9") + " "
    + cite("Romans 5:1") + " "
    + cite("Romans 8:1") + " "
    + cite("Philippians 1:6") + " "
    "Paul’s question is sharp because the danger is real: " + cite("Galatians 3:3") + " "
    "We still turn from sin, because we are loved, not because love expires when we stumble. "
    "The God who justified us through faith is the God who carries His work on to completion."
)
C7["questions"] = [
    "Am I trying to finish, by my effort, what grace began?",
    "What does %s say salvation is, and what it is not?" % cite("Ephesians 2:8–9"),
    "Since I have been justified through faith, what do I have, according to %s?" % cite("Romans 5:1"),
    "Does %s leave room for condemnation for those in Christ Jesus?" % cite("Romans 8:1"),
    "Who carries the good work to completion, according to %s?" % cite("Philippians 1:6"),
    "What would change if obedience were gratitude instead of rent?",
]
C7["truths"] = [
    "I am saved by grace through faith, not by works.",
    "I have peace with God through Jesus Christ.",
    "There is now no condemnation for me in Christ.",
    "He who began a good work in me will carry it on.",
    "I do not stay acceptable by finishing in my own strength.",
    "I can confess a sin without starting salvation over.",
]
C7["replacement"] = (
    "Jesus did not save me and then leave acceptance up to me. I am saved by grace through faith. "
    "I have peace with God, there is no condemnation in Christ, and He will carry to completion the work He began."
)
C7["actions"] = [
    "<strong>Write the two sentences separately:</strong> “Jesus saved me” and “I must keep myself acceptable.” Cross out the second if it disagrees with %s." % cite("Ephesians 2:8–9"),
    "<strong>Read %s each morning</strong> before you review yesterday’s failures." % cite("Romans 8:1"),
    "<strong>Confess one real sin</strong> as a child who is already welcomed, not as a stranger applying again.",
    "<strong>Do one act of obedience today</strong> and write “gratitude” beside it, not “rent.”",
]
C7["prayer"] = (
    "Lord, I have been trying to keep myself acceptable to You. Thank You for what %s says. "
    "Teach me to obey because I am already Yours, not to earn the welcome Jesus gave. Amen."
) % cite("Ephesians 2:8–9")

C8 = dict(
    num=8, file="Jesus-Is-One-Way-Among-Many",
    belief="Jesus is one good way to God among many.",
    key="John 14:6",
    also=["Acts 4:12", "1 Timothy 2:5", "John 3:16"],
    pearls=["christ-identity-of", "salvation", "christ-divinity-of", "christ-mission-of", "love-by-god"],
    reading="christ-identity-of", gc=[8, 7, 31],
    songs=[
        ("jesus", "The song is about Jesus Himself, not about one option on a list."),
        ("onegod", "There is one true God, and He has made Himself known in His Son."),
        ("inchrist", "Hope is in Christ alone, not in a menu of paths."),
        ("great", "How great Thou art praises the God who gave His Son, not a vague higher power."),
    ],
    origins="Kindness, and sometimes a fear of sounding proud, can turn Jesus into one good teacher among others. Friends of other faiths, a school that treats every religion as the same, or a church that avoids His hard sayings can make “all sincere paths lead to God” feel polite. Respect for people is right. Changing what Jesus said about Himself is not.",
    self=[
        "All sincere roads lead to the same God.",
        "Jesus is best for me, not true for everyone.",
        "It is arrogant to say He is the only way.",
        "A good life matters more than who He is.",
        "I can love Jesus and leave the door open to every other path.",
        "His words about being the way were for that culture only.",
    ],
    errors=[
        ("All-or-nothing thinking", "If exclusive claims feel unkind, they must be false."),
        ("Discounting the positive", "Setting aside the words Jesus and the apostles actually spoke."),
        ("Mind reading", "Deciding that people of other faiths cannot be loved unless their path is equal."),
        ("Emotional reasoning", "Feeling uncomfortable with His claim and treating the discomfort as a correction of Jesus."),
    ],
    prompt="When I made Jesus one option among many",
    moment="I softened His claim so that every path could be equal",
    example="Jesus is the way, the truth, and the life. I can love people and still say no one comes to the Father except through Him.",
    tracker="A conversation where I told the truth about Jesus with respect",
)
C8["teaches"] = (
    "We can be respectful toward people of every faith and still repeat what Jesus said. "
    + cite("John 14:6") + " "
    + cite("Acts 4:12") + " "
    + cite("1 Timothy 2:5") + " "
    + cite("John 3:16") + " "
    "Love for the world is why the Father gave His Son. It is not a reason to call every other name equal to His. "
    "Sincerity is not the same as the way God gave."
)
C8["questions"] = [
    "Am I protecting people’s dignity, or editing Jesus so I will not feel awkward?",
    "What does Jesus call Himself in %s, and who comes to the Father except through Him?" % cite("John 14:6"),
    "Is there another name given for salvation, according to %s?" % cite("Acts 4:12"),
    "How many mediators does %s allow?" % cite("1 Timothy 2:5"),
    "Does %s sound like one option among many, or like a gift for the world?" % cite("John 3:16"),
    "How can I love a friend of another faith without pretending Jesus agreed with every road?",
]
C8["truths"] = [
    "Jesus is the way, the truth, and the life.",
    "No one comes to the Father except through Him.",
    "Salvation is found in no other name.",
    "There is one mediator, the man Christ Jesus.",
    "God loved the world by giving His Son, not by approving every path.",
    "I can be respectful and still tell the truth.",
]
C8["replacement"] = (
    "Jesus is not one good way among many. He said He is the way, the truth, and the life, and that no one comes to the Father except through Him. "
    "There is no other name given for salvation. I can honor people and still say that."
)
C8["actions"] = [
    "<strong>Read %s slowly</strong> and write Jesus’ words in your own notebook without softening them." % cite("John 14:6"),
    "<strong>Pray for one friend of another faith by name,</strong> asking God to make Christ known, not to make every path equal.",
    "<strong>Practice one respectful sentence</strong> you could say: “I care about you, and I believe Jesus is the way God gave.”",
    "<strong>Read %s</strong> and note that the claim is about His name, not about winning an argument." % cite("Acts 4:12"),
]
C8["prayer"] = (
    "Lord Jesus, I have treated You as one option among many. Thank You for what %s says. "
    "Give me love for people and courage to say that You are the way. Amen."
) % cite("John 14:6")

C9 = dict(
    num=9, file="Jesus-Doesnt-Understand-What-Im-Going-Through",
    belief="Jesus doesn’t understand what I’m going through.",
    key="Hebrews 4:15",
    also=["Hebrews 2:17–18", "Isaiah 53:3", "John 11:35", "Hebrews 4:14–16"],
    pearls=["christ-humanity-of", "suffering", "temptation", "christ-personality-of", "mercy"],
    reading="christ-humanity-of", gc=[8, 27, 28],
    songs=[
        ("knows", "He knows the pain you assume is too human for Him."),
        ("held", "You can stop explaining yourself to a Savior who already understands."),
        ("worn", "Weariness is not foreign to the Man of sorrows."),
        ("tender", "Softly and tenderly, Jesus is calling the one who feels alone in this."),
    ],
    origins="A lonely illness, a grief no one else shares, a temptation you are ashamed to name, or a picture of Jesus as only distant and divine can make Him seem unable to understand. If He never married, never lost this job, or never lived in your city, the mind decides He cannot know this pain. Scripture says something stronger than “He has a theory about suffering.” He took on flesh, was tempted, sorrowed, and wept.",
    self=[
        "Jesus cannot know what this feels like.",
        "He was too holy to understand my temptation.",
        "My pain is a modern problem He never faced.",
        "If He understood, He would have stopped it.",
        "I need someone who has lived my exact story.",
        "I should not bother Him with something this human.",
    ],
    errors=[
        ("All-or-nothing thinking", "If Jesus did not live my exact details, He cannot understand me at all."),
        ("Mind reading", "Deciding what the Son of God is unable to grasp."),
        ("Discounting the positive", "Ignoring that He was tempted, suffered, sorrowed, and wept."),
        ("Emotional reasoning", "Feeling alone and concluding that Christ is a stranger to this pain."),
    ],
    prompt="When I decided Jesus could not understand",
    moment="my pain or temptation felt too human for Him",
    example="Jesus was tempted as I am, and He is able to help me. I can come to Him with this.",
    tracker="A pain I brought to Jesus instead of deciding He would not understand",
)
C9["teaches"] = (
    "The Son of God did not skip the human part. "
    + cite("Hebrews 4:15") + " "
    + cite("Hebrews 2:17–18") + " "
    + cite("Isaiah 53:3") + " "
    + cite("John 11:35") + " "
    + cite("Hebrews 4:14–16") + " "
    "He does not have to have held your exact job to know weakness, temptation, grief, and sorrow. "
    "Because He suffered when He was tempted, He is able to help. You may approach the throne of grace with confidence."
)
C9["questions"] = [
    "What part of this pain have I decided is off-limits to Jesus?",
    "What does %s say about His sympathy with our weaknesses?" % cite("Hebrews 4:15"),
    "Why is He able to help those who are tempted, according to %s?" % cite("Hebrews 2:17–18"),
    "Does %s sound like a Savior who has never met grief?" % cite("Isaiah 53:3"),
    "What did Jesus do at the tomb of His friend, in %s?" % cite("John 11:35"),
    "What would I say to Him today if I believed He understands and is able to help?",
]
C9["truths"] = [
    "Jesus was tempted in every way that I am, yet without sin.",
    "He is able to sympathize with my weakness.",
    "He was a man of sorrows, acquainted with grief.",
    "Jesus wept.",
    "Because He suffered when tempted, He is able to help me.",
    "I may come to Him with confidence and find mercy.",
]
C9["replacement"] = (
    "Jesus does understand what I am going through. He was tempted as we are, He was a man of sorrows, and He wept. "
    "Because He suffered, He is able to help, and I may come to Him with confidence."
)
C9["actions"] = [
    "<strong>Name the pain in one sentence</strong> and read %s over it." % cite("Hebrews 4:15"),
    "<strong>Read %s</strong> and write “He is able to help” under the temptation or sorrow you have been hiding." % cite("Hebrews 2:17–18"),
    "<strong>Tell one safe believer,</strong> “I have thought Jesus does not understand this,” and ask them to pray %s with you." % cite("John 11:35"),
    "<strong>Come to Him once today</strong> without cleaning the story up first.",
]
C9["prayer"] = (
    "Lord Jesus, I have believed You cannot understand this. Thank You for what %s says. "
    "You know weakness, and You are able to help. I come to You with this as it is. Amen."
) % cite("Hebrews 4:15")

C10 = dict(
    num=10, file="My-Sins-Are-Too-Bad-For-Jesus",
    belief="Jesus died for other people’s sins, but not ones as bad as mine.",
    key="1 Timothy 1:15",
    also=["Isaiah 53:6", "1 John 2:1–2", "John 6:37", "Romans 5:8", "Hebrews 7:25"],
    pearls=["forgiveness", "christ-sacrifice-of", "sin-consequences-of", "mercy", "salvation"],
    reading="forgiveness", gc=[26, 14, 7],
    songs=[
        ("east", "The forgiveness of God reaches the person who feels too far gone."),
        ("clean", "The cross is able to make the guilty clean."),
        ("forgive", "Forgiveness is His to give, even when you cannot imagine it."),
        ("lovesme", "Jesus loves me, this I know, is true for a sinner who feels like the worst."),
    ],
    origins="A secret sin, a public failure, abuse you committed or suffered, or years of hearing that some people are too far gone can put your name on the exception list. Other people get the cross. You get the footnote. Shame is loud. It is not the measure of the atonement. Paul, who called himself the worst of sinners, did not find an exception clause with his name on it.",
    self=[
        "My sin is the one exception.",
        "Jesus died for church people, not for what I did.",
        "If people knew, they would agree I am past forgiveness.",
        "I can believe the gospel for others and not for myself.",
        "I have to pay the rest of this down before I can come.",
        "The cross was enough for them and too small for me.",
    ],
    errors=[
        ("All-or-nothing thinking", "If my sin is serious, it must be beyond the cross."),
        ("Personalization", "Taking a general promise and silently removing your own name."),
        ("Emotional reasoning", "Feeling unforgivable and treating the feeling as theology."),
        ("Discounting the positive", "Ignoring “the worst,” “us all,” and “I will never drive away.”"),
    ],
    prompt="When I left my sin outside the cross",
    moment="I decided my sin was the exception Jesus did not die for",
    example="Christ Jesus came to save sinners, and He will not drive away the one who comes to Him. That includes me.",
    tracker="A sin I stopped calling too bad for the cross",
)
C10["teaches"] = (
    "The gospel does not come with a list of sins too bad to include. "
    + cite("1 Timothy 1:15") + " "
    + cite("Isaiah 53:6") + " "
    + cite("1 John 2:1–2") + " "
    + cite("John 6:37") + " "
    + cite("Romans 5:8") + " "
    + cite("Hebrews 7:25") + " "
    "He is able to save completely those who draw near through Him. "
    "Your sin is real. It is not heavier than the iniquity the Lord laid on His Son."
)
C10["questions"] = [
    "Which sin have I quietly removed from the cross?",
    "Who did Christ Jesus come to save, according to %s?" % cite("1 Timothy 1:15"),
    "Whose iniquity did the Lord lay on Him, in %s?" % cite("Isaiah 53:6"),
    "If I sin, who is my advocate, according to %s?" % cite("1 John 2:1–2"),
    "What does Jesus promise the one who comes to Him, in %s?" % cite("John 6:37"),
    "Would I tell a friend with this same sin that the cross was too small?",
]
C10["truths"] = [
    "Christ Jesus came into the world to save sinners.",
    "The Lord laid the iniquity of us all on Him.",
    "If I sin, I have an advocate, Jesus Christ the Righteous One.",
    "He is the atoning sacrifice for sins, not only for the respectable ones.",
    "The one who comes to Him He will never drive away.",
    "He is able to save completely those who draw near through Him.",
]
C10["replacement"] = (
    "Jesus did not die for other people’s sins and leave mine out. He came to save sinners, of whom Paul called himself the worst. "
    "The Lord laid on Him the iniquity of us all. The one who comes to Him He will never drive away."
)
C10["actions"] = [
    "<strong>Write the sin you think is too bad,</strong> then write %s underneath it." % cite("1 Timothy 1:15"),
    "<strong>Read %s</strong> and circle “us all.” Put your initials beside those words as your application, not as a change to the verse." % cite("Isaiah 53:6"),
    "<strong>Tell one safe believer the exception you have believed,</strong> and ask them to read %s with you." % cite("John 6:37"),
    "<strong>Come to Jesus once with that sin named,</strong> without promising you will earn the forgiveness.",
]
C10["prayer"] = (
    "Lord Jesus, I have believed my sin is the one You did not die for. Thank You for what %s says. "
    "I come to You with it. Do not drive me away. Amen."
) % cite("1 Timothy 1:15")

CARDS = [C6, C7, C8, C9, C10]


def main():
    paths = []
    text = (g.ROOT / "belief-lists/spiritual-religious.html").read_text()
    for d in CARDS:
        if d["belief"] not in text:
            raise SystemExit("list wording differs: " + d["belief"])
        if d["file"] not in text:
            raise SystemExit("list is not wired to " + d["file"])
        g.write_card(d)
        paths.append(g.ROOT / "belief-cards" / ("Belief-%03d-%s.html" % (d["num"], d["file"])))
    g.print_pdfs(paths)
    print("list links confirmed")


if __name__ == "__main__":
    main()
