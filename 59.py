from itertools import combinations_with_replacement, permutations

xor_string = [36,22,80,0,0,4,23,25,19,17,88,4,4,19,21,11,88,22,23,23,29,69,12,24,0,88,25,11,12,2,10,28,5,6,12,25,10,22,80,10,30,80,10,22,21,69,23,22,69,61,5,9,29,2,66,11,80,8,23,3,17,88,19,0,20,21,7,10,17,17,29,20,69,8,17,21,29,2,22,84,80,71,60,21,69,11,5,8,21,25,22,88,3,0,10,25,0,10,5,8,88,2,0,27,25,21,10,31,6,25,2,16,21,82,69,35,63,11,88,4,13,29,80,22,13,29,22,88,31,3,88,3,0,10,25,0,11,80,10,30,80,23,29,19,12,8,2,10,27,17,9,11,45,95,88,57,69,16,17,19,29,80,23,29,19,0,22,4,9,1,80,3,23,5,11,28,92,69,9,5,12,12,21,69,13,30,0,0,0,0,27,4,0,28,28,28,84,80,4,22,80,0,20,21,2,25,30,17,88,21,29,8,2,0,11,3,12,23,30,69,30,31,23,88,4,13,29,80,0,22,4,12,10,21,69,11,5,8,88,31,3,88,4,13,17,3,69,11,21,23,17,21,22,88,65,69,83,80,84,87,68,69,83,80,84,87,73,69,83,80,84,87,65,83,88,91,69,29,4,6,86,92,69,15,24,12,27,24,69,28,21,21,29,30,1,11,80,10,22,80,17,16,21,69,9,5,4,28,2,4,12,5,23,29,80,10,30,80,17,16,21,69,27,25,23,27,28,0,84,80,22,23,80,17,16,17,17,88,25,3,88,4,13,29,80,17,10,5,0,88,3,16,21,80,10,30,80,17,16,25,22,88,3,0,10,25,0,11,80,12,11,80,10,26,4,4,17,30,0,28,92,69,30,2,10,21,80,12,12,80,4,12,80,10,22,19,0,88,4,13,29,80,20,13,17,1,10,17,17,13,2,0,88,31,3,88,4,13,29,80,6,17,2,6,20,21,69,30,31,9,20,31,18,11,94,69,54,17,8,29,28,28,84,80,44,88,24,4,14,21,69,30,31,16,22,20,69,12,24,4,12,80,17,16,21,69,11,5,8,88,31,3,88,4,13,17,3,69,11,21,23,17,21,22,88,25,22,88,17,69,11,25,29,12,24,69,8,17,23,12,80,10,30,80,17,16,21,69,11,1,16,25,2,0,88,31,3,88,4,13,29,80,21,29,2,12,21,21,17,29,2,69,23,22,69,12,24,0,88,19,12,10,19,9,29,80,18,16,31,22,29,80,1,17,17,8,29,4,0,10,80,12,11,80,84,67,80,10,10,80,7,1,80,21,13,4,17,17,30,2,88,4,13,29,80,22,13,29,69,23,22,69,12,24,12,11,80,22,29,2,12,29,3,69,29,1,16,25,28,69,12,31,69,11,92,69,17,4,69,16,17,22,88,4,13,29,80,23,25,4,12,23,80,22,9,2,17,80,70,76,88,29,16,20,4,12,8,28,12,29,20,69,26,9,69,11,80,17,23,80,84,88,31,3,88,4,13,29,80,21,29,2,12,21,21,17,29,2,69,12,31,69,12,24,0,88,20,12,25,29,0,12,21,23,86,80,44,88,7,12,20,28,69,11,31,10,22,80,22,16,31,18,88,4,13,25,4,69,12,24,0,88,3,16,21,80,10,30,80,17,16,25,22,88,3,0,10,25,0,11,80,17,23,80,7,29,80,4,8,0,23,23,8,12,21,17,17,29,28,28,88,65,75,78,68,81,65,67,81,72,70,83,64,68,87,74,70,81,75,70,81,67,80,4,22,20,69,30,2,10,21,80,8,13,28,17,17,0,9,1,25,11,31,80,17,16,25,22,88,30,16,21,18,0,10,80,7,1,80,22,17,8,73,88,17,11,28,80,17,16,21,11,88,4,4,19,25,11,31,80,17,16,21,69,11,1,16,25,2,0,88,2,10,23,4,73,88,4,13,29,80,11,13,29,7,29,2,69,75,94,84,76,65,80,65,66,83,77,67,80,64,73,82,65,67,87,75,72,69,17,3,69,17,30,1,29,21,1,88,0,23,23,20,16,27,21,1,84,80,18,16,25,6,16,80,0,0,0,23,29,3,22,29,3,69,12,24,0,88,0,0,10,25,8,29,4,0,10,80,10,30,80,4,88,19,12,10,19,9,29,80,18,16,31,22,29,80,1,17,17,8,29,4,0,10,80,12,11,80,84,86,80,35,23,28,9,23,7,12,22,23,69,25,23,4,17,30,69,12,24,0,88,3,4,21,21,69,11,4,0,8,3,69,26,9,69,15,24,12,27,24,69,49,80,13,25,20,69,25,2,23,17,6,0,28,80,4,12,80,17,16,25,22,88,3,16,21,92,69,49,80,13,25,6,0,88,20,12,11,19,10,14,21,23,29,20,69,12,24,4,12,80,17,16,21,69,11,5,8,88,31,3,88,4,13,29,80,22,29,2,12,29,3,69,73,80,78,88,65,74,73,70,69,83,80,84,87,72,84,88,91,69,73,95,87,77,70,69,83,80,84,87,70,87,77,80,78,88,21,17,27,94,69,25,28,22,23,80,1,29,0,0,22,20,22,88,31,11,88,4,13,29,80,20,13,17,1,10,17,17,13,2,0,88,31,3,88,4,13,29,80,6,17,2,6,20,21,75,88,62,4,21,21,9,1,92,69,12,24,0,88,3,16,21,80,10,30,80,17,16,25,22,88,29,16,20,4,12,8,28,12,29,20,69,26,9,69,65,64,69,31,25,19,29,3,69,12,24,0,88,18,12,9,5,4,28,2,4,12,21,69,80,22,10,13,2,17,16,80,21,23,7,0,10,89,69,23,22,69,12,24,0,88,19,12,10,19,16,21,22,0,10,21,11,27,21,69,23,22,69,12,24,0,88,0,0,10,25,8,29,4,0,10,80,10,30,80,4,88,19,12,10,19,9,29,80,18,16,31,22,29,80,1,17,17,8,29,4,0,10,80,12,11,80,84,86,80,36,22,20,69,26,9,69,11,25,8,17,28,4,10,80,23,29,17,22,23,30,12,22,23,69,49,80,13,25,6,0,88,28,12,19,21,18,17,3,0,88,18,0,29,30,69,25,18,9,29,80,17,23,80,1,29,4,0,10,29,12,22,21,69,12,24,0,88,3,16,21,3,69,23,22,69,12,24,0,88,3,16,26,3,0,9,5,0,22,4,69,11,21,23,17,21,22,88,25,11,88,7,13,17,19,13,88,4,13,29,80,0,0,0,10,22,21,11,12,3,69,25,2,0,88,21,19,29,30,69,22,5,8,26,21,23,11,94]
xor_string = [chr(i) for i in xor_string]
xor_string = "".join(xor_string)


def sxor(s1,s2):
    mul = int(len(s1) / len(s2)  + 1)
    s2 *= mul
    s2 = s2[:len(s1)]
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))


alpha = "abcdefghijklmnopqrstuvwxyz"
common_words = [
"ability",
"able",
"about",
"above",
"accept",
"according",
"account",
"across",
"act",
"action",
"activity",
"actually",
"add",
"address",
"administration",
"admit",
"adult",
"affect",
"after",
"again",
"against",
"age",
"agency",
"agent",
"ago",
"agree",
"agreement",
"ahead",
"air",
"all",
"allow",
"almost",
"alone",
"along",
"already",
"also",
"although",
"always",
"American",
"among",
"amount",
"analysis",
"and",
"animal",
"another",
"answer",
"any",
"anyone",
"anything",
"appear",
"apply",
"approach",
"area",
"argue",
"arm",
"around",
"arrive",
"art",
"article",
"artist",
"as",
"ask",
"assume",
"at",
"attack",
"attention",
"attorney",
"audience",
"author",
"authority",
"available",
"avoid",
"away",
"baby",
"back",
"bad",
"bag",
"ball",
"bank",
"bar",
"base",
"be",
"beat",
"beautiful",
"because",
"become",
"bed",
"before",
"begin",
"behavior",
"behind",
"believe",
"benefit",
"best",
"better",
"between",
"beyond",
"big",
"bill",
"billion",
"bit",
"black",
"blood",
"blue",
"board",
"body",
"book",
"born",
"both",
"box",
"boy",
"break",
"bring",
"brother",
"budget",
"build",
"building",
"business",
"but",
"buy",
"by",
"call",
"camera",
"campaign",
"can",
"cancer",
"candidate",
"capital",
"car",
"card",
"care",
"career",
"carry",
"case",
"catch",
"cause",
"cell",
"center",
"central",
"century",
"certain",
"certainly",
"chair",
"challenge",
"chance",
"change",
"character",
"charge",
"check",
"child",
"choice",
"choose",
"church",
"citizen",
"city",
"civil",
"claim",
"class",
"clear",
"clearly",
"close",
"coach",
"cold",
"collection",
"college",
"color",
"come",
"commercial",
"common",
"community",
"company",
"compare",
"computer",
"concern",
"condition",
"conference",
"Congress",
"consider",
"consumer",
"contain",
"continue",
"control",
"cost",
"could",
"country",
"couple",
"course",
"court",
"cover",
"create",
"crime",
"cultural",
"culture",
"cup",
"current",
"customer",
"cut",
"dark",
"data",
"daughter",
"day",
"dead",
"deal",
"death",
"debate",
"decade",
"decide",
"decision",
"deep",
"defense",
"degree",
"Democrat",
"democratic",
"describe",
"design",
"despite",
"detail",
"determine",
"develop",
"development",
"die",
"difference",
"different",
"difficult",
"dinner",
"direction",
"director",
"discover",
"discuss",
"discussion",
"disease",
"do",
"doctor",
"dog",
"door",
"down",
"draw",
"dream",
"drive",
"drop",
"drug",
"during",
"each",
"early",
"east",
"easy",
"eat",
"economic",
"economy",
"edge",
"education",
"effect",
"effort",
"eight",
"either",
"election",
"else",
"employee",
"end",
"energy",
"enjoy",
"enough",
"enter",
"entire",
"environment",
"environmental",
"especially",
"establish",
"even",
"evening",
"event",
"ever",
"every",
"everybody",
"everyone",
"everything",
"evidence",
"exactly",
"example",
"executive",
"exist",
"expect",
"experience",
"expert",
"explain",
"eye",
"face",
"fact",
"factor",
"fail",
"fall",
"family",
"far",
"fast",
"father",
"fear",
"federal",
"feel",
"feeling",
"few",
"field",
"fight",
"figure",
"fill",
"film",
"final",
"finally",
"financial",
"find",
"fine",
"finger",
"finish",
"fire",
"firm",
"first",
"fish",
"five",
"floor",
"fly",
"focus",
"follow",
"food",
"foot",
"for",
"force",
"foreign",
"forget",
"form",
"former",
"forward",
"four",
"free",
"friend",
"from",
"front",
"full",
"fund",
"future",
"game",
"garden",
"gas",
"general",
"generation",
"get",
"girl",
"give",
"glass",
"go",
"goal",
"good",
"government",
"great",
"green",
"ground",
"group",
"grow",
"growth",
"guess",
"gun",
"guy",
"hair",
"half",
"hand",
"hang",
"happen",
"happy",
"hard",
"have",
"he",
"head",
"health",
"hear",
"heart",
"heat",
"heavy",
"help",
"her",
"here",
"herself",
"high",
"him",
"himself",
"his",
"history",
"hit",
"hold",
"home",
"hope",
"hospital",
"hot",
"hotel",
"hour",
"house",
"how",
"however",
"huge",
"human",
"hundred",
"husband",
"idea",
"identify",
"if",
"image",
"imagine",
"impact",
"important",
"improve",
"in",
"include",
"including",
"increase",
"indeed",
"indicate",
"individual",
"industry",
"information",
"inside",
"instead",
"institution",
"interest",
"interesting",
"international",
"interview",
"into",
"investment",
"involve",
"issue",
"it",
"item",
"its",
"itself",
"job",
"join",
"just",
"keep",
"key",
"kid",
"kill",
"kind",
"kitchen",
"know",
"knowledge",
"land",
"language",
"large",
"last",
"late",
"later",
"laugh",
"law",
"lawyer",
"lay",
"lead",
"leader",
"learn",
"least",
"leave",
"left",
"leg",
"legal",
"less",
"let",
"letter",
"level",
"lie",
"life",
"light",
"like",
"likely",
"line",
"list",
"listen",
"little",
"live",
"local",
"long",
"look",
"lose",
"loss",
"lot",
"love",
"low",
"machine",
"magazine",
"main",
"maintain",
"major",
"majority",
"make",
"man",
"manage",
"management",
"manager",
"many",
"market",
"marriage",
"material",
"matter",
"may",
"maybe",
"me",
"mean",
"measure",
"media",
"medical",
"meet",
"meeting",
"member",
"memory",
"mention",
"message",
"method",
"middle",
"might",
"military",
"million",
"mind",
"minute",
"miss",
"mission",
"model",
"modern",
"moment",
"money",
"month",
"more",
"morning",
"most",
"mother",
"mouth",
"move",
"movement",
"movie",
"Mr",
"Mrs",
"much",
"music",
"must",
"my",
"myself",
"name",
"nation",
"national",
"natural",
"nature",
"near",
"nearly",
"necessary",
"need",
"network",
"never",
"new",
"news",
"newspaper",
"next",
"nice",
"night",
"no",
"none",
"nor",
"north",
"not",
"note",
"nothing",
"notice",
"now",
"n't",
"number",
"occur",
"of",
"off",
"offer",
"office",
"officer",
"official",
"often",
"oh",
"oil",
"ok",
"old",
"on",
"once",
"one",
"only",
"onto",
"open",
"operation",
"opportunity",
"option",
"or",
"order",
"organization",
"other",
"others",
"our",
"out",
"outside",
"over",
"own",
"owner",
"page",
"pain",
"painting",
"paper",
"parent",
"part",
"participant",
"particular",
"particularly",
"partner",
"party",
"pass",
"past",
"patient",
"pattern",
"pay",
"peace",
"people",
"per",
"perform",
"performance",
"perhaps",
"period",
"person",
"personal",
"phone",
"physical",
"pick",
"picture",
"piece",
"place",
"plan",
"plant",
"play",
"player",
"PM",
"point",
"police",
"policy",
"political",
"politics",
"poor",
"popular",
"population",
"position",
"positive",
"possible",
"power",
"practice",
"prepare",
"present",
"president",
"pressure",
"pretty",
"prevent",
"price",
"private",
"probably",
"problem",
"process",
"produce",
"product",
"production",
"professional",
"professor",
"program",
"project",
"property",
"protect",
"prove",
"provide",
"public",
"pull",
"purpose",
"push",
"put",
"quality",
"question",
"quickly",
"quite",
"race",
"radio",
"raise",
"range",
"rate",
"rather",
"reach",
"read",
"ready",
"real",
"reality",
"realize",
"really",
"reason",
"receive",
"recent",
"recently",
"recognize",
"record",
"red",
"reduce",
"reflect",
"region",
"relate",
"relationship",
"religious",
"remain",
"remember",
"remove",
"report",
"represent",
"Republican",
"require",
"research",
"resource",
"respond",
"response",
"responsibility",
"rest",
"result",
"return",
"reveal",
"rich",
"right",
"rise",
"risk",
"road",
"rock",
"role",
"room",
"rule",
"run",
"safe",
"same",
"save",
"say",
"scene",
"school",
"science",
"scientist",
"score",
"sea",
"season",
"seat",
"second",
"section",
"security",
"see",
"seek",
"seem",
"sell",
"send",
"senior",
"sense",
"series",
"serious",
"serve",
"service",
"set",
"seven",
"several",
"sex",
"sexual",
"shake",
"share",
"she",
"shoot",
"short",
"shot",
"should",
"shoulder",
"show",
"side",
"sign",
"significant",
"similar",
"simple",
"simply",
"since",
"sing",
"single",
"sister",
"sit",
"site",
"situation",
"six",
"size",
"skill",
"skin",
"small",
"smile",
"so",
"social",
"society",
"soldier",
"some",
"somebody",
"someone",
"something",
"sometimes",
"son",
"song",
"soon",
"sort",
"sound",
"source",
"south",
"southern",
"space",
"speak",
"special",
"specific",
"speech",
"spend",
"sport",
"spring",
"staff",
"stage",
"stand",
"standard",
"star",
"start",
"state",
"statement",
"station",
"stay",
"step",
"still",
"stock",
"stop",
"store",
"story",
"strategy",
"street",
"strong",
"structure",
"student",
"study",
"stuff",
"style",
"subject",
"success",
"successful",
"such",
"suddenly",
"suffer",
"suggest",
"summer",
"support",
"sure",
"surface",
"system",
"table",
"take",
"talk",
"task",
"tax",
"teach",
"teacher",
"team",
"technology",
"television",
"tell",
"ten",
"tend",
"term",
"test",
"than",
"thank",
"that",
"the",
"their",
"them",
"themselves",
"then",
"theory",
"there",
"these",
"they",
"thing",
"think",
"third",
"this",
"those",
"though",
"thought",
"thousand",
"threat",
"three",
"through",
"throughout",
"throw",
"thus",
"time",
"to",
"today",
"together",
"tonight",
"too",
"top",
"total",
"tough",
"toward",
"town",
"trade",
"traditional",
"training",
"travel",
"treat",
"treatment",
"tree",
"trial",
"trip",
"trouble",
"true",
"truth",
"try",
"turn",
"TV",
"two",
"type",
"under",
"understand",
"unit",
"until",
"up",
"upon",
"us",
"use",
"usually",
"value",
"various",
"very",
"victim",
"view",
"violence",
"visit",
"voice",
"vote",
"wait",
"walk",
"wall",
"want",
"war",
"watch",
"water",
"way",
"we",
"weapon",
"wear",
"week",
"weight",
"well",
"west",
"western",
"what",
"whatever",
"when",
"where",
"whether",
"which",
"while",
"white",
"who",
"whole",
"whom",
"whose",
"why",
"wide",
"wife",
"will",
"win",
"wind",
"window",
"wish",
"with",
"within",
"without",
"woman",
"wonder",
"word",
"work",
"worker",
"world",
"worry",
"would",
"write",
"writer",
"wrong",
"yard",
"yeah",
"year",
"yes",
"yet",
"you",
"young",
"your",
"yourself"]

results = []
for i in permutations(alpha, 3):
    key = "".join(i)
    decrypted = sxor(xor_string, key)
    found_words = sum([1 for i in common_words if i in decrypted])
    results.append([found_words, key])


results.sort()
for res in results[-5:]:
    key = res[1]
    text = sxor(xor_string, key)
    print(text)
    print(res)
    print(sum([ord(i) for i in text]))

