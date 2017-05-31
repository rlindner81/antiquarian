def get_books(articles_info, volumes_min, volumes_max):
    volumes = (
        {
            "number": "1",
            "historical_year": "historical years 1966-1979",
            "name": "the-digital-antiquarian-vol-01",
            "title": "The Digital Antiquarian, Volume 1: 1966-1979",
            "cover": "cover-vol-01.jpg",
            "articles": (
                "on-the-trail-of-the-oregon-trail-part-1",
                "on-the-trail-of-the-oregon-trail-part-2",
                "on-the-trail-of-the-oregon-trail-part-3",
                "on-the-trail-of-the-oregon-trail-part-4",
                "on-the-trail-of-the-oregon-trail-part-5",
                "in-defense-of-basic",
                "hunt-the-wumpus-part-1",
                "hunt-the-wumpus-part-2",
                "will-crowthers-adventure-part-1",
                "will-crowthers-adventure-part-2",
                "the-completed-adventure-part-1",
                "the-completed-adventure-part-2",
                "the-completed-adventure-part-3",
                "the-trash-80-part-1",
                "the-trash-80-part-2",
                "the-trash-80-part-3",
                "eliza-part-1",
                "eliza-part-2",
                "eliza-part-3",
                "adventureland-part-1",
                "adventureland-part-2",
                "dog-star-adventure",
                "a-few-questions-for-lance-micklus",
                "a-busy-1979",
                "the-count",
                "two-adventuring-cultures",
                "microsoft-adventure",
                "ludic-narrative-nee-storygame",
                "the-rise-of-experiential-games",
                "dungeons-and-dragons",
                "defining-the-crpg",
                "from-the-tabletop-to-the-computer",
                "the-first-crpgs",
                "temple-of-apshai"
            )
        },
        {
            "number": "2",
            "historical_year": "historical year 1980",
            "name": "the-digital-antiquarian-vol-02",
            "title": "The Digital Antiquarian, Volume 2: 1980",
            "cover": "cover-vol-02.jpg",
            "articles": (
                "a-busy-1980",
                "robert-lafores-interactive-fiction",
                "binning-the-trash-80",
                "jobs-and-woz",
                "the-apple-ii",
                "eamon-part-1",
                "a-journey-into-the-wonderful-world-of-eamon",
                "eamon-part-2",
                "ken-and-roberta",
                "mystery-house-part-1",
                "mystery-house-part-2",
                "on-line-systems-is-born",
                "the-wizard-and-the-princess-part-1",
                "the-wizard-and-the-princess-part-2",
                "dunjonquest",
                "edu-ware",
                "interactive-fantasies",
                "the-prisoner-part-1",
                "the-prisoner-part-2",
                "a-word-on-akalabeth-and-chronology",
                "lord-british",
                "akalabeth",
                "california-pacific",
                "the-roots-of-infocom",
                "zork-on-the-pdp-10",
                "the-birth-of-infocom",
                "zil-and-the-z-machine",
                "selling-zork",
                "parser-games",
                "exploring-zork-part-1",
                "exploring-zork-part-2",
                "exploring-zork-part-3"
            )
        },
        {
            "number": "3",
            "historical_year": "historical year 1981",
            "name": "the-digital-antiquarian-vol-03",
            "title": "The Digital Antiquarian, Volume 3: 1981",
            "cover": "cover-vol-03.jpg",
            "articles": (
                "silas-warner-and-muse-software",
                "robot-war",
                "ultima-part-1",
                "ultima-part-2",
                "ultima-part-3",
                "summer-camp",
                "sex-comes-to-the-micros",
                "softporn",
                "a-tale-of-two-languages",
                "pascal-and-the-p-machine",
                "the-roots-of-sir-tech",
                "making-wizardry",
                "playing-wizardry",
                "the-wizardry-phenomenon",
                "of-game-consoles-home-computers-and-personal-computers",
                "computers-for-the-masses",
                "this-game-is-over",
                "castle-wolfenstein",
                "my-eamon-problem",
                "sentient-software",
                "micro-men",
                "the-ibm-pc-part-1",
                "the-ibm-pc-part-2",
                "the-ibm-pc-part-3",
                "the-ibm-pc-part-4",
                "infocom-going-it-alone",
                "the-adventure-bundle",
                "zork-ii-part-1",
                "zork-ii-part-2"
            )
        },
        {
            "number": "4",
            "historical_year": "historical year 1982",
            "name": "the-digital-antiquarian-vol-04",
            "title": "The Digital Antiquarian, Volume 4: 1982",
            "cover": "cover-vol-04.jpg",
            "articles": (
                "time-zone",
                "time-zone-tackling-the-monster",
                "time-zone-aftermath",
                "ludic-murder",
                "britains-occult-uncle",
                "the-dennis-wheatley-crime-dossiers",
                "deadline",
                "playing-deadline-part-1",
                "playing-deadline-part-2",
                "playing-deadline-part-3",
                "playing-deadline-part-4",
                "the-zork-users-group",
                "japan",
                "japanese-adventuring",
                "broderbund",
                "choplifter",
                "the-prisoner-2",
                "saga",
                "zork-iii-part-1",
                "zork-iii-part-2",
                "starcross",
                "the-magnificent-penguin",
                "transylvania",
                "the-wizardry-and-ultima-sequels",
                "playing-ultima-ii-part-1",
                "playing-ultima-ii-part-2",
                "level-9",
                "the-bbc-micro",
                "phoenix-and-acornsoft",
                "a-gallery-of-unfortunate-events",
                "the-speccy",
                "the-hobbit",
                "summer-camp-is-over",
                "the-commodore-64"
            )
        },
        {
            "number": "5",
            "historical_year": "historical year 1983",
            "name": "the-digital-antiquarian-vol-05",
            "title": "The Digital Antiquarian, Volume 5: 1983",
            "cover": "cover-vol-05.jpg",
            "articles": (
                "business-is-war",
                "shiny-and-exciting-vs-dull-and-boring",
                "xerox-parc",
                "lisa",
                "seeing-farther",
                "the-pinball-wizard",
                "dan-bunten-and-m-u-l-e",
                "free-fall-part-1-archon",
                "free-fall-part-2-murder-on-the-zinderneuf",
                "suspended",
                "the-top-of-its-game",
                "the-witness",
                "planetfall",
                "enchanter",
                "infidel",
                "origin-systems",
                "the-legend-of-escape-from-mt-drash",
                "ultima-iii-in-pictures",
                "the-dawn-of-multimedia",
                "the-laser-craze",
                "1983-in-british-computing",
                "peter-killworths-1983",
                "snowball",
                "the-quill"
            )
        },
        {
            "number": "6",
            "historical_year": "historical year 1984",
            "name": "the-digital-antiquarian-vol-06",
            "title": "The Digital Antiquarian, Volume 6: 1984",
            "cover": "cover-vol-06.jpg",
            "articles": (
                "popcorn-and-peanuts",
                "the-unmaking-and-remaking-of-sierra-on-line",
                "a-computer-for-every-home",
                "from-automated-simulations-to-epyx",
                "how-things-work-commodore-64-and-summer-games-edition",
                "seven-cities-of-gold",
                "sorcerer",
                "seastalker",
                "bookware",
                "rendezvous-with-rama",
                "fahrenheit-451-the-book",
                "fahrenheit-451-the-game",
                "dragonworld",
                "michael-crichton",
                "from-congo-to-amazon",
                "amazon-in-pictures",
                "shadowkeep",
                "masters-of-the-game",
                "cutthroats",
                "douglas-adams",
                "the-computerized-hitchhikers",
                "hitchhiking-the-galaxy-infocom-style",
                "suspect",
                "sherlock",
                "this-tormented-business-part-1",
                "elite",
                "mike-singleton-and-the-lords-of-midnight",
                "the-legend-of-ultimate-play-the-game",
                "the-merry-pranksters-of-automata"
            )
        },
        {
            "number": "7",
            "historical_year": "historical year 1985",
            "name": "the-digital-antiquarian-vol-07",
            "title": "The Digital Antiquarian, Volume 7: 1985",
            "cover": "cover-vol-07.jpg",
            "articles": (
                "this-tormented-business-part-2",
                "ql-pawn",
                "macintosh",
                "macware",
                "mindwhell-or-the-poet-and-the-hackers",
                "essex-and-brimstone",
                "this-tormented-business-part-3",
                "down-from-the-top",
                "wishbringer",
                "fooblitzky",
                "a-mind-forever-voyaging-part-1-steve-meretzkys-interiors",
                "a-mind-forever-voyaging-part-2-dont-go-back-to-rockvil",
                "a-mind-forever-voyaging-part-3-through-strange-seas-of-thought-alone",
                "spellbreaker",
                "perry-mason-the-case-of-the-mandarin-murder",
                "nine-princes-in-amber",
                "an-alternate-chronicle-of-amber",
                "comprehend",
                "of-wizards-and-bards",
                "the-road-to-iv",
                "ultima-iv",
                "human-engineered-software-or-the-software-icarus",
                "project-space-station-part-1-the-reality",
                "project-space-station-part-2-the-dream",
                "project-space-station-part-3-the-game",
                "apple-carmen-sandiego-and-the-rise-of-edutainment"
            )
        },
        {
            "number": "8",
            "historical_year": "historical year 1986",
            "name": "the-digital-antiquarian-vol-08",
            "title": "The Digital Antiquarian, Volume 8: 1986",
            "cover": "cover-vol-08.jpg",
            "articles": (
                "access-software",
                "leader-board",
                "the-magnificient-penguin-hangs-up-his-tuxedo",
                "amnesia",
                "the-fractal-phenomenon",
                "send-in-the-clones",
                "the-forth-dimension",
                "starflight",
                "jim-levy-and-activision",
                "alter-ego",
                "dortes-view-alter-ego",
                "portal",
                "bookwares-sunset-2",
                "accolade-artech-and-killed-until-dead",
                "simon-schusters-treks-to-nowhere",
                "ballyhoo",
                "out-of-the-frying-pan",
                "trinity",
                "t-plus-5-bombs-in-space",
                "t-plus-4-bombing-nevada",
                "t-plus-3-edward-teller-and-his-superbomb",
                "t-plus-2-the-bomb-at-the-crossroads",
                "t-plus-1-bombing-japan",
                "t-plus-0-the-fulcrum-of-history",
                "t-plus-6-all-roads-lead-to-the-kensington-gardens",
                "trinity-postscript-selling-tragedy",
                "leather-goddesses-of-phobos-or-sex-comes-to-the-micros-again",
                "moonmist",
                "microproses-simulation-industrial-complex-or-the-ballad-of-sid-and-wild-bill",
                "the-68000-wars-part-1-lorraine",
                "the-68000-wars-part-2-jack-is-back",
                "icbm",
                "the-68000-wars-part-3-we-made-amiga-they-fucked-it-up",
                "defender-of-the-crown",
                "on-s-d-i-just-a-little-and-king-of-chicago-quite-a-lot",
                "brian-fargo-and-interplay",
                "fire-and-rain",
                "the-pawns-second-life-or-when-tony-met-anita"
            )
        },
        {
            "number": "9",
            "historical_year": "historical year 1987",
            "name": "the-digital-antiquarian-vol-09",
            "title": "The Digital Antiquarian, Volume 9: 1987",
            "cover": "cover-vol-09.jpg",
            "articles": (
                "thieves-and-jinxes-or-when-michael-met-anita",
                "kaos",
                "topologika",
                "the-evolution-of-the-epyx-games",
                "accolade-gets-distinctive",
                "pirates",
                "a-new-force-in-games-part-1-fractal-dreamers",
                "commodore-the-amiga-years",
                "a-new-force-in-games-part-2-a-habitat-in-cyberspace",
                "a-new-force-in-games-part-3-scumm",
                "the-14-deadly-sins-of-graphic-adventure-design",
                "splendid-isolation-sierra-at-mid-decade",
                "leisure-suit-larry-in-the-land-of-the-lounge-lizards",
                "hollywood-daves-hijinx",
                "bureaucracy",
                "and-into-the-fire",
                "stationfall",
                "the-campy-cosmic-horror-of-h-p-lovecraft",
                "lovecraft-on-the-tabletop",
                "the-lurking-horror",
                "mit-and-gue-or-the-annotated-lurking-horror",
                "nord-and-bert",
                "plundered-hearts",
                "beyond-zork",
                "border-zone",
                "cliff-johnsons-fools-errand",
                "the-68000-wars-part-4-rock-lobster",
                "the-faery-tale-life-of-microillusions",
                "dungeon-master-part-1-the-making-of",
                "dungeon-master-part-2-the-playing-of",
                "a-pirates-life-for-me-part-1-dont-copy-that-floppy",
                "a-pirates-life-for-me-part-2-the-scene",
                "a-pirates-life-for-me-part-3-case-studies-in-copy-protection",
                "bill-williams-the-story-of-a-life"
            )
        },
        {
            "number": "10",
            "historical_year": "historical year 1988",
            "name": "the-digital-antiquarian-vol-10",
            "title": "The Digital Antiquarian, Volume 10: 1988",
            "cover": "cover-vol-10.jpg",
            "articles": (
                "silicon-hollywood-cinemawares-transitional-period",
                "the-road-to-v",
                "ultima-v",
                "friends-of-the-wasteland-the-legacy-of-flying-buffalo",
                "wasteland",
                "joel-billings-and-ssi",
                "ten-odd-years-at-tsr",
                "opening-the-gold-box-part-3-from-tabletop-to-desktop",
                "opening-the-gold-box-part-4-pool-of-radiance",
                "generation-nintendo",
                "sherlock-the-riddle-of-the-crown-jewels",
                "the-bruce-youth",
                "zork-zero",
                "corrupted-fish",
                "tales-of-the-gnome-ranger",
                "kit-williamss-golden-hare-part-1-the-contest",
                "kit-williamss-golden-hare-part-2-the-aftermath",
                "the-end-of-the-line-for-level-9-as-the-market-takes-its-toll-on-magnetic-scrolls"
            )
        },
        {
            "number": "11",
            "historical_year": "historical year 1989",
            "name": "the-digital-antiquarian-vol-11",
            "title": "The Digital Antiquarian, Volume 11: 1989",
            "cover": "cover-vol-11.jpg",
            "articles": (
                "simcity-part-1-will-wrights-city-in-a-box",
                "one-is-enough-for-simcity",
                "acorn-and-amstrad"
            )
        }
    )

    volumes_min = 0 if volumes_min is None else max(0, volumes_min - 1)
    volumes_max = len(volumes) if volumes_max is None else min(len(volumes), volumes_max)

    books = list()
    for index in range(volumes_min, volumes_max):
        volume = volumes[index]
        # expand articles
        volume["articles"] = map(lambda x: articles_info[x], volume["articles"])

        volume["description"] = \
            "This is volume {} of a series of ebooks collecting the articles from Jimmy Maher's " \
            "Digital Antiquarian blog, an ongoing history of interactive entertainment. " \
            "This volume covers the {}. Please note that some multimedia elements -- " \
            "pictures, screenshots, movies, audio -- may display imperfectly or not at all on many e-readers." \
            "".format(volume["number"], volume["historical_year"])
        #
        #
        # make non-comments and comments variant
        book = volume.copy()
        book["has_comments"] = False
        book["description"] += \
            "This version does not include comments made by readers of the original articles. " \
            "Another version is available that does."

        book_comments = volume.copy()
        book_comments["has_comments"] = True
        book_comments["name"] += "-comments"
        book_comments["title"] += ", Comments Edition"
        book_comments["cover"] = book_comments["cover"][:-4] + "-comments.jpg"
        book_comments["description"] += \
            "This version does include comments made by readers of the original articles. " \
            "Another version is available that does not."

        books.append(book)
        books.append(book_comments)
    return books
