#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

emojis="""⛑🏻 Helmet With White Cross, Type-1-2
⛑🏼 Helmet With White Cross, Type-3
⛑🏽 Helmet With White Cross, Type-4
⛑🏾 Helmet With White Cross, Type-5
⛑🏿 Helmet With White Cross, Type-6
💏🏻 Kiss, Type-1-2
💏🏼 Kiss, Type-3
💏🏽 Kiss, Type-4
💏🏾 Kiss, Type-5
💏🏿 Kiss, Type-6
💑🏻 Couple With Heart, Type-1-2
💑🏼 Couple With Heart, Type-3
💑🏽 Couple With Heart, Type-4
💑🏾 Couple With Heart, Type-5
💑🏿 Couple With Heart, Type-6
⛷🏻 Skier, Type-1-2
⛷🏼 Skier, Type-3
⛷🏽 Skier, Type-4
⛷🏾 Skier, Type-5
⛷🏿 Skier, Type-6
😀 Grinning Face
😁 Beaming Face With Smiling Eyes
😂 Face With Tears of Joy
🤣 Rolling on the Floor Laughing
😃 Grinning Face With Big Eyes
😄 Grinning Face With Smiling Eyes
😅 Grinning Face With Sweat
😆 Grinning Squinting Face
😉 Winking Face
😊 Smiling Face With Smiling Eyes
😋 Face Savoring Food
😎 Smiling Face With Sunglasses
😍 Smiling Face With Heart-Eyes
😘 Face Blowing a Kiss
🥰 Smiling Face With 3 Hearts
😗 Kissing Face
😙 Kissing Face With Smiling Eyes
😚 Kissing Face With Closed Eyes
☺️ Smiling Face
🙂 Slightly Smiling Face
🤗 Hugging Face
🤩 Star-Struck
🤔 Thinking Face
🤨 Face With Raised Eyebrow
😐 Neutral Face
😑 Expressionless Face
😶 Face Without Mouth
🙄 Face With Rolling Eyes
😏 Smirking Face
😣 Persevering Face
😥 Sad but Relieved Face
😮 Face With Open Mouth
🤐 Zipper-Mouth Face
😯 Hushed Face
😪 Sleepy Face
😫 Tired Face
😴 Sleeping Face
😌 Relieved Face
😛 Face With Tongue
😜 Winking Face With Tongue
😝 Squinting Face With Tongue
🤤 Drooling Face
😒 Unamused Face
😓 Downcast Face With Sweat
😔 Pensive Face
😕 Confused Face
🙃 Upside-Down Face
🤑 Money-Mouth Face
😲 Astonished Face
☹️ Frowning Face
🙁 Slightly Frowning Face
😖 Confounded Face
😞 Disappointed Face
😟 Worried Face
😤 Face With Steam From Nose
😢 Crying Face
😭 Loudly Crying Face
😦 Frowning Face With Open Mouth
😧 Anguished Face
😨 Fearful Face
😩 Weary Face
🤯 Exploding Head
😬 Grimacing Face
😰 Anxious Face With Sweat
😱 Face Screaming in Fear
🥵 Hot Face
🥶 Cold Face
😳 Flushed Face
🤪 Zany Face
😵 Dizzy Face
😡 Pouting Face
😠 Angry Face
🤬 Face With Symbols on Mouth
😷 Face With Medical Mask
🤒 Face With Thermometer
🤕 Face With Head-Bandage
🤢 Nauseated Face
🤮 Face Vomiting
🤧 Sneezing Face
😇 Smiling Face With Halo
🤠 Cowboy Hat Face
🤡 Clown Face
🥳 Partying Face
🥴 Woozy Face
🥺 Pleading Face
🤥 Lying Face
🤫 Shushing Face
🤭 Face With Hand Over Mouth
🧐 Face With Monocle
🤓 Nerd Face
😈 Smiling Face With Horns
👿 Angry Face With Horns
👹 Ogre
👺 Goblin
💀 Skull
☠️ Skull and Crossbones
👻 Ghost
👽 Alien
👾 Alien Monster
🤖 Robot Face
💩 Pile of Poo
😺 Grinning Cat Face
😸 Grinning Cat Face With Smiling Eyes
😹 Cat Face With Tears of Joy
😻 Smiling Cat Face With Heart-Eyes
😼 Cat Face With Wry Smile
😽 Kissing Cat Face
🙀 Weary Cat Face
😿 Crying Cat Face
😾 Pouting Cat Face
🙈 See-No-Evil Monkey
🙉 Hear-No-Evil Monkey
🙊 Speak-No-Evil Monkey
🏻 Light Skin Tone
🏼 Medium-Light Skin Tone
🏽 Medium Skin Tone
🏾 Medium-Dark Skin Tone
🏿 Dark Skin Tone
👶 Baby
👶🏻 Baby: Light Skin Tone
👶🏼 Baby: Medium-Light Skin Tone
👶🏽 Baby: Medium Skin Tone
👶🏾 Baby: Medium-Dark Skin Tone
👶🏿 Baby: Dark Skin Tone
🧒 Child
🧒🏻 Child: Light Skin Tone
🧒🏼 Child: Medium-Light Skin Tone
🧒🏽 Child: Medium Skin Tone
🧒🏾 Child: Medium-Dark Skin Tone
🧒🏿 Child: Dark Skin Tone
👦 Boy
👦🏻 Boy: Light Skin Tone
👦🏼 Boy: Medium-Light Skin Tone
👦🏽 Boy: Medium Skin Tone
👦🏾 Boy: Medium-Dark Skin Tone
👦🏿 Boy: Dark Skin Tone
👧 Girl
👧🏻 Girl: Light Skin Tone
👧🏼 Girl: Medium-Light Skin Tone
👧🏽 Girl: Medium Skin Tone
👧🏾 Girl: Medium-Dark Skin Tone
👧🏿 Girl: Dark Skin Tone
🧑 Adult
🧑🏻 Adult: Light Skin Tone
🧑🏼 Adult: Medium-Light Skin Tone
🧑🏽 Adult: Medium Skin Tone
🧑🏾 Adult: Medium-Dark Skin Tone
🧑🏿 Adult: Dark Skin Tone
👨 Man
👨🏻 Man: Light Skin Tone
👨🏼 Man: Medium-Light Skin Tone
👨🏽 Man: Medium Skin Tone
👨🏾 Man: Medium-Dark Skin Tone
👨🏿 Man: Dark Skin Tone
👩 Woman
👩🏻 Woman: Light Skin Tone
👩🏼 Woman: Medium-Light Skin Tone
👩🏽 Woman: Medium Skin Tone
👩🏾 Woman: Medium-Dark Skin Tone
👩🏿 Woman: Dark Skin Tone
🧓 Older Adult
🧓🏻 Older Adult: Light Skin Tone
🧓🏼 Older Adult: Medium-Light Skin Tone
🧓🏽 Older Adult: Medium Skin Tone
🧓🏾 Older Adult: Medium-Dark Skin Tone
🧓🏿 Older Adult: Dark Skin Tone
👴 Old Man
👴🏻 Old Man: Light Skin Tone
👴🏼 Old Man: Medium-Light Skin Tone
👴🏽 Old Man: Medium Skin Tone
👴🏾 Old Man: Medium-Dark Skin Tone
👴🏿 Old Man: Dark Skin Tone
👵 Old Woman
👵🏻 Old Woman: Light Skin Tone
👵🏼 Old Woman: Medium-Light Skin Tone
👵🏽 Old Woman: Medium Skin Tone
👵🏾 Old Woman: Medium-Dark Skin Tone
👵🏿 Old Woman: Dark Skin Tone
👨‍⚕️ Man Health Worker
👨🏻‍⚕️ Man Health Worker: Light Skin Tone
👨🏼‍⚕️ Man Health Worker: Medium-Light Skin Tone
👨🏽‍⚕️ Man Health Worker: Medium Skin Tone
👨🏾‍⚕️ Man Health Worker: Medium-Dark Skin Tone
👨🏿‍⚕️ Man Health Worker: Dark Skin Tone
👩‍⚕️ Woman Health Worker
👩🏻‍⚕️ Woman Health Worker: Light Skin Tone
👩🏼‍⚕️ Woman Health Worker: Medium-Light Skin Tone
👩🏽‍⚕️ Woman Health Worker: Medium Skin Tone
👩🏾‍⚕️ Woman Health Worker: Medium-Dark Skin Tone
👩🏿‍⚕️ Woman Health Worker: Dark Skin Tone
👨‍🎓 Man Student
👨🏻‍🎓 Man Student: Light Skin Tone
👨🏼‍🎓 Man Student: Medium-Light Skin Tone
👨🏽‍🎓 Man Student: Medium Skin Tone
👨🏾‍🎓 Man Student: Medium-Dark Skin Tone
👨🏿‍🎓 Man Student: Dark Skin Tone
👩‍🎓 Woman Student
👩🏻‍🎓 Woman Student: Light Skin Tone
👩🏼‍🎓 Woman Student: Medium-Light Skin Tone
👩🏽‍🎓 Woman Student: Medium Skin Tone
👩🏾‍🎓 Woman Student: Medium-Dark Skin Tone
👩🏿‍🎓 Woman Student: Dark Skin Tone
👨‍🏫 Man Teacher
👨🏻‍🏫 Man Teacher: Light Skin Tone
👨🏼‍🏫 Man Teacher: Medium-Light Skin Tone
👨🏽‍🏫 Man Teacher: Medium Skin Tone
👨🏾‍🏫 Man Teacher: Medium-Dark Skin Tone
👨🏿‍🏫 Man Teacher: Dark Skin Tone
👩‍🏫 Woman Teacher
👩🏻‍🏫 Woman Teacher: Light Skin Tone
👩🏼‍🏫 Woman Teacher: Medium-Light Skin Tone
👩🏽‍🏫 Woman Teacher: Medium Skin Tone
👩🏾‍🏫 Woman Teacher: Medium-Dark Skin Tone
👩🏿‍🏫 Woman Teacher: Dark Skin Tone
👨‍⚖️ Man Judge
👨🏻‍⚖️ Man Judge: Light Skin Tone
👨🏼‍⚖️ Man Judge: Medium-Light Skin Tone
👨🏽‍⚖️ Man Judge: Medium Skin Tone
👨🏾‍⚖️ Man Judge: Medium-Dark Skin Tone
👨🏿‍⚖️ Man Judge: Dark Skin Tone
👩‍⚖️ Woman Judge
👩🏻‍⚖️ Woman Judge: Light Skin Tone
👩🏼‍⚖️ Woman Judge: Medium-Light Skin Tone
👩🏽‍⚖️ Woman Judge: Medium Skin Tone
👩🏾‍⚖️ Woman Judge: Medium-Dark Skin Tone
👩🏿‍⚖️ Woman Judge: Dark Skin Tone
👨‍🌾 Man Farmer
👨🏻‍🌾 Man Farmer: Light Skin Tone
👨🏼‍🌾 Man Farmer: Medium-Light Skin Tone
👨🏽‍🌾 Man Farmer: Medium Skin Tone
👨🏾‍🌾 Man Farmer: Medium-Dark Skin Tone
👨🏿‍🌾 Man Farmer: Dark Skin Tone
👩‍🌾 Woman Farmer
👩🏻‍🌾 Woman Farmer: Light Skin Tone
👩🏼‍🌾 Woman Farmer: Medium-Light Skin Tone
👩🏽‍🌾 Woman Farmer: Medium Skin Tone
👩🏾‍🌾 Woman Farmer: Medium-Dark Skin Tone
👩🏿‍🌾 Woman Farmer: Dark Skin Tone
👨‍🍳 Man Cook
👨🏻‍🍳 Man Cook: Light Skin Tone
👨🏼‍🍳 Man Cook: Medium-Light Skin Tone
👨🏽‍🍳 Man Cook: Medium Skin Tone
👨🏾‍🍳 Man Cook: Medium-Dark Skin Tone
👨🏿‍🍳 Man Cook: Dark Skin Tone
👩‍🍳 Woman Cook
👩🏻‍🍳 Woman Cook: Light Skin Tone
👩🏼‍🍳 Woman Cook: Medium-Light Skin Tone
👩🏽‍🍳 Woman Cook: Medium Skin Tone
👩🏾‍🍳 Woman Cook: Medium-Dark Skin Tone
👩🏿‍🍳 Woman Cook: Dark Skin Tone
👨‍🔧 Man Mechanic
👨🏻‍🔧 Man Mechanic: Light Skin Tone
👨🏼‍🔧 Man Mechanic: Medium-Light Skin Tone
👨🏽‍🔧 Man Mechanic: Medium Skin Tone
👨🏾‍🔧 Man Mechanic: Medium-Dark Skin Tone
👨🏿‍🔧 Man Mechanic: Dark Skin Tone
👩‍🔧 Woman Mechanic
👩🏻‍🔧 Woman Mechanic: Light Skin Tone
👩🏼‍🔧 Woman Mechanic: Medium-Light Skin Tone
👩🏽‍🔧 Woman Mechanic: Medium Skin Tone
👩🏾‍🔧 Woman Mechanic: Medium-Dark Skin Tone
👩🏿‍🔧 Woman Mechanic: Dark Skin Tone
👨‍🏭 Man Factory Worker
👨🏻‍🏭 Man Factory Worker: Light Skin Tone
👨🏼‍🏭 Man Factory Worker: Medium-Light Skin Tone
👨🏽‍🏭 Man Factory Worker: Medium Skin Tone
👨🏾‍🏭 Man Factory Worker: Medium-Dark Skin Tone
👨🏿‍🏭 Man Factory Worker: Dark Skin Tone
👩‍🏭 Woman Factory Worker
👩🏻‍🏭 Woman Factory Worker: Light Skin Tone
👩🏼‍🏭 Woman Factory Worker: Medium-Light Skin Tone
👩🏽‍🏭 Woman Factory Worker: Medium Skin Tone
👩🏾‍🏭 Woman Factory Worker: Medium-Dark Skin Tone
👩🏿‍🏭 Woman Factory Worker: Dark Skin Tone
👨‍💼 Man Office Worker
👨🏻‍💼 Man Office Worker: Light Skin Tone
👨🏼‍💼 Man Office Worker: Medium-Light Skin Tone
👨🏽‍💼 Man Office Worker: Medium Skin Tone
👨🏾‍💼 Man Office Worker: Medium-Dark Skin Tone
👨🏿‍💼 Man Office Worker: Dark Skin Tone
👩‍💼 Woman Office Worker
👩🏻‍💼 Woman Office Worker: Light Skin Tone
👩🏼‍💼 Woman Office Worker: Medium-Light Skin Tone
👩🏽‍💼 Woman Office Worker: Medium Skin Tone
👩🏾‍💼 Woman Office Worker: Medium-Dark Skin Tone
👩🏿‍💼 Woman Office Worker: Dark Skin Tone
👨‍🔬 Man Scientist
👨🏻‍🔬 Man Scientist: Light Skin Tone
👨🏼‍🔬 Man Scientist: Medium-Light Skin Tone
👨🏽‍🔬 Man Scientist: Medium Skin Tone
👨🏾‍🔬 Man Scientist: Medium-Dark Skin Tone
👨🏿‍🔬 Man Scientist: Dark Skin Tone
👩‍🔬 Woman Scientist
👩🏻‍🔬 Woman Scientist: Light Skin Tone
👩🏼‍🔬 Woman Scientist: Medium-Light Skin Tone
👩🏽‍🔬 Woman Scientist: Medium Skin Tone
👩🏾‍🔬 Woman Scientist: Medium-Dark Skin Tone
👩🏿‍🔬 Woman Scientist: Dark Skin Tone
👨‍💻 Man Technologist
👨🏻‍💻 Man Technologist: Light Skin Tone
👨🏼‍💻 Man Technologist: Medium-Light Skin Tone
👨🏽‍💻 Man Technologist: Medium Skin Tone
👨🏾‍💻 Man Technologist: Medium-Dark Skin Tone
👨🏿‍💻 Man Technologist: Dark Skin Tone
👩‍💻 Woman Technologist
👩🏻‍💻 Woman Technologist: Light Skin Tone
👩🏼‍💻 Woman Technologist: Medium-Light Skin Tone
👩🏽‍💻 Woman Technologist: Medium Skin Tone
👩🏾‍💻 Woman Technologist: Medium-Dark Skin Tone
👩🏿‍💻 Woman Technologist: Dark Skin Tone
👨‍🎤 Man Singer
👨🏻‍🎤 Man Singer: Light Skin Tone
👨🏼‍🎤 Man Singer: Medium-Light Skin Tone
👨🏽‍🎤 Man Singer: Medium Skin Tone
👨🏾‍🎤 Man Singer: Medium-Dark Skin Tone
👨🏿‍🎤 Man Singer: Dark Skin Tone
👩‍🎤 Woman Singer
👩🏻‍🎤 Woman Singer: Light Skin Tone
👩🏼‍🎤 Woman Singer: Medium-Light Skin Tone
👩🏽‍🎤 Woman Singer: Medium Skin Tone
👩🏾‍🎤 Woman Singer: Medium-Dark Skin Tone
👩🏿‍🎤 Woman Singer: Dark Skin Tone
👨‍🎨 Man Artist
👨🏻‍🎨 Man Artist: Light Skin Tone
👨🏼‍🎨 Man Artist: Medium-Light Skin Tone
👨🏽‍🎨 Man Artist: Medium Skin Tone
👨🏾‍🎨 Man Artist: Medium-Dark Skin Tone
👨🏿‍🎨 Man Artist: Dark Skin Tone
👩‍🎨 Woman Artist
👩🏻‍🎨 Woman Artist: Light Skin Tone
👩🏼‍🎨 Woman Artist: Medium-Light Skin Tone
👩🏽‍🎨 Woman Artist: Medium Skin Tone
👩🏾‍🎨 Woman Artist: Medium-Dark Skin Tone
👩🏿‍🎨 Woman Artist: Dark Skin Tone
👨‍✈️ Man Pilot
👨🏻‍✈️ Man Pilot: Light Skin Tone
👨🏼‍✈️ Man Pilot: Medium-Light Skin Tone
👨🏽‍✈️ Man Pilot: Medium Skin Tone
👨🏾‍✈️ Man Pilot: Medium-Dark Skin Tone
👨🏿‍✈️ Man Pilot: Dark Skin Tone
👩‍✈️ Woman Pilot
👩🏻‍✈️ Woman Pilot: Light Skin Tone
👩🏼‍✈️ Woman Pilot: Medium-Light Skin Tone
👩🏽‍✈️ Woman Pilot: Medium Skin Tone
👩🏾‍✈️ Woman Pilot: Medium-Dark Skin Tone
👩🏿‍✈️ Woman Pilot: Dark Skin Tone
👨‍🚀 Man Astronaut
👨🏻‍🚀 Man Astronaut: Light Skin Tone
👨🏼‍🚀 Man Astronaut: Medium-Light Skin Tone
👨🏽‍🚀 Man Astronaut: Medium Skin Tone
👨🏾‍🚀 Man Astronaut: Medium-Dark Skin Tone
👨🏿‍🚀 Man Astronaut: Dark Skin Tone
👩‍🚀 Woman Astronaut
👩🏻‍🚀 Woman Astronaut: Light Skin Tone
👩🏼‍🚀 Woman Astronaut: Medium-Light Skin Tone
👩🏽‍🚀 Woman Astronaut: Medium Skin Tone
👩🏾‍🚀 Woman Astronaut: Medium-Dark Skin Tone
👩🏿‍🚀 Woman Astronaut: Dark Skin Tone
👨‍🚒 Man Firefighter
👨🏻‍🚒 Man Firefighter: Light Skin Tone
👨🏼‍🚒 Man Firefighter: Medium-Light Skin Tone
👨🏽‍🚒 Man Firefighter: Medium Skin Tone
👨🏾‍🚒 Man Firefighter: Medium-Dark Skin Tone
👨🏿‍🚒 Man Firefighter: Dark Skin Tone
👩‍🚒 Woman Firefighter
👩🏻‍🚒 Woman Firefighter: Light Skin Tone
👩🏼‍🚒 Woman Firefighter: Medium-Light Skin Tone
👩🏽‍🚒 Woman Firefighter: Medium Skin Tone
👩🏾‍🚒 Woman Firefighter: Medium-Dark Skin Tone
👩🏿‍🚒 Woman Firefighter: Dark Skin Tone
👮 Police Officer
👮🏻 Police Officer: Light Skin Tone
👮🏼 Police Officer: Medium-Light Skin Tone
👮🏽 Police Officer: Medium Skin Tone
👮🏾 Police Officer: Medium-Dark Skin Tone
👮🏿 Police Officer: Dark Skin Tone
👮‍♂️ Man Police Officer
👮🏻‍♂️ Man Police Officer: Light Skin Tone
👮🏼‍♂️ Man Police Officer: Medium-Light Skin Tone
👮🏽‍♂️ Man Police Officer: Medium Skin Tone
👮🏾‍♂️ Man Police Officer: Medium-Dark Skin Tone
👮🏿‍♂️ Man Police Officer: Dark Skin Tone
👮‍♀️ Woman Police Officer
👮🏻‍♀️ Woman Police Officer: Light Skin Tone
👮🏼‍♀️ Woman Police Officer: Medium-Light Skin Tone
👮🏽‍♀️ Woman Police Officer: Medium Skin Tone
👮🏾‍♀️ Woman Police Officer: Medium-Dark Skin Tone
👮🏿‍♀️ Woman Police Officer: Dark Skin Tone
🕵️ Detective
🕵🏻 Detective: Light Skin Tone
🕵🏼 Detective: Medium-Light Skin Tone
🕵🏽 Detective: Medium Skin Tone
🕵🏾 Detective: Medium-Dark Skin Tone
🕵🏿 Detective: Dark Skin Tone
🕵️‍♂️ Man Detective
🕵🏻‍♂️ Man Detective: Light Skin Tone
🕵🏼‍♂️ Man Detective: Medium-Light Skin Tone
🕵🏽‍♂️ Man Detective: Medium Skin Tone
🕵🏾‍♂️ Man Detective: Medium-Dark Skin Tone
🕵🏿‍♂️ Man Detective: Dark Skin Tone
🕵️‍♀️ Woman Detective
🕵🏻‍♀️ Woman Detective: Light Skin Tone
🕵🏼‍♀️ Woman Detective: Medium-Light Skin Tone
🕵🏽‍♀️ Woman Detective: Medium Skin Tone
🕵🏾‍♀️ Woman Detective: Medium-Dark Skin Tone
🕵🏿‍♀️ Woman Detective: Dark Skin Tone
💂 Guard
💂🏻 Guard: Light Skin Tone
💂🏼 Guard: Medium-Light Skin Tone
💂🏽 Guard: Medium Skin Tone
💂🏾 Guard: Medium-Dark Skin Tone
💂🏿 Guard: Dark Skin Tone
💂‍♂️ Man Guard
💂🏻‍♂️ Man Guard: Light Skin Tone
💂🏼‍♂️ Man Guard: Medium-Light Skin Tone
💂🏽‍♂️ Man Guard: Medium Skin Tone
💂🏾‍♂️ Man Guard: Medium-Dark Skin Tone
💂🏿‍♂️ Man Guard: Dark Skin Tone
💂‍♀️ Woman Guard
💂🏻‍♀️ Woman Guard: Light Skin Tone
💂🏼‍♀️ Woman Guard: Medium-Light Skin Tone
💂🏽‍♀️ Woman Guard: Medium Skin Tone
💂🏾‍♀️ Woman Guard: Medium-Dark Skin Tone
💂🏿‍♀️ Woman Guard: Dark Skin Tone
👷 Construction Worker
👷🏻 Construction Worker: Light Skin Tone
👷🏼 Construction Worker: Medium-Light Skin Tone
👷🏽 Construction Worker: Medium Skin Tone
👷🏾 Construction Worker: Medium-Dark Skin Tone
👷🏿 Construction Worker: Dark Skin Tone
👷‍♂️ Man Construction Worker
👷🏻‍♂️ Man Construction Worker: Light Skin Tone
👷🏼‍♂️ Man Construction Worker: Medium-Light Skin Tone
👷🏽‍♂️ Man Construction Worker: Medium Skin Tone
👷🏾‍♂️ Man Construction Worker: Medium-Dark Skin Tone
👷🏿‍♂️ Man Construction Worker: Dark Skin Tone
👷‍♀️ Woman Construction Worker
👷🏻‍♀️ Woman Construction Worker: Light Skin Tone
👷🏼‍♀️ Woman Construction Worker: Medium-Light Skin Tone
👷🏽‍♀️ Woman Construction Worker: Medium Skin Tone
👷🏾‍♀️ Woman Construction Worker: Medium-Dark Skin Tone
👷🏿‍♀️ Woman Construction Worker: Dark Skin Tone
🤴 Prince
🤴🏻 Prince: Light Skin Tone
🤴🏼 Prince: Medium-Light Skin Tone
🤴🏽 Prince: Medium Skin Tone
🤴🏾 Prince: Medium-Dark Skin Tone
🤴🏿 Prince: Dark Skin Tone
👸 Princess
👸🏻 Princess: Light Skin Tone
👸🏼 Princess: Medium-Light Skin Tone
👸🏽 Princess: Medium Skin Tone
👸🏾 Princess: Medium-Dark Skin Tone
👸🏿 Princess: Dark Skin Tone
👳 Person Wearing Turban
👳🏻 Person Wearing Turban: Light Skin Tone
👳🏼 Person Wearing Turban: Medium-Light Skin Tone
👳🏽 Person Wearing Turban: Medium Skin Tone
👳🏾 Person Wearing Turban: Medium-Dark Skin Tone
👳🏿 Person Wearing Turban: Dark Skin Tone
👳‍♂️ Man Wearing Turban
👳🏻‍♂️ Man Wearing Turban: Light Skin Tone
👳🏼‍♂️ Man Wearing Turban: Medium-Light Skin Tone
👳🏽‍♂️ Man Wearing Turban: Medium Skin Tone
👳🏾‍♂️ Man Wearing Turban: Medium-Dark Skin Tone
👳🏿‍♂️ Man Wearing Turban: Dark Skin Tone
👳‍♀️ Woman Wearing Turban
👳🏻‍♀️ Woman Wearing Turban: Light Skin Tone
👳🏼‍♀️ Woman Wearing Turban: Medium-Light Skin Tone
👳🏽‍♀️ Woman Wearing Turban: Medium Skin Tone
👳🏾‍♀️ Woman Wearing Turban: Medium-Dark Skin Tone
👳🏿‍♀️ Woman Wearing Turban: Dark Skin Tone
👲 Man With Chinese Cap
👲🏻 Man With Chinese Cap: Light Skin Tone
👲🏼 Man With Chinese Cap: Medium-Light Skin Tone
👲🏽 Man With Chinese Cap: Medium Skin Tone
👲🏾 Man With Chinese Cap: Medium-Dark Skin Tone
👲🏿 Man With Chinese Cap: Dark Skin Tone
🧕 Woman With Headscarf
🧕🏻 Person With Headscarf: Light Skin Tone
🧕🏼 Person With Headscarf: Medium-Light Skin Tone
🧕🏽 Person With Headscarf: Medium Skin Tone
🧕🏾 Person With Headscarf: Medium-Dark Skin Tone
🧕🏿 Person With Headscarf: Dark Skin Tone
🧔 Bearded Person
🧔🏻 Bearded Person: Light Skin Tone
🧔🏼 Bearded Person: Medium-Light Skin Tone
🧔🏽 Bearded Person: Medium Skin Tone
🧔🏾 Bearded Person: Medium-Dark Skin Tone
🧔🏿 Bearded Person: Dark Skin Tone
👱 Blond-Haired Person
👱🏻 Blond-Haired Person: Light Skin Tone
👱🏼 Blond-Haired Person: Medium-Light Skin Tone
👱🏽 Blond-Haired Person: Medium Skin Tone
👱🏾 Blond-Haired Person: Medium-Dark Skin Tone
👱🏿 Blond-Haired Person: Dark Skin Tone
👱‍♂️ Blond-Haired Man
👱🏻‍♂️ Blond-Haired Man: Light Skin Tone
👱🏼‍♂️ Blond-Haired Man: Medium-Light Skin Tone
👱🏽‍♂️ Blond-Haired Man: Medium Skin Tone
👱🏾‍♂️ Blond-Haired Man: Medium-Dark Skin Tone
👱🏿‍♂️ Blond-Haired Man: Dark Skin Tone
👱‍♀️ Blond-Haired Woman
👱🏻‍♀️ Blond-Haired Woman: Light Skin Tone
👱🏼‍♀️ Blond-Haired Woman: Medium-Light Skin Tone
👱🏽‍♀️ Blond-Haired Woman: Medium Skin Tone
👱🏾‍♀️ Blond-Haired Woman: Medium-Dark Skin Tone
👱🏿‍♀️ Blond-Haired Woman: Dark Skin Tone
👨‍🦰 Man, Red Haired
👨🏻‍🦰 Man, Red Haired: Light Skin Tone
👨🏼‍🦰 Man, Red Haired: Medium-Light Skin Tone
👨🏽‍🦰 Man, Red Haired: Medium Skin Tone
👨🏾‍🦰 Man, Red Haired: Medium-Dark Skin Tone
👨🏿‍🦰 Man, Red Haired: Dark Skin Tone
👩‍🦰 Woman, Red Haired
👩🏻‍🦰 Woman, Red Haired: Light Skin Tone
👩🏼‍🦰 Woman, Red Haired: Medium-Light Skin Tone
👩🏽‍🦰 Woman, Red Haired: Medium Skin Tone
👩🏾‍🦰 Woman, Red Haired: Medium-Dark Skin Tone
👩🏿‍🦰 Woman, Red Haired: Dark Skin Tone
👨‍🦱 Man, Curly Haired
👨🏻‍🦱 Man, Curly Haired: Light Skin Tone
👨🏼‍🦱 Man, Curly Haired: Medium-Light Skin Tone
👨🏽‍🦱 Man, Curly Haired: Medium Skin Tone
👨🏾‍🦱 Man, Curly Haired: Medium-Dark Skin Tone
👨🏿‍🦱 Man, Curly Haired: Dark Skin Tone
👩‍🦱 Woman, Curly Haired
👩🏻‍🦱 Woman, Curly Haired: Light Skin Tone
👩🏼‍🦱 Woman, Curly Haired: Medium-Light Skin Tone
👩🏽‍🦱 Woman, Curly Haired: Medium Skin Tone
👩🏾‍🦱 Woman, Curly Haired: Medium-Dark Skin Tone
👩🏿‍🦱 Woman, Curly Haired: Dark Skin Tone
👨‍🦲 Man, Bald
👨🏻‍🦲 Man, Bald: Light Skin Tone
👨🏼‍🦲 Man, Bald: Medium-Light Skin Tone
👨🏽‍🦲 Man, Bald: Medium Skin Tone
👨🏾‍🦲 Man, Bald: Medium-Dark Skin Tone
👨🏿‍🦲 Man, Bald: Dark Skin Tone
👩‍🦲 Woman, Bald
👩🏻‍🦲 Woman, Bald: Light Skin Tone
👩🏼‍🦲 Woman, Bald: Medium-Light Skin Tone
👩🏽‍🦲 Woman, Bald: Medium Skin Tone
👩🏾‍🦲 Woman, Bald: Medium-Dark Skin Tone
👩🏿‍🦲 Woman, Bald: Dark Skin Tone
👨‍🦳 Man, White Haired
👨🏻‍🦳 Man, White Haired: Light Skin Tone
👨🏼‍🦳 Man, White Haired: Medium-Light Skin Tone
👨🏽‍🦳 Man, White Haired: Medium Skin Tone
👨🏾‍🦳 Man, White Haired: Medium-Dark Skin Tone
👨🏿‍🦳 Man, White Haired: Dark Skin Tone
👩‍🦳 Woman, White Haired
👩🏻‍🦳 Woman, White Haired: Light Skin Tone
👩🏼‍🦳 Woman, White Haired: Medium-Light Skin Tone
👩🏽‍🦳 Woman, White Haired: Medium Skin Tone
👩🏾‍🦳 Woman, White Haired: Medium-Dark Skin Tone
👩🏿‍🦳 Woman, White Haired: Dark Skin Tone
🤵 Man in Tuxedo
🤵🏻 Man in Tuxedo: Light Skin Tone
🤵🏼 Man in Tuxedo: Medium-Light Skin Tone
🤵🏽 Man in Tuxedo: Medium Skin Tone
🤵🏾 Man in Tuxedo: Medium-Dark Skin Tone
🤵🏿 Man in Tuxedo: Dark Skin Tone
👰 Bride With Veil
👰🏻 Bride With Veil: Light Skin Tone
👰🏼 Bride With Veil: Medium-Light Skin Tone
👰🏽 Bride With Veil: Medium Skin Tone
👰🏾 Bride With Veil: Medium-Dark Skin Tone
👰🏿 Bride With Veil: Dark Skin Tone
🤰 Pregnant Woman
🤰🏻 Pregnant Woman: Light Skin Tone
🤰🏼 Pregnant Woman: Medium-Light Skin Tone
🤰🏽 Pregnant Woman: Medium Skin Tone
🤰🏾 Pregnant Woman: Medium-Dark Skin Tone
🤰🏿 Pregnant Woman: Dark Skin Tone
🤱 Breast-Feeding
🤱🏻 Breast-Feeding: Light Skin Tone
🤱🏼 Breast-Feeding: Medium-Light Skin Tone
🤱🏽 Breast-Feeding: Medium Skin Tone
🤱🏾 Breast-Feeding: Medium-Dark Skin Tone
🤱🏿 Breast-Feeding: Dark Skin Tone
👼 Baby Angel
👼🏻 Baby Angel: Light Skin Tone
👼🏼 Baby Angel: Medium-Light Skin Tone
👼🏽 Baby Angel: Medium Skin Tone
👼🏾 Baby Angel: Medium-Dark Skin Tone
👼🏿 Baby Angel: Dark Skin Tone
🎅 Santa Claus
🎅🏻 Santa Claus: Light Skin Tone
🎅🏼 Santa Claus: Medium-Light Skin Tone
🎅🏽 Santa Claus: Medium Skin Tone
🎅🏾 Santa Claus: Medium-Dark Skin Tone
🎅🏿 Santa Claus: Dark Skin Tone
🤶 Mrs. Claus
🤶🏻 Mrs. Claus: Light Skin Tone
🤶🏼 Mrs. Claus: Medium-Light Skin Tone
🤶🏽 Mrs. Claus: Medium Skin Tone
🤶🏾 Mrs. Claus: Medium-Dark Skin Tone
🤶🏿 Mrs. Claus: Dark Skin Tone
🦸 Superhero
🦸🏻 Superhero: Light Skin Tone
🦸🏼 Superhero: Medium-Light Skin Tone
🦸🏽 Superhero: Medium Skin Tone
🦸🏾 Superhero: Medium-Dark Skin Tone
🦸🏿 Superhero: Dark Skin Tone
🦸‍♀️ Woman Superhero
🦸🏻‍♀️ Woman Superhero: Light Skin Tone
🦸🏼‍♀️ Woman Superhero: Medium-Light Skin Tone
🦸🏽‍♀️ Woman Superhero: Medium Skin Tone
🦸🏾‍♀️ Woman Superhero: Medium-Dark Skin Tone
🦸🏿‍♀️ Woman Superhero: Dark Skin Tone
🦸‍♂️ Man Superhero
🦸🏻‍♂️ Man Superhero: Light Skin Tone
🦸🏼‍♂️ Man Superhero: Medium-Light Skin Tone
🦸🏽‍♂️ Man Superhero: Medium Skin Tone
🦸🏾‍♂️ Man Superhero: Medium-Dark Skin Tone
👯🏻 Woman With Bunny Ears, Type-1-2
🦸🏿‍♂️ Man Superhero: Dark Skin Tone
👯🏼 Woman With Bunny Ears, Type-3
👯🏽 Woman With Bunny Ears, Type-4
🦹 Supervillain
👯🏾 Woman With Bunny Ears, Type-5
👯🏿 Woman With Bunny Ears, Type-6
🦹🏻 Supervillain: Light Skin Tone
🦹🏼 Supervillain: Medium-Light Skin Tone
👯🏻‍♂️ Men With Bunny Ears Partying, Type-1-2
🦹🏽 Supervillain: Medium Skin Tone
👯🏼‍♂️ Men With Bunny Ears Partying, Type-3
🦹🏾 Supervillain: Medium-Dark Skin Tone
👯🏽‍♂️ Men With Bunny Ears Partying, Type-4
🦹🏿 Supervillain: Dark Skin Tone
👯🏾‍♂️ Men With Bunny Ears Partying, Type-5
🦹‍♀️ Woman Supervillain
👯🏿‍♂️ Men With Bunny Ears Partying, Type-6
🦹🏻‍♀️ Woman Supervillain: Light Skin Tone
👯🏻‍♀️ Women With Bunny Ears Partying, Type-1-2
👯🏼‍♀️ Women With Bunny Ears Partying, Type-3
🦹🏼‍♀️ Woman Supervillain: Medium-Light Skin Tone
👯🏽‍♀️ Women With Bunny Ears Partying, Type-4
🦹🏽‍♀️ Woman Supervillain: Medium Skin Tone
👯🏾‍♀️ Women With Bunny Ears Partying, Type-5
👯🏿‍♀️ Women With Bunny Ears Partying, Type-6
🦹🏾‍♀️ Woman Supervillain: Medium-Dark Skin Tone
🦹🏿‍♀️ Woman Supervillain: Dark Skin Tone
🦹‍♂️ Man Supervillain
🦹🏻‍♂️ Man Supervillain: Light Skin Tone
🦹🏼‍♂️ Man Supervillain: Medium-Light Skin Tone
🦹🏽‍♂️ Man Supervillain: Medium Skin Tone
👫🏻 Man and Woman Holding Hands, Type-1-2
👫🏼 Man and Woman Holding Hands, Type-3
🦹🏾‍♂️ Man Supervillain: Medium-Dark Skin Tone
👫🏽 Man and Woman Holding Hands, Type-4
👫🏾 Man and Woman Holding Hands, Type-5
🦹🏿‍♂️ Man Supervillain: Dark Skin Tone
👫🏿 Man and Woman Holding Hands, Type-6
🧙 Mage
👬🏻 Two Men Holding Hands, Type-1-2
👬🏼 Two Men Holding Hands, Type-3
🧙🏻 Mage: Light Skin Tone
👬🏽 Two Men Holding Hands, Type-4
🧙🏼 Mage: Medium-Light Skin Tone
👬🏾 Two Men Holding Hands, Type-5
🧙🏽 Mage: Medium Skin Tone
👬🏿 Two Men Holding Hands, Type-6
🧙🏾 Mage: Medium-Dark Skin Tone
🧙🏿 Mage: Dark Skin Tone
🧙‍♀️ Woman Mage
👭🏻 Two Women Holding Hands, Type-1-2
👭🏼 Two Women Holding Hands, Type-3
🧙🏻‍♀️ Woman Mage: Light Skin Tone
👭🏽 Two Women Holding Hands, Type-4
👭🏾 Two Women Holding Hands, Type-5
🧙🏼‍♀️ Woman Mage: Medium-Light Skin Tone
👭🏿 Two Women Holding Hands, Type-6
🧙🏽‍♀️ Woman Mage: Medium Skin Tone
🧙🏾‍♀️ Woman Mage: Medium-Dark Skin Tone
🧙🏿‍♀️ Woman Mage: Dark Skin Tone
🧙‍♂️ Man Mage
🧙🏻‍♂️ Man Mage: Light Skin Tone
👪🏻 Family, Type-1-2
👪🏼 Family, Type-3
🧙🏼‍♂️ Man Mage: Medium-Light Skin Tone
👪🏽 Family, Type-4
👪🏾 Family, Type-5
🧙🏽‍♂️ Man Mage: Medium Skin Tone
👪🏿 Family, Type-6
🧙🏾‍♂️ Man Mage: Medium-Dark Skin Tone
🧙🏿‍♂️ Man Mage: Dark Skin Tone
🧚 Fairy
🧚🏻 Fairy: Light Skin Tone
🧚🏼 Fairy: Medium-Light Skin Tone
🧚🏽 Fairy: Medium Skin Tone
🧚🏾 Fairy: Medium-Dark Skin Tone
🧚🏿 Fairy: Dark Skin Tone
🧚‍♀️ Woman Fairy
🧚🏻‍♀️ Woman Fairy: Light Skin Tone
🧚🏼‍♀️ Woman Fairy: Medium-Light Skin Tone
🧚🏽‍♀️ Woman Fairy: Medium Skin Tone
🧚🏾‍♀️ Woman Fairy: Medium-Dark Skin Tone
🧚🏿‍♀️ Woman Fairy: Dark Skin Tone
🧚‍♂️ Man Fairy
🧚🏻‍♂️ Man Fairy: Light Skin Tone
🧚🏼‍♂️ Man Fairy: Medium-Light Skin Tone
🧚🏽‍♂️ Man Fairy: Medium Skin Tone
🧚🏾‍♂️ Man Fairy: Medium-Dark Skin Tone
🧚🏿‍♂️ Man Fairy: Dark Skin Tone
🧛 Vampire
🧛🏻 Vampire: Light Skin Tone
🧛🏼 Vampire: Medium-Light Skin Tone
🧛🏽 Vampire: Medium Skin Tone
🧛🏾 Vampire: Medium-Dark Skin Tone
🧛🏿 Vampire: Dark Skin Tone
🧛‍♀️ Woman Vampire
🧛🏻‍♀️ Woman Vampire: Light Skin Tone
🧛🏼‍♀️ Woman Vampire: Medium-Light Skin Tone
🧛🏽‍♀️ Woman Vampire: Medium Skin Tone
🧛🏾‍♀️ Woman Vampire: Medium-Dark Skin Tone
🧛🏿‍♀️ Woman Vampire: Dark Skin Tone
🧛‍♂️ Man Vampire
🧛🏻‍♂️ Man Vampire: Light Skin Tone
🧛🏼‍♂️ Man Vampire: Medium-Light Skin Tone
🧛🏽‍♂️ Man Vampire: Medium Skin Tone
🧛🏾‍♂️ Man Vampire: Medium-Dark Skin Tone
🧛🏿‍♂️ Man Vampire: Dark Skin Tone
🧜 Merperson
🧜🏻 Merperson: Light Skin Tone
🧜🏼 Merperson: Medium-Light Skin Tone
🧜🏽 Merperson: Medium Skin Tone
🧜🏾 Merperson: Medium-Dark Skin Tone
🧜🏿 Merperson: Dark Skin Tone
🧜‍♀️ Mermaid
🧜🏻‍♀️ Mermaid: Light Skin Tone
🧜🏼‍♀️ Mermaid: Medium-Light Skin Tone
🧜🏽‍♀️ Mermaid: Medium Skin Tone
🧜🏾‍♀️ Mermaid: Medium-Dark Skin Tone
🧜🏿‍♀️ Mermaid: Dark Skin Tone
🧜‍♂️ Merman
🧜🏻‍♂️ Merman: Light Skin Tone
🧜🏼‍♂️ Merman: Medium-Light Skin Tone
🧜🏽‍♂️ Merman: Medium Skin Tone
🧜🏾‍♂️ Merman: Medium-Dark Skin Tone
🧜🏿‍♂️ Merman: Dark Skin Tone
🧝 Elf
🧝🏻 Elf: Light Skin Tone
🧝🏼 Elf: Medium-Light Skin Tone
🧝🏽 Elf: Medium Skin Tone
🧝🏾 Elf: Medium-Dark Skin Tone
🧝🏿 Elf: Dark Skin Tone
🧝‍♀️ Woman Elf
🧝🏻‍♀️ Woman Elf: Light Skin Tone
🧝🏼‍♀️ Woman Elf: Medium-Light Skin Tone
🧝🏽‍♀️ Woman Elf: Medium Skin Tone
🧝🏾‍♀️ Woman Elf: Medium-Dark Skin Tone
🧝🏿‍♀️ Woman Elf: Dark Skin Tone
🧝‍♂️ Man Elf
🧝🏻‍♂️ Man Elf: Light Skin Tone
🧝🏼‍♂️ Man Elf: Medium-Light Skin Tone
🧝🏽‍♂️ Man Elf: Medium Skin Tone
🧝🏾‍♂️ Man Elf: Medium-Dark Skin Tone
🧝🏿‍♂️ Man Elf: Dark Skin Tone
🧞 Genie
🧞‍♀️ Woman Genie
🧞‍♂️ Man Genie
🧟 Zombie
🧟🏻 Zombie: Light Skin Tone
🧟🏼 Zombie: Medium-Light Skin Tone
🧟🏽 Zombie: Medium Skin Tone
🧟🏾 Zombie: Medium-Dark Skin Tone
🧟🏿 Zombie: Dark Skin Tone
🧟‍♀️ Woman Zombie
🧟‍♂️ Man Zombie
🙍 Person Frowning
🙍🏻 Person Frowning: Light Skin Tone
🙍🏼 Person Frowning: Medium-Light Skin Tone
🙍🏽 Person Frowning: Medium Skin Tone
🙍🏾 Person Frowning: Medium-Dark Skin Tone
🙍🏿 Person Frowning: Dark Skin Tone
🙍‍♂️ Man Frowning
🙍🏻‍♂️ Man Frowning: Light Skin Tone
🙍🏼‍♂️ Man Frowning: Medium-Light Skin Tone
🙍🏽‍♂️ Man Frowning: Medium Skin Tone
🙍🏾‍♂️ Man Frowning: Medium-Dark Skin Tone
🙍🏿‍♂️ Man Frowning: Dark Skin Tone
🙍‍♀️ Woman Frowning
🙍🏻‍♀️ Woman Frowning: Light Skin Tone
🙍🏼‍♀️ Woman Frowning: Medium-Light Skin Tone
🙍🏽‍♀️ Woman Frowning: Medium Skin Tone
🙍🏾‍♀️ Woman Frowning: Medium-Dark Skin Tone
🙍🏿‍♀️ Woman Frowning: Dark Skin Tone
🙎 Person Pouting
🙎🏻 Person Pouting: Light Skin Tone
🙎🏼 Person Pouting: Medium-Light Skin Tone
🙎🏽 Person Pouting: Medium Skin Tone
🙎🏾 Person Pouting: Medium-Dark Skin Tone
🙎🏿 Person Pouting: Dark Skin Tone
🙎‍♂️ Man Pouting
🙎🏻‍♂️ Man Pouting: Light Skin Tone
🙎🏼‍♂️ Man Pouting: Medium-Light Skin Tone
🙎🏽‍♂️ Man Pouting: Medium Skin Tone
🙎🏾‍♂️ Man Pouting: Medium-Dark Skin Tone
🙎🏿‍♂️ Man Pouting: Dark Skin Tone
🙎‍♀️ Woman Pouting
🙎🏻‍♀️ Woman Pouting: Light Skin Tone
🙎🏼‍♀️ Woman Pouting: Medium-Light Skin Tone
🙎🏽‍♀️ Woman Pouting: Medium Skin Tone
🙎🏾‍♀️ Woman Pouting: Medium-Dark Skin Tone
🙎🏿‍♀️ Woman Pouting: Dark Skin Tone
🙅 Person Gesturing No
🙅🏻 Person Gesturing No: Light Skin Tone
🙅🏼 Person Gesturing No: Medium-Light Skin Tone
🙅🏽 Person Gesturing No: Medium Skin Tone
🙅🏾 Person Gesturing No: Medium-Dark Skin Tone
🙅🏿 Person Gesturing No: Dark Skin Tone
🙅‍♂️ Man Gesturing No
🙅🏻‍♂️ Man Gesturing No: Light Skin Tone
🙅🏼‍♂️ Man Gesturing No: Medium-Light Skin Tone
🤝🏻 Handshake, Type-1-2
🤝🏼 Handshake, Type-3
🙅🏽‍♂️ Man Gesturing No: Medium Skin Tone
🤝🏽 Handshake, Type-4
🤝🏾 Handshake, Type-5
🙅🏾‍♂️ Man Gesturing No: Medium-Dark Skin Tone
🤝🏿 Handshake, Type-6
🙅🏿‍♂️ Man Gesturing No: Dark Skin Tone
🙅‍♀️ Woman Gesturing No
🙅🏻‍♀️ Woman Gesturing No: Light Skin Tone
🙅🏼‍♀️ Woman Gesturing No: Medium-Light Skin Tone
🙅🏽‍♀️ Woman Gesturing No: Medium Skin Tone
🙅🏾‍♀️ Woman Gesturing No: Medium-Dark Skin Tone
🙅🏿‍♀️ Woman Gesturing No: Dark Skin Tone
🙆 Person Gesturing OK
🙆🏻 Person Gesturing OK: Light Skin Tone
🙆🏼 Person Gesturing OK: Medium-Light Skin Tone
🙆🏽 Person Gesturing OK: Medium Skin Tone
🙆🏾 Person Gesturing OK: Medium-Dark Skin Tone
🙆🏿 Person Gesturing OK: Dark Skin Tone
🙆‍♂️ Man Gesturing OK
🙆🏻‍♂️ Man Gesturing OK: Light Skin Tone
🙆🏼‍♂️ Man Gesturing OK: Medium-Light Skin Tone
🙆🏽‍♂️ Man Gesturing OK: Medium Skin Tone
🙆🏾‍♂️ Man Gesturing OK: Medium-Dark Skin Tone
🙆🏿‍♂️ Man Gesturing OK: Dark Skin Tone
🙆‍♀️ Woman Gesturing OK
🙆🏻‍♀️ Woman Gesturing OK: Light Skin Tone
🙆🏼‍♀️ Woman Gesturing OK: Medium-Light Skin Tone
🙆🏽‍♀️ Woman Gesturing OK: Medium Skin Tone
🙆🏾‍♀️ Woman Gesturing OK: Medium-Dark Skin Tone
🙆🏿‍♀️ Woman Gesturing OK: Dark Skin Tone
💁 Person Tipping Hand
💁🏻 Person Tipping Hand: Light Skin Tone
💁🏼 Person Tipping Hand: Medium-Light Skin Tone
💁🏽 Person Tipping Hand: Medium Skin Tone
💁🏾 Person Tipping Hand: Medium-Dark Skin Tone
💁🏿 Person Tipping Hand: Dark Skin Tone
💁‍♂️ Man Tipping Hand
💁🏻‍♂️ Man Tipping Hand: Light Skin Tone
💁🏼‍♂️ Man Tipping Hand: Medium-Light Skin Tone
💁🏽‍♂️ Man Tipping Hand: Medium Skin Tone
💁🏾‍♂️ Man Tipping Hand: Medium-Dark Skin Tone
💁🏿‍♂️ Man Tipping Hand: Dark Skin Tone
💁‍♀️ Woman Tipping Hand
💁🏻‍♀️ Woman Tipping Hand: Light Skin Tone
💁🏼‍♀️ Woman Tipping Hand: Medium-Light Skin Tone
💁🏽‍♀️ Woman Tipping Hand: Medium Skin Tone
💁🏾‍♀️ Woman Tipping Hand: Medium-Dark Skin Tone
💁🏿‍♀️ Woman Tipping Hand: Dark Skin Tone
🙋 Person Raising Hand
🙋🏻 Person Raising Hand: Light Skin Tone
🙋🏼 Person Raising Hand: Medium-Light Skin Tone
🙋🏽 Person Raising Hand: Medium Skin Tone
🙋🏾 Person Raising Hand: Medium-Dark Skin Tone
🙋🏿 Person Raising Hand: Dark Skin Tone
🙋‍♂️ Man Raising Hand
🙋🏻‍♂️ Man Raising Hand: Light Skin Tone
🙋🏼‍♂️ Man Raising Hand: Medium-Light Skin Tone
🙋🏽‍♂️ Man Raising Hand: Medium Skin Tone
🙋🏾‍♂️ Man Raising Hand: Medium-Dark Skin Tone
🙋🏿‍♂️ Man Raising Hand: Dark Skin Tone
🙋‍♀️ Woman Raising Hand
🙋🏻‍♀️ Woman Raising Hand: Light Skin Tone
🙋🏼‍♀️ Woman Raising Hand: Medium-Light Skin Tone
🙋🏽‍♀️ Woman Raising Hand: Medium Skin Tone
🙋🏾‍♀️ Woman Raising Hand: Medium-Dark Skin Tone
🙋🏿‍♀️ Woman Raising Hand: Dark Skin Tone
🙇 Person Bowing
🙇🏻 Person Bowing: Light Skin Tone
🙇🏼 Person Bowing: Medium-Light Skin Tone
🙇🏽 Person Bowing: Medium Skin Tone
🙇🏾 Person Bowing: Medium-Dark Skin Tone
🙇🏿 Person Bowing: Dark Skin Tone
🙇‍♂️ Man Bowing
🙇🏻‍♂️ Man Bowing: Light Skin Tone
🙇🏼‍♂️ Man Bowing: Medium-Light Skin Tone
🙇🏽‍♂️ Man Bowing: Medium Skin Tone
🙇🏾‍♂️ Man Bowing: Medium-Dark Skin Tone
🙇🏿‍♂️ Man Bowing: Dark Skin Tone
🙇‍♀️ Woman Bowing
🙇🏻‍♀️ Woman Bowing: Light Skin Tone
🙇🏼‍♀️ Woman Bowing: Medium-Light Skin Tone
🙇🏽‍♀️ Woman Bowing: Medium Skin Tone
🙇🏾‍♀️ Woman Bowing: Medium-Dark Skin Tone
🙇🏿‍♀️ Woman Bowing: Dark Skin Tone
🤦 Person Facepalming
🤦🏻 Person Facepalming: Light Skin Tone
🤦🏼 Person Facepalming: Medium-Light Skin Tone
🤦🏽 Person Facepalming: Medium Skin Tone
🤦🏾 Person Facepalming: Medium-Dark Skin Tone
🤦🏿 Person Facepalming: Dark Skin Tone
🤦‍♂️ Man Facepalming
🤦🏻‍♂️ Man Facepalming: Light Skin Tone
🤦🏼‍♂️ Man Facepalming: Medium-Light Skin Tone
🤦🏽‍♂️ Man Facepalming: Medium Skin Tone
🤦🏾‍♂️ Man Facepalming: Medium-Dark Skin Tone
🤦🏿‍♂️ Man Facepalming: Dark Skin Tone
🤦‍♀️ Woman Facepalming
🤦🏻‍♀️ Woman Facepalming: Light Skin Tone
🤦🏼‍♀️ Woman Facepalming: Medium-Light Skin Tone
🤦🏽‍♀️ Woman Facepalming: Medium Skin Tone
🤦🏾‍♀️ Woman Facepalming: Medium-Dark Skin Tone
🤦🏿‍♀️ Woman Facepalming: Dark Skin Tone
🤷 Person Shrugging
🤷🏻 Person Shrugging: Light Skin Tone
🤷🏼 Person Shrugging: Medium-Light Skin Tone
🤷🏽 Person Shrugging: Medium Skin Tone
🤷🏾 Person Shrugging: Medium-Dark Skin Tone
🤷🏿 Person Shrugging: Dark Skin Tone
🤷‍♂️ Man Shrugging
🤷🏻‍♂️ Man Shrugging: Light Skin Tone
🤷🏼‍♂️ Man Shrugging: Medium-Light Skin Tone
🤷🏽‍♂️ Man Shrugging: Medium Skin Tone
🤷🏾‍♂️ Man Shrugging: Medium-Dark Skin Tone
🤷🏿‍♂️ Man Shrugging: Dark Skin Tone
🤷‍♀️ Woman Shrugging
🤷🏻‍♀️ Woman Shrugging: Light Skin Tone
🤷🏼‍♀️ Woman Shrugging: Medium-Light Skin Tone
🤷🏽‍♀️ Woman Shrugging: Medium Skin Tone
🤷🏾‍♀️ Woman Shrugging: Medium-Dark Skin Tone
🤷🏿‍♀️ Woman Shrugging: Dark Skin Tone
💆 Person Getting Massage
💆🏻 Person Getting Massage: Light Skin Tone
💆🏼 Person Getting Massage: Medium-Light Skin Tone
💆🏽 Person Getting Massage: Medium Skin Tone
💆🏾 Person Getting Massage: Medium-Dark Skin Tone
💆🏿 Person Getting Massage: Dark Skin Tone
💆‍♂️ Man Getting Massage
💆🏻‍♂️ Man Getting Massage: Light Skin Tone
💆🏼‍♂️ Man Getting Massage: Medium-Light Skin Tone
💆🏽‍♂️ Man Getting Massage: Medium Skin Tone
💆🏾‍♂️ Man Getting Massage: Medium-Dark Skin Tone
💆🏿‍♂️ Man Getting Massage: Dark Skin Tone
💆‍♀️ Woman Getting Massage
💆🏻‍♀️ Woman Getting Massage: Light Skin Tone
💆🏼‍♀️ Woman Getting Massage: Medium-Light Skin Tone
💆🏽‍♀️ Woman Getting Massage: Medium Skin Tone
💆🏾‍♀️ Woman Getting Massage: Medium-Dark Skin Tone
💆🏿‍♀️ Woman Getting Massage: Dark Skin Tone
💇 Person Getting Haircut
💇🏻 Person Getting Haircut: Light Skin Tone
💇🏼 Person Getting Haircut: Medium-Light Skin Tone
💇🏽 Person Getting Haircut: Medium Skin Tone
💇🏾 Person Getting Haircut: Medium-Dark Skin Tone
💇🏿 Person Getting Haircut: Dark Skin Tone
💇‍♂️ Man Getting Haircut
💇🏻‍♂️ Man Getting Haircut: Light Skin Tone
💇🏼‍♂️ Man Getting Haircut: Medium-Light Skin Tone
💇🏽‍♂️ Man Getting Haircut: Medium Skin Tone
💇🏾‍♂️ Man Getting Haircut: Medium-Dark Skin Tone
💇🏿‍♂️ Man Getting Haircut: Dark Skin Tone
💇‍♀️ Woman Getting Haircut
💇🏻‍♀️ Woman Getting Haircut: Light Skin Tone
💇🏼‍♀️ Woman Getting Haircut: Medium-Light Skin Tone
💇🏽‍♀️ Woman Getting Haircut: Medium Skin Tone
💇🏾‍♀️ Woman Getting Haircut: Medium-Dark Skin Tone
💇🏿‍♀️ Woman Getting Haircut: Dark Skin Tone
🚶 Person Walking
🚶🏻 Person Walking: Light Skin Tone
🚶🏼 Person Walking: Medium-Light Skin Tone
🚶🏽 Person Walking: Medium Skin Tone
🚶🏾 Person Walking: Medium-Dark Skin Tone
🚶🏿 Person Walking: Dark Skin Tone
🚶‍♂️ Man Walking
🚶🏻‍♂️ Man Walking: Light Skin Tone
🚶🏼‍♂️ Man Walking: Medium-Light Skin Tone
🚶🏽‍♂️ Man Walking: Medium Skin Tone
🚶🏾‍♂️ Man Walking: Medium-Dark Skin Tone
🚶🏿‍♂️ Man Walking: Dark Skin Tone
🚶‍♀️ Woman Walking
🚶🏻‍♀️ Woman Walking: Light Skin Tone
🚶🏼‍♀️ Woman Walking: Medium-Light Skin Tone
🚶🏽‍♀️ Woman Walking: Medium Skin Tone
🚶🏾‍♀️ Woman Walking: Medium-Dark Skin Tone
🚶🏿‍♀️ Woman Walking: Dark Skin Tone
🏃 Person Running
🏃🏻 Person Running: Light Skin Tone
🏃🏼 Person Running: Medium-Light Skin Tone
🏃🏽 Person Running: Medium Skin Tone
🏃🏾 Person Running: Medium-Dark Skin Tone
🏃🏿 Person Running: Dark Skin Tone
🏃‍♂️ Man Running
🏃🏻‍♂️ Man Running: Light Skin Tone
🏃🏼‍♂️ Man Running: Medium-Light Skin Tone
🏃🏽‍♂️ Man Running: Medium Skin Tone
🏃🏾‍♂️ Man Running: Medium-Dark Skin Tone
🏃🏿‍♂️ Man Running: Dark Skin Tone
🏃‍♀️ Woman Running
🏃🏻‍♀️ Woman Running: Light Skin Tone
🏃🏼‍♀️ Woman Running: Medium-Light Skin Tone
🏃🏽‍♀️ Woman Running: Medium Skin Tone
🏃🏾‍♀️ Woman Running: Medium-Dark Skin Tone
🏃🏿‍♀️ Woman Running: Dark Skin Tone
💃 Woman Dancing
💃🏻 Woman Dancing: Light Skin Tone
💃🏼 Woman Dancing: Medium-Light Skin Tone
💃🏽 Woman Dancing: Medium Skin Tone
💃🏾 Woman Dancing: Medium-Dark Skin Tone
💃🏿 Woman Dancing: Dark Skin Tone
🕺 Man Dancing
🕺🏻 Man Dancing: Light Skin Tone
🕺🏼 Man Dancing: Medium-Light Skin Tone
🕺🏽 Man Dancing: Medium Skin Tone
🕺🏾 Man Dancing: Medium-Dark Skin Tone
🕺🏿 Man Dancing: Dark Skin Tone
👯 People With Bunny Ears
👯‍♂️ Men With Bunny Ears
👯‍♀️ Women With Bunny Ears
🧖 Person in Steamy Room
🧖🏻 Person in Steamy Room: Light Skin Tone
🧖🏼 Person in Steamy Room: Medium-Light Skin Tone
🧖🏽 Person in Steamy Room: Medium Skin Tone
🧖🏾 Person in Steamy Room: Medium-Dark Skin Tone
🧖🏿 Person in Steamy Room: Dark Skin Tone
🧖‍♀️ Woman in Steamy Room
🧖🏻‍♀️ Woman in Steamy Room: Light Skin Tone
🧖🏼‍♀️ Woman in Steamy Room: Medium-Light Skin Tone
🧖🏽‍♀️ Woman in Steamy Room: Medium Skin Tone
🧖🏾‍♀️ Woman in Steamy Room: Medium-Dark Skin Tone
🧖🏿‍♀️ Woman in Steamy Room: Dark Skin Tone
🧖‍♂️ Man in Steamy Room
🧖🏻‍♂️ Man in Steamy Room: Light Skin Tone
🧖🏼‍♂️ Man in Steamy Room: Medium-Light Skin Tone
🧖🏽‍♂️ Man in Steamy Room: Medium Skin Tone
🧖🏾‍♂️ Man in Steamy Room: Medium-Dark Skin Tone
🧖🏿‍♂️ Man in Steamy Room: Dark Skin Tone
🧗 Person Climbing
🧗🏻 Person Climbing: Light Skin Tone
🧗🏼 Person Climbing: Medium-Light Skin Tone
🧗🏽 Person Climbing: Medium Skin Tone
🧗🏾 Person Climbing: Medium-Dark Skin Tone
🧗🏿 Person Climbing: Dark Skin Tone
🧗‍♀️ Woman Climbing
🧗🏻‍♀️ Woman Climbing: Light Skin Tone
🧗🏼‍♀️ Woman Climbing: Medium-Light Skin Tone
🧗🏽‍♀️ Woman Climbing: Medium Skin Tone
🧗🏾‍♀️ Woman Climbing: Medium-Dark Skin Tone
🧗🏿‍♀️ Woman Climbing: Dark Skin Tone
🧗‍♂️ Man Climbing
🧗🏻‍♂️ Man Climbing: Light Skin Tone
🧗🏼‍♂️ Man Climbing: Medium-Light Skin Tone
🧗🏽‍♂️ Man Climbing: Medium Skin Tone
🧗🏾‍♂️ Man Climbing: Medium-Dark Skin Tone
🧗🏿‍♂️ Man Climbing: Dark Skin Tone
🧘 Person in Lotus Position
🧘🏻 Person in Lotus Position: Light Skin Tone
🧘🏼 Person in Lotus Position: Medium-Light Skin Tone
🧘🏽 Person in Lotus Position: Medium Skin Tone
🧘🏾 Person in Lotus Position: Medium-Dark Skin Tone
🧘🏿 Person in Lotus Position: Dark Skin Tone
🧘‍♀️ Woman in Lotus Position
🧘🏻‍♀️ Woman in Lotus Position: Light Skin Tone
🧘🏼‍♀️ Woman in Lotus Position: Medium-Light Skin Tone
🧘🏽‍♀️ Woman in Lotus Position: Medium Skin Tone
🧘🏾‍♀️ Woman in Lotus Position: Medium-Dark Skin Tone
🧘🏿‍♀️ Woman in Lotus Position: Dark Skin Tone
🧘‍♂️ Man in Lotus Position
🧘🏻‍♂️ Man in Lotus Position: Light Skin Tone
🧘🏼‍♂️ Man in Lotus Position: Medium-Light Skin Tone
🧘🏽‍♂️ Man in Lotus Position: Medium Skin Tone
🧘🏾‍♂️ Man in Lotus Position: Medium-Dark Skin Tone
🧘🏿‍♂️ Man in Lotus Position: Dark Skin Tone
🛀 Person Taking Bath
🛀🏻 Person Taking Bath: Light Skin Tone
🛀🏼 Person Taking Bath: Medium-Light Skin Tone
🛀🏽 Person Taking Bath: Medium Skin Tone
🛀🏾 Person Taking Bath: Medium-Dark Skin Tone
🛀🏿 Person Taking Bath: Dark Skin Tone
🛌 Person in Bed
🛌🏻 Person in Bed: Light Skin Tone
🛌🏼 Person in Bed: Medium-Light Skin Tone
🛌🏽 Person in Bed: Medium Skin Tone
🛌🏾 Person in Bed: Medium-Dark Skin Tone
🛌🏿 Person in Bed: Dark Skin Tone
🕴️ Man in Suit Levitating
🕴🏻 Man in Suit Levitating: Light Skin Tone
🕴🏼 Man in Suit Levitating: Medium-Light Skin Tone
🕴🏽 Man in Suit Levitating: Medium Skin Tone
🕴🏾 Man in Suit Levitating: Medium-Dark Skin Tone
🕴🏿 Man in Suit Levitating: Dark Skin Tone
🗣️ Speaking Head
👤 Bust in Silhouette
👥 Busts in Silhouette
🤺 Person Fencing
🏇 Horse Racing
🏇🏻 Horse Racing: Light Skin Tone
🏇🏼 Horse Racing: Medium-Light Skin Tone
🏇🏽 Horse Racing: Medium Skin Tone
🏇🏾 Horse Racing: Medium-Dark Skin Tone
🏇🏿 Horse Racing: Dark Skin Tone
⛷️ Skier
🏂 Snowboarder
🏂🏻 Snowboarder: Light Skin Tone
🏂🏼 Snowboarder: Medium-Light Skin Tone
🏂🏽 Snowboarder: Medium Skin Tone
🏂🏾 Snowboarder: Medium-Dark Skin Tone
🏂🏿 Snowboarder: Dark Skin Tone
🏌️ Person Golfing
🏌🏻 Person Golfing: Light Skin Tone
🏌🏼 Person Golfing: Medium-Light Skin Tone
🏌🏽 Person Golfing: Medium Skin Tone
🏌🏾 Person Golfing: Medium-Dark Skin Tone
🏌🏿 Person Golfing: Dark Skin Tone
🏌️‍♂️ Man Golfing
🏌🏻‍♂️ Man Golfing: Light Skin Tone
🏌🏼‍♂️ Man Golfing: Medium-Light Skin Tone
🏌🏽‍♂️ Man Golfing: Medium Skin Tone
🏌🏾‍♂️ Man Golfing: Medium-Dark Skin Tone
🏌🏿‍♂️ Man Golfing: Dark Skin Tone
🏌️‍♀️ Woman Golfing
🏌🏻‍♀️ Woman Golfing: Light Skin Tone
🏌🏼‍♀️ Woman Golfing: Medium-Light Skin Tone
🏌🏽‍♀️ Woman Golfing: Medium Skin Tone
🏌🏾‍♀️ Woman Golfing: Medium-Dark Skin Tone
🏌🏿‍♀️ Woman Golfing: Dark Skin Tone
🏄 Person Surfing
🏄🏻 Person Surfing: Light Skin Tone
🏄🏼 Person Surfing: Medium-Light Skin Tone
🏄🏽 Person Surfing: Medium Skin Tone
🏄🏾 Person Surfing: Medium-Dark Skin Tone
🏄🏿 Person Surfing: Dark Skin Tone
🏄‍♂️ Man Surfing
🏄🏻‍♂️ Man Surfing: Light Skin Tone
🏄🏼‍♂️ Man Surfing: Medium-Light Skin Tone
🏄🏽‍♂️ Man Surfing: Medium Skin Tone
🏄🏾‍♂️ Man Surfing: Medium-Dark Skin Tone
🏄🏿‍♂️ Man Surfing: Dark Skin Tone
🏄‍♀️ Woman Surfing
🏄🏻‍♀️ Woman Surfing: Light Skin Tone
🏄🏼‍♀️ Woman Surfing: Medium-Light Skin Tone
🏄🏽‍♀️ Woman Surfing: Medium Skin Tone
🏄🏾‍♀️ Woman Surfing: Medium-Dark Skin Tone
🏄🏿‍♀️ Woman Surfing: Dark Skin Tone
🚣 Person Rowing Boat
🚣🏻 Person Rowing Boat: Light Skin Tone
🚣🏼 Person Rowing Boat: Medium-Light Skin Tone
🚣🏽 Person Rowing Boat: Medium Skin Tone
🚣🏾 Person Rowing Boat: Medium-Dark Skin Tone
🚣🏿 Person Rowing Boat: Dark Skin Tone
🚣‍♂️ Man Rowing Boat
🚣🏻‍♂️ Man Rowing Boat: Light Skin Tone
🚣🏼‍♂️ Man Rowing Boat: Medium-Light Skin Tone
🚣🏽‍♂️ Man Rowing Boat: Medium Skin Tone
🚣🏾‍♂️ Man Rowing Boat: Medium-Dark Skin Tone
🚣🏿‍♂️ Man Rowing Boat: Dark Skin Tone
🚣‍♀️ Woman Rowing Boat
🚣🏻‍♀️ Woman Rowing Boat: Light Skin Tone
🚣🏼‍♀️ Woman Rowing Boat: Medium-Light Skin Tone
🚣🏽‍♀️ Woman Rowing Boat: Medium Skin Tone
🚣🏾‍♀️ Woman Rowing Boat: Medium-Dark Skin Tone
🚣🏿‍♀️ Woman Rowing Boat: Dark Skin Tone
🏊 Person Swimming
🏊🏻 Person Swimming: Light Skin Tone
🏊🏼 Person Swimming: Medium-Light Skin Tone
🏊🏽 Person Swimming: Medium Skin Tone
🏊🏾 Person Swimming: Medium-Dark Skin Tone
🏊🏿 Person Swimming: Dark Skin Tone
🏊‍♂️ Man Swimming
🏊🏻‍♂️ Man Swimming: Light Skin Tone
🏊🏼‍♂️ Man Swimming: Medium-Light Skin Tone
🏊🏽‍♂️ Man Swimming: Medium Skin Tone
🏊🏾‍♂️ Man Swimming: Medium-Dark Skin Tone
🏊🏿‍♂️ Man Swimming: Dark Skin Tone
🏊‍♀️ Woman Swimming
🏊🏻‍♀️ Woman Swimming: Light Skin Tone
🏊🏼‍♀️ Woman Swimming: Medium-Light Skin Tone
🏊🏽‍♀️ Woman Swimming: Medium Skin Tone
🏊🏾‍♀️ Woman Swimming: Medium-Dark Skin Tone
🏊🏿‍♀️ Woman Swimming: Dark Skin Tone
⛹️ Person Bouncing Ball
⛹🏻 Person Bouncing Ball: Light Skin Tone
⛹🏼 Person Bouncing Ball: Medium-Light Skin Tone
⛹🏽 Person Bouncing Ball: Medium Skin Tone
⛹🏾 Person Bouncing Ball: Medium-Dark Skin Tone
⛹🏿 Person Bouncing Ball: Dark Skin Tone
⛹️‍♂️ Man Bouncing Ball
⛹🏻‍♂️ Man Bouncing Ball: Light Skin Tone
⛹🏼‍♂️ Man Bouncing Ball: Medium-Light Skin Tone
⛹🏽‍♂️ Man Bouncing Ball: Medium Skin Tone
⛹🏾‍♂️ Man Bouncing Ball: Medium-Dark Skin Tone
⛹🏿‍♂️ Man Bouncing Ball: Dark Skin Tone
⛹️‍♀️ Woman Bouncing Ball
⛹🏻‍♀️ Woman Bouncing Ball: Light Skin Tone
⛹🏼‍♀️ Woman Bouncing Ball: Medium-Light Skin Tone
⛹🏽‍♀️ Woman Bouncing Ball: Medium Skin Tone
⛹🏾‍♀️ Woman Bouncing Ball: Medium-Dark Skin Tone
⛹🏿‍♀️ Woman Bouncing Ball: Dark Skin Tone
🏋️ Person Lifting Weights
🏋🏻 Person Lifting Weights: Light Skin Tone
🏋🏼 Person Lifting Weights: Medium-Light Skin Tone
🏋🏽 Person Lifting Weights: Medium Skin Tone
🏋🏾 Person Lifting Weights: Medium-Dark Skin Tone
🏋🏿 Person Lifting Weights: Dark Skin Tone
🏋️‍♂️ Man Lifting Weights
🏋🏻‍♂️ Man Lifting Weights: Light Skin Tone
🏋🏼‍♂️ Man Lifting Weights: Medium-Light Skin Tone
🏋🏽‍♂️ Man Lifting Weights: Medium Skin Tone
🏋🏾‍♂️ Man Lifting Weights: Medium-Dark Skin Tone
🏋🏿‍♂️ Man Lifting Weights: Dark Skin Tone
🏋️‍♀️ Woman Lifting Weights
🏋🏻‍♀️ Woman Lifting Weights: Light Skin Tone
🏋🏼‍♀️ Woman Lifting Weights: Medium-Light Skin Tone
🏋🏽‍♀️ Woman Lifting Weights: Medium Skin Tone
🏋🏾‍♀️ Woman Lifting Weights: Medium-Dark Skin Tone
🏋🏿‍♀️ Woman Lifting Weights: Dark Skin Tone
🚴 Person Biking
🚴🏻 Person Biking: Light Skin Tone
🚴🏼 Person Biking: Medium-Light Skin Tone
🚴🏽 Person Biking: Medium Skin Tone
🚴🏾 Person Biking: Medium-Dark Skin Tone
🚴🏿 Person Biking: Dark Skin Tone
🚴‍♂️ Man Biking
🚴🏻‍♂️ Man Biking: Light Skin Tone
🚴🏼‍♂️ Man Biking: Medium-Light Skin Tone
🚴🏽‍♂️ Man Biking: Medium Skin Tone
🚴🏾‍♂️ Man Biking: Medium-Dark Skin Tone
🚴🏿‍♂️ Man Biking: Dark Skin Tone
🚴‍♀️ Woman Biking
🚴🏻‍♀️ Woman Biking: Light Skin Tone
🚴🏼‍♀️ Woman Biking: Medium-Light Skin Tone
🚴🏽‍♀️ Woman Biking: Medium Skin Tone
🚴🏾‍♀️ Woman Biking: Medium-Dark Skin Tone
🚴🏿‍♀️ Woman Biking: Dark Skin Tone
🚵 Person Mountain Biking
🚵🏻 Person Mountain Biking: Light Skin Tone
🚵🏼 Person Mountain Biking: Medium-Light Skin Tone
🚵🏽 Person Mountain Biking: Medium Skin Tone
🚵🏾 Person Mountain Biking: Medium-Dark Skin Tone
🚵🏿 Person Mountain Biking: Dark Skin Tone
🚵‍♂️ Man Mountain Biking
🚵🏻‍♂️ Man Mountain Biking: Light Skin Tone
🚵🏼‍♂️ Man Mountain Biking: Medium-Light Skin Tone
🚵🏽‍♂️ Man Mountain Biking: Medium Skin Tone
🚵🏾‍♂️ Man Mountain Biking: Medium-Dark Skin Tone
🚵🏿‍♂️ Man Mountain Biking: Dark Skin Tone
🚵‍♀️ Woman Mountain Biking
🚵🏻‍♀️ Woman Mountain Biking: Light Skin Tone
🚵🏼‍♀️ Woman Mountain Biking: Medium-Light Skin Tone
🚵🏽‍♀️ Woman Mountain Biking: Medium Skin Tone
🚵🏾‍♀️ Woman Mountain Biking: Medium-Dark Skin Tone
🚵🏿‍♀️ Woman Mountain Biking: Dark Skin Tone
🏎️ Racing Car
🏍️ Motorcycle
🤸 Person Cartwheeling
🤸🏻 Person Cartwheeling: Light Skin Tone
🤸🏼 Person Cartwheeling: Medium-Light Skin Tone
🤸🏽 Person Cartwheeling: Medium Skin Tone
🤼🏻 Wrestlers, Type-1-2
🤸🏾 Person Cartwheeling: Medium-Dark Skin Tone
🤼🏼 Wrestlers, Type-3
🤸🏿 Person Cartwheeling: Dark Skin Tone
🤸‍♂️ Man Cartwheeling
🤼🏽 Wrestlers, Type-4
🤼🏾 Wrestlers, Type-5
🤸🏻‍♂️ Man Cartwheeling: Light Skin Tone
🤼🏿 Wrestlers, Type-6
🤼🏻‍♂️ Men Wrestling, Type-1-2
🤸🏼‍♂️ Man Cartwheeling: Medium-Light Skin Tone
🤼🏼‍♂️ Men Wrestling, Type-3
🤼🏽‍♂️ Men Wrestling, Type-4
🤸🏽‍♂️ Man Cartwheeling: Medium Skin Tone
🤼🏾‍♂️ Men Wrestling, Type-5
🤸🏾‍♂️ Man Cartwheeling: Medium-Dark Skin Tone
🤼🏿‍♂️ Men Wrestling, Type-6
🤸🏿‍♂️ Man Cartwheeling: Dark Skin Tone
🤼🏻‍♀️ Women Wrestling, Type-1-2
🤼🏼‍♀️ Women Wrestling, Type-3
🤼🏽‍♀️ Women Wrestling, Type-4
🤸‍♀️ Woman Cartwheeling
🤼🏾‍♀️ Women Wrestling, Type-5
🤼🏿‍♀️ Women Wrestling, Type-6
🤸🏻‍♀️ Woman Cartwheeling: Light Skin Tone
🤸🏼‍♀️ Woman Cartwheeling: Medium-Light Skin Tone
🤸🏽‍♀️ Woman Cartwheeling: Medium Skin Tone
🤸🏾‍♀️ Woman Cartwheeling: Medium-Dark Skin Tone
🤸🏿‍♀️ Woman Cartwheeling: Dark Skin Tone
🤼 People Wrestling
🤼‍♂️ Men Wrestling
🤼‍♀️ Women Wrestling
🤽 Person Playing Water Polo
🤽🏻 Person Playing Water Polo: Light Skin Tone
🤽🏼 Person Playing Water Polo: Medium-Light Skin Tone
🤽🏽 Person Playing Water Polo: Medium Skin Tone
🤽🏾 Person Playing Water Polo: Medium-Dark Skin Tone
🤽🏿 Person Playing Water Polo: Dark Skin Tone
🤽‍♂️ Man Playing Water Polo
🤽🏻‍♂️ Man Playing Water Polo: Light Skin Tone
🤽🏼‍♂️ Man Playing Water Polo: Medium-Light Skin Tone
🤽🏽‍♂️ Man Playing Water Polo: Medium Skin Tone
🤽🏾‍♂️ Man Playing Water Polo: Medium-Dark Skin Tone
🤽🏿‍♂️ Man Playing Water Polo: Dark Skin Tone
🤽‍♀️ Woman Playing Water Polo
🤽🏻‍♀️ Woman Playing Water Polo: Light Skin Tone
🤽🏼‍♀️ Woman Playing Water Polo: Medium-Light Skin Tone
🤽🏽‍♀️ Woman Playing Water Polo: Medium Skin Tone
🤽🏾‍♀️ Woman Playing Water Polo: Medium-Dark Skin Tone
🤽🏿‍♀️ Woman Playing Water Polo: Dark Skin Tone
🤾 Person Playing Handball
🤾🏻 Person Playing Handball: Light Skin Tone
🤾🏼 Person Playing Handball: Medium-Light Skin Tone
🤾🏽 Person Playing Handball: Medium Skin Tone
🤾🏾 Person Playing Handball: Medium-Dark Skin Tone
🤾🏿 Person Playing Handball: Dark Skin Tone
🤾‍♂️ Man Playing Handball
🤾🏻‍♂️ Man Playing Handball: Light Skin Tone
🤾🏼‍♂️ Man Playing Handball: Medium-Light Skin Tone
🤾🏽‍♂️ Man Playing Handball: Medium Skin Tone
🤾🏾‍♂️ Man Playing Handball: Medium-Dark Skin Tone
🤾🏿‍♂️ Man Playing Handball: Dark Skin Tone
🤾‍♀️ Woman Playing Handball
🤾🏻‍♀️ Woman Playing Handball: Light Skin Tone
🤾🏼‍♀️ Woman Playing Handball: Medium-Light Skin Tone
🤾🏽‍♀️ Woman Playing Handball: Medium Skin Tone
🤾🏾‍♀️ Woman Playing Handball: Medium-Dark Skin Tone
🤾🏿‍♀️ Woman Playing Handball: Dark Skin Tone
🤹 Person Juggling
🤹🏻 Person Juggling: Light Skin Tone
🤹🏼 Person Juggling: Medium-Light Skin Tone
🤹🏽 Person Juggling: Medium Skin Tone
🤹🏾 Person Juggling: Medium-Dark Skin Tone
🤹🏿 Person Juggling: Dark Skin Tone
🤹‍♂️ Man Juggling
🤹🏻‍♂️ Man Juggling: Light Skin Tone
🤹🏼‍♂️ Man Juggling: Medium-Light Skin Tone
🤹🏽‍♂️ Man Juggling: Medium Skin Tone
🤹🏾‍♂️ Man Juggling: Medium-Dark Skin Tone
🤹🏿‍♂️ Man Juggling: Dark Skin Tone
🤹‍♀️ Woman Juggling
🤹🏻‍♀️ Woman Juggling: Light Skin Tone
🤹🏼‍♀️ Woman Juggling: Medium-Light Skin Tone
🤹🏽‍♀️ Woman Juggling: Medium Skin Tone
🤹🏾‍♀️ Woman Juggling: Medium-Dark Skin Tone
🤹🏿‍♀️ Woman Juggling: Dark Skin Tone
👫 Man and Woman Holding Hands
👬 Two Men Holding Hands
👭 Two Women Holding Hands
💏 Kiss
👩‍❤️‍💋‍👨 Kiss: Woman, Man
👨‍❤️‍💋‍👨 Kiss: Man, Man
👩‍❤️‍💋‍👩 Kiss: Woman, Woman
💑 Couple With Heart
👩‍❤️‍👨 Couple With Heart: Woman, Man
👨‍❤️‍👨 Couple With Heart: Man, Man
👩‍❤️‍👩 Couple With Heart: Woman, Woman
👪 Family
👨‍👩‍👦 Family: Man, Woman, Boy
👨‍👩‍👧 Family: Man, Woman, Girl
👨‍👩‍👧‍👦 Family: Man, Woman, Girl, Boy
👨‍👩‍👦‍👦 Family: Man, Woman, Boy, Boy
👨‍👩‍👧‍👧 Family: Man, Woman, Girl, Girl
👨‍👨‍👦 Family: Man, Man, Boy
👨‍👨‍👧 Family: Man, Man, Girl
👨‍👨‍👧‍👦 Family: Man, Man, Girl, Boy
👨‍👨‍👦‍👦 Family: Man, Man, Boy, Boy
👨‍👨‍👧‍👧 Family: Man, Man, Girl, Girl
👩‍👩‍👦 Family: Woman, Woman, Boy
👩‍👩‍👧 Family: Woman, Woman, Girl
👩‍👩‍👧‍👦 Family: Woman, Woman, Girl, Boy
👩‍👩‍👦‍👦 Family: Woman, Woman, Boy, Boy
👩‍👩‍👧‍👧 Family: Woman, Woman, Girl, Girl
👨‍👦 Family: Man, Boy
👨‍👦‍👦 Family: Man, Boy, Boy
👨‍👧 Family: Man, Girl
👨‍👧‍👦 Family: Man, Girl, Boy
👨‍👧‍👧 Family: Man, Girl, Girl
👩‍👦 Family: Woman, Boy
👩‍👦‍👦 Family: Woman, Boy, Boy
👩‍👧 Family: Woman, Girl
👩‍👧‍👦 Family: Woman, Girl, Boy
👩‍👧‍👧 Family: Woman, Girl, Girl
🤳 Selfie
🤳🏻 Selfie: Light Skin Tone
🤳🏼 Selfie: Medium-Light Skin Tone
🤳🏽 Selfie: Medium Skin Tone
🤳🏾 Selfie: Medium-Dark Skin Tone
🤳🏿 Selfie: Dark Skin Tone
💪 Flexed Biceps
💪🏻 Flexed Biceps: Light Skin Tone
💪🏼 Flexed Biceps: Medium-Light Skin Tone
💪🏽 Flexed Biceps: Medium Skin Tone
💪🏾 Flexed Biceps: Medium-Dark Skin Tone
💪🏿 Flexed Biceps: Dark Skin Tone
🦵 Leg
🦵🏻 Leg: Light Skin Tone
🦵🏼 Leg: Medium-Light Skin Tone
🦵🏽 Leg: Medium Skin Tone
🦵🏾 Leg: Medium-Dark Skin Tone
🦵🏿 Leg: Dark Skin Tone
🦶 Foot
🦶🏻 Foot: Light Skin Tone
🦶🏼 Foot: Medium-Light Skin Tone
🦶🏽 Foot: Medium Skin Tone
🦶🏾 Foot: Medium-Dark Skin Tone
🦶🏿 Foot: Dark Skin Tone
👈 Backhand Index Pointing Left
👈🏻 Backhand Index Pointing Left: Light Skin Tone
👈🏼 Backhand Index Pointing Left: Medium-Light Skin Tone
👈🏽 Backhand Index Pointing Left: Medium Skin Tone
👈🏾 Backhand Index Pointing Left: Medium-Dark Skin Tone
👈🏿 Backhand Index Pointing Left: Dark Skin Tone
👉 Backhand Index Pointing Right
👉🏻 Backhand Index Pointing Right: Light Skin Tone
👉🏼 Backhand Index Pointing Right: Medium-Light Skin Tone
👉🏽 Backhand Index Pointing Right: Medium Skin Tone
👉🏾 Backhand Index Pointing Right: Medium-Dark Skin Tone
👉🏿 Backhand Index Pointing Right: Dark Skin Tone
☝️ Index Pointing Up
☝🏻 Index Pointing Up: Light Skin Tone
☝🏼 Index Pointing Up: Medium-Light Skin Tone
☝🏽 Index Pointing Up: Medium Skin Tone
☝🏾 Index Pointing Up: Medium-Dark Skin Tone
☝🏿 Index Pointing Up: Dark Skin Tone
👆 Backhand Index Pointing Up
👆🏻 Backhand Index Pointing Up: Light Skin Tone
👆🏼 Backhand Index Pointing Up: Medium-Light Skin Tone
👆🏽 Backhand Index Pointing Up: Medium Skin Tone
👆🏾 Backhand Index Pointing Up: Medium-Dark Skin Tone
👆🏿 Backhand Index Pointing Up: Dark Skin Tone
🖕 Middle Finger
🖕🏻 Middle Finger: Light Skin Tone
🖕🏼 Middle Finger: Medium-Light Skin Tone
🖕🏽 Middle Finger: Medium Skin Tone
🖕🏾 Middle Finger: Medium-Dark Skin Tone
🖕🏿 Middle Finger: Dark Skin Tone
👇 Backhand Index Pointing Down
👇🏻 Backhand Index Pointing Down: Light Skin Tone
👇🏼 Backhand Index Pointing Down: Medium-Light Skin Tone
👇🏽 Backhand Index Pointing Down: Medium Skin Tone
👇🏾 Backhand Index Pointing Down: Medium-Dark Skin Tone
👇🏿 Backhand Index Pointing Down: Dark Skin Tone
✌️ Victory Hand
✌🏻 Victory Hand: Light Skin Tone
✌🏼 Victory Hand: Medium-Light Skin Tone
✌🏽 Victory Hand: Medium Skin Tone
✌🏾 Victory Hand: Medium-Dark Skin Tone
✌🏿 Victory Hand: Dark Skin Tone
🤞 Crossed Fingers
🤞🏻 Crossed Fingers: Light Skin Tone
🤞🏼 Crossed Fingers: Medium-Light Skin Tone
🤞🏽 Crossed Fingers: Medium Skin Tone
🤞🏾 Crossed Fingers: Medium-Dark Skin Tone
🤞🏿 Crossed Fingers: Dark Skin Tone
🖖 Vulcan Salute
🖖🏻 Vulcan Salute: Light Skin Tone
🖖🏼 Vulcan Salute: Medium-Light Skin Tone
🖖🏽 Vulcan Salute: Medium Skin Tone
🖖🏾 Vulcan Salute: Medium-Dark Skin Tone
🖖🏿 Vulcan Salute: Dark Skin Tone
🤘 Sign of the Horns
🤘🏻 Sign of the Horns: Light Skin Tone
🤘🏼 Sign of the Horns: Medium-Light Skin Tone
🤘🏽 Sign of the Horns: Medium Skin Tone
🤘🏾 Sign of the Horns: Medium-Dark Skin Tone
🤘🏿 Sign of the Horns: Dark Skin Tone
🤙 Call Me Hand
🤙🏻 Call Me Hand: Light Skin Tone
🤙🏼 Call Me Hand: Medium-Light Skin Tone
🤙🏽 Call Me Hand: Medium Skin Tone
🤙🏾 Call Me Hand: Medium-Dark Skin Tone
🤙🏿 Call Me Hand: Dark Skin Tone
🖐️ Hand With Fingers Splayed
🖐🏻 Hand With Fingers Splayed: Light Skin Tone
🖐🏼 Hand With Fingers Splayed: Medium-Light Skin Tone
🖐🏽 Hand With Fingers Splayed: Medium Skin Tone
🖐🏾 Hand With Fingers Splayed: Medium-Dark Skin Tone
🖐🏿 Hand With Fingers Splayed: Dark Skin Tone
✋ Raised Hand
✋🏻 Raised Hand: Light Skin Tone
✋🏼 Raised Hand: Medium-Light Skin Tone
✋🏽 Raised Hand: Medium Skin Tone
✋🏾 Raised Hand: Medium-Dark Skin Tone
✋🏿 Raised Hand: Dark Skin Tone
👌 OK Hand
👌🏻 OK Hand: Light Skin Tone
👌🏼 OK Hand: Medium-Light Skin Tone
👌🏽 OK Hand: Medium Skin Tone
👌🏾 OK Hand: Medium-Dark Skin Tone
👌🏿 OK Hand: Dark Skin Tone
👍 Thumbs Up
👍🏻 Thumbs Up: Light Skin Tone
👍🏼 Thumbs Up: Medium-Light Skin Tone
👍🏽 Thumbs Up: Medium Skin Tone
👍🏾 Thumbs Up: Medium-Dark Skin Tone
👍🏿 Thumbs Up: Dark Skin Tone
👎 Thumbs Down
👎🏻 Thumbs Down: Light Skin Tone
👎🏼 Thumbs Down: Medium-Light Skin Tone
👎🏽 Thumbs Down: Medium Skin Tone
👎🏾 Thumbs Down: Medium-Dark Skin Tone
👎🏿 Thumbs Down: Dark Skin Tone
✊ Raised Fist
✊🏻 Raised Fist: Light Skin Tone
✊🏼 Raised Fist: Medium-Light Skin Tone
✊🏽 Raised Fist: Medium Skin Tone
✊🏾 Raised Fist: Medium-Dark Skin Tone
✊🏿 Raised Fist: Dark Skin Tone
👊 Oncoming Fist
👊🏻 Oncoming Fist: Light Skin Tone
👊🏼 Oncoming Fist: Medium-Light Skin Tone
👊🏽 Oncoming Fist: Medium Skin Tone
👊🏾 Oncoming Fist: Medium-Dark Skin Tone
👊🏿 Oncoming Fist: Dark Skin Tone
🤛 Left-Facing Fist
🤛🏻 Left-Facing Fist: Light Skin Tone
🤛🏼 Left-Facing Fist: Medium-Light Skin Tone
🤛🏽 Left-Facing Fist: Medium Skin Tone
🤛🏾 Left-Facing Fist: Medium-Dark Skin Tone
🤛🏿 Left-Facing Fist: Dark Skin Tone
🤜 Right-Facing Fist
🤜🏻 Right-Facing Fist: Light Skin Tone
🤜🏼 Right-Facing Fist: Medium-Light Skin Tone
🤜🏽 Right-Facing Fist: Medium Skin Tone
🤜🏾 Right-Facing Fist: Medium-Dark Skin Tone
🤜🏿 Right-Facing Fist: Dark Skin Tone
🤚 Raised Back of Hand
🤚🏻 Raised Back of Hand: Light Skin Tone
🤚🏼 Raised Back of Hand: Medium-Light Skin Tone
🤚🏽 Raised Back of Hand: Medium Skin Tone
🤚🏾 Raised Back of Hand: Medium-Dark Skin Tone
🤚🏿 Raised Back of Hand: Dark Skin Tone
👋 Waving Hand
👋🏻 Waving Hand: Light Skin Tone
👋🏼 Waving Hand: Medium-Light Skin Tone
👋🏽 Waving Hand: Medium Skin Tone
👋🏾 Waving Hand: Medium-Dark Skin Tone
👋🏿 Waving Hand: Dark Skin Tone
🤟 Love-You Gesture
🤟🏻 Love-You Gesture: Light Skin Tone
🤟🏼 Love-You Gesture: Medium-Light Skin Tone
🤟🏽 Love-You Gesture: Medium Skin Tone
🤟🏾 Love-You Gesture: Medium-Dark Skin Tone
🤟🏿 Love-You Gesture: Dark Skin Tone
✍️ Writing Hand
✍🏻 Writing Hand: Light Skin Tone
✍🏼 Writing Hand: Medium-Light Skin Tone
✍🏽 Writing Hand: Medium Skin Tone
✍🏾 Writing Hand: Medium-Dark Skin Tone
✍🏿 Writing Hand: Dark Skin Tone
👏 Clapping Hands
👏🏻 Clapping Hands: Light Skin Tone
👏🏼 Clapping Hands: Medium-Light Skin Tone
👏🏽 Clapping Hands: Medium Skin Tone
👏🏾 Clapping Hands: Medium-Dark Skin Tone
👏🏿 Clapping Hands: Dark Skin Tone
👐 Open Hands
👐🏻 Open Hands: Light Skin Tone
👐🏼 Open Hands: Medium-Light Skin Tone
👐🏽 Open Hands: Medium Skin Tone
👐🏾 Open Hands: Medium-Dark Skin Tone
👐🏿 Open Hands: Dark Skin Tone
🙌 Raising Hands
🙌🏻 Raising Hands: Light Skin Tone
🙌🏼 Raising Hands: Medium-Light Skin Tone
🙌🏽 Raising Hands: Medium Skin Tone
🙌🏾 Raising Hands: Medium-Dark Skin Tone
🙌🏿 Raising Hands: Dark Skin Tone
🤲 Palms Up Together
🤲🏻 Palms Up Together: Light Skin Tone
🤲🏼 Palms Up Together: Medium-Light Skin Tone
🤲🏽 Palms Up Together: Medium Skin Tone
🤲🏾 Palms Up Together: Medium-Dark Skin Tone
🤲🏿 Palms Up Together: Dark Skin Tone
🙏 Folded Hands
🙏🏻 Folded Hands: Light Skin Tone
🙏🏼 Folded Hands: Medium-Light Skin Tone
🙏🏽 Folded Hands: Medium Skin Tone
🙏🏾 Folded Hands: Medium-Dark Skin Tone
🙏🏿 Folded Hands: Dark Skin Tone
🤝 Handshake
💅 Nail Polish
💅🏻 Nail Polish: Light Skin Tone
💅🏼 Nail Polish: Medium-Light Skin Tone
💅🏽 Nail Polish: Medium Skin Tone
💅🏾 Nail Polish: Medium-Dark Skin Tone
💅🏿 Nail Polish: Dark Skin Tone
👂 Ear
👂🏻 Ear: Light Skin Tone
👂🏼 Ear: Medium-Light Skin Tone
👂🏽 Ear: Medium Skin Tone
👂🏾 Ear: Medium-Dark Skin Tone
👂🏿 Ear: Dark Skin Tone
👃 Nose
👃🏻 Nose: Light Skin Tone
👃🏼 Nose: Medium-Light Skin Tone
👃🏽 Nose: Medium Skin Tone
👃🏾 Nose: Medium-Dark Skin Tone
👃🏿 Nose: Dark Skin Tone
🦰 Emoji Component Red Hair
🦱 Emoji Component Curly Hair
🦲 Emoji Component Bald
🦳 Emoji Component White Hair
👣 Footprints
👀 Eyes
👁️ Eye
👁️‍🗨️ Eye in Speech Bubble
🧠 Brain
🦴 Bone
🦷 Tooth
👅 Tongue
👄 Mouth
💋 Kiss Mark
💘 Heart With Arrow
❤️ Red Heart
💓 Beating Heart
💔 Broken Heart
💕 Two Hearts
💖 Sparkling Heart
💗 Growing Heart
💙 Blue Heart
💚 Green Heart
💛 Yellow Heart
🧡 Orange Heart
💜 Purple Heart
🖤 Black Heart
💝 Heart With Ribbon
💞 Revolving Hearts
💟 Heart Decoration
❣️ Heavy Heart Exclamation
💌 Love Letter
💤 Zzz
💢 Anger Symbol
💣 Bomb
💥 Collision
💦 Sweat Droplets
💨 Dashing Away
💫 Dizzy
💬 Speech Balloon
🗨️ Left Speech Bubble
🗯️ Right Anger Bubble
💭 Thought Balloon
🕳️ Hole
👓 Glasses
🕶️ Sunglasses
🥽 Goggles
🥼 Lab Coat
👔 Necktie
👕 T-Shirt
👖 Jeans
🧣 Scarf
🧤 Gloves
🧥 Coat
🧦 Socks
👗 Dress
👘 Kimono
👙 Bikini
👚 Woman’s Clothes
👛 Purse
👜 Handbag
👝 Clutch Bag
🛍️ Shopping Bags
🎒 School Backpack
👞 Man’s Shoe
👟 Running Shoe
🥾 Hiking Boot
🥿 Flat Shoe
👠 High-Heeled Shoe
👡 Woman’s Sandal
👢 Woman’s Boot
👑 Crown
👒 Woman’s Hat
🎩 Top Hat
🎓 Graduation Cap
🧢 Billed Cap
⛑️ Rescue Worker’s Helmet
📿 Prayer Beads
💄 Lipstick
💍 Ring
💎 Gem Stone
🐵 Monkey Face
🐒 Monkey
🦍 Gorilla
🐶 Dog Face
🐕 Dog
🐩 Poodle
🐺 Wolf Face
🦊 Fox Face
🦝 Raccoon
🐱 Cat Face
🐈 Cat
🦁 Lion Face
🐯 Tiger Face
🐅 Tiger
🐆 Leopard
🐴 Horse Face
🐎 Horse
🦄 Unicorn Face
🦓 Zebra
🦌 Deer
🐮 Cow Face
🐂 Ox
🐃 Water Buffalo
🐄 Cow
🐷 Pig Face
🐖 Pig
🐗 Boar
🐽 Pig Nose
🐏 Ram
🐑 Ewe
🐐 Goat
🐪 Camel
🐫 Two-Hump Camel
🦙 Llama
🦒 Giraffe
🐘 Elephant
🦏 Rhinoceros
🦛 Hippopotamus
🐭 Mouse Face
🐁 Mouse
🐀 Rat
🐹 Hamster Face
🐰 Rabbit Face
🐇 Rabbit
🐿️ Chipmunk
🦔 Hedgehog
🦇 Bat
🐻 Bear Face
🐨 Koala
🐼 Panda Face
🦘 Kangaroo
🦡 Badger
🐾 Paw Prints
🦃 Turkey
🐔 Chicken
🐓 Rooster
🐣 Hatching Chick
🐤 Baby Chick
🐥 Front-Facing Baby Chick
🐦 Bird
🐧 Penguin
🕊️ Dove
🦅 Eagle
🦆 Duck
🦢 Swan
🦉 Owl
🦚 Peacock
🦜 Parrot
🐸 Frog Face
🐊 Crocodile
🐢 Turtle
🦎 Lizard
🐍 Snake
🐲 Dragon Face
🐉 Dragon
🦕 Sauropod
🦖 T-Rex
🐳 Spouting Whale
🐋 Whale
🐬 Dolphin
🐟 Fish
🐠 Tropical Fish
🐡 Blowfish
🦈 Shark
🐙 Octopus
🐚 Spiral Shell
🦀 Crab
🦞 Lobster
🦐 Shrimp
🦑 Squid
🐌 Snail
🦋 Butterfly
🐛 Bug
🐜 Ant
🐝 Honeybee
🐞 Lady Beetle
🦗 Cricket
🕷️ Spider
🕸️ Spider Web
🦂 Scorpion
🦟 Mosquito
🦠 Microbe
💐 Bouquet
🌸 Cherry Blossom
💮 White Flower
🏵️ Rosette
🌹 Rose
🥀 Wilted Flower
🌺 Hibiscus
🌻 Sunflower
🌼 Blossom
🌷 Tulip
🌱 Seedling
🌲 Evergreen Tree
🌳 Deciduous Tree
🌴 Palm Tree
🌵 Cactus
🌾 Sheaf of Rice
🌿 Herb
☘️ Shamrock
🍀 Four Leaf Clover
🍁 Maple Leaf
🍂 Fallen Leaf
🍃 Leaf Fluttering in Wind
🍇 Grapes
🍈 Melon
🍉 Watermelon
🍊 Tangerine
🍋 Lemon
🍌 Banana
🍍 Pineapple
🥭 Mango
🍎 Red Apple
🍏 Green Apple
🍐 Pear
🍑 Peach
🍒 Cherries
🍓 Strawberry
🥝 Kiwi Fruit
🍅 Tomato
🥥 Coconut
🥑 Avocado
🍆 Eggplant
🥔 Potato
🥕 Carrot
🌽 Ear of Corn
🌶️ Hot Pepper
🥒 Cucumber
🥬 Leafy Green
🥦 Broccoli
🍄 Mushroom
🥜 Peanuts
🌰 Chestnut
🍞 Bread
🥐 Croissant
🥖 Baguette Bread
🥨 Pretzel
🥯 Bagel
🥞 Pancakes
🧀 Cheese Wedge
🍖 Meat on Bone
🍗 Poultry Leg
🥩 Cut of Meat
🥓 Bacon
🍔 Hamburger
🍟 French Fries
🍕 Pizza
🌭 Hot Dog
🥪 Sandwich
🌮 Taco
🌯 Burrito
🥙 Stuffed Flatbread
🥚 Egg
🍳 Cooking
🥘 Shallow Pan of Food
🍲 Pot of Food
🥣 Bowl With Spoon
🥗 Green Salad
🍿 Popcorn
🧂 Salt
🥫 Canned Food
🍱 Bento Box
🍘 Rice Cracker
🍙 Rice Ball
🍚 Cooked Rice
🍛 Curry Rice
🍜 Steaming Bowl
🍝 Spaghetti
🍠 Roasted Sweet Potato
🍢 Oden
🍣 Sushi
🍤 Fried Shrimp
🍥 Fish Cake With Swirl
🥮 Moon Cake
🍡 Dango
🥟 Dumpling
🥠 Fortune Cookie
🥡 Takeout Box
🍦 Soft Ice Cream
🍧 Shaved Ice
🍨 Ice Cream
🍩 Doughnut
🍪 Cookie
🎂 Birthday Cake
🍰 Shortcake
🧁 Cupcake
🥧 Pie
🍫 Chocolate Bar
🍬 Candy
🍭 Lollipop
🍮 Custard
🍯 Honey Pot
🍼 Baby Bottle
🥛 Glass of Milk
☕ Hot Beverage
🍵 Teacup Without Handle
🍶 Sake
🍾 Bottle With Popping Cork
🍷 Wine Glass
🍸 Cocktail Glass
🍹 Tropical Drink
🍺 Beer Mug
🍻 Clinking Beer Mugs
🥂 Clinking Glasses
🥃 Tumbler Glass
🥤 Cup With Straw
🥢 Chopsticks
🍽️ Fork and Knife With Plate
🍴 Fork and Knife
🥄 Spoon
🔪 Kitchen Knife
🏺 Amphora
🌍 Globe Showing Europe-Africa
🌎 Globe Showing Americas
🌏 Globe Showing Asia-Australia
🌐 Globe With Meridians
🗺️ World Map
🗾 Map of Japan
🧭 Compass
🏔️ Snow-Capped Mountain
⛰️ Mountain
🌋 Volcano
🗻 Mount Fuji
🏕️ Camping
🏖️ Beach With Umbrella
🏜️ Desert
🏝️ Desert Island
🏞️ National Park
🏟️ Stadium
🏛️ Classical Building
🏗️ Building Construction
🏘️ Houses
🏚️ Derelict House
🏠 House
🏡 House With Garden
🧱 Brick
🏢 Office Building
🏣 Japanese Post Office
🏤 Post Office
🏥 Hospital
🏦 Bank
🏨 Hotel
🏩 Love Hotel
🏪 Convenience Store
🏫 School
🏬 Department Store
🏭 Factory
🏯 Japanese Castle
🏰 Castle
💒 Wedding
🗼 Tokyo Tower
🗽 Statue of Liberty
⛪ Church
🕌 Mosque
🕍 Synagogue
⛩️ Shinto Shrine
🕋 Kaaba
⛲ Fountain
⛺ Tent
🌁 Foggy
🌃 Night With Stars
🏙️ Cityscape
🌄 Sunrise Over Mountains
🌅 Sunrise
🌆 Cityscape at Dusk
🌇 Sunset
🌉 Bridge at Night
♨️ Hot Springs
🌌 Milky Way
🎠 Carousel Horse
🎡 Ferris Wheel
🎢 Roller Coaster
💈 Barber Pole
🎪 Circus Tent
🚂 Locomotive
🚃 Railway Car
🚄 High-Speed Train
🚅 Bullet Train
🚆 Train
🚇 Metro
🚈 Light Rail
🚉 Station
🚊 Tram
🚝 Monorail
🚞 Mountain Railway
🚋 Tram Car
🚌 Bus
🚍 Oncoming Bus
🚎 Trolleybus
🚐 Minibus
🚑 Ambulance
🚒 Fire Engine
🚓 Police Car
🚔 Oncoming Police Car
🚕 Taxi
🚖 Oncoming Taxi
🚗 Automobile
🚘 Oncoming Automobile
🚙 Sport Utility Vehicle
🚚 Delivery Truck
🚛 Articulated Lorry
🚜 Tractor
🚲 Bicycle
🛴 Kick Scooter
🛹 Skateboard
🛵 Motor Scooter
🚏 Bus Stop
🛣️ Motorway
🛤️ Railway Track
🛢️ Oil Drum
⛽ Fuel Pump
🚨 Police Car Light
🚥 Horizontal Traffic Light
🚦 Vertical Traffic Light
🛑 Stop Sign
🚧 Construction
⚓ Anchor
⛵ Sailboat
🛶 Canoe
🚤 Speedboat
🛳️ Passenger Ship
⛴️ Ferry
🛥️ Motor Boat
🚢 Ship
✈️ Airplane
🛩️ Small Airplane
🛫 Airplane Departure
🛬 Airplane Arrival
💺 Seat
🚁 Helicopter
🚟 Suspension Railway
🚠 Mountain Cableway
🚡 Aerial Tramway
🛰️ Satellite
🚀 Rocket
🛸 Flying Saucer
🛎️ Bellhop Bell
🧳 Luggage
⌛ Hourglass Done
⏳ Hourglass Not Done
⌚ Watch
⏰ Alarm Clock
⏱️ Stopwatch
⏲️ Timer Clock
🕰️ Mantelpiece Clock
🕛 Twelve O’clock
🕧 Twelve-Thirty
🕐 One O’clock
🕜 One-Thirty
🕑 Two O’clock
🕝 Two-Thirty
🕒 Three O’clock
🕞 Three-Thirty
🕓 Four O’clock
🕟 Four-Thirty
🕔 Five O’clock
🕠 Five-Thirty
🕕 Six O’clock
🕡 Six-Thirty
🕖 Seven O’clock
🕢 Seven-Thirty
🕗 Eight O’clock
🕣 Eight-Thirty
🕘 Nine O’clock
🕤 Nine-Thirty
🕙 Ten O’clock
🕥 Ten-Thirty
🕚 Eleven O’clock
🕦 Eleven-Thirty
🌑 New Moon
🌒 Waxing Crescent Moon
🌓 First Quarter Moon
🌔 Waxing Gibbous Moon
🌕 Full Moon
🌖 Waning Gibbous Moon
🌗 Last Quarter Moon
🌘 Waning Crescent Moon
🌙 Crescent Moon
🌚 New Moon Face
🌛 First Quarter Moon Face
🌜 Last Quarter Moon Face
🌡️ Thermometer
☀️ Sun
🌝 Full Moon Face
🌞 Sun With Face
⭐ White Medium Star
🌟 Glowing Star
🌠 Shooting Star
☁️ Cloud
⛅ Sun Behind Cloud
⛈️ Cloud With Lightning and Rain
🌤️ Sun Behind Small Cloud
🌥️ Sun Behind Large Cloud
🌦️ Sun Behind Rain Cloud
🌧️ Cloud With Rain
🌨️ Cloud With Snow
🌩️ Cloud With Lightning
🌪️ Tornado
🌫️ Fog
🌬️ Wind Face
🌀 Cyclone
🌈 Rainbow
🌂 Closed Umbrella
☂️ Umbrella
☔ Umbrella With Rain Drops
⛱️ Umbrella on Ground
⚡ High Voltage
❄️ Snowflake
☃️ Snowman
⛄ Snowman Without Snow
☄️ Comet
🔥 Fire
💧 Droplet
🌊 Water Wave
🎃 Jack-O-Lantern
🎄 Christmas Tree
🎆 Fireworks
🎇 Sparkler
🧨 Firecracker
✨ Sparkles
🎈 Balloon
🎉 Party Popper
🎊 Confetti Ball
🎋 Tanabata Tree
🎍 Pine Decoration
🎎 Japanese Dolls
🎏 Carp Streamer
🎐 Wind Chime
🎑 Moon Viewing Ceremony
🧧 Red Gift Envelope
🎀 Ribbon
🎁 Wrapped Gift
🎗️ Reminder Ribbon
🎟️ Admission Tickets
🎫 Ticket
🎖️ Military Medal
🏆 Trophy
🏅 Sports Medal
🥇 1st Place Medal
🥈 2nd Place Medal
🥉 3rd Place Medal
⚽ Soccer Ball
⚾ Baseball
🥎 Softball
🏀 Basketball
🏐 Volleyball
🏈 American Football
🏉 Rugby Football
🎾 Tennis
🥏 Flying Disc
🎳 Bowling
🏏 Cricket Game
🏑 Field Hockey
🏒 Ice Hockey
🥍 Lacrosse
🏓 Ping Pong
🏸 Badminton
🥊 Boxing Glove
🥋 Martial Arts Uniform
🥅 Goal Net
⛳ Flag in Hole
⛸️ Ice Skate
🎣 Fishing Pole
🎽 Running Shirt
🎿 Skis
🛷 Sled
🥌 Curling Stone
🎯 Direct Hit
🎱 Pool 8 Ball
🔮 Crystal Ball
🧿 Nazar Amulet
🎮 Video Game
🕹️ Joystick
🎰 Slot Machine
🎲 Game Die
🧩 Jigsaw
🧸 Teddy Bear
♠️ Spade Suit
♥️ Heart Suit
♦️ Diamond Suit
♣️ Club Suit
♟️ Chess Pawn
🃏 Joker
🀄 Mahjong Red Dragon
🎴 Flower Playing Cards
🎭 Performing Arts
🖼️ Framed Picture
🎨 Artist Palette
🔇 Muted Speaker
🔈 Speaker Low Volume
🔉 Speaker Medium Volume
🔊 Speaker High Volume
📢 Loudspeaker
📣 Megaphone
📯 Postal Horn
🔔 Bell
🔕 Bell With Slash
🎼 Musical Score
🎵 Musical Note
🎶 Musical Notes
🎙️ Studio Microphone
🎚️ Level Slider
🎛️ Control Knobs
🎤 Microphone
🎧 Headphone
📻 Radio
🎷 Saxophone
🎸 Guitar
🎹 Musical Keyboard
🎺 Trumpet
🎻 Violin
🥁 Drum
📱 Mobile Phone
📲 Mobile Phone With Arrow
☎️ Telephone
📞 Telephone Receiver
📟 Pager
📠 Fax Machine
🔋 Battery
🔌 Electric Plug
💻 Laptop Computer
🖥️ Desktop Computer
🖨️ Printer
⌨️ Keyboard
🖱️ Computer Mouse
🖲️ Trackball
💽 Computer Disk
💾 Floppy Disk
💿 Optical Disk
📀 DVD
🧮 Abacus
🎥 Movie Camera
🎞️ Film Frames
📽️ Film Projector
🎬 Clapper Board
📺 Television
📷 Camera
📸 Camera With Flash
📹 Video Camera
📼 Videocassette
🔍 Magnifying Glass Tilted Left
🔎 Magnifying Glass Tilted Right
🕯️ Candle
💡 Light Bulb
🔦 Flashlight
🏮 Red Paper Lantern
📔 Notebook With Decorative Cover
📕 Closed Book
📖 Open Book
📗 Green Book
📘 Blue Book
📙 Orange Book
📚 Books
📓 Notebook
📒 Ledger
📃 Page With Curl
📜 Scroll
📄 Page Facing Up
📰 Newspaper
🗞️ Rolled-Up Newspaper
📑 Bookmark Tabs
🔖 Bookmark
🏷️ Label
💰 Money Bag
💴 Yen Banknote
💵 Dollar Banknote
💶 Euro Banknote
💷 Pound Banknote
💸 Money With Wings
💳 Credit Card
🧾 Receipt
💹 Chart Increasing With Yen
💱 Currency Exchange
💲 Heavy Dollar Sign
✉️ Envelope
📧 E-Mail
📨 Incoming Envelope
📩 Envelope With Arrow
📤 Outbox Tray
📥 Inbox Tray
📦 Package
📫 Closed Mailbox With Raised Flag
📪 Closed Mailbox With Lowered Flag
📬 Open Mailbox With Raised Flag
📭 Open Mailbox With Lowered Flag
📮 Postbox
🗳️ Ballot Box With Ballot
✏️ Pencil
✒️ Black Nib
🖋️ Fountain Pen
🖊️ Pen
🖌️ Paintbrush
🖍️ Crayon
📝 Memo
💼 Briefcase
📁 File Folder
📂 Open File Folder
🗂️ Card Index Dividers
📅 Calendar
📆 Tear-Off Calendar
🗒️ Spiral Notepad
🗓️ Spiral Calendar
📇 Card Index
📈 Chart Increasing
📉 Chart Decreasing
📊 Bar Chart
📋 Clipboard
📌 Pushpin
📍 Round Pushpin
📎 Paperclip
🖇️ Linked Paperclips
📏 Straight Ruler
📐 Triangular Ruler
✂️ Scissors
🗃️ Card File Box
🗄️ File Cabinet
🗑️ Wastebasket
🔒 Locked
🔓 Unlocked
🔏 Locked With Pen
🔐 Locked With Key
🔑 Key
🗝️ Old Key
🔨 Hammer
⛏️ Pick
⚒️ Hammer and Pick
🛠️ Hammer and Wrench
🗡️ Dagger
⚔️ Crossed Swords
🔫 Pistol
🏹 Bow and Arrow
🛡️ Shield
🔧 Wrench
🔩 Nut and Bolt
⚙️ Gear
🗜️ Clamp
⚖️ Balance Scale
🔗 Link
⛓️ Chains
🧰 Toolbox
🧲 Magnet
⚗️ Alembic
🧪 Test Tube
🧫 Petri Dish
🧬 DNA
🧯 Fire Extinguisher
🔬 Microscope
🔭 Telescope
📡 Satellite Antenna
💉 Syringe
💊 Pill
🚪 Door
🛏️ Bed
🛋️ Couch and Lamp
🚽 Toilet
🚿 Shower
🛁 Bathtub
🧴 Lotion Bottle
🧵 Thread
🧶 Yarn
🧷 Safety Pin
🧹 Broom
🧺 Basket
🧻 Roll of Toilet Paper
🧼 Soap
🧽 Sponge
🛒 Shopping Cart
🚬 Cigarette
⚰️ Coffin
⚱️ Funeral Urn
🗿 Moai
🏧 Atm Sign
🚮 Litter in Bin Sign
🚰 Potable Water
♿ Wheelchair Symbol
🚹 Men’s Room
🚺 Women’s Room
🚻 Restroom
🚼 Baby Symbol
🚾 Water Closet
🛂 Passport Control
🛃 Customs
🛄 Baggage Claim
🛅 Left Luggage
⚠️ Warning
🚸 Children Crossing
⛔ No Entry
🚫 Prohibited
🚳 No Bicycles
🚭 No Smoking
🚯 No Littering
🚱 Non-Potable Water
🚷 No Pedestrians
📵 No Mobile Phones
🔞 No One Under Eighteen
☢️ Radioactive
☣️ Biohazard
⬆️ Up Arrow
↗️ Up-Right Arrow
➡️ Right Arrow
↘️ Down-Right Arrow
⬇️ Down Arrow
↙️ Down-Left Arrow
⬅️ Left Arrow
↖️ Up-Left Arrow
↕️ Up-Down Arrow
↔️ Left-Right Arrow
↩️ Right Arrow Curving Left
↪️ Left Arrow Curving Right
⤴️ Right Arrow Curving Up
⤵️ Right Arrow Curving Down
🔃 Clockwise Vertical Arrows
🔄 Counterclockwise Arrows Button
🔙 Back Arrow
🔚 End Arrow
🔛 On! Arrow
🔜 Soon Arrow
🔝 Top Arrow
🛐 Place of Worship
⚛️ Atom Symbol
♾️ Infinity
🕉️ Om
✡️ Star of David
☸️ Wheel of Dharma
☯️ Yin Yang
✝️ Latin Cross
☦️ Orthodox Cross
☪️ Star and Crescent
☮️ Peace Symbol
🕎 Menorah
🔯 Dotted Six-Pointed Star
♈ Aries
♉ Taurus
♊ Gemini
♋ Cancer
♌ Leo
♍ Virgo
♎ Libra
♏ Scorpio
♐ Sagittarius
♑ Capricorn
♒ Aquarius
♓ Pisces
⛎ Ophiuchus
🔀 Shuffle Tracks Button
🔁 Repeat Button
🔂 Repeat Single Button
▶️ Play Button
⏩ Fast-Forward Button
⏭️ Next Track Button
⏯️ Play or Pause Button
◀️ Reverse Button
⏪ Fast Reverse Button
⏮️ Last Track Button
🔼 Upwards Button
⏫ Fast Up Button
🔽 Downwards Button
⏬ Fast Down Button
⏸️ Pause Button
⏹️ Stop Button
⏺️ Record Button
⏏️ Eject Button
🎦 Cinema
🔅 Dim Button
🔆 Bright Button
📶 Antenna Bars
📳 Vibration Mode
📴 Mobile Phone Off
♀️ Female Sign
♂️ Male Sign
⚕️ Medical Symbol
♻️ Recycling Symbol
⚜️ Fleur-De-Lis
🔱 Trident Emblem
📛 Name Badge
🔰 Japanese Symbol for Beginner
⭕ Heavy Large Circle
✅ White Heavy Check Mark
☑️ Ballot Box With Check
✔️ Heavy Check Mark
✖️ Heavy Multiplication X
❌ Cross Mark
❎ Cross Mark Button
➕ Heavy Plus Sign
➖ Heavy Minus Sign
➗ Heavy Division Sign
➰ Curly Loop
➿ Double Curly Loop
〽️ Part Alternation Mark
✳️ Eight-Spoked Asterisk
✴️ Eight-Pointed Star
❇️ Sparkle
‼️ Double Exclamation Mark
⁉️ Exclamation Question Mark
❓ Question Mark
❔ White Question Mark
❕ White Exclamation Mark
❗ Exclamation Mark
〰️ Wavy Dash
©️ Copyright
®️ Registered
™️ Trade Mark
#️⃣ Keycap Number Sign
*️⃣ Keycap Asterisk
0️⃣ Keycap Digit Zero
1️⃣ Keycap Digit One
2️⃣ Keycap Digit Two
3️⃣ Keycap Digit Three
4️⃣ Keycap Digit Four
5️⃣ Keycap Digit Five
6️⃣ Keycap Digit Six
7️⃣ Keycap Digit Seven
8️⃣ Keycap Digit Eight
9️⃣ Keycap Digit Nine
🔟 Keycap 10
💯 Hundred Points
🔠 Input Latin Uppercase
🔡 Input Latin Lowercase
🔢 Input Numbers
🔣 Input Symbols
🔤 Input Latin Letters
🅰️ A Button (blood Type)
🆎 Ab Button (blood Type)
🅱️ B Button (blood Type)
🆑 CL Button
🆒 Cool Button
🆓 Free Button
ℹ️ Information
🆔 ID Button
Ⓜ️ Circled M
🆕 New Button
🆖 NG Button
🅾️ O Button (blood Type)
🆗 OK Button
🅿️ P Button
🆘 SOS Button
🆙 Up! Button
🆚 Vs Button
🈁 Japanese “here” Button
🈂️ Japanese “service Charge” Button
🈷️ Japanese “monthly Amount” Button
🈶 Japanese “not Free of Charge” Button
🈯 Japanese “reserved” Button
🉐 Japanese “bargain” Button
🈹 Japanese “discount” Button
🈚 Japanese “free of Charge” Button
🈲 Japanese “prohibited” Button
🉑 Japanese “acceptable” Button
🈸 Japanese “application” Button
🈴 Japanese “passing Grade” Button
🈳 Japanese “vacancy” Button
㊗️ Japanese “congratulations” Button
㊙️ Japanese “secret” Button
🈺 Japanese “open for Business” Button
🈵 Japanese “no Vacancy” Button
▪️ Black Small Square
▫️ White Small Square
◻️ White Medium Square
◼️ Black Medium Square
◽ White Medium-Small Square
◾ Black Medium-Small Square
⬛ Black Large Square
⬜ White Large Square
🔶 Large Orange Diamond
🔷 Large Blue Diamond
🔸 Small Orange Diamond
🔹 Small Blue Diamond
🔺 Red Triangle Pointed Up
🔻 Red Triangle Pointed Down
💠 Diamond With a Dot
🔘 Radio Button
🔲 Black Square Button
🔳 White Square Button
⚪ White Circle
⚫ Black Circle
🔴 Red Circle
🔵 Blue Circle
🏁 Chequered Flag
🚩 Triangular Flag
🎌 Crossed Flags
🏴 Black Flag
🏳️ White Flag
🏳️‍🌈 Rainbow Flag
🏴‍☠️ Pirate Flag
🇦🇨 Ascension Island
🇦🇩 Andorra
🇦🇪 United Arab Emirates
🇦🇫 Afghanistan
🇦🇬 Antigua & Barbuda
🇦🇮 Anguilla
🇦🇱 Albania
🇦🇲 Armenia
🇦🇴 Angola
🇦🇶 Antarctica
🇦🇷 Argentina
🇦🇸 American Samoa
🇦🇹 Austria
🇦🇺 Australia
🇦🇼 Aruba
🇦🇽 Åland Islands
🇦🇿 Azerbaijan
🇧🇦 Bosnia & Herzegovina
🇧🇧 Barbados
🇧🇩 Bangladesh
🇧🇪 Belgium
🇧🇫 Burkina Faso
🇧🇬 Bulgaria
🇧🇭 Bahrain
🇧🇮 Burundi
🇧🇯 Benin
🇧🇱 St. Barthélemy
🇧🇲 Bermuda
🇧🇳 Brunei
🇧🇴 Bolivia
🇧🇶 Caribbean Netherlands
🇧🇷 Brazil
🇧🇸 Bahamas
🇧🇹 Bhutan
🇧🇻 Bouvet Island
🇧🇼 Botswana
🇧🇾 Belarus
🇧🇿 Belize
🇨🇦 Canada
🇨🇨 Cocos (Keeling) Islands
🇨🇩 Congo - Kinshasa
🇨🇫 Central African Republic
🇨🇬 Congo - Brazzaville
🇨🇭 Switzerland
🇨🇮 Côte D’Ivoire
🇨🇰 Cook Islands
🇨🇱 Chile
🇨🇲 Cameroon
🇨🇳 China
🇨🇴 Colombia
🇨🇵 Clipperton Island
🇨🇷 Costa Rica
🇨🇺 Cuba
🇨🇻 Cape Verde
🇨🇼 Curaçao
🇨🇽 Christmas Island
🇨🇾 Cyprus
🇨🇿 Czechia
🇩🇪 Germany
🇩🇬 Diego Garcia
🇩🇯 Djibouti
🇩🇰 Denmark
🇩🇲 Dominica
🇩🇴 Dominican Republic
🇩🇿 Algeria
🇪🇦 Ceuta & Melilla
🇪🇨 Ecuador
🇪🇪 Estonia
🇪🇬 Egypt
🇪🇭 Western Sahara
🇪🇷 Eritrea
🇪🇸 Spain
🇪🇹 Ethiopia
🇪🇺 European Union
🇫🇮 Finland
🇫🇯 Fiji
🇫🇰 Falkland Islands
🇫🇲 Micronesia
🇫🇴 Faroe Islands
🇫🇷 France
🇬🇦 Gabon
🇬🇧 United Kingdom
🇬🇩 Grenada
🇬🇪 Georgia
🇬🇫 French Guiana
🇬🇬 Guernsey
🇬🇭 Ghana
🇬🇮 Gibraltar
🇬🇱 Greenland
🇬🇲 Gambia
🇬🇳 Guinea
🇬🇵 Guadeloupe
🇬🇶 Equatorial Guinea
🇬🇷 Greece
🇬🇸 South Georgia & South Sandwich Islands
🇬🇹 Guatemala
🇬🇺 Guam
🇬🇼 Guinea-Bissau
🇬🇾 Guyana
🇭🇰 Hong Kong SAR China
🇭🇲 Heard & McDonald Islands
🇭🇳 Honduras
🇭🇷 Croatia
🇭🇹 Haiti
🇭🇺 Hungary
🇮🇨 Canary Islands
🇮🇩 Indonesia
🇮🇪 Ireland
🇮🇱 Israel
🇮🇲 Isle of Man
🇮🇳 India
🇮🇴 British Indian Ocean Territory
🇮🇶 Iraq
🇮🇷 Iran
🇮🇸 Iceland
🇮🇹 Italy
🇯🇪 Jersey
🇯🇲 Jamaica
🇯🇴 Jordan
🇯🇵 Japan
🇰🇪 Kenya
🇰🇬 Kyrgyzstan
🇰🇭 Cambodia
🇰🇮 Kiribati
🇰🇲 Comoros
🇰🇳 St. Kitts & Nevis
🇰🇵 North Korea
🇰🇷 South Korea
🇰🇼 Kuwait
🇰🇾 Cayman Islands
🇰🇿 Kazakhstan
🇱🇦 Laos
🇱🇧 Lebanon
🇱🇨 St. Lucia
🇱🇮 Liechtenstein
🇱🇰 Sri Lanka
🇱🇷 Liberia
🇱🇸 Lesotho
🇱🇹 Lithuania
🇱🇺 Luxembourg
🇱🇻 Latvia
🇱🇾 Libya
🇲🇦 Morocco
🇲🇨 Monaco
🇲🇩 Moldova
🇲🇪 Montenegro
🇲🇫 St. Martin
🇲🇬 Madagascar
🇲🇭 Marshall Islands
🇲🇰 Macedonia
🇲🇱 Mali
🇲🇲 Myanmar (Burma)
🇲🇳 Mongolia
🇲🇴 Macau SAR China
🇲🇵 Northern Mariana Islands
🇲🇶 Martinique
🇲🇷 Mauritania
🇲🇸 Montserrat
🇲🇹 Malta
🇲🇺 Mauritius
🇲🇻 Maldives
🇲🇼 Malawi
🇲🇽 Mexico
🇲🇾 Malaysia
🇲🇿 Mozambique
🇳🇦 Namibia
🇳🇨 New Caledonia
🇳🇪 Niger
🇳🇫 Norfolk Island
🇳🇬 Nigeria
🇳🇮 Nicaragua
🇳🇱 Netherlands
🇳🇴 Norway
🇳🇵 Nepal
🇳🇷 Nauru
🇳🇺 Niue
🇳🇿 New Zealand
🇴🇲 Oman
🇵🇦 Panama
🇵🇪 Peru
🇵🇫 French Polynesia
🇵🇬 Papua New Guinea
🇵🇭 Philippines
🇵🇰 Pakistan
🇵🇱 Poland
🇵🇲 St. Pierre & Miquelon
🇵🇳 Pitcairn Islands
🇵🇷 Puerto Rico
🇵🇸 Palestinian Territories
🇵🇹 Portugal
🇵🇼 Palau
🇵🇾 Paraguay
🇶🇦 Qatar
🇷🇪 Réunion
🇷🇴 Romania
🇷🇸 Serbia
🇷🇺 Russia
🇷🇼 Rwanda
🇸🇦 Saudi Arabia
🇸🇧 Solomon Islands
🇸🇨 Seychelles
🇸🇩 Sudan
🇸🇪 Sweden
🇸🇬 Singapore
🇸🇭 St. Helena
🇸🇮 Slovenia
🇸🇯 Svalbard & Jan Mayen
🇸🇰 Slovakia
🇸🇱 Sierra Leone
🇸🇲 San Marino
🇸🇳 Senegal
🇸🇴 Somalia
🇸🇷 Suriname
🇸🇸 South Sudan
🇸🇹 São Tomé & Príncipe
🇸🇻 El Salvador
🇸🇽 Sint Maarten
🇸🇾 Syria
🇸🇿 Swaziland
🇹🇦 Tristan Da Cunha
🇹🇨 Turks & Caicos Islands
🇹🇩 Chad
🇹🇫 French Southern Territories
🇹🇬 Togo
🇹🇭 Thailand
🇹🇯 Tajikistan
🇹🇰 Tokelau
🇹🇱 Timor-Leste
🇹🇲 Turkmenistan
🇹🇳 Tunisia
🇹🇴 Tonga
🇹🇷 Turkey
🇹🇹 Trinidad & Tobago
🇹🇻 Tuvalu
🇹🇼 Taiwan
🇹🇿 Tanzania
🇺🇦 Ukraine
🇺🇬 Uganda
🇺🇲 U.S. Outlying Islands
🇺🇳 United Nations
🇺🇸 United States
🇺🇾 Uruguay
🇺🇿 Uzbekistan
🇻🇦 Vatican City
🇻🇨 St. Vincent & Grenadines
🇻🇪 Venezuela
🇻🇬 British Virgin Islands
🇻🇮 U.S. Virgin Islands
🇻🇳 Vietnam
🇻🇺 Vanuatu
🇼🇫 Wallis & Futuna
🇼🇸 Samoa
🇽🇰 Kosovo
🇾🇪 Yemen
🇾🇹 Mayotte
🇿🇦 South Africa
🇿🇲 Zambia
🇿🇼 Zimbabwe
🏴󠁧󠁢󠁥󠁮󠁧󠁿 England
🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scotland
🏴󠁧󠁢󠁷󠁬󠁳󠁿 Wales
🥆 Rifle
🤻 Modern Pentathlon
🇦 Regional Indicator Symbol Letter A
🇧 Regional Indicator Symbol Letter B
🇨 Regional Indicator Symbol Letter C
🇩 Regional Indicator Symbol Letter D
🇪 Regional Indicator Symbol Letter E
🇫 Regional Indicator Symbol Letter F
🇬 Regional Indicator Symbol Letter G
🇭 Regional Indicator Symbol Letter H
🇮 Regional Indicator Symbol Letter I
🇯 Regional Indicator Symbol Letter J
🇰 Regional Indicator Symbol Letter K
🇱 Regional Indicator Symbol Letter L
🇲 Regional Indicator Symbol Letter M
🇳 Regional Indicator Symbol Letter N
🇴 Regional Indicator Symbol Letter O
🇵 Regional Indicator Symbol Letter P
🇶 Regional Indicator Symbol Letter Q
🇷 Regional Indicator Symbol Letter R
🇸 Regional Indicator Symbol Letter S
🇹 Regional Indicator Symbol Letter T
🇺 Regional Indicator Symbol Letter U
🇻 Regional Indicator Symbol Letter V
🇼 Regional Indicator Symbol Letter W
🇽 Regional Indicator Symbol Letter X
🇾 Regional Indicator Symbol Letter Y
🇿 Regional Indicator Symbol Letter Z
🐱‍🏍 Stunt Cat
🐱‍🚀 Astro Cat
🐱‍🐉 Dino Cat
🐱‍💻 Hacker Cat
🐱‍👤 Ninja Cat
🐱‍👓 Hipster Cat
◯‍◯‍◯‍◯‍◯ Olympic Rings
🏴󠁢󠁩󠁢󠁭󠁿 Flag for Bujumbura (BI-BM)
🏴󠁡󠁺󠁸󠁣󠁩󠁿 Flag for Khojali (AZ-XCI)
🏴󠁡󠁲󠁲󠁿 Flag for Río Negro (AR-R)
🏴󠁢󠁥󠁷󠁡󠁬󠁿 Flag for Wallonia (BE-WAL)
👨🏻‍👨🏻‍👦🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
🏴󠁡󠁺󠁬󠁡󠁮󠁿 Flag for Lankaran District (AZ-LAN)
♴ Recycling Symbol for Type-2 Plastics
🏴󠁡󠁺󠁸󠁩󠁺󠁿 Flag for Khizi (AZ-XIZ)
🏴󠁢󠁧󠀰󠀹󠁿 Flag for Kardzhali (BG-09)
👨🏾‍❤️‍💋‍👩🏽 Kiss - Man: Medium-Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁳󠁩󠀰󠀲󠀲󠁿 Flag for Dol pri Ljubljani (SI-022)
👨🏽‍👩🏽‍👧🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁢󠁩󠁢󠁲󠁿 Flag for Bururi (BI-BR)
🖹 Document with Text
👩🏾‍👦🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁵󠁡󠀴󠀶󠁿 Flag for Lvivshchyna (UA-46)
👩🏿‍👦🏿‍👦🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁡󠁺󠁴󠁯󠁶󠁿 Flag for Tovuz (AZ-TOV)
🏴󠁭󠁫󠀷󠀳󠁿 Flag for Strumica (MK-73)
🏴󠁢󠁩󠁣󠁡󠁿 Flag for Cankuzo (BI-CA)
🏴󠁡󠁺󠁴󠁡󠁲󠁿 Flag for Tartar (AZ-TAR)
🏴󠁡󠁵󠁳󠁡󠁿 Flag for South Australia (AU-SA)
🏴󠁢󠁳󠁨󠁩󠁿 Flag for Harbour Island (BS-HI)
👨🏿‍❤️‍💋‍👨🏻 Kiss - Man: Dark Skin Tone, Man: Light Skin Tone
󠁨 Tag Latin Small Letter H
🏴󠁬󠁶󠀰󠀸󠀵󠁿 Flag for Sala (LV-085)
⚮ Divorce Symbol
⛶ Square Four Corners
🏴󠁢󠁩󠁫󠁩󠁿 Flag for Kirundo (BI-KI)
🏴󠁢󠁩󠁫󠁹󠁿 Flag for Kayanza (BI-KY)
🏴󠁡󠁺󠁵󠁣󠁡󠁿 Flag for Ujar (AZ-UCA)
🏴󠁡󠁺󠁳󠁩󠁹󠁿 Flag for Siazan (AZ-SIY)
󠁗 Tag Latin Capital Letter W
👩🏿‍❤️‍💋‍👨 Kiss - Woman: Dark Skin Tone, Man
🏴󠁢󠁢󠀱󠀱󠁿 Flag for Saint Thomas (BB-11)
🏴󠁢󠁩󠁮󠁧󠁿 Flag for Ngozi (BI-NG)
🏴󠁣󠁦󠁨󠁭󠁿 Flag for Haut-Mbomou (CF-HM)
🏴󠁢󠁩󠁫󠁲󠁿 Flag for Karuzi (BI-KR)
🏴󠁢󠁩󠁭󠁹󠁿 Flag for Muyinga (BI-MY)
🏴󠁣󠁮󠀱󠀲󠁿 Flag for Tianjin (CN-12)
🏴󠁭󠁡󠀱󠀵󠁿 Flag for Laâyoune-Boujdour-Sakia El Hamra (MA-15)
👩🏾‍👨🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁮󠁧󠁦󠁣󠁿 Flag for Federal Capital Territory (NG-FC)
🏴󠁢󠁩󠁲󠁹󠁿 Flag for Ruyigi (BI-RY)
🏴󠁢󠁩󠁭󠁵󠁿 Flag for Muramvya (BI-MU)
🏴󠁢󠁧󠀲󠀷󠁿 Flag for Shumen (BG-27)
⚌ Digram for Greater Yang
🏴󠁡󠁺󠁳󠁭󠁩󠁿 Flag for Shamakhi (AZ-SMI)
👩🏾‍👩🏾‍👧🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🛆 Triangle with Rounded Corners
🕴🏽‍♀️ Woman in Business Suit Levitating: Medium Skin Tone
👩🏼‍❤️‍💋‍👩🏽 Kiss - Woman: Medium-Light Skin Tone, Woman: Medium Skin Tone
🏴󠁢󠁩󠁲󠁭󠁿 Flag for Rumonge (BI-RM)
⚄ Die Face-5
🏴󠁡󠁺󠁳󠁲󠁿 Flag for Shirvan (AZ-SR)
🏴󠁡󠁺󠁳󠁭󠁸󠁿 Flag for Samukh (AZ-SMX)
🏴󠁢󠁪󠁤󠁯󠁿 Flag for Donga (BJ-DO)
👩🏽‍👩🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone
🛦 Up-Pointing Military Airplane
🏴󠁡󠁺󠁳󠁵󠁳󠁿 Flag for Shusha (AZ-SUS)
🏴󠁣󠁨󠁶󠁳󠁿 Flag for Valais (CH-VS)
🏴󠁡󠁺󠁳󠁡󠁿 Flag for Shaki (AZ-SA)
👨🏾‍👨🏾‍👧🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁡󠁦󠁨󠁥󠁬󠁿 Flag for Helmand (AF-HEL)
🏴󠁳󠁩󠀰󠀸󠀵󠁿 Flag for Novo Mesto (SI-085)
⚆ White Circle with Dot Right
🏴󠁡󠁺󠁳󠁢󠁮󠁿 Flag for Shabran (AZ-SBN)
🏴󠁣󠁯󠁣󠁡󠁳󠁿 Flag for Casanare (CO-CAS)
👩🏼‍❤️‍👩 Couple With Heart - Woman: Medium-Light Skin Tone, Woman
🏴󠁢󠁪󠁡󠁬󠁿 Flag for Alibori (BJ-AL)
🏴󠁢󠁦󠀱󠀲󠁿 Flag for Sahel (BF-12)
🏴󠁢󠁪󠁡󠁫󠁿 Flag for Atakora (BJ-AK)
👩‍👦‍👶 Family: Woman, Boy, Baby
♶ Recycling Symbol for Type-4 Plastics
🏴󠁡󠁺󠁳󠁡󠁴󠁿 Flag for Saatly (AZ-SAT)
⚁ Die Face-2
🏴󠁧󠁲󠁡󠁿 Flag for East Macedonia and Thrace (GR-A)
⚐ White Flag
☗ Black Shogi Piece
🏴󠁡󠁺󠁮󠁸󠁿 Flag for Nakhchivan AR (AZ-NX)
🏴󠁡󠁺󠁳󠁡󠁫󠁿 Flag for Shaki District (AZ-SAK)
🏴󠁡󠁺󠁱󠁢󠁡󠁿 Flag for Quba (AZ-QBA)
👩🏻‍👧🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone
🏴󠁡󠁤󠀰󠀶󠁿 Flag for Sant Julià de Lòria (AD-06)
👨🏼‍❤️‍👩🏽 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Medium Skin Tone
🏴󠁳󠁳󠁪󠁧󠁿 Flag for Jonglei (SS-JG)
🏴󠁮󠁺󠁭󠁷󠁴󠁿 Flag for Manawatu-Wanganui (NZ-MWT)
👨‍👩‍👶‍👶 Family: Man, Woman, Baby, Baby
👩🏻‍👨🏻‍👦🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
🏴󠁡󠁺󠁱󠁡󠁺󠁿 Flag for Qazakh (AZ-QAZ)
⚃ Die Face-4
🏴󠁡󠁺󠁳󠁡󠁢󠁿 Flag for Sabirabad (AZ-SAB)
🏴󠁢󠁪󠁢󠁯󠁿 Flag for Borgou (BJ-BO)
🏴󠁭󠁸󠁳󠁬󠁰󠁿 Flag for San Luis Potosí (MX-SLP)
👨🏼‍❤️‍💋‍👨🏾 Kiss - Man: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
☈ Thunderstorm
🏴󠁢󠁧󠀲󠀱󠁿 Flag for Smolyan (BG-21)
🏴󠁵󠁳󠁮󠁤󠁿 Flag for North Dakota (US-ND)
🀥 Mahjong Tile Chrysanthemum
🏴󠁥󠁧󠁢󠁡󠁿 Flag for Red Sea (EG-BA)
🏴󠁡󠁧󠀰󠀷󠁿 Flag for Saint Peter (AG-07)
👨🏿‍👨🏿‍👶🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁢󠁪󠁺󠁯󠁿 Flag for Zou (BJ-ZO)
👩🏿‍❤️‍💋‍👩 Kiss - Woman: Dark Skin Tone, Woman
🏴󠁢󠁪󠁬󠁩󠁿 Flag for Littoral (BJ-LI)
🏴󠁡󠁺󠁣󠁡󠁬󠁿 Flag for Jalilabad (AZ-CAL)
🏴󠁬󠁲󠁭󠁹󠁿 Flag for Maryland (LR-MY)
🏴󠁣󠁮󠀷󠀱󠁿 Flag for Taiwan (CN-71)
🏴󠁡󠁲󠁥󠁿 Flag for Entre Ríos (AR-E)
👩🏿‍❤️‍💋‍👨🏽 Kiss - Woman: Dark Skin Tone, Man: Medium Skin Tone
🏴󠁡󠁺󠁱󠁵󠁳󠁿 Flag for Qusar (AZ-QUS)
👩🏽‍❤️‍👨🏽 Couple With Heart - Woman: Medium Skin Tone, Man: Medium Skin Tone
👨‍❤️‍💋‍👩🏻 Kiss - Man, Woman: Light Skin Tone
⚂ Die Face-3
🏴󠁴󠁭󠁳󠁿 Flag for Aşgabat (TM-S)
🏴󠁫󠁥󠀴󠀲󠁿 Flag for Trans Nzoia (KE-42)
🏴󠁢󠁪󠁯󠁵󠁿 Flag for Ouémé (BJ-OU)
🏴󠁭󠁫󠀵󠀳󠁿 Flag for Mogila (MK-53)
🏴󠁣󠁨󠁵󠁲󠁿 Flag for Uri (CH-UR)
🏴󠁵󠁳󠁣󠁯󠁿 Flag for Colorado (US-CO)
👨🏾‍❤️‍💋‍👩🏿 Kiss - Man: Medium-Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁮󠁬󠁺󠁨󠁿 Flag for South Holland (NL-ZH)
👨‍👩‍👧‍👶 Family: Man, Woman, Girl, Baby
🏴󠁳󠁩󠀲󠀰󠀶󠁿 Flag for Šmarješke Toplice (SI-206)
👩🏽‍❤️‍👨🏼 Couple With Heart - Woman: Medium Skin Tone, Man: Medium-Light Skin Tone
⚬ Medium Small White Circle
👩🏾‍❤️‍👩🏻 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Light Skin Tone
👩🏼‍❤️‍👨 Couple With Heart - Woman: Medium-Light Skin Tone, Man
🏴󠁢󠁮󠁴󠁵󠁿 Flag for Tutong (BN-TU)
🏴󠁡󠁺󠁯󠁧󠁵󠁿 Flag for Oghuz (AZ-OGU)
🏴󠁬󠁢󠁢󠁩󠁿 Flag for Beqaa (LB-BI)
🏴󠁢󠁧󠀰󠀶󠁿 Flag for Vratsa (BG-06)
👨🏽‍👩🏽‍👶🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👨🏽‍❤️‍👩🏼 Couple With Heart - Man: Medium Skin Tone, Woman: Medium-Light Skin Tone
☴ Trigram for Wind
⛛ Heavy White Down-Pointing Triangle
🏴󠁡󠁺󠁱󠁡󠁢󠁿 Flag for Qabala (AZ-QAB)
🏴󠁣󠁤󠁳󠁵󠁿 Flag for Sud-Ubangi (CD-SU)
♳ Recycling Symbol for Type-1 Plastics
🏴󠁶󠁥󠁹󠁿 Flag for Delta Amacuro (VE-Y)
👩🏿‍❤️‍💋‍👩🏿 Kiss - Woman: Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁢󠁯󠁬󠁿 Flag for La Paz (BO-L)
🏴󠁢󠁯󠁮󠁿 Flag for Pando (BO-N)
🏴󠁣󠁦󠁮󠁭󠁿 Flag for Nana-Mambéré (CF-NM)
🏴󠁭󠁫󠀲󠀷󠁿 Flag for Dolneni (MK-27)
👩‍❤️‍💋‍👩🏾 Kiss - Woman, Woman: Medium-Dark Skin Tone
♷ Recycling Symbol for Type-5 Plastics
👩🏾‍❤️‍👨🏽 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Medium Skin Tone
🏴󠁡󠁺󠁱󠁯󠁢󠁿 Flag for Gobustan (AZ-QOB)
👩🏽‍👦🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone
👨🏿‍👩🏿‍👶🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
👩🏻‍❤️‍👨🏾 Couple With Heart - Woman: Light Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁲󠁯󠁢󠁶󠁿 Flag for Braşov (RO-BV)
🏴󠁢󠁧󠀲󠀴󠁿 Flag for Stara Zagora (BG-24)
🏴󠁧󠁨󠁡󠁨󠁿 Flag for Ashanti (GH-AH)
🏴󠁡󠁺󠁱󠁢󠁩󠁿 Flag for Qubadli (AZ-QBI)
🏴󠁭󠁮󠀰󠀳󠀹󠁿 Flag for Khentii (MN-039)
🏴󠁶󠁮󠁳󠁧󠁿 Flag for Ho Chi Minh City (VN-SG)
👨‍👨‍👶‍👦 Family: Man, Man, Baby, Boy
⛟ Black Truck
🏴󠁢󠁯󠁨󠁿 Flag for Chuquisaca (BO-H)
🏴󠁡󠁺󠁱󠁡󠁸󠁿 Flag for Qakh (AZ-QAX)
⚟ Three Lines Converging Left
🏴󠁵󠁳󠁮󠁥󠁿 Flag for Nebraska (US-NE)
🏴󠁥󠁳󠁭󠁤󠁿 Flag for Madrid Autonomous Community (ES-MD)
🏴󠁭󠁤󠁴󠁡󠁿 Flag for Taraclia (MD-TA)
♡ White Heart Suit
🏴󠁢󠁡󠁢󠁲󠁣󠁿 Flag for Brčko District (BA-BRC)
🏴󠁴󠁷󠁫󠁨󠁨󠁿 Flag for Kaohsiung (TW-KHH)
🏴󠁬󠁴󠁫󠁵󠁿 Flag for Kaunas County (LT-KU)
󠀫 Tag Plus Sign
🏴󠁡󠁬󠀰󠀵󠁿 Flag for Gjirokastër County (AL-05)
👨🏻‍❤️‍👩🏿 Couple With Heart - Man: Light Skin Tone, Woman: Dark Skin Tone
🏴󠁣󠁡󠁯󠁮󠁿 Flag for Ontario (CA-ON)
🏴󠁥󠁣󠁮󠁿 Flag for Napo (EC-N)
🏴󠁢󠁯󠁣󠁿 Flag for Cochabamba (BO-C)
👩🏽‍❤️‍👨🏾 Couple With Heart - Woman: Medium Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁳󠁣󠀲󠀵󠁿 Flag for Roche Caiman (SC-25)
🏴󠁭󠁫󠀴󠀰󠁿 Flag for Kičevo (MK-40)
👩🏾‍❤️‍👨 Couple With Heart - Woman: Medium-Dark Skin Tone, Man
👩🏾‍❤️‍👩🏿 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Dark Skin Tone
☱ Trigram for Lake
👩‍❤️‍💋‍👨🏻 Kiss - Woman, Man: Light Skin Tone
♩ Quarter Note
⚅ Die Face-6
👩🏿‍❤️‍👨🏻 Couple With Heart - Woman: Dark Skin Tone, Man: Light Skin Tone
♱ East Syriac Cross
🏴󠁡󠁺󠁩󠁳󠁭󠁿 Flag for Ismailli (AZ-ISM)
🏴󠁴󠁲󠀲󠀹󠁿 Flag for Gümüşhane (TR-29)
🏴󠁮󠁡󠁫󠁥󠁿 Flag for Kavango East (NA-KE)
👨🏿‍👧🏿‍👧🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
⚏ Digram for Greater Yin
🏴󠁰󠁴󠀰󠀸󠁿 Flag for Faro (PT-08)
🏴󠁣󠁵󠀱󠀰󠁿 Flag for Las Tunas (CU-10)
♙ White Chess Pawn
👩‍👩‍👦‍👶 Family: Woman, Woman, Boy, Baby
🏴󠁭󠁵󠁢󠁲󠁿 Flag for Beau-Bassin Rose-Hill (MU-BR)
👩🏿‍❤️‍👩🏼 Couple With Heart - Woman: Dark Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁬󠁴󠀳󠀲󠁿 Flag for Panevėžio Municipality (LT-32)
👩🏾‍❤️‍💋‍👩🏼 Kiss - Woman: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁲󠁵󠁡󠁬󠁴󠁿 Flag for Altai Krai (RU-ALT)
👨🏼‍❤️‍👨🏻 Couple With Heart - Man: Medium-Light Skin Tone, Man: Light Skin Tone
👨🏿‍❤️‍💋‍👨🏾 Kiss - Man: Dark Skin Tone, Man: Medium-Dark Skin Tone
👩🏿‍❤️‍👩🏽 Couple With Heart - Woman: Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁢󠁮󠁴󠁥󠁿 Flag for Temburong (BN-TE)
🏴󠁢󠁮󠁢󠁥󠁿 Flag for Belait (BN-BE)
♆ Neptune
👨🏿‍❤️‍💋‍👩🏾 Kiss - Man: Dark Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁢󠁯󠁰󠁿 Flag for Potosí (BO-P)
🏴󠁡󠁺󠁮󠁥󠁦󠁿 Flag for Neftchala (AZ-NEF)
👩🏻‍👧🏻‍👶🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
🏴󠁭󠁡󠀰󠀱󠁿 Flag for Tangier-Tétouan (MA-01)
👨🏼‍❤️‍💋‍👨🏽 Kiss - Man: Medium-Light Skin Tone, Man: Medium Skin Tone
♚ Black Chess King
👩🏻‍❤️‍💋‍👩🏽 Kiss - Woman: Light Skin Tone, Woman: Medium Skin Tone
🏴󠁳󠁩󠀰󠀱󠀱󠁿 Flag for Celje (SI-011)
👨🏼‍❤️‍💋‍👨🏼 Kiss - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
👨🏽‍❤️‍👨🏻 Couple With Heart - Man: Medium Skin Tone, Man: Light Skin Tone
👩🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁩󠁲󠀱󠀹󠁿 Flag for Gilan (IR-19)
👨🏽‍❤️‍💋‍👩🏻 Kiss - Man: Medium Skin Tone, Woman: Light Skin Tone
👨🏽‍❤️‍💋‍👨🏽 Kiss - Man: Medium Skin Tone, Man: Medium Skin Tone
🤵🏼‍♀️ Woman in Tuxedo: Medium-Light Skin Tone
👩🏽‍❤️‍💋‍👩🏿 Kiss - Woman: Medium Skin Tone, Woman: Dark Skin Tone
🏴󠁡󠁤󠀰󠀷󠁿 Flag for Andorra la Vella (AD-07)
👨🏾‍❤️‍💋‍👨🏼 Kiss - Man: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
🏴󠁧󠁢󠁮󠁩󠁲󠁿 Flag for Northern Ireland (GB-NIR)
👩🏻‍❤️‍💋‍👩🏼 Kiss - Woman: Light Skin Tone, Woman: Medium-Light Skin Tone
👨🏾‍❤️‍💋‍👨🏿 Kiss - Man: Medium-Dark Skin Tone, Man: Dark Skin Tone
🏴󠁥󠁧󠁦󠁹󠁭󠁿 Flag for Faiyum (EG-FYM)
🏴󠁢󠁲󠁡󠁣󠁿 Flag for Acre (BR-AC)
⚞ Three Lines Converging Right
🏴󠁭󠁸󠁪󠁡󠁬󠁿 Flag for Jalisco (MX-JAL)
👨🏾‍❤️‍💋‍👨🏾 Kiss - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁭󠁸󠁣󠁭󠁸󠁿 Flag for Ciudad de Mexico (MX-CMX)
👩🏼‍👨🏼‍👦🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩‍❤️‍💋‍👨🏾 Kiss - Woman, Man: Medium-Dark Skin Tone
♇ Pluto
👩🏿‍❤️‍💋‍👨🏿 Kiss - Woman: Dark Skin Tone, Man: Dark Skin Tone
👨🏿‍❤️‍💋‍👨🏼 Kiss - Man: Dark Skin Tone, Man: Medium-Light Skin Tone
󠀥 Tag Percent Sign
🏴󠁫󠁨󠀱󠀳󠁿 Flag for Preah Vihear (KH-13)
👨🏾‍❤️‍💋‍👨 Kiss - Man: Medium-Dark Skin Tone, Man
♖ White Chess Rook
🏴󠁢󠁪󠁣󠁯󠁿 Flag for Collines (BJ-CO)
🏴󠁡󠁺󠁭󠁡󠁳󠁿 Flag for Masally (AZ-MAS)
👩🏿‍❤️‍💋‍👩🏻 Kiss - Woman: Dark Skin Tone, Woman: Light Skin Tone
👨🏽‍❤️‍👩🏽 Couple With Heart - Man: Medium Skin Tone, Woman: Medium Skin Tone
👩🏾‍❤️‍💋‍👩🏿 Kiss - Woman: Medium-Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁢󠁪󠁰󠁬󠁿 Flag for Plateau (BJ-PL)
👨🏻‍❤️‍👨🏽 Couple With Heart - Man: Light Skin Tone, Man: Medium Skin Tone
👨🏽‍❤️‍👩🏻 Couple With Heart - Man: Medium Skin Tone, Woman: Light Skin Tone
🏴󠁡󠁺󠁭󠁩󠁿 Flag for Mingachevir (AZ-MI)
👩🏿‍❤️‍💋‍👨🏼 Kiss - Woman: Dark Skin Tone, Man: Medium-Light Skin Tone
♕ White Chess Queen
👩🏽‍❤️‍💋‍👨🏾 Kiss - Woman: Medium Skin Tone, Man: Medium-Dark Skin Tone
👩🏾‍❤️‍💋‍👩🏻 Kiss - Woman: Medium-Dark Skin Tone, Woman: Light Skin Tone
👩‍👩‍👶‍👧 Family: Woman, Woman, Baby, Girl
߷ NKo Symbol Gbakurunen
👩🏿‍❤️‍💋‍👩🏾 Kiss - Woman: Dark Skin Tone, Woman: Medium-Dark Skin Tone
👩🏻‍👦🏻‍👧🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
🏴󠁡󠁺󠁬󠁥󠁲󠁿 Flag for Lerik (AZ-LER)
🏴󠁳󠁶󠁳󠁳󠁿 Flag for San Salvador (SV-SS)
👨🏽‍👦🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁲󠁵󠁣󠁥󠁿 Flag for Chechen (RU-CE)
󠁇 Tag Latin Capital Letter G
👨🏼‍👩🏼‍👦🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👨🏾‍❤️‍👨🏼 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
󠁡 Tag Latin Small Letter a
🏴󠁡󠁺󠁮󠁡󠁿 Flag for Naftalan (AZ-NA)
🏴󠁢󠁦󠀱󠀳󠁿 Flag for Sud-Ouest (BF-13)
🏴󠁴󠁲󠀳󠀴󠁿 Flag for Istanbul (TR-34)
🎔 Heart with Tip On the Left
👨🏽‍❤️‍👨🏽 Couple With Heart - Man: Medium Skin Tone, Man: Medium Skin Tone
👩🏽‍❤️‍👩🏽 Couple With Heart - Woman: Medium Skin Tone, Woman: Medium Skin Tone
♁ Earth
👨🏽‍❤️‍👨🏾 Couple With Heart - Man: Medium Skin Tone, Man: Medium-Dark Skin Tone
👨🏾‍❤️‍👩🏽 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Medium Skin Tone
󠁉 Tag Latin Capital Letter I
👩🏼‍❤️‍👩🏻 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Light Skin Tone
󠁬 Tag Latin Small Letter L
👨🏿‍❤️‍👩🏼 Couple With Heart - Man: Dark Skin Tone, Woman: Medium-Light Skin Tone
👨🏼‍❤️‍👨🏼 Couple With Heart - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
👨🏻‍❤️‍👨 Couple With Heart - Man: Light Skin Tone, Man
👩🏽‍👩🏽‍👧🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
🎝 Beamed Descending Musical Notes
👨🏾‍❤️‍👩🏿 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁢󠁲󠁲󠁯󠁿 Flag for Rondônia (BR-RO)
♄ Saturn
☖ White Shogi Piece
👨🏾‍❤️‍💋‍👩🏻 Kiss - Man: Medium-Dark Skin Tone, Woman: Light Skin Tone
👨🏾‍❤️‍👨🏿 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Dark Skin Tone
🏴󠁢󠁧󠀰󠀲󠁿 Flag for Burgas (BG-02)
🏴󠁢󠁦󠀰󠀹󠁿 Flag for Hauts-Bassins (BF-09)
👩🏾‍❤️‍💋‍👩🏾 Kiss - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
👨🏼‍❤️‍👨🏽 Couple With Heart - Man: Medium-Light Skin Tone, Man: Medium Skin Tone
👨🏿‍❤️‍👩🏾 Couple With Heart - Man: Dark Skin Tone, Woman: Medium-Dark Skin Tone
👨🏿‍❤️‍👨🏻 Couple With Heart - Man: Dark Skin Tone, Man: Light Skin Tone
🏴󠁢󠁲󠁡󠁬󠁿 Flag for Alagoas (BR-AL)
🏴󠁪󠁰󠀴󠀷󠁿 Flag for Okinawa (JP-47)
👨🏿‍❤️‍👩🏽 Couple With Heart - Man: Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁫󠁥󠀴󠀰󠁿 Flag for Tana River (KE-40)
👨🏿‍👶🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone
👨🏿‍👩🏿‍👶🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
👩🏻‍👶🏻‍👧🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
🏴󠁩󠁲󠀲󠀹󠁿 Flag for South Khorasan (IR-29)
🏴󠁡󠁺󠁬󠁡󠁿 Flag for Lankaran (AZ-LA)
👩🏼‍❤️‍👩🏾 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
👨‍👨‍👧‍👶 Family: Man, Man, Girl, Baby
🕴️‍♀️ Woman in Business Suit Levitating
🏴󠁢󠁲󠁲󠁮󠁿 Flag for Rio Grande do Norte (BR-RN)
♅ Uranus
🏴󠁡󠁺󠁧󠁡󠁤󠁿 Flag for Gadabay (AZ-GAD)
☵ Trigram for Water
👩🏽‍❤️‍💋‍👩🏽 Kiss - Woman: Medium Skin Tone, Woman: Medium Skin Tone
🏴󠁡󠁴󠀹󠁿 Flag for Vienna (AT-9)
🏴󠁢󠁲󠁳󠁥󠁿 Flag for Sergipe (BR-SE)
👨🏻‍👦🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone
🏴󠁡󠁦󠁴󠁡󠁫󠁿 Flag for Takhar (AF-TAK)
⚝ Outlined White Star
👩🏼‍👧🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏾‍❤️‍💋‍👩🏽 Kiss - Woman: Medium-Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁬󠁶󠀰󠀲󠀵󠁿 Flag for Daugavpils Municipality (LV-025)
👩‍❤️‍👨🏼 Couple With Heart - Woman, Man: Medium-Light Skin Tone
🏴󠁡󠁺󠁬󠁡󠁣󠁿 Flag for Lachin (AZ-LAC)
☙ Reversed Rotated Floral Heart Bullet
👩🏼‍❤️‍👩🏽 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Medium Skin Tone
🏴󠁲󠁯󠁧󠁪󠁿 Flag for Gorj (RO-GJ)
🏴󠁡󠁺󠁢󠁡󠁿 Flag for Baku (AZ-BA)
🏴󠁡󠁺󠁩󠁭󠁩󠁿 Flag for Imishli (AZ-IMI)
🏴󠁬󠁡󠁸󠁥󠁿 Flag for Sekong (LA-XE)
🏴󠁢󠁪󠁫󠁯󠁿 Flag for Kouffo (BJ-KO)
👨🏼‍❤️‍👩🏻 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Light Skin Tone
🏴󠁢󠁲󠁲󠁲󠁿 Flag for Roraima (BR-RR)
⛮ Gear with Handles
🏴󠁢󠁩󠁢󠁬󠁿 Flag for Bujumbura Rural (BI-BL)
🏴󠁥󠁲󠁳󠁫󠁿 Flag for Northern Red Sea (ER-SK)
󠁛 Tag Left Square Bracket
⛯ Map Symbol for Lighthouse
👨🏻‍👨🏻‍👧🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
🏴󠁡󠁺󠁸󠁡󠁣󠁿 Flag for Khachmaz (AZ-XAC)
👨🏿‍❤️‍👩 Couple With Heart - Man: Dark Skin Tone, Woman
🏴󠁭󠁤󠁳󠁴󠁿 Flag for Strășeni (MD-ST)
☤ Caduceus
🏴󠁤󠁺󠀱󠀴󠁿 Flag for Tiaret (DZ-14)
🕾 White Touchtone Telephone
👨🏼‍❤️‍💋‍👨🏿 Kiss - Man: Medium-Light Skin Tone, Man: Dark Skin Tone
☡ Caution Sign
🏴󠁮󠁯󠀱󠀴󠁿 Flag for Sogn og Fjordane (NO-14)
🏴󠁣󠁤󠁴󠁡󠁿 Flag for Tanganyika (CD-TA)
🏴󠁳󠁩󠀱󠀸󠀲󠁿 Flag for Sveti Andraž v Slovenskih Goricah (SI-182)
🏴󠁢󠁳󠁢󠁩󠁿 Flag for Bimini (BS-BI)
👨🏿‍❤️‍👨🏽 Couple With Heart - Man: Dark Skin Tone, Man: Medium Skin Tone
👩🏾‍❤️‍👨🏿 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Dark Skin Tone
♪ Eighth Note
👩🏼‍❤️‍👨🏿 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Dark Skin Tone
🏴󠁶󠁮󠀴󠀹󠁿 Flag for Vĩnh Long (VN-49)
󠀻 Tag Semicolon
🏴󠁣󠁡󠁮󠁢󠁿 Flag for New Brunswick (CA-NB)
👨🏾‍👩🏾‍👧🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁲󠁵󠁬󠁥󠁮󠁿 Flag for Leningrad (RU-LEN)
☨ Cross of Lorraine
🏴󠁢󠁲󠁴󠁯󠁿 Flag for Tocantins (BR-TO)
👨🏼‍❤️‍💋‍👩🏼 Kiss - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁴󠁨󠀱󠀶󠁿 Flag for Lopburi (TH-16)
☲ Trigram for Fire
☧ Chi Rho
👨🏿‍❤️‍👨🏾 Couple With Heart - Man: Dark Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁢󠁳󠁣󠁥󠁿 Flag for Central Eleuthera (BS-CE)
🏴󠁢󠁳󠁥󠁧󠁿 Flag for East Grand Bahama (BS-EG)
👨🏾‍👶🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁮󠁧󠁣󠁲󠁿 Flag for Cross River (NG-CR)
👨🏻‍👧🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone
⛋ White Diamond In Square
🏴󠁢󠁩󠁭󠁡󠁿 Flag for Makamba (BI-MA)
👩🏻‍👶🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone
👩🏾‍❤️‍👩🏼 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁢󠁳󠁣󠁫󠁿 Flag for Crooked Island (BS-CK)
󠁘 Tag Latin Capital Letter X
🏴󠁲󠁵󠁢󠁲󠁹󠁿 Flag for Bryansk (RU-BRY)
🏴󠁧󠁲󠁬󠁿 Flag for South Aegean (GR-L)
☐ Ballot Box
👨🏽‍❤️‍💋‍👩🏾 Kiss - Man: Medium Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁢󠁳󠁥󠁸󠁿 Flag for Exuma (BS-EX)
🏴󠁩󠁤󠁫󠁡󠁿 Flag for Kalimantan (ID-KA)
👨🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨🏽‍👦🏽‍👧🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
👨🏻‍❤️‍💋‍👩 Kiss - Man: Light Skin Tone, Woman
👩🏾‍❤️‍💋‍👨🏼 Kiss - Woman: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
🀚 Mahjong Tile Two of Circles
🏴󠁢󠁳󠁧󠁣󠁿 Flag for Grand Cay (BS-GC)
🏴󠁬󠁶󠀰󠀷󠀷󠁿 Flag for Rēzekne Municipality (LV-077)
👩🏿‍❤️‍👨🏾 Couple With Heart - Woman: Dark Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁮󠁯󠀱󠀰󠁿 Flag for Vest-Agder (NO-10)
🏴󠁡󠁭󠁴󠁶󠁿 Flag for Tavush (AM-TV)
🖠 Sideways Black Up Pointing Index
🏴󠁢󠁳󠁩󠁮󠁿 Flag for Inagua (BS-IN)
🏴󠁢󠁳󠁦󠁰󠁿 Flag for Freeport (BS-FP)
🏴󠁢󠁳󠁮󠁯󠁿 Flag for North Abaco (BS-NO)
🏴󠁲󠁵󠁭󠁯󠁷󠁿 Flag for Moscow (RU-MOW)
👨🏼‍👩🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁳󠁩󠀰󠀰󠀴󠁿 Flag for Bohinj (SI-004)
👨🏽‍👨🏽‍👦🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁢󠁳󠁭󠁧󠁿 Flag for Mayaguana (BS-MG)
★ Black Star
⛦ Left-Handed Interlaced Pentagram
♝ Black Chess Bishop
🏴󠁢󠁲󠁤󠁦󠁿 Flag for Federal District (BR-DF)
🏴󠁡󠁺󠁨󠁡󠁣󠁿 Flag for Hajigabul (AZ-HAC)
🏴󠁣󠁵󠀱󠀳󠁿 Flag for Santiago de Cuba (CU-13)
🏴󠁡󠁺󠁧󠁹󠁧󠁿 Flag for Goygol (AZ-GYG)
🏴󠁩󠁲󠀱󠀳󠁿 Flag for Sistan and Baluchestan (IR-13)
👨🏿‍👦🏿‍👧🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁦󠁪󠁥󠁿 Flag for Eastern (FJ-E)
👩🏼‍👩🏼‍👧🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁡󠁭󠁥󠁲󠁿 Flag for Yerevan (AM-ER)
👩🏿‍❤️‍👩🏻 Couple With Heart - Woman: Dark Skin Tone, Woman: Light Skin Tone
🏴󠁣󠁮󠀳󠀱󠁿 Flag for Shanghai (CN-31)
🏴󠁡󠁺󠁧󠁯󠁲󠁿 Flag for Goranboy (AZ-GOR)
🏴󠁢󠁳󠁮󠁳󠁿 Flag for North Andros (BS-NS)
🏴󠁴󠁶󠁦󠁵󠁮󠁿 Flag for Funafuti (TV-FUN)
👩🏿‍❤️‍👨🏽 Couple With Heart - Woman: Dark Skin Tone, Man: Medium Skin Tone
🏴󠁭󠁸󠁤󠁵󠁲󠁿 Flag for Durango (MX-DUR)
🕮 Book
👩🏼‍❤️‍👨🏼 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
👩🏾‍👦🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👨‍👨‍👶 Family: Man, Man, Baby
🏴󠁮󠁬󠁢󠁱󠀱󠁿 Flag for Bonaire (NL-BQ1)
󠁮 Tag Latin Small Letter N
🏴󠁩󠁲󠀰󠀱󠁿 Flag for East Azerbaijan (IR-01)
👨🏾‍👩🏾‍👦🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👨🏿‍👩🏿‍👦🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
👩🏿‍❤️‍👨 Couple With Heart - Woman: Dark Skin Tone, Man
👨🏻‍❤️‍💋‍👨 Kiss - Man: Light Skin Tone, Man
👨‍❤️‍💋‍👩🏾 Kiss - Man, Woman: Medium-Dark Skin Tone
🏴󠁱󠁡󠁵󠁳󠁿 Flag for Umm Salal (QA-US)
👩‍👨‍👦‍👶 Family: Woman, Man, Boy, Baby
👨‍👦‍👶 Family: Man, Boy, Baby
👨🏼‍❤️‍💋‍👩🏾 Kiss - Man: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
👨🏾‍❤️‍💋‍👨🏻 Kiss - Man: Medium-Dark Skin Tone, Man: Light Skin Tone
♽ Partially-Recycled Paper Symbol
👨🏿‍👨🏿‍👦🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
👨🏻‍❤️‍💋‍👨🏿 Kiss - Man: Light Skin Tone, Man: Dark Skin Tone
🏴󠁢󠁳󠁳󠁡󠁿 Flag for South Andros (BS-SA)
🏴󠁡󠁺󠁧󠁯󠁹󠁿 Flag for Goychay (AZ-GOY)
👩‍❤️‍💋‍👩🏿 Kiss - Woman, Woman: Dark Skin Tone
🏴󠁢󠁳󠁳󠁥󠁿 Flag for South Eleuthera (BS-SE)
🏴󠁢󠁲󠁡󠁭󠁿 Flag for Amazonas (BR-AM)
👨🏽‍👦🏽‍👶🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
👨🏾‍❤️‍💋‍👩🏼 Kiss - Man: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
👨🏻‍❤️‍💋‍👨🏼 Kiss - Man: Light Skin Tone, Man: Medium-Light Skin Tone
👨🏻‍❤️‍💋‍👩🏻 Kiss - Man: Light Skin Tone, Woman: Light Skin Tone
👨‍❤️‍💋‍👨🏻 Kiss - Man, Man: Light Skin Tone
👩🏼‍❤️‍💋‍👨🏿 Kiss - Woman: Medium-Light Skin Tone, Man: Dark Skin Tone
👨🏼‍❤️‍💋‍👩🏽 Kiss - Man: Medium-Light Skin Tone, Woman: Medium Skin Tone
👩🏿‍❤️‍💋‍👨🏻 Kiss - Woman: Dark Skin Tone, Man: Light Skin Tone
👩‍❤️‍💋‍👩🏻 Kiss - Woman, Woman: Light Skin Tone
👩🏽‍❤️‍👩 Couple With Heart - Woman: Medium Skin Tone, Woman
🏴󠁭󠁸󠁡󠁧󠁵󠁿 Flag for Aguascalientes (MX-AGU)
👩‍👶‍👧 Family: Woman, Baby, Girl
🏴󠁭󠁣󠁰󠁨󠁿 Flag for Port Hercules (MC-PH)
🖛 Sideways Black Right Pointing Index
󠀢 Tag Quotation Mark
🏴󠁧󠁥󠁫󠁫󠁿 Flag for Kvemo Kartli (GE-KK)
👩🏽‍❤️‍👨 Couple With Heart - Woman: Medium Skin Tone, Man
🏴󠁡󠁺󠁤󠁡󠁳󠁿 Flag for Dashkasan (AZ-DAS)
👩🏾‍❤️‍💋‍👨🏻 Kiss - Woman: Medium-Dark Skin Tone, Man: Light Skin Tone
👩🏽‍❤️‍💋‍👨 Kiss - Woman: Medium Skin Tone, Man
👨‍❤️‍👨🏼 Couple With Heart - Man, Man: Medium-Light Skin Tone
👩🏾‍❤️‍💋‍👨🏿 Kiss - Woman: Medium-Dark Skin Tone, Man: Dark Skin Tone
👨🏿‍❤️‍💋‍👩🏿 Kiss - Man: Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁡󠁬󠀰󠀱󠁿 Flag for Berat County (AL-01)
👩🏿‍❤️‍💋‍👨🏾 Kiss - Woman: Dark Skin Tone, Man: Medium-Dark Skin Tone
👨🏿‍❤️‍💋‍👨🏿 Kiss - Man: Dark Skin Tone, Man: Dark Skin Tone
👨🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏻‍❤️‍💋‍👨🏾 Kiss - Woman: Light Skin Tone, Man: Medium-Dark Skin Tone
👨‍❤️‍💋‍👩🏼 Kiss - Man, Woman: Medium-Light Skin Tone
👩🏽‍❤️‍💋‍👨🏿 Kiss - Woman: Medium Skin Tone, Man: Dark Skin Tone
👩🏼‍❤️‍💋‍👩🏾 Kiss - Woman: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
👩🏻‍❤️‍💋‍👨 Kiss - Woman: Light Skin Tone, Man
🏴󠁢󠁳󠁳󠁯󠁿 Flag for South Abaco (BS-SO)
👩🏿‍❤️‍💋‍👩🏼 Kiss - Woman: Dark Skin Tone, Woman: Medium-Light Skin Tone
⚎ Digram for Lesser Yang
🏴󠁥󠁳󠁧󠁡󠁿 Flag for Galicia (ES-GA)
👨🏿‍❤️‍👨🏼 Couple With Heart - Man: Dark Skin Tone, Man: Medium-Light Skin Tone
👨🏼‍❤️‍👨🏿 Couple With Heart - Man: Medium-Light Skin Tone, Man: Dark Skin Tone
👨🏼‍❤️‍👩🏼 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
👨🏽‍❤️‍👨🏿 Couple With Heart - Man: Medium Skin Tone, Man: Dark Skin Tone
🏴󠁡󠁺󠁦󠁵󠁺󠁿 Flag for Fizuli (AZ-FUZ)
👩🏻‍❤️‍💋‍👨🏻 Kiss - Woman: Light Skin Tone, Man: Light Skin Tone
👩🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁢󠁳󠁲󠁣󠁿 Flag for Rum Cay (BS-RC)
🏴󠁡󠁺󠁢󠁥󠁹󠁿 Flag for Beylagan (AZ-BEY)
🏴󠁡󠁺󠁢󠁡󠁲󠁿 Flag for Barda (AZ-BAR)
👨🏽‍👨🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone
👩‍❤️‍👨🏾 Couple With Heart - Woman, Man: Medium-Dark Skin Tone
👩‍❤️‍👩🏼 Couple With Heart - Woman, Woman: Medium-Light Skin Tone
👨🏼‍❤️‍👩🏿 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Dark Skin Tone
🏴󠁢󠁳󠁮󠁥󠁿 Flag for North Eleuthera (BS-NE)
⚊ Monogram for Yang
👩🏼‍❤️‍💋‍👩🏼 Kiss - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁡󠁺󠁢󠁩󠁬󠁿 Flag for Bilasuvar (AZ-BIL)
🏴󠁣󠁧󠀹󠁿 Flag for Niari (CG-9)
👨🏼‍❤️‍👨🏾 Couple With Heart - Man: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
👨‍👧‍👶 Family: Man, Girl, Baby
👨🏿‍👦🏿‍👶🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
👨🏼‍❤️‍👩 Couple With Heart - Man: Medium-Light Skin Tone, Woman
⛒ Circled Crossing Lanes
👨🏻‍❤️‍💋‍👨🏽 Kiss - Man: Light Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁴󠀱󠀱󠁿 Flag for Paro (BT-11)
👩🏻‍❤️‍👨🏽 Couple With Heart - Woman: Light Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁴󠀱󠀳󠁿 Flag for Haa (BT-13)
🏴󠁡󠁺󠁣󠁡󠁢󠁿 Flag for Jabrayil (AZ-CAB)
🏴󠁳󠁣󠀰󠀵󠁿 Flag for Anse Royale (SC-05)
🏴󠁩󠁮󠁤󠁬󠁿 Flag for Delhi (IN-DL)
󠁁 Tag Latin Capital Letter a
🏴󠁭󠁹󠀰󠀷󠁿 Flag for Penang (MY-07)
♼ Recycled Paper Symbol
👨🏻‍👧🏻‍👶🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
🏴󠁩󠁮󠁭󠁰󠁿 Flag for Madhya Pradesh (IN-MP)
🏴󠁡󠁤󠀰󠀵󠁿 Flag for Ordino (AD-05)
🏴󠁮󠁺󠁮󠁴󠁬󠁿 Flag for Northland (NZ-NTL)
⚍ Digram for Lesser Yin
🏴󠁣󠁵󠀰󠀸󠁿 Flag for Ciego de Ávila (CU-08)
🏴󠁩󠁤󠁰󠁰󠁿 Flag for Papua Islands (ID-PP)
🕄 Notched Right Semicircle with Three Dots
🖀 Telephone On Top of Modem
👨🏻‍❤️‍👩🏾 Couple With Heart - Man: Light Skin Tone, Woman: Medium-Dark Skin Tone
☒ Ballot Box with X
🏴󠁢󠁴󠀱󠀵󠁿 Flag for Thimphu (BT-15)
👩🏼‍👨🏼‍👶🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁺󠁷󠁭󠁩󠁿 Flag for Midlands (ZW-MI)
🏴󠁪󠁰󠀳󠀷󠁿 Flag for Kagawa (JP-37)
🏴󠁡󠁺󠁡󠁧󠁵󠁿 Flag for Agsu (AZ-AGU)
🏴󠁫󠁰󠀰󠀱󠁿 Flag for Pyongyang (KP-01)
👨🏼‍👦🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁢󠁴󠀳󠀳󠁿 Flag for Bumthang (BT-33)
🏴󠁢󠁴󠀲󠀳󠁿 Flag for Punakha (BT-23)
🏴󠁢󠁳󠁷󠁧󠁿 Flag for West Grand Bahama (BS-WG)
🏴󠁵󠁳󠁭󠁰󠁿 Flag for Northern Mariana Islands (US-MP)
🏴󠁡󠁺󠁡󠁧󠁭󠁿 Flag for Agdam (AZ-AGM)
👩🏼‍❤️‍💋‍👨🏼 Kiss - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
🏴󠁢󠁴󠀴󠀲󠁿 Flag for Mongar (BT-42)
🏴󠁢󠁴󠀲󠀴󠁿 Flag for Wangdue Phodrang (BT-24)
🏴󠁢󠁴󠀳󠀲󠁿 Flag for Trongsa (BT-32)
🏴󠁣󠁤󠁢󠁣󠁿 Flag for Bas-Congo (CD-BC)
👩🏿‍❤️‍👨🏼 Couple With Heart - Woman: Dark Skin Tone, Man: Medium-Light Skin Tone
🏴󠁢󠁴󠀳󠀱󠁿 Flag for Sarpang (BT-31)
🏴󠁢󠁴󠀳󠀴󠁿 Flag for Zhemgang (BT-34)
🏴󠁣󠁮󠀶󠀴󠁿 Flag for Ningxia (CN-64)
🏴󠁢󠁴󠀲󠀲󠁿 Flag for Dagana (BT-22)
🏴󠁡󠁲󠁳󠁿 Flag for Santa Fe (AR-S)
🏴󠁡󠁺󠁡󠁧󠁳󠁿 Flag for Agdash (AZ-AGS)
👨🏾‍👨🏾‍👦🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁡󠁺󠁢󠁡󠁬󠁿 Flag for Balakan (AZ-BAL)
🏴󠁥󠁧󠁫󠁦󠁳󠁿 Flag for Kafr el-Sheikh (EG-KFS)
🏴󠁢󠁴󠀴󠀱󠁿 Flag for Trashigang (BT-41)
🏴󠁡󠁺󠁡󠁳󠁴󠁿 Flag for Astara (AZ-AST)
♭ Music Flat Sign
👩🏻‍❤️‍💋‍👨🏽 Kiss - Woman: Light Skin Tone, Man: Medium Skin Tone
🏴󠁤󠁫󠀸󠀵󠁿 Flag for Zealand (DK-85)
🏴󠁢󠁷󠁦󠁲󠁿 Flag for Francistown (BW-FR)
🏴󠁢󠁥󠁶󠁬󠁧󠁿 Flag for Flanders (BE-VLG)
🏴󠁱󠁡󠁤󠁡󠁿 Flag for Doha (QA-DA)
🏴󠁢󠁷󠁣󠁥󠁿 Flag for Central (BW-CE)
🏴󠁢󠁳󠁡󠁫󠁿 Flag for Acklins (BS-AK)
🏴󠁢󠁴󠁧󠁡󠁿 Flag for Gasa (BT-GA)
🏴󠁢󠁴󠀴󠀳󠁿 Flag for Pemagatshel (BT-43)
🏴󠁡󠁺󠁡󠁧󠁣󠁿 Flag for Aghjabadi (AZ-AGC)
👨🏽‍👧🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone
👨‍❤️‍👩🏾 Couple With Heart - Man, Woman: Medium-Dark Skin Tone
🏴󠁢󠁴󠀴󠀴󠁿 Flag for Lhuntse (BT-44)
👨🏾‍❤️‍💋‍👩 Kiss - Man: Medium-Dark Skin Tone, Woman
👩‍👨‍👦‍👦 Family: Woman, Man, Boy, Boy
2️ Digit Two
🏴󠁢󠁷󠁣󠁨󠁿 Flag for Chobe (BW-CH)
🏴󠁢󠁴󠁴󠁹󠁿 Flag for Trashiyangtse (BT-TY)
🏴󠁰󠁧󠁮󠁩󠁫󠁿 Flag for New Ireland (PG-NIK)
🏴󠁢󠁴󠀴󠀵󠁿 Flag for Samdrup Jongkhar (BT-45)
🏴󠁢󠁳󠁳󠁳󠁿 Flag for San Salvador (BS-SS)
🏴󠁣󠁮󠀹󠀱󠁿 Flag for Hong Kong SAR China (CN-91)
👩🏿‍❤️‍👩 Couple With Heart - Woman: Dark Skin Tone, Woman
🏴󠁭󠁹󠀱󠀱󠁿 Flag for Terengganu (MY-11)
👨🏽‍❤️‍👨 Couple With Heart - Man: Medium Skin Tone, Man
󠁐 Tag Latin Capital Letter P
🏴󠁢󠁴󠀲󠀱󠁿 Flag for Tsirang (BT-21)
♮ Music Natural Sign
🏴󠁢󠁷󠁪󠁷󠁿 Flag for Jwaneng (BW-JW)
👨🏻‍❤️‍👨🏿 Couple With Heart - Man: Light Skin Tone, Man: Dark Skin Tone
🏴󠁢󠁪󠁡󠁱󠁿 Flag for Atlantique (BJ-AQ)
🏴󠁢󠁷󠁮󠁷󠁿 Flag for North West (BW-NW)
👨🏼‍❤️‍💋‍👩🏻 Kiss - Man: Medium-Light Skin Tone, Woman: Light Skin Tone
🏴󠁰󠁫󠁴󠁡󠁿 Flag for Federally Administered Tribal Areas (PK-TA)
♬ Beamed Sixteenth Notes
🏴󠁢󠁷󠁮󠁥󠁿 Flag for North East (BW-NE)
👩🏿‍👦🏿‍👶🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁲󠁳󠁫󠁭󠁿 Flag for Kosovo-Metohija (RS-KM)
🏴󠁢󠁷󠁫󠁬󠁿 Flag for Kgatleng (BW-KL)
👩‍👩‍👶‍👦 Family: Woman, Woman, Baby, Boy
🏴󠁢󠁷󠁫󠁧󠁿 Flag for Kgalagadi (BW-KG)
👨🏻‍❤️‍👩🏻 Couple With Heart - Man: Light Skin Tone, Woman: Light Skin Tone
👨🏾‍👨🏾‍👧🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👨🏽‍👩🏽‍👧🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
⚨ Vertical Male with Stroke Sign
🏴󠁢󠁩󠁲󠁴󠁿 Flag for Rutana (BI-RT)
🏴󠁢󠁷󠁳󠁥󠁿 Flag for South East (BW-SE)
🏴󠁢󠁯󠁢󠁿 Flag for Beni (BO-B)
🏴󠁢󠁷󠁧󠁨󠁿 Flag for Ghanzi (BW-GH)
🏴󠁢󠁳󠁭󠁣󠁿 Flag for Mangrove Cay (BS-MC)
🏴󠁡󠁴󠀴󠁿 Flag for Upper Austria (AT-4)
👨🏽‍❤️‍💋‍👩🏼 Kiss - Man: Medium Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁢󠁷󠁫󠁷󠁿 Flag for Kweneng (BW-KW)
👩🏾‍👩🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏾‍👨🏾‍👦🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩‍👨‍👶‍👶 Family: Woman, Man, Baby, Baby
👩🏾‍❤️‍👩 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman
🏴󠁣󠁡󠁹󠁴󠁿 Flag for Yukon (CA-YT)
🏴󠁡󠁴󠀶󠁿 Flag for Styria (AT-6)
👨🏿‍👧🏿‍👦🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁴󠀱󠀴󠁿 Flag for Samtse (BT-14)
🏴󠁢󠁷󠁳󠁰󠁿 Flag for Selibe Phikwe (BW-SP)
👨🏽‍❤️‍💋‍👨🏾 Kiss - Man: Medium Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁢󠁷󠁳󠁯󠁿 Flag for Southern (BW-SO)
₿ Bitcoin Sign
👨🏽‍👩🏽‍👦🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁢󠁤󠁢󠁿 Flag for Chittagong Division (BD-B)
🏴󠁢󠁷󠁳󠁴󠁿 Flag for Sowa Town (BW-ST)
🏴󠁦󠁩󠀱󠀰󠁿 Flag for Lapland (FI-10)
👨🏿‍👨🏿‍👶🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁢󠀰󠀱󠁿 Flag for Christ Church (BB-01)
🏴󠁩󠁮󠁧󠁡󠁿 Flag for Goa (IN-GA)
🖡 Sideways Black Down Pointing Index
🏴󠁩󠁲󠀱󠀰󠁿 Flag for Khuzestan (IR-10)
👩🏼‍👧🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩‍❤️‍👨🏻 Couple With Heart - Woman, Man: Light Skin Tone
👨🏼‍❤️‍👨 Couple With Heart - Man: Medium-Light Skin Tone, Man
🏴󠁥󠁳󠁣󠁭󠁿 Flag for Castile-La Mancha (ES-CM)
🏴󠁣󠁨󠁺󠁨󠁿 Flag for Zürich (CH-ZH)
👩‍👨‍👧 Family: Woman, Man, Girl
☏ White Telephone
🏴󠁢󠁯󠁯󠁿 Flag for Oruro (BO-O)
♔ White Chess King
👩🏿‍👨🏿‍👦🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
 Beats 1 Logo
🏴󠁢󠁹󠁨󠁭󠁿 Flag for Minsk (BY-HM)
☽ First Quarter Moon
🏴󠁫󠁥󠀱󠀲󠁿 Flag for Kericho (KE-12)
🀈 Mahjong Tile Two of Characters
🏴󠁩󠁮󠁨󠁰󠁿 Flag for Himachal Pradesh (IN-HP)
☛ Black Right Pointing Index
♛ Black Chess Queen
👨🏻‍👩🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone
👩🏻‍👧🏻‍👦🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁵󠁳󠁲󠁩󠁿 Flag for Rhode Island (US-RI)
🏴󠁳󠁳󠁬󠁫󠁿 Flag for Lakes (SS-LK)
󠁖 Tag Latin Capital Letter V
🏴󠁢󠁹󠁨󠁯󠁿 Flag for Homel (BY-HO)
👩🏿‍👩🏿‍👧🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁥󠁣󠁭󠁿 Flag for Manabí (EC-M)
🏴󠁢󠁲󠁰󠁩󠁿 Flag for Piauí (BR-PI)
🏴󠁢󠁹󠁨󠁲󠁿 Flag for Hrodna (BY-HR)
🏴󠁥󠁳󠁥󠁸󠁿 Flag for Extremadura (ES-EX)
👩‍👨‍👧‍👶 Family: Woman, Man, Girl, Baby
⚢ Doubled Female Sign
☻ Black Smiling Face
🏴󠁰󠁨󠀰󠀰󠁿 Flag for Metro Manila (PH-00)
👨🏾‍❤️‍👩🏻 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Light Skin Tone
🏴󠁢󠁪󠁭󠁯󠁿 Flag for Mono (BJ-MO)
☚ Black Left Pointing Index
🏴󠁭󠁴󠀴󠀱󠁿 Flag for Pietà (MT-41)
☭ Hammer and Sickle
🏴󠁢󠁹󠁭󠁩󠁿 Flag for Minsk Region (BY-MI)
☾ Last Quarter Moon
🏴󠁳󠁤󠁲󠁳󠁿 Flag for Red Sea (SD-RS)
⛧ Inverted Pentagram
🏴󠁢󠁹󠁶󠁩󠁿 Flag for Vitebsk (BY-VI)
🏴󠁡󠁬󠀰󠀶󠁿 Flag for Korçë County (AL-06)
🎕 Bouquet of Flowers
👩🏿‍❤️‍👩🏾 Couple With Heart - Woman: Dark Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁢󠁹󠁭󠁡󠁿 Flag for Magileu (BY-MA)
⛼ Headstone Graveyard Symbol
🏴󠁲󠁵󠁫󠁢󠁿 Flag for Kabardino-Balkar (RU-KB)
🏴󠁢󠁳󠁭󠁩󠁿 Flag for Moore’s Island (BS-MI)
🏴󠁳󠁥󠁹󠁿 Flag for Västernorrland (SE-Y)
👨🏾‍👧🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁢󠁧󠀱󠀹󠁿 Flag for Silistra (BG-19)
👩🏻‍❤️‍💋‍👩 Kiss - Woman: Light Skin Tone, Woman
👨🏿‍👦🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁮󠁯󠀲󠀱󠁿 Flag for Svalbard (NO-21)
⛆ Rain
🏴󠁢󠁺󠁣󠁺󠁬󠁿 Flag for Corozal (BZ-CZL)
🏴󠁢󠁳󠁳󠁷󠁿 Flag for Spanish Wells (BS-SW)
👨‍❤️‍👩 Couple With Heart - Man, Woman
🏴󠁥󠁴󠁡󠁭󠁿 Flag for Amhara (ET-AM)
👩🏻‍❤️‍👨 Couple With Heart - Woman: Light Skin Tone, Man
🏴󠁭󠁨󠁬󠁿 Flag for Ralik Chain (MH-L)
🏴󠁡󠁴󠀸󠁿 Flag for Vorarlberg (AT-8)
👩🏻‍👩🏻‍👶🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🏴󠁢󠁺󠁴󠁯󠁬󠁿 Flag for Toledo (BZ-TOL)
🏴󠁥󠁳󠁰󠁶󠁿 Flag for Basque Country (ES-PV)
👩‍❤️‍👩🏽 Couple With Heart - Woman, Woman: Medium Skin Tone
☍ Opposition
👩‍👨‍👧‍👦 Family: Woman, Man, Girl, Boy
🏴󠁢󠁺󠁳󠁣󠁿 Flag for Stann Creek (BZ-SC)
🏴󠁣󠁮󠀵󠀲󠁿 Flag for Guizhou (CN-52)
👩🏻‍❤️‍👩🏿 Couple With Heart - Woman: Light Skin Tone, Woman: Dark Skin Tone
👩‍❤️‍👩🏾 Couple With Heart - Woman, Woman: Medium-Dark Skin Tone
☫ Farsi Symbol
🏴󠁬󠁡󠁸󠁳󠁿 Flag for Xaisomboun (LA-XS)
☌ Conjunction
🏴󠁢󠁷󠁬󠁯󠁿 Flag for Lobatse (BW-LO)
🏴󠁣󠁦󠁭󠁢󠁿 Flag for Mbomou (CF-MB)
🏴󠁳󠁨󠁴󠁡󠁿 Flag for Tristan da Cunha (SH-TA)
👨🏼‍❤️‍💋‍👩🏿 Kiss - Man: Medium-Light Skin Tone, Woman: Dark Skin Tone
👩🏾‍❤️‍👨🏾 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
👨🏽‍❤️‍💋‍👨🏼 Kiss - Man: Medium Skin Tone, Man: Medium-Light Skin Tone
🏴󠁡󠁴󠀷󠁿 Flag for Tyrol (AT-7)
☊ Ascending Node
🏴󠁰󠁴󠀲󠀰󠁿 Flag for Azores (PT-20)
🏴󠁡󠁯󠁬󠁵󠁡󠁿 Flag for Luanda (AO-LUA)
👩🏽‍❤️‍💋‍👩 Kiss - Woman: Medium Skin Tone, Woman
🏴󠁶󠁮󠀲󠀴󠁿 Flag for Quảng Bình (VN-24)
☋ Descending Node
⛣ Heavy Circle with Stroke and Two Dots Above
🏴󠁧󠁤󠀰󠀳󠁿 Flag for Saint George (GD-03)
🏴󠁢󠁳󠁲󠁩󠁿 Flag for Ragged Island (BS-RI)
👨‍👨‍👦‍👧 Family: Man, Man, Boy, Girl
🏴󠁮󠁰󠀵󠁿 Flag for Sudur Pashchimanchal (NP-5)
🧕🏻‍♀️ Woman With Headscarf: Light Skin Tone
🏴󠁬󠁡󠁶󠁩󠁿 Flag for Vientiane Province (LA-VI)
🏴󠁰󠁨󠀰󠀱󠁿 Flag for Ilocos (PH-01)
♸ Recycling Symbol for Type-6 Plastics
👨🏼‍👨🏼‍👦🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁴󠁲󠀳󠀵󠁿 Flag for Izmir (TR-35)
🏴󠁣󠁤󠁭󠁯󠁿 Flag for Mongala (CD-MO)
👩🏼‍👩🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👨🏽‍👧🏽‍👦🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁣󠁤󠁨󠁵󠁿 Flag for Haut-Uélé (CD-HU)
🀢 Mahjong Tile Plum
⛬ Historic Site
🏴󠁣󠁤󠁮󠁫󠁿 Flag for North Kivu (CD-NK)
🏴󠁣󠁤󠁭󠁡󠁿 Flag for Maniema (CD-MA)
🏴󠁣󠁤󠁫󠁮󠁿 Flag for Kinshasa (CD-KN)
‍ Zero Width Joiner
🏴󠁣󠁦󠁡󠁣󠁿 Flag for Ouham (CF-AC)
🏴󠁣󠁤󠁫󠁧󠁿 Flag for Kwango (CD-KG)
🏴󠁣󠁤󠁭󠁮󠁿 Flag for Mai-Ndombe (CD-MN)
🏴󠁣󠁤󠁳󠁡󠁿 Flag for Sankuru (CD-SA)
🏴󠁣󠁦󠁢󠁢󠁿 Flag for Bamingui-Bangoran (CF-BB)
🏴󠁣󠁤󠁴󠁵󠁿 Flag for Tshuapa (CD-TU)
🏴󠁣󠁤󠁫󠁥󠁿 Flag for Kasaï-Oriental (CD-KE)
👨🏾‍👧🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
󠀲 Tag Digit Two
⛡ Restricted Left Entry-2
🏴󠁣󠁤󠁩󠁴󠁿 Flag for Ituri (CD-IT)
🏴󠁣󠁤󠁨󠁬󠁿 Flag for Haut-Lomami (CD-HL)
🏴󠁣󠁤󠁴󠁯󠁿 Flag for Tshopo (CD-TO)
🏴󠁢󠁧󠀱󠀲󠁿 Flag for Montana (BG-12)
🏴󠁣󠁦󠁢󠁧󠁦󠁿 Flag for Bangui (CF-BGF)
🏴󠁣󠁤󠁫󠁳󠁿 Flag for Kasaï (CD-KS)
🏴󠁣󠁤󠁳󠁫󠁿 Flag for South Kivu (CD-SK)
🏴󠁣󠁦󠁨󠁳󠁿 Flag for Mambéré-Kadéï (CF-HS)
🏴󠁣󠁤󠁫󠁣󠁿 Flag for Kasaï Central (CD-KC)
🏴󠁣󠁨󠁮󠁷󠁿 Flag for Nidwalden (CH-NW)
🏴󠁢󠁳󠁨󠁴󠁿 Flag for Hope Town (BS-HT)
🏴󠁣󠁦󠁳󠁥󠁿 Flag for Sangha-Mbaéré (CF-SE)
🏴󠁣󠁨󠁦󠁲󠁿 Flag for Fribourg (CH-FR)
🏴󠁣󠁨󠁳󠁯󠁿 Flag for Solothurn (CH-SO)
🏴󠁣󠁦󠁬󠁢󠁿 Flag for Lobaye (CF-LB)
🏴󠁣󠁧󠀱󠀳󠁿 Flag for Sangha (CG-13)
🏴󠁣󠁨󠁡󠁩󠁿 Flag for Appenzell Innerrhoden (CH-AI)
🏴󠁣󠁧󠀵󠁿 Flag for Kouilou (CG-5)
🏴󠁣󠁧󠀸󠁿 Flag for Cuvette (CG-8)
🏴󠁣󠁦󠁭󠁰󠁿 Flag for Ombella-M’Poko (CF-MP)
🏴󠁣󠁤󠁬󠁯󠁿 Flag for Lomami (CD-LO)
🏴󠁣󠁨󠁯󠁷󠁿 Flag for Obwalden (CH-OW)
🏴󠁣󠁦󠁫󠁧󠁿 Flag for Kémo (CF-KG)
🏴󠁣󠁨󠁳󠁺󠁿 Flag for Schwyz (CH-SZ)
🏴󠁣󠁧󠀲󠁿 Flag for Lékoumou (CG-2)
🏴󠁣󠁨󠁳󠁧󠁿 Flag for St. Gallen (CH-SG)
🏴󠁣󠁧󠀷󠁿 Flag for Likouala (CG-7)
🏴󠁣󠁨󠁬󠁵󠁿 Flag for Lucerne (CH-LU)
🏴󠁣󠁧󠀱󠀴󠁿 Flag for Plateaux (CG-14)
🏴󠁣󠁧󠁢󠁺󠁶󠁿 Flag for Brazzaville (CG-BZV)
🛱 Oncoming Fire Engine
👨🏿‍👧🏿‍👶🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁣󠁤󠁫󠁬󠁿 Flag for Kwilu (CD-KL)
🏴󠁣󠁨󠁧󠁲󠁿 Flag for Graubünden (CH-GR)
🏴󠁣󠁧󠀱󠀵󠁿 Flag for Cuvette-Ouest (CG-15)
🏴󠁣󠁨󠁡󠁲󠁿 Flag for Appenzell Ausserrhoden (CH-AR)
🏴󠁣󠁨󠁡󠁧󠁿 Flag for Aargau (CH-AG)
🖈 Black Pushpin
󠀠 Tag Space
🏴󠁣󠁤󠁨󠁫󠁿 Flag for Haut-Katanga (CD-HK)
🏴󠁳󠁡󠀰󠀳󠁿 Flag for Al Madinah (SA-03)
🏴󠁣󠁭󠁳󠁷󠁿 Flag for Southwest (CM-SW)
🏴󠁣󠁩󠁧󠁤󠁿 Flag for Gôh-Djiboua (CI-GD)
🏴󠁣󠁭󠁮󠁯󠁿 Flag for North (CM-NO)
👨🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁣󠁨󠁢󠁳󠁿 Flag for Basel-Stadt (CH-BS)
🏴󠁵󠁳󠁮󠁭󠁿 Flag for New Mexico (US-NM)
🏴󠁣󠁩󠁣󠁭󠁿 Flag for Comoé (CI-CM)
🏴󠁣󠁩󠁳󠁶󠁿 Flag for Savanes (CI-SV)
🏴󠁣󠁩󠁤󠁮󠁿 Flag for Denguélé (CI-DN)
👩‍👶‍👦 Family: Woman, Baby, Boy
🏴󠁣󠁬󠁭󠁡󠁿 Flag for Magallanes Region (CL-MA)
🏴󠁣󠁭󠁮󠁷󠁿 Flag for Northwest (CM-NW)
🏴󠁢󠁳󠁣󠁯󠁿 Flag for Central Abaco (BS-CO)
🏴󠁣󠁭󠁣󠁥󠁿 Flag for Centre (CM-CE)
🏴󠁣󠁬󠁭󠁬󠁿 Flag for Maule (CL-ML)
🏴󠁣󠁬󠁣󠁯󠁿 Flag for Coquimbo (CL-CO)
🏴󠁣󠁭󠁬󠁴󠁿 Flag for Littoral (CM-LT)
🏴󠁣󠁩󠁹󠁭󠁿 Flag for Yamoussoukro (CI-YM)
🏴󠁣󠁬󠁴󠁡󠁿 Flag for Tarapacá (CL-TA)
🏴󠁣󠁬󠁡󠁴󠁿 Flag for Atacama (CL-AT)
🏴󠁣󠁬󠁬󠁲󠁿 Flag for Los Ríos (CL-LR)
🏴󠁣󠁭󠁡󠁤󠁿 Flag for Adamawa (CM-AD)
🏴󠁣󠁩󠁢󠁳󠁿 Flag for Bas-Sassandra (CI-BS)
🏴󠁣󠁩󠁬󠁣󠁿 Flag for Lacs (CI-LC)
🧟🏿‍♂️ Man Zombie: Dark Skin Tone
🏴󠁧󠁤󠀱󠀰󠁿 Flag for Carriacou and Petite Martinique (GD-10)
🏴󠁣󠁩󠁭󠁧󠁿 Flag for Montagnes (CI-MG)
🏴󠁣󠁩󠁷󠁲󠁿 Flag for Woroba (CI-WR)
🏴󠁡󠁴󠀵󠁿 Flag for Salzburg (AT-5)
♞ Black Chess Knight
🏴󠁡󠁦󠁫󠁤󠁺󠁿 Flag for Kunduz (AF-KDZ)
🏴󠁣󠁮󠀳󠀵󠁿 Flag for Fujian (CN-35)
🖫 White Hard Shell Floppy Disk
🏴󠁣󠁮󠀴󠀱󠁿 Flag for Henan (CN-41)
🏴󠁣󠁮󠀶󠀳󠁿 Flag for Qinghai (CN-63)
👨🏼‍👩🏼‍👧🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁣󠁮󠀴󠀵󠁿 Flag for Guangxi (CN-45)
🗭 Right Thought Bubble
🏴󠁣󠁮󠀴󠀶󠁿 Flag for Hainan (CN-46)
🏴󠁣󠁮󠀳󠀲󠁿 Flag for Jiangsu (CN-32)
👨🏾‍👨🏾‍👶🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁣󠁯󠁢󠁯󠁹󠁿 Flag for Boyacá (CO-BOY)
🏴󠁭󠁲󠀱󠀳󠁿 Flag for Nouakchott Ouest (MR-13)
🏴󠁣󠁮󠀴󠀲󠁿 Flag for Hubei (CN-42)
🏴󠁣󠁦󠁨󠁫󠁿 Flag for Haute-Kotto (CF-HK)
🏴󠁣󠁯󠁣󠁡󠁬󠁿 Flag for Caldas (CO-CAL)
👨🏿‍❤️‍💋‍👨 Kiss - Man: Dark Skin Tone, Man
🏴󠁣󠁮󠀵󠀰󠁿 Flag for Chongqing (CN-50)
🏴󠁣󠁮󠀳󠀶󠁿 Flag for Jiangxi (CN-36)
🏴󠁢󠁧󠀱󠀸󠁿 Flag for Ruse (BG-18)
🏴󠁣󠁯󠁡󠁲󠁡󠁿 Flag for Arauca (CO-ARA)
🏴󠁣󠁯󠁣󠁡󠁱󠁿 Flag for Caquetá (CO-CAQ)
🏴󠁡󠁲󠁭󠁿 Flag for Mendoza (AR-M)
🏴󠁡󠁲󠁧󠁿 Flag for Santiago del Estero (AR-G)
👨🏽‍👶🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁣󠁯󠁧󠁵󠁡󠁿 Flag for Guainía (CO-GUA)
🏴󠁣󠁵󠀰󠀹󠁿 Flag for Camagüey (CU-09)
🏴󠁣󠁯󠁰󠁵󠁴󠁿 Flag for Putumayo (CO-PUT)
🏴󠁣󠁲󠁧󠁿 Flag for Guanacaste (CR-G)
🏴󠁢󠁲󠁰󠁲󠁿 Flag for Paraná (BR-PR)
🏴󠁣󠁲󠁣󠁿 Flag for Cartago (CR-C)
👩🏻‍❤️‍👨🏻 Couple With Heart - Woman: Light Skin Tone, Man: Light Skin Tone
🏴󠁢󠁲󠁡󠁰󠁿 Flag for Amapá (BR-AP)
🏴󠁣󠁲󠁬󠁿 Flag for Limón (CR-L)
🏴󠁣󠁯󠁮󠁳󠁡󠁿 Flag for Norte de Santander (CO-NSA)
🏴󠁣󠁯󠁶󠁡󠁵󠁿 Flag for Vaupés (CO-VAU)
👩🏼‍❤️‍💋‍👩🏿 Kiss - Woman: Medium-Light Skin Tone, Woman: Dark Skin Tone
🏴󠁣󠁵󠀰󠀶󠁿 Flag for Cienfuegos (CU-06)
🏴󠁬󠁡󠁡󠁴󠁿 Flag for Attapeu (LA-AT)
🏴󠁣󠁲󠁰󠁿 Flag for Puntarenas (CR-P)
🏴󠁣󠁨󠁢󠁬󠁿 Flag for Basel-Landschaft (CH-BL)
🏴󠁣󠁵󠀰󠀵󠁿 Flag for Villa Clara (CU-05)
🏴󠁣󠁵󠀰󠀴󠁿 Flag for Matanzas (CU-04)
🏴󠁣󠁵󠀰󠀷󠁿 Flag for Sancti Spíritus (CU-07)
🏴󠁣󠁯󠁧󠁵󠁶󠁿 Flag for Guaviare (CO-GUV)
🖗 White Down Pointing Left Hand Index
🏴󠁣󠁯󠁬󠁡󠁧󠁿 Flag for La Guajira (CO-LAG)
🏴󠁣󠁯󠁨󠁵󠁩󠁿 Flag for Huila (CO-HUI)
👨🏼‍👩🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁢󠁺󠁣󠁹󠁿 Flag for Cayo (BZ-CY)
🏴󠁣󠁯󠁣󠁯󠁲󠁿 Flag for Córdoba (CO-COR)
🏴󠁣󠁯󠁳󠁡󠁮󠁿 Flag for Santander (CO-SAN)
🛨 Up-Pointing Small Airplane
👨🏻‍👩🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone
🏴󠁣󠁺󠀷󠀱󠁿 Flag for Olomoucký kraj (CZ-71)
🏴󠁣󠁺󠀵󠀲󠁿 Flag for Královéhradecký kraj (CZ-52)
🏴󠁲󠁯󠁢󠁮󠁿 Flag for Bistriţa-Năsăud (RO-BN)
🏴󠁡󠁲󠁴󠁿 Flag for Tucumán (AR-T)
🏴󠁣󠁺󠀸󠀰󠁿 Flag for Moravskoslezský kraj (CZ-80)
🏴󠁡󠁲󠁶󠁿 Flag for Tierra del Fuego (AR-V)
🏴󠁡󠁴󠀲󠁿 Flag for Carinthia (AT-2)
🏴󠁤󠁥󠁨󠁥󠁿 Flag for Hesse (DE-HE)
🏴󠁴󠁲󠀰󠀶󠁿 Flag for Ankara (TR-06)
🏴󠁣󠁶󠁳󠁿 Flag for Sotavento Islands (CV-S)
🏴󠁩󠁮󠁵󠁴󠁿 Flag for Uttarakhand (IN-UT)
⛫ Castle
🏴󠁢󠁧󠀲󠀰󠁿 Flag for Sliven (BG-20)
🏴󠁧󠁮󠁭󠁿 Flag for Mamou Region (GN-M)
🏴󠁣󠁮󠀶󠀵󠁿 Flag for Xinjiang (CN-65)
🏴󠁣󠁵󠀱󠀱󠁿 Flag for Holguín (CU-11)
🏴󠁣󠁮󠀶󠀲󠁿 Flag for Gansu (CN-62)
🏴󠁣󠁵󠀱󠀶󠁿 Flag for Mayabeque (CU-16)
🏴󠁣󠁺󠀴󠀱󠁿 Flag for Karlovarský kraj (CZ-41)
🏴󠁣󠁵󠀱󠀴󠁿 Flag for Guantánamo (CU-14)
🏴󠁳󠁡󠀰󠀲󠁿 Flag for Makkah (SA-02)
🏴󠁣󠁺󠀳󠀲󠁿 Flag for Plzeňský kraj (CZ-32)
👩🏻‍👩🏻‍👧🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
🏴󠁣󠁺󠀲󠀰󠁿 Flag for Středočeský kraj (CZ-20)
🏴󠁣󠁺󠀶󠀳󠁿 Flag for Kraj Vysočina (CZ-63)
🏴󠁣󠁹󠀰󠀲󠁿 Flag for Limassol (CY-02)
🏴󠁣󠁺󠀵󠀱󠁿 Flag for Liberecký kraj (CZ-51)
🏴󠁣󠁶󠁢󠁿 Flag for Barlavento Islands (CV-B)
👩🏾‍❤️‍💋‍👩 Kiss - Woman: Medium-Dark Skin Tone, Woman
☇ Lightning
🏴󠁤󠁭󠀰󠀲󠁿 Flag for Saint Andrew (DM-02)
🏴󠁤󠁭󠀱󠀰󠁿 Flag for Saint Paul (DM-10)
🏴󠁣󠁯󠁲󠁩󠁳󠁿 Flag for Risaralda (CO-RIS)
🏴󠁣󠁯󠁣󠁡󠁵󠁿 Flag for Cauca (CO-CAU)
🏴󠁣󠁮󠀳󠀷󠁿 Flag for Shandong (CN-37)
🏴󠁣󠁮󠀴󠀳󠁿 Flag for Hunan (CN-43)
🏴󠁣󠁦󠁯󠁰󠁿 Flag for Ouham-Pendé (CF-OP)
👨🏼‍👨🏼‍👧🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁤󠁥󠁳󠁴󠁿 Flag for Saxony-Anhalt (DE-ST)
🏴󠁤󠁯󠀳󠀴󠁿 Flag for Cibao Noroeste (DO-34)
👩🏽‍👩🏽‍👦🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁤󠁭󠀰󠀸󠁿 Flag for Saint Mark (DM-08)
🏴󠁤󠁫󠀸󠀴󠁿 Flag for Capital Region (DK-84)
🏴󠁢󠁱󠁢󠁯󠁿 Flag for Bonaire (BQ-BO)
🏴󠁤󠁯󠀳󠀶󠁿 Flag for Cibao Sur (DO-36)
🏴󠁧󠁲󠁨󠁿 Flag for Central Greece (GR-H)
🏴󠁣󠁮󠀱󠀴󠁿 Flag for Shanxi (CN-14)
🏴󠁤󠁺󠀰󠀲󠁿 Flag for Chlef (DZ-02)
🏴󠁤󠁪󠁡󠁳󠁿 Flag for Ali Sabieh (DJ-AS)
☉ Sun
🏴󠁣󠁵󠀱󠀵󠁿 Flag for Artemisa (CU-15)
🏴󠁤󠁭󠀰󠀷󠁿 Flag for Saint Luke (DM-07)
🏴󠁤󠁪󠁴󠁡󠁿 Flag for Tadjourah (DJ-TA)
🏴󠁤󠁯󠀳󠀳󠁿 Flag for Cibao Nordeste (DO-33)
🏴󠁦󠁲󠁨󠁤󠁦󠁿 Flag for Hauts-de-France (FR-HDF)
🏴󠁣󠁯󠁭󠁡󠁧󠁿 Flag for Magdalena (CO-MAG)
👩🏻‍❤️‍💋‍👨🏿 Kiss - Woman: Light Skin Tone, Man: Dark Skin Tone
🏴󠁣󠁹󠀰󠀱󠁿 Flag for Nicosia (CY-01)
🏴󠁤󠁯󠀴󠀱󠁿 Flag for Valdesia (DO-41)
🏴󠁤󠁯󠀳󠀹󠁿 Flag for Higüamo (DO-39)
🏴󠁣󠁲󠁡󠁿 Flag for Alajuela (CR-A)
🏴󠁭󠁸󠁢󠁣󠁳󠁿 Flag for Baja California Sur (MX-BCS)
🏴󠁤󠁺󠀱󠀵󠁿 Flag for Tizi Ouzou (DZ-15)
🏴󠁤󠁭󠀰󠀳󠁿 Flag for Saint David (DM-03)
🏴󠁤󠁺󠀳󠀰󠁿 Flag for Ouargla (DZ-30)
🏴󠁤󠁺󠀱󠀱󠁿 Flag for Tamanghasset (DZ-11)
🏴󠁤󠁺󠀱󠀲󠁿 Flag for Tébessa (DZ-12)
🏴󠁤󠁥󠁳󠁮󠁿 Flag for Saxony (DE-SN)
🏴󠁤󠁺󠀴󠀲󠁿 Flag for Tipasa (DZ-42)
👨‍❤️‍💋‍👩 Kiss - Man, Woman
🏴󠁤󠁯󠀳󠀸󠁿 Flag for Enriquillo (DO-38)
⚳ Ceres
🏴󠁤󠁺󠀰󠀶󠁿 Flag for Béjaïa (DZ-06)
🏴󠁤󠁺󠀳󠀸󠁿 Flag for Tissemsilt (DZ-38)
🏴󠁤󠁺󠀲󠀶󠁿 Flag for Médéa (DZ-26)
🏴󠁤󠁺󠀱󠀰󠁿 Flag for Bouira (DZ-10)
🏴󠁤󠁺󠀳󠀶󠁿 Flag for El Tarf (DZ-36)
🏴󠁤󠁺󠀱󠀷󠁿 Flag for Djelfa (DZ-17)
🖑 Reversed Raised Hand with Fingers Splayed
🏴󠁤󠁺󠀰󠀵󠁿 Flag for Batna (DZ-05)
🏴󠁣󠁲󠁳󠁪󠁿 Flag for San José (CR-SJ)
🏴󠁤󠁺󠀲󠀳󠁿 Flag for Annaba (DZ-23)
🏴󠁤󠁺󠀰󠀷󠁿 Flag for Biskra (DZ-07)
🏴󠁡󠁲󠁺󠁿 Flag for Santa Cruz (AR-Z)
🏴󠁤󠁺󠀴󠀳󠁿 Flag for Mila (DZ-43)
🏴󠁤󠁺󠀳󠀷󠁿 Flag for Tindouf (DZ-37)
🏴󠁤󠁺󠀴󠀱󠁿 Flag for Souk Ahras (DZ-41)
🏴󠁤󠁺󠀳󠀳󠁿 Flag for Illizi (DZ-33)
⛤ Pentagram
🏴󠁤󠁺󠀳󠀲󠁿 Flag for El Bayadh (DZ-32)
🏴󠁤󠁺󠀳󠀵󠁿 Flag for Boumerdès (DZ-35)
🏴󠁤󠁺󠀴󠀰󠁿 Flag for Khenchela (DZ-40)
🏴󠁰󠁷󠀲󠀱󠀸󠁿 Flag for Ngarchelong (PW-218)
🏴󠁤󠁺󠀲󠀷󠁿 Flag for Mostaganem (DZ-27)
🏴󠁡󠁲󠁷󠁿 Flag for Corrientes (AR-W)
🏴󠁥󠁥󠀶󠀷󠁿 Flag for Pärnu (EE-67)
🏴󠁥󠁣󠁲󠁿 Flag for Los Ríos (EC-R)
🏴󠁥󠁣󠁣󠁿 Flag for Carchi (EC-C)
🏴󠁥󠁣󠁬󠁿 Flag for Loja (EC-L)
🏴󠁥󠁥󠀷󠀰󠁿 Flag for Rapla (EE-70)
🏴󠁥󠁥󠀵󠀱󠁿 Flag for Järva (EE-51)
🏴󠁥󠁣󠁳󠁿 Flag for Morona-Santiago (EC-S)
🏴󠁥󠁥󠀷󠀴󠁿 Flag for Saare (EE-74)
🏴󠁥󠁥󠀵󠀷󠁿 Flag for Lääne (EE-57)
🏴󠁥󠁣󠁩󠁿 Flag for Imbabura (EC-I)
🏴󠁡󠁲󠁵󠁿 Flag for Chubut (AR-U)
🏴󠁤󠁺󠀴󠀷󠁿 Flag for Ghardaïa (DZ-47)
🏴󠁥󠁥󠀴󠀹󠁿 Flag for Jõgeva (EE-49)
🏴󠁤󠁺󠀴󠀶󠁿 Flag for Aïn Témouchent (DZ-46)
🏴󠁥󠁣󠁢󠁿 Flag for Bolívar (EC-B)
🏴󠁥󠁣󠁷󠁿 Flag for Galápagos (EC-W)
🏴󠁥󠁣󠁵󠁿 Flag for Sucumbíos (EC-U)
🏴󠁥󠁣󠁡󠁿 Flag for Azuay (EC-A)
🀁 Mahjong Tile South Wind
⛨ Black Cross On Shield
🏴󠁤󠁺󠀰󠀴󠁿 Flag for Oum El Bouaghi (DZ-04)
🏴󠁵󠁳󠁮󠁹󠁿 Flag for New York (US-NY)
🏴󠁡󠁲󠁸󠁿 Flag for Córdoba (AR-X)
🏴󠁤󠁺󠀴󠀴󠁿 Flag for Aïn Defla (DZ-44)
🏴󠁤󠁺󠀴󠀸󠁿 Flag for Relizane (DZ-48)
🏴󠁥󠁥󠀶󠀵󠁿 Flag for Põlva (EE-65)
🏴󠁥󠁣󠁹󠁿 Flag for Pastaza (EC-Y)
🏴󠁥󠁣󠁤󠁿 Flag for Orellana (EC-D)
🏴󠁥󠁥󠀸󠀲󠁿 Flag for Valga (EE-82)
🏴󠁤󠁯󠀳󠀵󠁿 Flag for Cibao Norte (DO-35)
󠁼 Tag Vertical Line
🏴󠁣󠁹󠀰󠀵󠁿 Flag for Paphos (CY-05)
⛉ Turned White Shogi Piece
👨🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁥󠁧󠁪󠁳󠁿 Flag for South Sinai (EG-JS)
🏴󠁥󠁧󠁢󠁨󠁿 Flag for Beheira (EG-BH)
🏴󠁥󠁧󠁩󠁳󠁿 Flag for Ismailia (EG-IS)
🏴󠁥󠁧󠁭󠁮󠁦󠁿 Flag for Monufia (EG-MNF)
󠁅 Tag Latin Capital Letter E
🏴󠁴󠁺󠀱󠀱󠁿 Flag for Zanzibar Central/South (TZ-11)
🏴󠁥󠁲󠁡󠁮󠁿 Flag for Anseba (ER-AN)
👩🏼‍❤️‍💋‍👨🏾 Kiss - Woman: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁥󠁲󠁭󠁡󠁿 Flag for Maekel (ER-MA)
🏴󠁥󠁥󠀸󠀶󠁿 Flag for Võru (EE-86)
🏴󠁤󠁺󠀲󠀰󠁿 Flag for Saïda (DZ-20)
🏴󠁥󠁧󠁫󠁮󠁿 Flag for Qena (EG-KN)
🏴󠁥󠁧󠁫󠁢󠁿 Flag for Qalyubia (EG-KB)
🏴󠁥󠁧󠁳󠁨󠁲󠁿 Flag for Al Sharqia (EG-SHR)
🏴󠁥󠁧󠁤󠁫󠁿 Flag for Dakahlia (EG-DK)
🏴󠁥󠁧󠁧󠁨󠁿 Flag for Gharbia (EG-GH)
⛘ Black Left Lane Merge
🏴󠁥󠁧󠁬󠁸󠁿 Flag for Luxor (EG-LX)
🏴󠁥󠁧󠁡󠁳󠁴󠁿 Flag for Asyut (EG-AST)
⚦ Male with Stroke Sign
🏴󠁤󠁭󠀰󠀹󠁿 Flag for Saint Patrick (DM-09)
🏴󠁥󠁧󠁡󠁳󠁮󠁿 Flag for Aswan (EG-ASN)
🏴󠁥󠁥󠀸󠀴󠁿 Flag for Viljandi (EE-84)
👩‍👨‍👦‍👧 Family: Woman, Man, Boy, Girl
🏴󠁥󠁥󠀷󠀸󠁿 Flag for Tartu (EE-78)
🏴󠁫󠁩󠁰󠁿 Flag for Phoenix Islands (KI-P)
🏴󠁥󠁧󠁭󠁮󠁿 Flag for Minya (EG-MN)
👨🏾‍👶🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁥󠁲󠁤󠁵󠁿 Flag for Debub (ER-DU)
👨🏾‍❤️‍👨🏾 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
👩🏿‍👨🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone
⚹ Sextile
🏴󠁥󠁧󠁤󠁴󠁿 Flag for Damietta (EG-DT)
🏴󠁤󠁺󠀰󠀹󠁿 Flag for Blida (DZ-09)
👨🏽‍👶🏽‍👧🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
🧕🏻‍♂️ Man With Headscarf: Light Skin Tone
🏴󠁦󠁩󠀰󠀲󠁿 Flag for South Karelia (FI-02)
🏴󠁦󠁩󠀰󠀹󠁿 Flag for Kymenlaakso (FI-09)
󠁓 Tag Latin Capital Letter S
⛠ Restricted Left Entry-1
👨🏼‍👶🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁦󠁩󠀰󠀵󠁿 Flag for Kainuu (FI-05)
👨🏽‍❤️‍💋‍👩🏿 Kiss - Man: Medium Skin Tone, Woman: Dark Skin Tone
🏴󠁤󠁪󠁯󠁢󠁿 Flag for Obock (DJ-OB)
👩🏼‍❤️‍💋‍👨 Kiss - Woman: Medium-Light Skin Tone, Man
🏴󠁥󠁣󠁳󠁥󠁿 Flag for Santa Elena (EC-SE)
🏴󠁥󠁴󠁨󠁡󠁿 Flag for Harari (ET-HA)
👨🏼‍👶🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏼‍👦🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁦󠁩󠀰󠀳󠁿 Flag for Southern Ostrobothnia (FI-03)
🏴󠁥󠁴󠁢󠁥󠁿 Flag for Benishangul-Gumuz (ET-BE)
👨🏻‍👨🏻‍👦🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
🏴󠁤󠁯󠀴󠀲󠁿 Flag for Yuma (DO-42)
🏴󠁡󠁲󠁮󠁿 Flag for Misiones (AR-N)
👨🏼‍👩🏼‍👶🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👨🏿‍❤️‍💋‍👩 Kiss - Man: Dark Skin Tone, Woman
⛜ Left Closed Entry
🏴󠁦󠁩󠀱󠀱󠁿 Flag for Pirkanmaa (FI-11)
🏴󠁥󠁧󠁭󠁴󠁿 Flag for Matrouh (EG-MT)
🏴󠁦󠁪󠁲󠁿 Flag for Rotuma (FJ-R)
👩🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
󠁃 Tag Latin Capital Letter C
🏴󠁣󠁮󠀲󠀱󠁿 Flag for Liaoning (CN-21)
🏴󠁦󠁭󠁫󠁳󠁡󠁿 Flag for Kosrae (FM-KSA)
🏴󠁦󠁲󠁮󠁡󠁱󠁿 Flag for Nouvelle-Aquitaine (FR-NAQ)
🏴󠁦󠁲󠁣󠁶󠁬󠁿 Flag for Centre-Val de Loire (FR-CVL)
⛌ Crossing Lanes
🏴󠁦󠁩󠀱󠀳󠁿 Flag for North Karelia (FI-13)
🏴󠁦󠁪󠁮󠁿 Flag for Northern (FJ-N)
🏴󠁢󠁴󠀱󠀲󠁿 Flag for Chukha (BT-12)
🏴󠁦󠁩󠀱󠀵󠁿 Flag for Northern Savonia (FI-15)
🏴󠁦󠁪󠁣󠁿 Flag for Central (FJ-C)
🏴󠁤󠁺󠀳󠀱󠁿 Flag for Oran (DZ-31)
🏴󠁣󠁬󠁢󠁩󠁿 Flag for Bío Bío (CL-BI)
🏴󠁦󠁩󠀱󠀶󠁿 Flag for Päijänne Tavastia (FI-16)
👨🏼‍👶🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁧󠁨󠁢󠁡󠁿 Flag for Brong-Ahafo (GH-BA)
👩‍👶 Family: Woman, Baby
🏴󠁧󠁥󠁩󠁭󠁿 Flag for Imereti (GE-IM)
🏴󠁣󠁺󠀶󠀴󠁿 Flag for Jihomoravský kraj (CZ-64)
⚴ Pallas
🗩 Right Speech Bubble
🏴󠁦󠁩󠀱󠀷󠁿 Flag for Satakunta (FI-17)
🏴󠁡󠁭󠁳󠁨󠁿 Flag for Shirak (AM-SH)
⛝ Squared Saltire
🏴󠁰󠁴󠀱󠀸󠁿 Flag for Viseu (PT-18)
🏴󠁧󠁥󠁭󠁭󠁿 Flag for Mtskheta-Mtianeti (GE-MM)
🕴🏼‍♀️ Woman in Business Suit Levitating: Medium-Light Skin Tone
🏴󠁦󠁲󠁧󠁥󠁳󠁿 Flag for Grand-Est (FR-GES)
🏴󠁧󠁤󠀰󠀲󠁿 Flag for Saint David (GD-02)
🏴󠁧󠁡󠀹󠁿 Flag for Woleu-Ntem (GA-9)
🏴󠁧󠁥󠁧󠁵󠁿 Flag for Guria (GE-GU)
♢ White Diamond Suit
🏴󠁣󠁩󠁡󠁢󠁿 Flag for Abidjan (CI-AB)
🏴󠁧󠁤󠀰󠀴󠁿 Flag for Saint John (GD-04)
⛂ Black Draughts Man
🏴󠁧󠁥󠁳󠁪󠁿 Flag for Samtskhe-Javakheti (GE-SJ)
🏴󠁧󠁥󠁳󠁺󠁿 Flag for Samegrelo-Zemo Svaneti (GE-SZ)
🏴󠁧󠁡󠀲󠁿 Flag for Haut-Ogooué (GA-2)
🏴󠁧󠁡󠀶󠁿 Flag for Ogooué-Ivindo (GA-6)
🏴󠁧󠁡󠀳󠁿 Flag for Moyen-Ogooué (GA-3)
🏴󠁧󠁥󠁳󠁫󠁿 Flag for Shida Kartli (GE-SK)
🏴󠁤󠁺󠀲󠀴󠁿 Flag for Guelma (DZ-24)
🏴󠁧󠁬󠁳󠁭󠁿 Flag for Sermersooq (GL-SM)
🏴󠁧󠁮󠁤󠁿 Flag for Kindia Region (GN-D)
🏴󠁧󠁨󠁵󠁥󠁿 Flag for Upper East (GH-UE)
⛚ Drive Slow Sign
🏴󠁧󠁲󠀶󠀹󠁿 Flag for Mount Athos (GR-69)
👨🏻‍❤️‍💋‍👩🏽 Kiss - Man: Light Skin Tone, Woman: Medium Skin Tone
🏴󠁧󠁨󠁵󠁷󠁿 Flag for Upper West (GH-UW)
🕽 Right Hand Telephone Receiver
👨🏾‍👦🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁧󠁬󠁫󠁵󠁿 Flag for Kujalleq (GL-KU)
🏴󠁡󠁲󠁰󠁿 Flag for Formosa (AR-P)
🏴󠁧󠁱󠁩󠁿 Flag for Insular (GQ-I)
🏴󠁧󠁮󠁢󠁿 Flag for Boké Region (GN-B)
🏴󠁧󠁨󠁮󠁰󠁿 Flag for Northern (GH-NP)
🏴󠁧󠁲󠁥󠁿 Flag for Thessaly (GR-E)
🏴󠁧󠁬󠁱󠁡󠁿 Flag for Qaasuitsup (GL-QA)
🏴󠁧󠁨󠁴󠁶󠁿 Flag for Volta (GH-TV)
🏴󠁧󠁲󠁦󠁿 Flag for Ionian Islands (GR-F)
🏴󠁧󠁱󠁣󠁿 Flag for Río Muni (GQ-C)
🏴󠁡󠁺󠁧󠁡󠁿 Flag for Ganja (AZ-GA)
🀤 Mahjong Tile Bamboo
👩🏻‍❤️‍👩🏼 Couple With Heart - Woman: Light Skin Tone, Woman: Medium-Light Skin Tone
👩🏻‍❤️‍👨🏼 Couple With Heart - Woman: Light Skin Tone, Man: Medium-Light Skin Tone
🏴󠁧󠁮󠁦󠁿 Flag for Faranah Region (GN-F)
🏴󠁧󠁬󠁱󠁥󠁿 Flag for Qeqqata (GL-QE)
🏴󠁥󠁣󠁰󠁿 Flag for Pichincha (EC-P)
🏴󠁧󠁮󠁣󠁿 Flag for Conakry (GN-C)
🏴󠁧󠁲󠁤󠁿 Flag for Epirus (GR-D)
🏴󠁧󠁴󠁺󠁡󠁿 Flag for Zacapa (GT-ZA)
🏴󠁧󠁴󠁪󠁡󠁿 Flag for Jalapa (GT-JA)
🏴󠁧󠁴󠁩󠁺󠁿 Flag for Izabal (GT-IZ)
🏴󠁧󠁴󠁰󠁥󠁿 Flag for Petén (GT-PE)
🏴󠁡󠁲󠁱󠁿 Flag for Neuquén (AR-Q)
🏴󠁡󠁤󠀰󠀸󠁿 Flag for Escaldes-Engordany (AD-08)
🏴󠁧󠁴󠁳󠁵󠁿 Flag for Suchitepéquez (GT-SU)
🏴󠁡󠁦󠁪󠁯󠁷󠁿 Flag for Jowzjan (AF-JOW)
🏴󠁧󠁴󠁢󠁶󠁿 Flag for Baja Verapaz (GT-BV)
🏴󠁧󠁹󠁰󠁴󠁿 Flag for Potaro-Siparuni (GY-PT)
🏴󠁧󠁴󠁨󠁵󠁿 Flag for Huehuetenango (GT-HU)
🏴󠁧󠁴󠁥󠁳󠁿 Flag for Escuintla (GT-ES)
🏴󠁧󠁷󠁬󠁿 Flag for Leste (GW-L)
🏴󠁧󠁴󠁣󠁭󠁿 Flag for Chimaltenango (GT-CM)
🏴󠁧󠁷󠁢󠁳󠁿 Flag for Bissau (GW-BS)
⛙ White Left Lane Merge
🏴󠁳󠁹󠁤󠁹󠁿 Flag for Deir ez-Zor (SY-DY)
🏴󠁧󠁹󠁤󠁥󠁿 Flag for Demerara-Mahaica (GY-DE)
🏴󠁧󠁴󠁴󠁯󠁿 Flag for Totonicapán (GT-TO)
🏴󠁨󠁮󠁣󠁨󠁿 Flag for Choluteca (HN-CH)
🏴󠁧󠁴󠁱󠁺󠁿 Flag for Quetzaltenango (GT-QZ)
🏴󠁨󠁮󠁡󠁴󠁿 Flag for Atlántida (HN-AT)
👨🏾‍👶🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁧󠁴󠁣󠁱󠁿 Flag for Chiquimula (GT-CQ)
🏴󠁧󠁹󠁣󠁵󠁿 Flag for Cuyuni-Mazaruni (GY-CU)
🏴󠁧󠁹󠁥󠁳󠁿 Flag for Essequibo Islands-West Demerara (GY-ES)
🏴󠁧󠁴󠁱󠁣󠁿 Flag for Quiché (GT-QC)
🏴󠁧󠁴󠁳󠁯󠁿 Flag for Sololá (GT-SO)
👨🏿‍👶🏿‍👶🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁨󠁲󠀰󠀶󠁿 Flag for Koprivnica-Križevci (HR-06)
🏴󠁥󠁥󠀴󠀴󠁿 Flag for Ida-Viru (EE-44)
🏴󠁨󠁲󠀰󠀷󠁿 Flag for Bjelovar-Bilogora (HR-07)
🏴󠁨󠁮󠁬󠁰󠁿 Flag for La Paz (HN-LP)
🏴󠁨󠁲󠀰󠀹󠁿 Flag for Lika-Senj (HR-09)
🏴󠁨󠁲󠀰󠀱󠁿 Flag for Zagreb County (HR-01)
🏴󠁦󠁲󠁰󠁦󠁿 Flag for French Polynesia (FR-PF)
🏴󠁨󠁲󠀲󠀱󠁿 Flag for Zagreb (HR-21)
🏴󠁮󠁯󠀱󠀱󠁿 Flag for Rogaland (NO-11)
🏴󠁨󠁮󠁬󠁥󠁿 Flag for Lempira (HN-LE)
🏴󠁨󠁲󠀱󠀱󠁿 Flag for Požega-Slavonia (HR-11)
🏴󠁨󠁲󠀱󠀶󠁿 Flag for Vukovar-Syrmia (HR-16)
🏴󠁨󠁮󠁣󠁰󠁿 Flag for Copán (HN-CP)
🏴󠁨󠁲󠀱󠀷󠁿 Flag for Split-Dalmatia (HR-17)
🏴󠁨󠁲󠀱󠀲󠁿 Flag for Brod-Posavina (HR-12)
🏴󠁨󠁮󠁯󠁣󠁿 Flag for Ocotepeque (HN-OC)
🏴󠁨󠁲󠀲󠀰󠁿 Flag for Međimurje (HR-20)
🏴󠁨󠁲󠀱󠀸󠁿 Flag for Istria (HR-18)
⚣ Doubled Male Sign
🏴󠁨󠁲󠀱󠀹󠁿 Flag for Dubrovnik-Neretva (HR-19)
🏴󠁨󠁮󠁣󠁬󠁿 Flag for Colón (HN-CL)
🏴󠁨󠁲󠀱󠀳󠁿 Flag for Zadar (HR-13)
🏴󠁨󠁮󠁣󠁲󠁿 Flag for Cortés (HN-CR)
🏴󠁨󠁴󠁣󠁥󠁿 Flag for Centre (HT-CE)
🏴󠁨󠁮󠁧󠁤󠁿 Flag for Gracias a Dios (HN-GD)
🏴󠁦󠁭󠁴󠁲󠁫󠁿 Flag for Chuuk (FM-TRK)
🏴󠁨󠁴󠁡󠁲󠁿 Flag for Artibonite (HT-AR)
🏴󠁨󠁮󠁹󠁯󠁿 Flag for Yoro (HN-YO)
🏴󠁨󠁮󠁯󠁬󠁿 Flag for Olancho (HN-OL)
🏴󠁨󠁮󠁩󠁮󠁿 Flag for Intibucá (HN-IN)
🏴󠁨󠁮󠁦󠁭󠁿 Flag for Francisco Morazán (HN-FM)
🏴󠁨󠁮󠁥󠁰󠁿 Flag for El Paraíso (HN-EP)
🏴󠁨󠁮󠁣󠁭󠁿 Flag for Comayagua (HN-CM)
🏴󠁨󠁲󠀱󠀵󠁿 Flag for Šibenik-Knin (HR-15)
🏴󠁨󠁲󠀱󠀴󠁿 Flag for Osijek-Baranja (HR-14)
🏴󠁨󠁮󠁳󠁢󠁿 Flag for Santa Bárbara (HN-SB)
🏴󠁨󠁮󠁶󠁡󠁿 Flag for Valle (HN-VA)
🏴󠁨󠁲󠀰󠀲󠁿 Flag for Krapina-Zagorje (HR-02)
🏴󠁨󠁵󠁥󠁲󠁿 Flag for Érd (HU-ER)
🏴󠁨󠁵󠁦󠁥󠁿 Flag for Fejér (HU-FE)
🏴󠁤󠁺󠀱󠀸󠁿 Flag for Jijel (DZ-18)
🏴󠁨󠁵󠁮󠁹󠁿 Flag for Nyíregyháza (HU-NY)
🏴󠁨󠁴󠁧󠁡󠁿 Flag for Grand’Anse (HT-GA)
🏴󠁨󠁵󠁢󠁺󠁿 Flag for Borsod-Abaúj-Zemplén (HU-BZ)
🏴󠁣󠁮󠀵󠀱󠁿 Flag for Sichuan (CN-51)
🏴󠁧󠁨󠁥󠁰󠁿 Flag for Eastern (GH-EP)
🏴󠁨󠁵󠁮󠁫󠁿 Flag for Nagykanizsa (HU-NK)
🏴󠁨󠁵󠁤󠁵󠁿 Flag for Dunaújváros (HU-DU)
🏴󠁥󠁴󠁤󠁤󠁿 Flag for Dire Dawa (ET-DD)
🏴󠁨󠁵󠁳󠁨󠁿 Flag for Szombathely (HU-SH)
🏴󠁨󠁵󠁳󠁮󠁿 Flag for Sopron (HU-SN)
🏴󠁨󠁵󠁧󠁹󠁿 Flag for Győr (HU-GY)
🏴󠁨󠁵󠁭󠁩󠁿 Flag for Miskolc (HU-MI)
🏴󠁨󠁵󠁤󠁥󠁿 Flag for Debrecen (HU-DE)
🏴󠁨󠁴󠁮󠁩󠁿 Flag for Nippes (HT-NI)
🏴󠁨󠁵󠁢󠁫󠁿 Flag for Bács-Kiskun (HU-BK)
🏴󠁨󠁵󠁨󠁢󠁿 Flag for Hajdú-Bihar (HU-HB)
🏴󠁨󠁵󠁢󠁡󠁿 Flag for Baranya (HU-BA)
🏴󠁵󠁳󠁫󠁳󠁿 Flag for Kansas (US-KS)
🏴󠁨󠁴󠁯󠁵󠁿 Flag for Ouest (HT-OU)
🏴󠁨󠁵󠁮󠁯󠁿 Flag for Nógrád (HU-NO)
🏴󠁨󠁵󠁳󠁤󠁿 Flag for Szeged (HU-SD)
🏴󠁨󠁵󠁳󠁦󠁿 Flag for Székesfehérvár (HU-SF)
🏴󠁨󠁵󠁳󠁫󠁿 Flag for Szolnok (HU-SK)
🏴󠁨󠁵󠁢󠁥󠁿 Flag for Békés (HU-BE)
🏴󠁨󠁵󠁰󠁥󠁿 Flag for Pest (HU-PE)
🏴󠁨󠁴󠁮󠁤󠁿 Flag for Nord (HT-ND)
🏴󠁨󠁵󠁪󠁮󠁿 Flag for Jász-Nagykun-Szolnok (HU-JN)
🏴󠁨󠁵󠁫󠁥󠁿 Flag for Komárom-Esztergom (HU-KE)
🏴󠁦󠁭󠁹󠁡󠁰󠁿 Flag for Yap (FM-YAP)
🏴󠁨󠁵󠁨󠁥󠁿 Flag for Heves (HU-HE)
🏴󠁨󠁵󠁢󠁣󠁿 Flag for Békéscsaba (HU-BC)
⛃ Black Draughts King
🏴󠁨󠁵󠁴󠁯󠁿 Flag for Tolna (HU-TO)
🏴󠁨󠁵󠁶󠁡󠁿 Flag for Vas (HU-VA)
🏴󠁨󠁵󠁶󠁭󠁿 Flag for Veszprém (HU-VM)
🏴󠁧󠁭󠁵󠁿 Flag for Upper River Division (GM-U)
🏴󠁩󠁤󠁮󠁵󠁿 Flag for Lesser Sunda Islands (ID-NU)
🏴󠁧󠁥󠁲󠁬󠁿 Flag for Racha-Lechkhumi and Kvemo Svaneti (GE-RL)
🏴󠁧󠁨󠁡󠁡󠁿 Flag for Greater Accra (GH-AA)
🏴󠁩󠁬󠁤󠁿 Flag for Southern District (IL-D)
🏴󠁡󠁯󠁺󠁡󠁩󠁿 Flag for Zaire (AO-ZAI)
🏴󠁩󠁬󠁨󠁡󠁿 Flag for Haifa District (IL-HA)
🏴󠁨󠁵󠁳󠁯󠁿 Flag for Somogy (HU-SO)
🏴󠁥󠁳󠁲󠁩󠁿 Flag for La Rioja (ES-RI)
🏴󠁩󠁬󠁭󠁿 Flag for Central District (IL-M)
🏴󠁥󠁴󠁧󠁡󠁿 Flag for Gambela (ET-GA)
🏴󠁶󠁮󠀰󠀲󠁿 Flag for Lào Cai (VN-02)
🏴󠁩󠁥󠁣󠁿 Flag for Connacht (IE-C)
🏴󠁨󠁵󠁶󠁥󠁿 Flag for Veszprém County (HU-VE)
🏴󠁨󠁵󠁴󠁢󠁿 Flag for Tatabánya (HU-TB)
🏴󠁨󠁵󠁺󠁥󠁿 Flag for Zalaegerszeg (HU-ZE)
👩🏾‍❤️‍👨🏼 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
🏴󠁩󠁮󠁣󠁨󠁿 Flag for Chandigarh (IN-CH)
🏴󠁤󠁭󠀱󠀱󠁿 Flag for Saint Peter (DM-11)
👨🏽‍👨🏽‍👶🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁣󠁬󠁡󠁩󠁿 Flag for Aysén (CL-AI)
🏴󠁩󠁱󠁳󠁤󠁿 Flag for Saladin (IQ-SD)
🏴󠁩󠁮󠁮󠁬󠁿 Flag for Nagaland (IN-NL)
🏴󠁩󠁱󠁮󠁡󠁿 Flag for Najaf (IQ-NA)
🏴󠁨󠁵󠁫󠁭󠁿 Flag for Kecskemét (HU-KM)
🏴󠁬󠁵󠁬󠁵󠁿 Flag for Luxembourg (LU-LU)
🏴󠁩󠁮󠁯󠁲󠁿 Flag for Odisha (IN-OR)
🏴󠁣󠁺󠀱󠀰󠁿 Flag for Praha, Hlavní mešto (CZ-10)
🏴󠁭󠁸󠁣󠁨󠁨󠁿 Flag for Chihuahua (MX-CHH)
🏴󠁩󠁮󠁪󠁨󠁿 Flag for Jharkhand (IN-JH)
🏴󠁩󠁱󠁫󠁡󠁿 Flag for Karbala (IQ-KA)
🏴󠁩󠁱󠁤󠁱󠁿 Flag for Dhi Qar (IQ-DQ)
🏴󠁩󠁮󠁰󠁹󠁿 Flag for Puducherry (IN-PY)
👩🏿‍👦🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁩󠁱󠁳󠁵󠁿 Flag for Sulaymaniyah (IQ-SU)
🏴󠁩󠁤󠁳󠁬󠁿 Flag for Sulawesi (ID-SL)
🏴󠁩󠁱󠁡󠁮󠁿 Flag for Al Anbar (IQ-AN)
⛇ Black Snowman
🏴󠁩󠁱󠁭󠁡󠁿 Flag for Maysan (IQ-MA)
🏴󠁥󠁧󠁳󠁵󠁺󠁿 Flag for Suez (EG-SUZ)
🏴󠁵󠁳󠁯󠁲󠁿 Flag for Oregon (US-OR)
🏴󠁩󠁱󠁤󠁩󠁿 Flag for Diyala (IQ-DI)
🏴󠁣󠁯󠁡󠁴󠁬󠁿 Flag for Atlántico (CO-ATL)
🏴󠁩󠁱󠁮󠁩󠁿 Flag for Nineveh (IQ-NI)
🏴󠁩󠁱󠁤󠁡󠁿 Flag for Dohuk (IQ-DA)
🏴󠁩󠁱󠁭󠁵󠁿 Flag for Al Muthanna (IQ-MU)
🏴󠁩󠁮󠁭󠁺󠁿 Flag for Mizoram (IN-MZ)
🏴󠁩󠁮󠁭󠁬󠁿 Flag for Meghalaya (IN-ML)
0️ Digit Zero
🏴󠁩󠁱󠁱󠁡󠁿 Flag for Al-Qādisiyyah (IQ-QA)
🏴󠁩󠁱󠁢󠁧󠁿 Flag for Baghdad (IQ-BG)
🏴󠁩󠁮󠁫󠁬󠁿 Flag for Kerala (IN-KL)
3️ Digit Three
🏴󠁩󠁱󠁡󠁲󠁿 Flag for Erbil (IQ-AR)
🏴󠁣󠁨󠁮󠁥󠁿 Flag for Neuchâtel (CH-NE)
🏴󠁩󠁲󠀱󠀱󠁿 Flag for Zanjan (IR-11)
🏴󠁩󠁲󠀲󠀵󠁿 Flag for Yazd (IR-25)
🏴󠁩󠁲󠀰󠀵󠁿 Flag for Ilam (IR-05)
🏴󠁧󠁭󠁢󠁿 Flag for Banjul (GM-B)
🏴󠁩󠁳󠀵󠁿 Flag for Northwestern (IS-5)
🏴󠁩󠁲󠀱󠀲󠁿 Flag for Semnan (IR-12)
🏴󠁩󠁳󠀲󠁿 Flag for Southern Peninsula (IS-2)
🏴󠁡󠁲󠁬󠁿 Flag for La Pampa (AR-L)
🏴󠁩󠁱󠁷󠁡󠁿 Flag for Wasit (IQ-WA)
🏴󠁩󠁮󠁬󠁤󠁿 Flag for Lakshadweep (IN-LD)
🏴󠁩󠁳󠀶󠁿 Flag for Northeastern (IS-6)
🏴󠁣󠁨󠁪󠁵󠁿 Flag for Jura (CH-JU)
👩🏿‍❤️‍💋‍👩🏽 Kiss - Woman: Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁨󠁵󠁺󠁡󠁿 Flag for Zala (HU-ZA)
👨🏾‍👨🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
⛢ Astronomical Symbol for Uranus
🏴󠁩󠁤󠁳󠁭󠁿 Flag for Sumatra (ID-SM)
🏴󠁧󠁭󠁭󠁿 Flag for Central River Division (GM-M)
🏴󠁩󠁲󠀲󠀶󠁿 Flag for Qom (IR-26)
🏴󠁡󠁲󠁫󠁿 Flag for Catamarca (AR-K)
👨🏻‍👶🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone
🏴󠁧󠁹󠁭󠁡󠁿 Flag for Mahaica-Berbice (GY-MA)
🏴󠁳󠁩󠀰󠀹󠀰󠁿 Flag for Piran (SI-090)
🏴󠁩󠁥󠁬󠁿 Flag for Leinster (IE-L)
🏴󠁩󠁲󠀲󠀸󠁿 Flag for Qazvin (IR-28)
🏴󠁩󠁱󠁢󠁡󠁿 Flag for Basra (IQ-BA)
🏴󠁩󠁲󠀲󠀲󠁿 Flag for Markazi (IR-22)
🏴󠁩󠁲󠀲󠀳󠁿 Flag for Hormozgan (IR-23)
🏴󠁣󠁡󠁮󠁵󠁿 Flag for Nunavut (CA-NU)
🏴󠁡󠁧󠀱󠀰󠁿 Flag for Barbuda (AG-10)
🏴󠁰󠁴󠀱󠀱󠁿 Flag for Lisbon (PT-11)
🏴󠁩󠁳󠀷󠁿 Flag for Eastern (IS-7)
👩🏾‍❤️‍👩🏾 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁪󠁯󠁩󠁲󠁿 Flag for Irbid (JO-IR)
🏴󠁪󠁭󠀱󠀱󠁿 Flag for Saint Elizabeth (JM-11)
🏴󠁪󠁯󠁡󠁺󠁿 Flag for Zarqa (JO-AZ)
󠁽 Tag Right Curly Bracket
🏴󠁩󠁲󠀲󠀷󠁿 Flag for Golestan (IR-27)
🏴󠁪󠁭󠀱󠀰󠁿 Flag for Westmoreland (JM-10)
🏴󠁥󠁳󠁮󠁣󠁿 Flag for Navarra Chartered Community (ES-NC)
🏴󠁩󠁴󠀴󠀲󠁿 Flag for Liguria (IT-42)
🏴󠁣󠁯󠁢󠁯󠁬󠁿 Flag for Bolívar (CO-BOL)
🏴󠁴󠁲󠀷󠀲󠁿 Flag for Batman (TR-72)
🏴󠁪󠁯󠁢󠁡󠁿 Flag for Balqa (JO-BA)
🏴󠁪󠁭󠀱󠀳󠁿 Flag for Clarendon (JM-13)
🏴󠁩󠁴󠀵󠀷󠁿 Flag for Marche (IT-57)
🏴󠁨󠁴󠁳󠁤󠁿 Flag for Sud (HT-SD)
🏴󠁣󠁭󠁥󠁳󠁿 Flag for East (CM-ES)
🏴󠁪󠁯󠁪󠁡󠁿 Flag for Jerash (JO-JA)
🏴󠁩󠁴󠀶󠀷󠁿 Flag for Molise (IT-67)
🏴󠁪󠁯󠁡󠁴󠁿 Flag for Tafilah (JO-AT)
⚼ Sesquiquadrate
🏴󠁪󠁯󠁡󠁪󠁿 Flag for Ajloun (JO-AJ)
🏴󠁪󠁯󠁡󠁱󠁿 Flag for Aqaba (JO-AQ)
🏴󠁧󠁭󠁮󠁿 Flag for North Bank Division (GM-N)
🏴󠁩󠁲󠀰󠀸󠁿 Flag for Chaharmahal and Bakhtiari (IR-08)
🏴󠁪󠁭󠀰󠀷󠁿 Flag for Trelawny (JM-07)
🏴󠁪󠁭󠀰󠀶󠁿 Flag for Saint Ann (JM-06)
🏴󠁦󠁩󠀱󠀲󠁿 Flag for Ostrobothnia (FI-12)
☼ White Sun with Rays
🏴󠁪󠁯󠁡󠁭󠁿 Flag for Amman (JO-AM)
🏴󠁩󠁴󠀵󠀵󠁿 Flag for Umbria (IT-55)
🏴󠁧󠁨󠁷󠁰󠁿 Flag for Western (GH-WP)
󠀧 Tag Apostrophe
🏴󠁪󠁰󠀳󠀸󠁿 Flag for Ehime (JP-38)
🏴󠁪󠁰󠀳󠀵󠁿 Flag for Yamaguchi (JP-35)
🏴󠁪󠁰󠀳󠀲󠁿 Flag for Shimane (JP-32)
🏴󠁣󠁬󠁡󠁲󠁿 Flag for Araucanía (CL-AR)
🏴󠁪󠁰󠀳󠀶󠁿 Flag for Tokushima (JP-36)
🏴󠁪󠁰󠀱󠀹󠁿 Flag for Yamanashi (JP-19)
🏴󠁪󠁰󠀱󠀵󠁿 Flag for Niigata (JP-15)
🏴󠁪󠁰󠀱󠀶󠁿 Flag for Toyama (JP-16)
👨🏿‍👶🏿‍👦🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁪󠁯󠁭󠁮󠁿 Flag for Ma’an (JO-MN)
🏴󠁪󠁰󠀲󠀹󠁿 Flag for Nara (JP-29)
🏴󠁪󠁰󠀰󠀲󠁿 Flag for Aomori (JP-02)
🏴󠁪󠁰󠀰󠀵󠁿 Flag for Akita (JP-05)
🏴󠁪󠁰󠀲󠀰󠁿 Flag for Nagano (JP-20)
🏴󠁪󠁰󠀳󠀱󠁿 Flag for Tottori (JP-31)
🏴󠁪󠁰󠀰󠀳󠁿 Flag for Iwate (JP-03)
🏴󠁪󠁰󠀱󠀴󠁿 Flag for Kanagawa (JP-14)
⛁ White Draughts King
🏴󠁪󠁰󠀱󠀷󠁿 Flag for Ishikawa (JP-17)
🏴󠁪󠁯󠁭󠁡󠁿 Flag for Mafraq (JO-MA)
🏴󠁪󠁰󠀲󠀲󠁿 Flag for Shizuoka (JP-22)
🏴󠁳󠁥󠁷󠁿 Flag for Dalarna (SE-W)
🏴󠁪󠁰󠀲󠀸󠁿 Flag for Hyōgo (JP-28)
🏴󠁪󠁰󠀰󠀸󠁿 Flag for Ibaraki (JP-08)
🏴󠁪󠁰󠀰󠀴󠁿 Flag for Miyagi (JP-04)
🏴󠁣󠁵󠀱󠀲󠁿 Flag for Granma (CU-12)
🏴󠁪󠁰󠀲󠀵󠁿 Flag for Shiga (JP-25)
👩🏿‍❤️‍👨🏿 Couple With Heart - Woman: Dark Skin Tone, Man: Dark Skin Tone
🏴󠁪󠁰󠀳󠀰󠁿 Flag for Wakayama (JP-30)
🏴󠁪󠁰󠀰󠀹󠁿 Flag for Tochigi (JP-09)
🏴󠁪󠁰󠀱󠀰󠁿 Flag for Gunma (JP-10)
🏴󠁪󠁰󠀲󠀴󠁿 Flag for Mie (JP-24)
🏴󠁪󠁯󠁭󠁤󠁿 Flag for Madaba (JO-MD)
🏴󠁪󠁰󠀱󠀲󠁿 Flag for Chiba (JP-12)
🏴󠁪󠁰󠀳󠀳󠁿 Flag for Okayama (JP-33)
🏴󠁫󠁥󠀱󠀱󠁿 Flag for Kakamega (KE-11)
🏴󠁫󠁥󠀲󠀴󠁿 Flag for Mandera (KE-24)
🏴󠁫󠁥󠀰󠀹󠁿 Flag for Isiolo (KE-09)
🏴󠁭󠁫󠀰󠀴󠁿 Flag for Bitola (MK-04)
🏴󠁫󠁥󠀱󠀰󠁿 Flag for Kajiado (KE-10)
🏴󠁫󠁥󠀱󠀴󠁿 Flag for Kilifi (KE-14)
👩🏻‍👨🏻‍👦🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
⛀ White Draughts Man
🏴󠁪󠁰󠀳󠀹󠁿 Flag for Kōchi (JP-39)
🏴󠁧󠁹󠁰󠁭󠁿 Flag for Pomeroon-Supenaam (GY-PM)
🏴󠁫󠁥󠀰󠀳󠁿 Flag for Bungoma (KE-03)
🏴󠁫󠁥󠀲󠀸󠁿 Flag for Mombasa (KE-28)
🏴󠁫󠁥󠀲󠀷󠁿 Flag for Migori (KE-27)
🏴󠁪󠁰󠀴󠀳󠁿 Flag for Kumamoto (JP-43)
🏴󠁫󠁥󠀳󠀲󠁿 Flag for Nandi (KE-32)
🏴󠁪󠁰󠀴󠀰󠁿 Flag for Fukuoka (JP-40)
🏴󠁫󠁥󠀱󠀵󠁿 Flag for Kirinyaga (KE-15)
🏴󠁫󠁥󠀰󠀴󠁿 Flag for Busia (KE-04)
🏴󠁫󠁥󠀲󠀱󠁿 Flag for Lamu (KE-21)
🏴󠁫󠁥󠀲󠀰󠁿 Flag for Laikipia (KE-20)
🏴󠁫󠁥󠀰󠀶󠁿 Flag for Embu (KE-06)
🏴󠁫󠁥󠀰󠀵󠁿 Flag for Elgeyo-Marakwet (KE-05)
🏴󠁪󠁰󠀴󠀵󠁿 Flag for Miyazaki (JP-45)
🏴󠁫󠁥󠀱󠀶󠁿 Flag for Kisii (KE-16)
👨🏿‍👨🏿‍👧🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁪󠁰󠀰󠀶󠁿 Flag for Yamagata (JP-06)
🏴󠁫󠁥󠀲󠀳󠁿 Flag for Makueni (KE-23)
🏴󠁫󠁥󠀰󠀲󠁿 Flag for Bomet (KE-02)
🏴󠁫󠁥󠀱󠀳󠁿 Flag for Kiambu (KE-13)
🏴󠁫󠁥󠀲󠀶󠁿 Flag for Meru (KE-26)
🏴󠁫󠁥󠀲󠀹󠁿 Flag for Murang’a (KE-29)
🏴󠁫󠁥󠀳󠀳󠁿 Flag for Narok (KE-33)
👨🏻‍👩🏻‍👧🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
🏴󠁫󠁥󠀳󠀶󠁿 Flag for Nyeri (KE-36)
🏴󠁫󠁧󠁣󠁿 Flag for Chuy (KG-C)
🏴󠁫󠁨󠀲󠀳󠁿 Flag for Kep (KH-23)
🏴󠁫󠁥󠀳󠀹󠁿 Flag for Taita-Taveta (KE-39)
🏴󠁫󠁨󠀱󠀲󠁿 Flag for Phnom Penh (KH-12)
🏴󠁫󠁥󠀴󠀴󠁿 Flag for Uasin Gishu (KE-44)
🏴󠁫󠁥󠀴󠀷󠁿 Flag for West Pokot (KE-47)
🏴󠁫󠁥󠀰󠀸󠁿 Flag for Homa Bay (KE-08)
🏴󠁫󠁨󠀲󠀵󠁿 Flag for Tbong Khmum (KH-25)
🏴󠁫󠁥󠀴󠀱󠁿 Flag for Tharaka-Nithi (KE-41)
🏴󠁫󠁨󠀱󠀱󠁿 Flag for Mondulkiri (KH-11)
🏴󠁫󠁨󠀱󠀸󠁿 Flag for Sihanoukville (KH-18)
🏴󠁫󠁥󠀳󠀸󠁿 Flag for Siaya (KE-38)
🏴󠁫󠁨󠀲󠀱󠁿 Flag for Takéo (KH-21)
🏴󠁫󠁨󠀲󠁿 Flag for Battambang (KH-2)
🏴󠁫󠁨󠀲󠀴󠁿 Flag for Pailin (KH-24)
🏴󠁫󠁨󠀱󠀴󠁿 Flag for Prey Veng (KH-14)
🏴󠁫󠁨󠀱󠀷󠁿 Flag for Siem Reap (KH-17)
🏴󠁫󠁨󠀱󠀹󠁿 Flag for Stung Treng (KH-19)
🏴󠁫󠁥󠀳󠀵󠁿 Flag for Nyandarua (KE-35)
🏴󠁫󠁨󠀱󠀰󠁿 Flag for Kratié (KH-10)
🏴󠁫󠁥󠀴󠀵󠁿 Flag for Vihiga (KE-45)
🏴󠁫󠁨󠀱󠁿 Flag for Banteay Meanchey (KH-1)
🏴󠁫󠁧󠁹󠁿 Flag for Issyk-Kul (KG-Y)
🏴󠁫󠁧󠁴󠁿 Flag for Talas (KG-T)
🏴󠁫󠁧󠁯󠁿 Flag for Osh Region (KG-O)
🏴󠁫󠁨󠀱󠀶󠁿 Flag for Ratanakiri (KH-16)
🏴󠁫󠁥󠀲󠀲󠁿 Flag for Machakos (KE-22)
🏴󠁫󠁧󠁪󠁿 Flag for Jalal-Abad (KG-J)
🏴󠁫󠁥󠀴󠀳󠁿 Flag for Turkana (KE-43)
🏴󠁫󠁥󠀳󠀴󠁿 Flag for Nyamira (KE-34)
🏴󠁫󠁧󠁧󠁢󠁿 Flag for Bishkek (KG-GB)
🏴󠁫󠁨󠀲󠀲󠁿 Flag for Oddar Meanchey (KH-22)
🏴󠁫󠁨󠀱󠀵󠁿 Flag for Pursat (KH-15)
🏴󠁫󠁥󠀳󠀷󠁿 Flag for Samburu (KE-37)
🏴󠁫󠁧󠁮󠁿 Flag for Naryn (KG-N)
⚿ Squared Key
⚸ Black Moon Lilith
🏴󠁫󠁲󠀴󠀵󠁿 Flag for North Jeolla (KR-45)
🏴󠁫󠁰󠀰󠀸󠁿 Flag for South Hamgyong (KP-08)
🏴󠁫󠁰󠀰󠀴󠁿 Flag for Chagang (KP-04)
🏴󠁡󠁲󠁪󠁿 Flag for San Juan (AR-J)
🏴󠁫󠁰󠀰󠀹󠁿 Flag for North Hamgyong (KP-09)
🏴󠁫󠁲󠀳󠀱󠁿 Flag for Ulsan (KR-31)
🏴󠁫󠁨󠀹󠁿 Flag for Koh Kong (KH-9)
🏴󠁫󠁰󠀱󠀳󠁿 Flag for Rason (KP-13)
⚤ Interlocked Female and Male Sign
👩🏼‍👨🏼‍👶🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁫󠁲󠀴󠀶󠁿 Flag for South Jeolla (KR-46)
🏴󠁥󠁣󠁯󠁿 Flag for El Oro (EC-O)
🏴󠁫󠁰󠀰󠀳󠁿 Flag for North Pyongan (KP-03)
🏴󠁫󠁨󠀶󠁿 Flag for Kampong Thom (KH-6)
🏴󠁫󠁨󠀵󠁿 Flag for Kampong Speu (KH-5)
🏴󠁫󠁲󠀳󠀰󠁿 Flag for Daejeon (KR-30)
🏴󠁫󠁲󠀴󠀲󠁿 Flag for Gangwon (KR-42)
🏴󠁥󠁴󠁡󠁡󠁿 Flag for Addis Ababa (ET-AA)
🏴󠁫󠁨󠀷󠁿 Flag for Kampot (KH-7)
🏴󠁫󠁨󠀳󠁿 Flag for Kampong Cham (KH-3)
🏴󠁫󠁰󠀱󠀰󠁿 Flag for Ryanggang (KP-10)
🏴󠁫󠁨󠀸󠁿 Flag for Kandal (KH-8)
🏴󠁫󠁲󠀲󠀸󠁿 Flag for Incheon (KR-28)
🏴󠁦󠁩󠀰󠀷󠁿 Flag for Central Ostrobothnia (FI-07)
🏴󠁫󠁰󠀰󠀵󠁿 Flag for South Hwanghae (KP-05)
🏴󠁫󠁲󠀴󠀴󠁿 Flag for South Chungcheong (KR-44)
🏴󠁫󠁷󠁪󠁡󠁿 Flag for Al Jahra (KW-JA)
🏴󠁫󠁺󠁳󠁥󠁶󠁿 Flag for North Kazakhstan (KZ-SEV)
🏴󠁫󠁲󠀵󠀰󠁿 Flag for Sejong (KR-50)
🏴󠁫󠁲󠀴󠀳󠁿 Flag for North Chungcheong (KR-43)
🏴󠁫󠁺󠁡󠁬󠁭󠁿 Flag for Almaty Region (KZ-ALM)
🏴󠁫󠁷󠁦󠁡󠁿 Flag for Al Farwaniyah (KW-FA)
⚲ Neuter
🏴󠁫󠁲󠀴󠀱󠁿 Flag for Gyeonggi (KR-41)
🏴󠁩󠁮󠁡󠁲󠁿 Flag for Arunachal Pradesh (IN-AR)
🏴󠁫󠁺󠁡󠁫󠁴󠁿 Flag for Aktobe (KZ-AKT)
🏴󠁬󠁡󠁨󠁯󠁿 Flag for Houaphanh (LA-HO)
👨🏻‍👶🏻‍👶🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🏴󠁫󠁺󠁭󠁡󠁮󠁿 Flag for Mangystau (KZ-MAN)
🏴󠁬󠁡󠁰󠁨󠁿 Flag for Phongsaly (LA-PH)
🏴󠁫󠁺󠁺󠁨󠁡󠁿 Flag for Jambyl (KZ-ZHA)
🏴󠁫󠁺󠁫󠁵󠁳󠁿 Flag for Kostanay (KZ-KUS)
🏴󠁫󠁺󠁫󠁺󠁹󠁿 Flag for Kyzylorda (KZ-KZY)
🏴󠁦󠁲󠁧󠁵󠁡󠁿 Flag for Guadeloupe (FR-GUA)
🏴󠁫󠁭󠁧󠁿 Flag for Grande Comore (KM-G)
🏴󠁬󠁡󠁬󠁰󠁿 Flag for Luang Prabang (LA-LP)
⚻ Quincunx
🏴󠁫󠁷󠁫󠁵󠁿 Flag for Al Asimah (KW-KU)
🏴󠁬󠁡󠁳󠁬󠁿 Flag for Salavan (LA-SL)
🏴󠁫󠁺󠁡󠁴󠁹󠁿 Flag for Atyrau (KZ-ATY)
🏴󠁫󠁷󠁡󠁨󠁿 Flag for Al Ahmadi (KW-AH)
🏴󠁫󠁺󠁰󠁡󠁶󠁿 Flag for Pavlodar (KZ-PAV)
🏴󠁬󠁡󠁯󠁵󠁿 Flag for Oudomxay (LA-OU)
🏴󠁬󠁡󠁣󠁨󠁿 Flag for Champasak (LA-CH)
🏴󠁫󠁷󠁭󠁵󠁿 Flag for Mubarak Al-Kabeer (KW-MU)
󠁏 Tag Latin Capital Letter O
🏴󠁬󠁡󠁶󠁴󠁿 Flag for Vientiane (LA-VT)
🏴󠁫󠁺󠁫󠁡󠁲󠁿 Flag for Karagandy (KZ-KAR)
🏴󠁪󠁭󠀰󠀹󠁿 Flag for Hanover (JM-09)
🏴󠁫󠁭󠁡󠁿 Flag for Anjouan (KM-A)
🏴󠁬󠁡󠁬󠁭󠁿 Flag for Luang Namtha (LA-LM)
🏴󠁬󠁡󠁸󠁡󠁿 Flag for Sainyabuli (LA-XA)
🏴󠁬󠁢󠁪󠁡󠁿 Flag for South (LB-JA)
🏴󠁬󠁫󠀶󠁿 Flag for North Western (LK-6)
🏴󠁬󠁩󠀰󠀲󠁿 Flag for Eschen (LI-02)
🏴󠁬󠁢󠁢󠁨󠁿 Flag for Baalbek-Hermel (LB-BH)
🏴󠁬󠁣󠀰󠀳󠁿 Flag for Choiseul (LC-03)
🏴󠁬󠁢󠁡󠁳󠁿 Flag for North (LB-AS)
🏴󠁦󠁲󠁯󠁣󠁣󠁿 Flag for Occitanie (FR-OCC)
🏴󠁬󠁫󠀲󠁿 Flag for Central (LK-2)
🏴󠁬󠁣󠀰󠀶󠁿 Flag for Gros Islet (LC-06)
🏴󠁦󠁩󠀰󠀴󠁿 Flag for Southern Savonia (FI-04)
🏴󠁬󠁣󠀰󠀵󠁿 Flag for Dennery (LC-05)
🏴󠁬󠁫󠀸󠁿 Flag for Uva (LK-8)
🏴󠁬󠁫󠀷󠁿 Flag for North Central (LK-7)
🏴󠁬󠁩󠀰󠀴󠁿 Flag for Mauren (LI-04)
🏴󠁬󠁣󠀰󠀷󠁿 Flag for Laborie (LC-07)
🏴󠁬󠁣󠀰󠀲󠁿 Flag for Castries (LC-02)
🏴󠁬󠁩󠀱󠀰󠁿 Flag for Triesenberg (LI-10)
⚺ Semisextile
🏴󠁬󠁣󠀱󠀲󠁿 Flag for Canaries (LC-12)
🏴󠁬󠁩󠀱󠀱󠁿 Flag for Vaduz (LI-11)
♲ Universal Recycling Symbol
🏴󠁬󠁢󠁮󠁡󠁿 Flag for Nabatieh (LB-NA)
🏴󠁬󠁩󠀰󠀶󠁿 Flag for Ruggell (LI-06)
🏴󠁬󠁣󠀱󠀰󠁿 Flag for Soufrière (LC-10)
🏴󠁫󠁥󠀰󠀷󠁿 Flag for Garissa (KE-07)
🏴󠁬󠁫󠀴󠁿 Flag for Northern (LK-4)
🏴󠁬󠁣󠀰󠀱󠁿 Flag for Anse la Raye (LC-01)
🏴󠁬󠁩󠀰󠀹󠁿 Flag for Triesen (LI-09)
🏴󠁬󠁩󠀰󠀳󠁿 Flag for Gamprin (LI-03)
🏴󠁬󠁳󠁨󠁿 Flag for Qacha’s Nek (LS-H)
🏴󠁣󠁦󠁫󠁢󠁿 Flag for Nana-Grébizi (CF-KB)
🏴󠁭󠁫󠀵󠀲󠁿 Flag for Makedonski Brod (MK-52)
🏴󠁬󠁴󠀱󠀴󠁿 Flag for Kalvarija (LT-14)
🏴󠁬󠁲󠁧󠁰󠁿 Flag for Gbarpolu (LR-GP)
🏴󠁬󠁴󠀱󠀵󠁿 Flag for Kauno Municipality (LT-15)
🏴󠁬󠁴󠀰󠀶󠁿 Flag for Biržai (LT-06)
🏴󠁬󠁴󠀱󠀲󠁿 Flag for Jurbarkas (LT-12)
🏴󠁦󠁲󠁷󠁦󠁿 Flag for Wallis & Futuna (FR-WF)
🏴󠁬󠁳󠁪󠁿 Flag for Mokhotlong (LS-J)
🏴󠁬󠁳󠁢󠁿 Flag for Butha-Buthe (LS-B)
🏴󠁬󠁳󠁫󠁿 Flag for Thaba-Tseka (LS-K)
🏴󠁬󠁴󠀱󠀰󠁿 Flag for Jonava (LT-10)
⚵ Juno
🏴󠁬󠁲󠁮󠁩󠁿 Flag for Nimba (LR-NI)
🏴󠁬󠁴󠀰󠀵󠁿 Flag for Birštonas (LT-05)
🏴󠁩󠁮󠁢󠁲󠁿 Flag for Bihar (IN-BR)
🏴󠁧󠁭󠁷󠁿 Flag for West Coast Division (GM-W)
🏴󠁬󠁴󠀰󠀷󠁿 Flag for Druskininkai (LT-07)
🏴󠁬󠁳󠁧󠁿 Flag for Quthing (LS-G)
🏴󠁬󠁲󠁬󠁯󠁿 Flag for Lofa (LR-LO)
🏴󠁫󠁰󠀰󠀷󠁿 Flag for Kangwon (KP-07)
🏴󠁬󠁳󠁦󠁿 Flag for Mohale’s Hoek (LS-F)
🏴󠁬󠁴󠀰󠀱󠁿 Flag for Akmenė (LT-01)
🏴󠁬󠁲󠁭󠁧󠁿 Flag for Margibi (LR-MG)
🀒 Mahjong Tile Three of Bamboos
🏴󠁬󠁴󠀱󠀳󠁿 Flag for Kaišiadorys (LT-13)
🏴󠁬󠁴󠀰󠀸󠁿 Flag for Elektrėnai (LT-08)
🏴󠁬󠁲󠁲󠁩󠁿 Flag for Rivercess (LR-RI)
󠁆 Tag Latin Capital Letter F
🏴󠁬󠁴󠀰󠀳󠁿 Flag for Alytus (LT-03)
🏴󠁬󠁴󠀰󠀹󠁿 Flag for Ignalina (LT-09)
🏴󠁬󠁳󠁥󠁿 Flag for Mafeteng (LS-E)
🏴󠁬󠁴󠀰󠀴󠁿 Flag for Anykščiai (LT-04)
🏴󠁬󠁲󠁳󠁩󠁿 Flag for Sinoe (LR-SI)
🏴󠁬󠁲󠁧󠁢󠁿 Flag for Grand Bassa (LR-GB)
🏴󠁦󠁲󠁧󠁦󠁿 Flag for French Guiana (FR-GF)
🏴󠁬󠁴󠀱󠀱󠁿 Flag for Joniškis (LT-11)
🏴󠁬󠁳󠁤󠁿 Flag for Berea (LS-D)
🏴󠁬󠁴󠀵󠀶󠁿 Flag for Vilkaviškis (LT-56)
🏴󠁬󠁴󠀴󠀱󠁿 Flag for Šakiai (LT-41)
🏴󠁬󠁴󠀴󠀰󠁿 Flag for Rokiškis (LT-40)
🏴󠁬󠁴󠀳󠀶󠁿 Flag for Prienai (LT-36)
🏴󠁬󠁴󠀳󠀸󠁿 Flag for Raseiniai (LT-38)
🏴󠁬󠁴󠀳󠀵󠁿 Flag for Plungė (LT-35)
🏴󠁬󠁴󠀴󠀸󠁿 Flag for Skuodas (LT-48)
🏴󠁬󠁴󠀳󠀱󠁿 Flag for Palanga (LT-31)
🏴󠁬󠁴󠀲󠀴󠁿 Flag for Lazdijai (LT-24)
🏴󠁬󠁴󠀲󠀷󠁿 Flag for Molėtai (LT-27)
🏴󠁬󠁴󠀴󠀵󠁿 Flag for Šilalė (LT-45)
🏴󠁬󠁴󠀴󠀲󠁿 Flag for Šalčininkai (LT-42)
🏴󠁬󠁴󠀵󠀱󠁿 Flag for Telšiai (LT-51)
🏴󠁬󠁴󠀳󠀷󠁿 Flag for Radviliškis (LT-37)
🏴󠁬󠁴󠀵󠀲󠁿 Flag for Trakai (LT-52)
🏴󠁦󠁭󠁰󠁮󠁩󠁿 Flag for Pohnpei (FM-PNI)
🏴󠁬󠁴󠀲󠀲󠁿 Flag for Kretinga (LT-22)
🏴󠁬󠁴󠀱󠀸󠁿 Flag for Kėdainiai (LT-18)
🏴󠁬󠁴󠀱󠀷󠁿 Flag for Kazlų Rūda (LT-17)
🏴󠁬󠁴󠀴󠀷󠁿 Flag for Širvintos (LT-47)
🏴󠁬󠁴󠀳󠀳󠁿 Flag for Panevėžys (LT-33)
🏴󠁬󠁴󠀴󠀳󠁿 Flag for Šiaulių Municipality (LT-43)
🏴󠁬󠁴󠀴󠀴󠁿 Flag for Šiauliai (LT-44)
🏴󠁬󠁴󠀱󠀹󠁿 Flag for Kelmė (LT-19)
🏴󠁬󠁴󠀵󠀵󠁿 Flag for Varėna (LT-55)
🏴󠁬󠁴󠀳󠀴󠁿 Flag for Pasvalys (LT-34)
🏴󠁬󠁴󠀲󠀱󠁿 Flag for Klaipėda (LT-21)
🏴󠁬󠁴󠀴󠀹󠁿 Flag for Švenčionys (LT-49)
🏴󠁬󠁴󠀵󠀴󠁿 Flag for Utena (LT-54)
🏴󠁬󠁴󠀲󠀹󠁿 Flag for Pagėgiai (LT-29)
🏴󠁬󠁴󠀵󠀰󠁿 Flag for Tauragė (LT-50)
🏴󠁬󠁴󠀴󠀶󠁿 Flag for Šilutė (LT-46)
🏴󠁬󠁴󠀵󠀳󠁿 Flag for Ukmergė (LT-53)
🏴󠁬󠁴󠀳󠀹󠁿 Flag for Rietavas (LT-39)
🏴󠁬󠁴󠀲󠀵󠁿 Flag for Marijampolė (LT-25)
🏴󠁬󠁴󠀲󠀶󠁿 Flag for Mažeikiai (LT-26)
🏴󠁬󠁴󠀲󠀳󠁿 Flag for Kupiškis (LT-23)
🏴󠁬󠁴󠀲󠀸󠁿 Flag for Neringa (LT-28)
🏴󠁬󠁶󠀰󠀰󠀱󠁿 Flag for Aglona (LV-001)
🏴󠁬󠁴󠀵󠀹󠁿 Flag for Visaginas (LT-59)
👩🏽‍👨🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁬󠁵󠁲󠁭󠁿 Flag for Remich (LU-RM)
🏴󠁬󠁴󠁶󠁬󠁿 Flag for Vilnius County (LT-VL)
🏴󠁬󠁴󠁭󠁲󠁿 Flag for Marijampolė County (LT-MR)
🏴󠁬󠁶󠀰󠀰󠀲󠁿 Flag for Aizkraukle (LV-002)
🏴󠁬󠁶󠀰󠀱󠀱󠁿 Flag for Ādaži (LV-011)
🏴󠁬󠁶󠀰󠀰󠀳󠁿 Flag for Aizpute (LV-003)
🏴󠁩󠁴󠀸󠀲󠁿 Flag for Sicily (IT-82)
🏴󠁣󠁯󠁣󠁥󠁳󠁿 Flag for Cesar (CO-CES)
🏴󠁬󠁶󠀰󠀰󠀴󠁿 Flag for Aknīste (LV-004)
🏴󠁬󠁴󠁴󠁡󠁿 Flag for Tauragė County (LT-TA)
🏴󠁬󠁶󠀰󠀱󠀳󠁿 Flag for Baldone (LV-013)
🏴󠁬󠁴󠁵󠁴󠁿 Flag for Utena County (LT-UT)
🏴󠁬󠁵󠁤󠁩󠁿 Flag for Diekirch (LU-DI)
🏴󠁬󠁶󠀰󠀰󠀸󠁿 Flag for Amata (LV-008)
🏴󠁬󠁴󠁡󠁬󠁿 Flag for Alytus County (LT-AL)
🏴󠁬󠁵󠁧󠁲󠁿 Flag for Grevenmacher (LU-GR)
🏴󠁬󠁵󠁣󠁬󠁿 Flag for Clervaux (LU-CL)
🏴󠁬󠁴󠁫󠁬󠁿 Flag for Klaipėda County (LT-KL)
🏴󠁬󠁵󠁶󠁤󠁿 Flag for Vianden (LU-VD)
🏴󠁬󠁴󠁳󠁡󠁿 Flag for Šiauliai County (LT-SA)
🏴󠁬󠁴󠁴󠁥󠁿 Flag for Telšiai County (LT-TE)
🏴󠁬󠁵󠁥󠁣󠁿 Flag for Echternach (LU-EC)
🏴󠁬󠁵󠁷󠁩󠁿 Flag for Wiltz (LU-WI)
🏴󠁬󠁴󠀶󠀰󠁿 Flag for Zarasai (LT-60)
🏴󠁬󠁶󠀰󠀰󠀷󠁿 Flag for Alūksne (LV-007)
🏴󠁫󠁺󠁶󠁯󠁳󠁿 Flag for East Kazakhstan (KZ-VOS)
🏴󠁦󠁲󠁮󠁯󠁲󠁿 Flag for Normandie (FR-NOR)
🏴󠁬󠁵󠁭󠁥󠁿 Flag for Mersch (LU-ME)
🏴󠁡󠁭󠁳󠁵󠁿 Flag for Syunik (AM-SU)
🏴󠁬󠁶󠀰󠀳󠀵󠁿 Flag for Ikšķile (LV-035)
🏴󠁬󠁶󠀰󠀱󠀵󠁿 Flag for Balvi (LV-015)
🏴󠁬󠁶󠀰󠀱󠀷󠁿 Flag for Beverīna (LV-017)
🏴󠁬󠁶󠀰󠀱󠀹󠁿 Flag for Burtnieki (LV-019)
🏴󠁬󠁶󠀰󠀲󠀷󠁿 Flag for Dundaga (LV-027)
🏴󠁬󠁶󠀰󠀲󠀱󠁿 Flag for Cesvaine (LV-021)
🏴󠁬󠁶󠀰󠀴󠀵󠁿 Flag for Kocēni (LV-045)
🏴󠁬󠁶󠀰󠀴󠀳󠁿 Flag for Kandava (LV-043)
🏴󠁬󠁶󠀰󠀳󠀲󠁿 Flag for Grobiņa (LV-032)
🏴󠁬󠁶󠀰󠀳󠀳󠁿 Flag for Gulbene (LV-033)
🏴󠁬󠁶󠀰󠀴󠀰󠁿 Flag for Jaunpils (LV-040)
⚶ Vesta
🏴󠁬󠁶󠀰󠀲󠀰󠁿 Flag for Carnikava (LV-020)
🏴󠁬󠁶󠀰󠀴󠀹󠁿 Flag for Krustpils (LV-049)
👩🏾‍👨🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁬󠁶󠀰󠀲󠀶󠁿 Flag for Dobele (LV-026)
🏴󠁬󠁶󠀰󠀴󠀲󠁿 Flag for Jēkabpils Municipality (LV-042)
🏴󠁬󠁶󠀰󠀳󠀱󠁿 Flag for Garkalne (LV-031)
🏴󠁬󠁶󠀰󠀳󠀰󠁿 Flag for Ērgļi (LV-030)
🏴󠁬󠁶󠀰󠀱󠀸󠁿 Flag for Brocēni (LV-018)
🏴󠁬󠁶󠀰󠀴󠀷󠁿 Flag for Krāslava (LV-047)
🏴󠁬󠁶󠀰󠀳󠀸󠁿 Flag for Jaunjelgava (LV-038)
🏴󠁬󠁶󠀰󠀱󠀶󠁿 Flag for Bauska (LV-016)
🏴󠁬󠁶󠀰󠀱󠀴󠁿 Flag for Baltinava (LV-014)
🏴󠁬󠁶󠀰󠀴󠀴󠁿 Flag for Kārsava (LV-044)
🏴󠁬󠁶󠀰󠀳󠀴󠁿 Flag for Iecava (LV-034)
🏴󠁬󠁶󠀰󠀳󠀹󠁿 Flag for Jaunpiebalga (LV-039)
🏴󠁬󠁶󠀰󠀲󠀲󠁿 Flag for Cēsis (LV-022)
🏴󠁬󠁶󠀰󠀵󠀰󠁿 Flag for Kuldīga (LV-050)
🏴󠁬󠁶󠀰󠀴󠀸󠁿 Flag for Krimulda (LV-048)
🏴󠁬󠁶󠀰󠀵󠀱󠁿 Flag for Ķegums (LV-051)
🏴󠁬󠁶󠀰󠀲󠀸󠁿 Flag for Durbe (LV-028)
🏴󠁬󠁶󠀰󠀲󠀳󠁿 Flag for Cibla (LV-023)
🏴󠁬󠁶󠀰󠀲󠀹󠁿 Flag for Engure (LV-029)
🏴󠁬󠁶󠀰󠀵󠀶󠁿 Flag for Līvāni (LV-056)
🏴󠁬󠁶󠀰󠀶󠀶󠁿 Flag for Nīca (LV-066)
🏴󠁬󠁶󠀰󠀷󠀹󠁿 Flag for Roja (LV-079)
🏴󠁬󠁶󠀰󠀵󠀲󠁿 Flag for Ķekava (LV-052)
🏴󠁬󠁶󠀰󠀷󠀰󠁿 Flag for Pārgauja (LV-070)
🏴󠁬󠁶󠀰󠀵󠀳󠁿 Flag for Lielvārde (LV-053)
🏴󠁬󠁶󠀰󠀷󠀲󠁿 Flag for Pļaviņas (LV-072)
🏴󠁬󠁶󠀰󠀷󠀱󠁿 Flag for Pāvilosta (LV-071)
🏴󠁣󠁡󠁮󠁳󠁿 Flag for Nova Scotia (CA-NS)
🏴󠁬󠁶󠀰󠀷󠀶󠁿 Flag for Rauna (LV-076)
🏴󠁬󠁶󠀰󠀵󠀴󠁿 Flag for Limbaži (LV-054)
🏴󠁬󠁶󠀰󠀶󠀴󠁿 Flag for Naukšēni (LV-064)
🏴󠁬󠁶󠀰󠀸󠀳󠁿 Flag for Rundāle (LV-083)
🏴󠁬󠁶󠀰󠀸󠀱󠁿 Flag for Rucava (LV-081)
🏴󠁬󠁶󠀰󠀶󠀳󠁿 Flag for Mērsrags (LV-063)
🏴󠁬󠁶󠀰󠀶󠀸󠁿 Flag for Olaine (LV-068)
🏴󠁬󠁶󠀰󠀶󠀱󠁿 Flag for Mālpils (LV-061)
🏴󠁬󠁶󠀰󠀸󠀷󠁿 Flag for Salaspils (LV-087)
🏴󠁬󠁶󠀰󠀶󠀲󠁿 Flag for Mārupe (LV-062)
🏴󠁬󠁶󠀰󠀸󠀴󠁿 Flag for Rūjiena (LV-084)
🏴󠁬󠁶󠀰󠀸󠀹󠁿 Flag for Saulkrasti (LV-089)
🏴󠁬󠁶󠀰󠀸󠀶󠁿 Flag for Salacgrīva (LV-086)
🏴󠁬󠁶󠀰󠀵󠀷󠁿 Flag for Lubāna (LV-057)
🏴󠁬󠁶󠀰󠀶󠀵󠁿 Flag for Nereta (LV-065)
🏴󠁬󠁶󠀰󠀶󠀹󠁿 Flag for Ozolnieki (LV-069)
🏴󠁬󠁶󠀰󠀸󠀰󠁿 Flag for Ropaži (LV-080)
🏴󠁬󠁶󠀰󠀸󠀲󠁿 Flag for Rugāji (LV-082)
🏴󠁬󠁶󠀰󠀷󠀸󠁿 Flag for Riebiņi (LV-078)
🏴󠁬󠁶󠀰󠀷󠀵󠁿 Flag for Priekuļi (LV-075)
🏴󠁬󠁶󠀰󠀵󠀸󠁿 Flag for Ludza (LV-058)
🏴󠁬󠁶󠀰󠀹󠀰󠁿 Flag for Sēja (LV-090)
🏴󠁬󠁶󠀰󠀷󠀴󠁿 Flag for Priekule (LV-074)
🏴󠁬󠁶󠀰󠀸󠀸󠁿 Flag for Saldus (LV-088)
🏴󠁬󠁶󠀰󠀵󠀵󠁿 Flag for Līgatne (LV-055)
🏴󠁬󠁶󠀰󠀷󠀳󠁿 Flag for Preiļi (LV-073)
🏴󠁬󠁹󠁫󠁦󠁿 Flag for Kufra (LY-KF)
👩🏿‍👨🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁬󠁶󠀰󠀹󠀹󠁿 Flag for Tukums (LV-099)
🏴󠁬󠁹󠁧󠁴󠁿 Flag for Ghat (LY-GT)
🏴󠁬󠁶󠀱󠀰󠀷󠁿 Flag for Viesīte (LV-107)
🏴󠁬󠁶󠁪󠁫󠁢󠁿 Flag for Jēkabpils (LV-JKB)
🏴󠁬󠁶󠀰󠀹󠀵󠁿 Flag for Stopiņi (LV-095)
🏴󠁬󠁶󠀰󠀹󠀱󠁿 Flag for Sigulda (LV-091)
🏴󠁬󠁶󠀰󠀹󠀳󠁿 Flag for Skrunda (LV-093)
🏴󠁬󠁶󠁬󠁰󠁸󠁿 Flag for Liepāja (LV-LPX)
🏴󠁬󠁶󠁤󠁧󠁶󠁿 Flag for Daugavpils (LV-DGV)
🏴󠁬󠁶󠀱󠀰󠀲󠁿 Flag for Varakļāni (LV-102)
🏴󠁬󠁹󠁪󠁧󠁿 Flag for Jabal al Gharbi (LY-JG)
🏴󠁬󠁹󠁪󠁡󠁿 Flag for Jabal al Akhdar (LY-JA)
🏴󠁧󠁲󠁫󠁿 Flag for North Aegean (GR-K)
🏴󠁬󠁶󠀰󠀹󠀲󠁿 Flag for Skrīveri (LV-092)
🏴󠁬󠁶󠀰󠀹󠀷󠁿 Flag for Talsi (LV-097)
🏴󠁬󠁹󠁭󠁢󠁿 Flag for Murqub (LY-MB)
🏴󠁬󠁶󠁪󠁥󠁬󠁿 Flag for Jelgava (LV-JEL)
🏴󠁬󠁹󠁢󠁡󠁿 Flag for Benghazi (LY-BA)
🏴󠁬󠁶󠁶󠁭󠁲󠁿 Flag for Valmiera (LV-VMR)
🏴󠁬󠁶󠀱󠀰󠀹󠁿 Flag for Viļāni (LV-109)
🏴󠁬󠁶󠀱󠀰󠀳󠁿 Flag for Vārkava (LV-103)
🏴󠁬󠁶󠁲󠁥󠁺󠁿 Flag for Rēzekne (LV-REZ)
🏴󠁬󠁶󠀱󠀱󠀰󠁿 Flag for Zilupe (LV-110)
🏴󠁬󠁶󠀰󠀹󠀶󠁿 Flag for Strenči (LV-096)
🏴󠁬󠁹󠁤󠁲󠁿 Flag for Derna (LY-DR)
🏴󠁬󠁶󠁶󠁥󠁮󠁿 Flag for Ventspils (LV-VEN)
🏴󠁬󠁶󠀱󠀰󠀴󠁿 Flag for Vecpiebalga (LV-104)
🏴󠁬󠁶󠀱󠀰󠀵󠁿 Flag for Vecumnieki (LV-105)
🏴󠁬󠁶󠀱󠀰󠀸󠁿 Flag for Viļaka (LV-108)
🏴󠁬󠁶󠁪󠁵󠁲󠁿 Flag for Jūrmala (LV-JUR)
🏴󠁬󠁶󠀱󠀰󠀱󠁿 Flag for Valka (LV-101)
🏴󠁬󠁶󠀰󠀹󠀸󠁿 Flag for Tērvete (LV-098)
🏴󠁬󠁶󠀰󠀹󠀴󠁿 Flag for Smiltene (LV-094)
🏴󠁭󠁡󠀰󠀶󠁿 Flag for Meknès-Tafilalet (MA-06)
🏴󠁭󠁣󠁦󠁯󠁿 Flag for Fontvieille (MC-FO)
🏴󠁬󠁹󠁳󠁲󠁿 Flag for Sirte (LY-SR)
🏴󠁭󠁣󠁭󠁡󠁿 Flag for Malbousquet (MC-MA)
🏴󠁬󠁹󠁳󠁢󠁿 Flag for Sabha (LY-SB)
🏴󠁡󠁤󠀰󠀴󠁿 Flag for La Massana (AD-04)
🏴󠁭󠁡󠀰󠀹󠁿 Flag for Chaouia-Ouardigha (MA-09)
🏴󠁰󠁥󠁣󠁵󠁳󠁿 Flag for Cusco (PE-CUS)
🏴󠁬󠁹󠁮󠁱󠁿 Flag for Nuqat al Khams (LY-NQ)
🏴󠁬󠁹󠁴󠁢󠁿 Flag for Tripoli (LY-TB)
🏴󠁭󠁡󠀱󠀱󠁿 Flag for Marrakesh-Tensift-El Haouz (MA-11)
🏴󠁭󠁣󠁣󠁬󠁿 Flag for La Colle (MC-CL)
🏴󠁧󠁮󠁬󠁿 Flag for Labé Region (GN-L)
🏴󠁭󠁡󠀰󠀳󠁿 Flag for Taza-Al Hoceima-Taounate (MA-03)
🏴󠁭󠁡󠀰󠀷󠁿 Flag for Rabat-Salé-Zemmour-Zaer (MA-07)
🏴󠁭󠁣󠁣󠁯󠁿 Flag for La Condamine (MC-CO)
🏴󠁭󠁡󠀱󠀶󠁿 Flag for Oued Ed-Dahab-Lagouira (MA-16)
🏴󠁬󠁹󠁷󠁳󠁿 Flag for Wadi al Shatii (LY-WS)
⚩ Horizontal Male with Stroke Sign
🏴󠁬󠁹󠁮󠁬󠁿 Flag for Nalut (LY-NL)
👨🏽‍👶🏽‍👦🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁭󠁡󠀱󠀲󠁿 Flag for Tadla-Azilal (MA-12)
🏴󠁬󠁹󠁭󠁱󠁿 Flag for Murzuq (LY-MQ)
🏴󠁬󠁹󠁷󠁤󠁿 Flag for Wadi al Hayaa (LY-WD)
🏴󠁭󠁡󠀱󠀴󠁿 Flag for Guelmim-Es Semara (MA-14)
🏴󠁭󠁣󠁭󠁧󠁿 Flag for Moneghetti (MC-MG)
🏴󠁭󠁡󠀰󠀲󠁿 Flag for Gharb-Chrarda-Béni Hssen (MA-02)
🏴󠁬󠁹󠁷󠁡󠁿 Flag for Al Wahat (LY-WA)
🏴󠁬󠁹󠁺󠁡󠁿 Flag for Zawiya (LY-ZA)
🏴󠁭󠁡󠀰󠀵󠁿 Flag for Fès-Boulemane (MA-05)
🏴󠁭󠁣󠁪󠁥󠁿 Flag for Jardin Exotique de Monaco (MC-JE)
🏴󠁭󠁣󠁧󠁡󠁿 Flag for La Gare (MC-GA)
🏴󠁭󠁤󠁣󠁴󠁿 Flag for Cantemir (MD-CT)
🏴󠁭󠁤󠁦󠁡󠁿 Flag for Fălești (MD-FA)
🏴󠁭󠁤󠁮󠁩󠁿 Flag for Nisporeni (MD-NI)
🏴󠁭󠁤󠁣󠁵󠁿 Flag for Chișinău (MD-CU)
🏴󠁭󠁤󠁳󠁯󠁿 Flag for Soroca (MD-SO)
🏴󠁭󠁣󠁳󠁰󠁿 Flag for Spélugues (MC-SP)
🏴󠁭󠁤󠁢󠁳󠁿 Flag for Basarabeasca (MD-BS)
🏴󠁭󠁤󠁩󠁡󠁿 Flag for Ialoveni (MD-IA)
🏴󠁭󠁤󠁢󠁲󠁿 Flag for Briceni (MD-BR)
🏴󠁭󠁤󠁨󠁩󠁿 Flag for Hîncești (MD-HI)
🏴󠁭󠁤󠁢󠁡󠁿 Flag for Bălţi (MD-BA)
🏴󠁴󠁲󠀵󠀰󠁿 Flag for Nevşehir (TR-50)
🏴󠁭󠁤󠁦󠁬󠁿 Flag for Florești (MD-FL)
🏴󠁬󠁡󠁢󠁬󠁿 Flag for Bolikhamsai (LA-BL)
🏴󠁭󠁤󠁯󠁣󠁿 Flag for Ocniţa (MD-OC)
🏴󠁭󠁤󠁬󠁥󠁿 Flag for Leova (MD-LE)
🏴󠁭󠁤󠁧󠁬󠁿 Flag for Glodeni (MD-GL)
🏴󠁭󠁤󠁣󠁡󠁿 Flag for Cahul (MD-CA)
🏴󠁭󠁤󠁤󠁲󠁿 Flag for Drochia (MD-DR)
🏴󠁭󠁤󠁣󠁲󠁿 Flag for Criuleni (MD-CR)
🏴󠁭󠁤󠁣󠁬󠁿 Flag for Călărași (MD-CL)
🏴󠁭󠁤󠁢󠁤󠁿 Flag for Bender (MD-BD)
🏴󠁭󠁤󠁣󠁭󠁿 Flag for Cimișlia (MD-CM)
🏴󠁭󠁤󠁳󠁤󠁿 Flag for Șoldănești (MD-SD)
🏴󠁭󠁤󠁳󠁩󠁿 Flag for Sîngerei (MD-SI)
🏴󠁭󠁤󠁤󠁯󠁿 Flag for Dondușeni (MD-DO)
🏴󠁭󠁤󠁤󠁵󠁿 Flag for Dubăsari (MD-DU)
🏴󠁭󠁤󠁥󠁤󠁿 Flag for Edineț (MD-ED)
🏴󠁥󠁳󠁭󠁬󠁿 Flag for Melilla (ES-ML)
🏴󠁭󠁤󠁯󠁲󠁿 Flag for Orhei (MD-OR)
🏴󠁭󠁤󠁲󠁩󠁿 Flag for Rîșcani (MD-RI)
👨🏼‍👧🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁭󠁧󠁡󠁿 Flag for Toamasina (MG-A)
🏴󠁭󠁥󠀰󠀴󠁿 Flag for Bijelo Polje (ME-04)
🏴󠁭󠁥󠀱󠀱󠁿 Flag for Mojkovac (ME-11)
🏴󠁭󠁧󠁭󠁿 Flag for Mahajanga (MG-M)
🏴󠁭󠁥󠀰󠀵󠁿 Flag for Budva (ME-05)
🏴󠁭󠁧󠁴󠁿 Flag for Antananarivo (MG-T)
🏴󠁭󠁫󠀰󠀵󠁿 Flag for Bogdanci (MK-05)
🏴󠁭󠁫󠀰󠀷󠁿 Flag for Bosilovo (MK-07)
👨🏾‍👩🏾‍👶🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁭󠁫󠀰󠀶󠁿 Flag for Bogovinje (MK-06)
🏴󠁭󠁥󠀱󠀴󠁿 Flag for Pljevlja (ME-14)
🏴󠁭󠁥󠀲󠀱󠁿 Flag for Žabljak (ME-21)
🏴󠁭󠁫󠀰󠀳󠁿 Flag for Berovo (MK-03)
👨🏾‍👧🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁩󠁲󠀰󠀴󠁿 Flag for Isfahan (IR-04)
🏴󠁭󠁥󠀱󠀶󠁿 Flag for Podgorica (ME-16)
🏴󠁭󠁥󠀱󠀰󠁿 Flag for Kotor (ME-10)
🏴󠁭󠁥󠀲󠀰󠁿 Flag for Ulcinj (ME-20)
🏴󠁭󠁥󠀰󠀱󠁿 Flag for Andrijevica (ME-01)
🏴󠁭󠁤󠁳󠁶󠁿 Flag for Ştefan Vodă (MD-SV)
🏴󠁭󠁧󠁵󠁿 Flag for Toliara (MG-U)
👨🏼‍👦🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁭󠁥󠀱󠀳󠁿 Flag for Plav (ME-13)
🏴󠁭󠁧󠁤󠁿 Flag for Antsiranana (MG-D)
🏴󠁭󠁧󠁦󠁿 Flag for Fianarantsoa (MG-F)
🏴󠁭󠁥󠀲󠀳󠁿 Flag for Petnjica (ME-23)
🏴󠁭󠁥󠀱󠀲󠁿 Flag for Nikšić (ME-12)
🏴󠁣󠁬󠁬󠁬󠁿 Flag for Los Lagos (CL-LL)
🏴󠁭󠁥󠀱󠀵󠁿 Flag for Plužine (ME-15)
🏴󠁭󠁥󠀱󠀹󠁿 Flag for Tivat (ME-19)
🏴󠁭󠁥󠀱󠀸󠁿 Flag for Šavnik (ME-18)
🏴󠁭󠁥󠀰󠀹󠁿 Flag for Kolašin (ME-09)
🏴󠁭󠁫󠀴󠀳󠁿 Flag for Kratovo (MK-43)
🏴󠁭󠁫󠀴󠀲󠁿 Flag for Kočani (MK-42)
🏴󠁭󠁫󠀳󠀵󠁿 Flag for Jegunovce (MK-35)
🏴󠁭󠁫󠀱󠀸󠁿 Flag for Gevgelija (MK-18)
🏴󠁭󠁫󠀰󠀸󠁿 Flag for Brvenica (MK-08)
🏴󠁭󠁫󠀳󠀳󠁿 Flag for Zrnovci (MK-33)
🏴󠁭󠁫󠀴󠀹󠁿 Flag for Lozovo (MK-49)
🏴󠁭󠁫󠀱󠀴󠁿 Flag for Vinica (MK-14)
🏴󠁭󠁫󠀱󠀱󠁿 Flag for Vasilevo (MK-11)
🏴󠁭󠁫󠀱󠀰󠁿 Flag for Valandovo (MK-10)
🏴󠁭󠁫󠀳󠀰󠁿 Flag for Želino (MK-30)
🏴󠁭󠁫󠀳󠀶󠁿 Flag for Kavadarci (MK-36)
🏴󠁭󠁫󠀳󠀲󠁿 Flag for Zelenikovo (MK-32)
🏴󠁭󠁫󠀵󠀰󠁿 Flag for Mavrovo and Rostuša (MK-50)
🏴󠁭󠁫󠀱󠀶󠁿 Flag for Vrapčište (MK-16)
🏴󠁭󠁫󠀵󠀵󠁿 Flag for Novaci (MK-55)
🏴󠁢󠁲󠁭󠁡󠁿 Flag for Maranhão (BR-MA)
🏴󠁭󠁫󠀱󠀳󠁿 Flag for Veles (MK-13)
🏴󠁭󠁫󠀱󠀹󠁿 Flag for Gostivar (MK-19)
🏴󠁭󠁫󠀲󠀰󠁿 Flag for Gradsko (MK-20)
🏴󠁭󠁫󠀵󠀴󠁿 Flag for Negotino (MK-54)
🏴󠁭󠁫󠀲󠀲󠁿 Flag for Debarca (MK-22)
🏴󠁭󠁫󠀴󠀱󠁿 Flag for Konče (MK-41)
🏴󠁭󠁫󠀳󠀴󠁿 Flag for Ilinden (MK-34)
🏴󠁬󠁢󠁡󠁫󠁿 Flag for Akkar (LB-AK)
🏴󠁭󠁫󠀴󠀸󠁿 Flag for Lipkovo (MK-48)
🏴󠁭󠁫󠀲󠀱󠁿 Flag for Debar (MK-21)
🏴󠁩󠁬󠁴󠁡󠁿 Flag for Tel Aviv District (IL-TA)
🏴󠁭󠁫󠀲󠀶󠁿 Flag for Dojran (MK-26)
🏴󠁭󠁫󠀳󠀷󠁿 Flag for Karbinci (MK-37)
🏴󠁭󠁫󠀵󠀱󠁿 Flag for Makedonska Kamenica (MK-51)
🏴󠁭󠁥󠀰󠀷󠁿 Flag for Danilovgrad (ME-07)
🏴󠁭󠁫󠀴󠀷󠁿 Flag for Kumanovo (MK-47)
🏴󠁭󠁫󠀵󠀶󠁿 Flag for Novo Selo (MK-56)
🏴󠁭󠁫󠀴󠀵󠁿 Flag for Krivogaštani (MK-45)
🏴󠁭󠁫󠀲󠀳󠁿 Flag for Delčevo (MK-23)
🏴󠁭󠁫󠀴󠀴󠁿 Flag for Kriva Palanka (MK-44)
🏴󠁭󠁫󠀱󠀲󠁿 Flag for Vevčani (MK-12)
🏴󠁭󠁫󠀴󠀶󠁿 Flag for Kruševo (MK-46)
🏴󠁭󠁫󠀶󠀶󠁿 Flag for Resen (MK-66)
🏴󠁭󠁭󠀰󠀷󠁿 Flag for Ayeyarwady (MM-07)
🏴󠁭󠁬󠀴󠁿 Flag for Ségou (ML-4)
🏴󠁭󠁭󠀱󠀱󠁿 Flag for Kachin (MM-11)
👩🏼‍❤️‍👨🏽 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Medium Skin Tone
🏴󠁭󠁫󠀵󠀹󠁿 Flag for Petrovec (MK-59)
🏴󠁭󠁫󠀵󠀸󠁿 Flag for Ohrid (MK-58)
🏴󠁭󠁫󠀷󠀲󠁿 Flag for Struga (MK-72)
👩‍👦‍👧 Family: Woman, Boy, Girl
🏴󠁭󠁭󠀰󠀶󠁿 Flag for Yangon (MM-06)
🏴󠁭󠁫󠀶󠀳󠁿 Flag for Probištip (MK-63)
👨‍❤️‍💋‍👨🏾 Kiss - Man, Man: Medium-Dark Skin Tone
🏴󠁭󠁫󠀷󠀴󠁿 Flag for Studeničani (MK-74)
🏴󠁭󠁭󠀰󠀵󠁿 Flag for Tanintharyi (MM-05)
🏴󠁭󠁬󠀳󠁿 Flag for Sikasso (ML-3)
🏴󠁭󠁫󠀸󠀰󠁿 Flag for Čaška (MK-80)
🏴󠁡󠁲󠁦󠁿 Flag for La Rioja (AR-F)
🏴󠁳󠁥󠁭󠁿 Flag for Skåne (SE-M)
🏴󠁭󠁬󠀵󠁿 Flag for Mopti (ML-5)
🏴󠁭󠁫󠀷󠀶󠁿 Flag for Tetovo (MK-76)
🏴󠁭󠁫󠀷󠀱󠁿 Flag for Staro Nagoričane (MK-71)
🏴󠁭󠁫󠀷󠀰󠁿 Flag for Sopište (MK-70)
🏴󠁭󠁫󠀸󠀳󠁿 Flag for Štip (MK-83)
🏴󠁭󠁬󠀷󠁿 Flag for Gao (ML-7)
🏴󠁭󠁫󠀸󠀱󠁿 Flag for Češinovo-Obleševo (MK-81)
🏴󠁭󠁭󠀱󠀲󠁿 Flag for Kayah (MM-12)
🏴󠁭󠁬󠀲󠁿 Flag for Koulikoro (ML-2)
🏴󠁭󠁭󠀰󠀱󠁿 Flag for Sagaing (MM-01)
🏴󠁭󠁫󠀶󠀰󠁿 Flag for Pehčevo (MK-60)
🏴󠁭󠁫󠀸󠀲󠁿 Flag for Čučer-Sandevo (MK-82)
🏴󠁭󠁭󠀰󠀲󠁿 Flag for Bago (MM-02)
🏴󠁭󠁭󠀰󠀴󠁿 Flag for Mandalay (MM-04)
🏴󠁭󠁫󠀶󠀹󠁿 Flag for Sveti Nikole (MK-69)
🏴󠁭󠁫󠀶󠀷󠁿 Flag for Rosoman (MK-67)
🏴󠁭󠁮󠀰󠀷󠀳󠁿 Flag for Arkhangai (MN-073)
🏴󠁭󠁲󠀰󠀳󠁿 Flag for Assaba (MR-03)
🏴󠁭󠁮󠀰󠀶󠀵󠁿 Flag for Govi-Altai (MN-065)
🏴󠁭󠁮󠀰󠀵󠀷󠁿 Flag for Zavkhan (MN-057)
󠁾 Tag Tilde
🏴󠁭󠁭󠀱󠀸󠁿 Flag for Naypyidaw (MM-18)
🏴󠁭󠁮󠀰󠀴󠀱󠁿 Flag for Khövsgöl (MN-041)
🏴󠁭󠁲󠀰󠀶󠁿 Flag for Trarza (MR-06)
🏴󠁭󠁮󠀰󠀵󠀱󠁿 Flag for Sükhbaatar (MN-051)
🏴󠁭󠁲󠀰󠀹󠁿 Flag for Tagant (MR-09)
🖃 Stamped Envelope
🏴󠁭󠁮󠀱󠁿 Flag for Ulaanbaatar (MN-1)
🏴󠁭󠁮󠀰󠀳󠀷󠁿 Flag for Darkhan-Uul (MN-037)
🏴󠁭󠁮󠀰󠀷󠀱󠁿 Flag for Bayan-Ölgii (MN-071)
🏴󠁭󠁮󠀰󠀴󠀶󠁿 Flag for Uvs (MN-046)
🏴󠁭󠁲󠀰󠀵󠁿 Flag for Brakna (MR-05)
🏴󠁭󠁲󠀰󠀲󠁿 Flag for Hodh El Gharbi (MR-02)
🏴󠁭󠁮󠀰󠀴󠀷󠁿 Flag for Töv (MN-047)
🏴󠁪󠁰󠀲󠀳󠁿 Flag for Aichi (JP-23)
🏴󠁭󠁮󠀰󠀵󠀳󠁿 Flag for Ömnögovi (MN-053)
🏴󠁭󠁲󠀰󠀴󠁿 Flag for Gorgol (MR-04)
🀫 Mahjong Tile Back
🏴󠁭󠁮󠀰󠀶󠀷󠁿 Flag for Bulgan (MN-067)
🏴󠁭󠁮󠀰󠀳󠀵󠁿 Flag for Orkhon (MN-035)
🏴󠁭󠁲󠀰󠀸󠁿 Flag for Dakhlet Nouadhibou (MR-08)
🏴󠁭󠁮󠀰󠀵󠀹󠁿 Flag for Dundgovi (MN-059)
🏴󠁭󠁮󠀰󠀶󠀳󠁿 Flag for Dornogovi (MN-063)
🏴󠁭󠁲󠀱󠀲󠁿 Flag for Inchiri (MR-12)
🏴󠁭󠁭󠀱󠀶󠁿 Flag for Rakhine (MM-16)
🏴󠁭󠁮󠀰󠀶󠀱󠁿 Flag for Dornod (MN-061)
🏴󠁭󠁮󠀰󠀴󠀳󠁿 Flag for Khovd (MN-043)
🏴󠁭󠁲󠀰󠀱󠁿 Flag for Hodh Ech Chargui (MR-01)
🏴󠁭󠁮󠀰󠀶󠀹󠁿 Flag for Bayankhongor (MN-069)
🏴󠁭󠁭󠀱󠀴󠁿 Flag for Chin (MM-14)
🏴󠁭󠁭󠀱󠀳󠁿 Flag for Kayin (MM-13)
🏴󠁭󠁮󠀰󠀵󠀵󠁿 Flag for Övörkhangai (MN-055)
👩🏽‍❤️‍💋‍👩🏻 Kiss - Woman: Medium Skin Tone, Woman: Light Skin Tone
󠀤 Tag Dollar Sign
🏴󠁭󠁲󠀱󠀱󠁿 Flag for Tiris Zemmour (MR-11)
🏴󠁭󠁴󠀱󠀱󠁿 Flag for Gudja (MT-11)
🏴󠁭󠁴󠀱󠀴󠁿 Flag for Għarb (MT-14)
🏴󠁭󠁴󠀱󠀶󠁿 Flag for Għasri (MT-16)
🏴󠁭󠁴󠀲󠀴󠁿 Flag for Lija (MT-24)
🏴󠁭󠁴󠀳󠀶󠁿 Flag for Munxar (MT-36)
🏴󠁭󠁴󠀱󠀸󠁿 Flag for Ħamrun (MT-18)
🏴󠁭󠁴󠀳󠀲󠁿 Flag for Mosta (MT-32)
🏴󠁭󠁴󠀱󠀰󠁿 Flag for Fontana (MT-10)
🏴󠁭󠁴󠀰󠀷󠁿 Flag for Dingli (MT-07)
👨🏾‍❤️‍💋‍👨🏽 Kiss - Man: Medium-Dark Skin Tone, Man: Medium Skin Tone
🏴󠁭󠁲󠀱󠀴󠁿 Flag for Nouakchott Nord (MR-14)
🏴󠁭󠁴󠀰󠀲󠁿 Flag for Balzan (MT-02)
🏴󠁭󠁴󠀲󠀱󠁿 Flag for Kalkara (MT-21)
🏴󠁭󠁴󠀰󠀵󠁿 Flag for Birżebbuġa (MT-05)
🏴󠁭󠁴󠀱󠀲󠁿 Flag for Gżira (MT-12)
🏴󠁭󠁴󠀲󠀳󠁿 Flag for Kirkop (MT-23)
🏴󠁭󠁴󠀳󠀹󠁿 Flag for Paola (MT-39)
🏴󠁭󠁴󠀲󠀷󠁿 Flag for Marsaskala (MT-27)
🏴󠁭󠁴󠀲󠀸󠁿 Flag for Marsaxlokk (MT-28)
🏴󠁭󠁴󠀳󠀴󠁿 Flag for Msida (MT-34)
🏴󠁭󠁴󠀳󠀷󠁿 Flag for Nadur (MT-37)
🏴󠁭󠁴󠀱󠀹󠁿 Flag for Iklin (MT-19)
🏴󠁫󠁺󠁡󠁫󠁭󠁿 Flag for Akmola (KZ-AKM)
🏴󠁭󠁴󠀱󠀳󠁿 Flag for Għajnsielem (MT-13)
🏴󠁭󠁴󠀰󠀸󠁿 Flag for Fgura (MT-08)
🏴󠁭󠁴󠀰󠀳󠁿 Flag for Birgu (MT-03)
🏴󠁭󠁴󠀳󠀸󠁿 Flag for Naxxar (MT-38)
🏴󠁭󠁴󠀳󠀰󠁿 Flag for Mellieħa (MT-30)
🏴󠁭󠁴󠀱󠀷󠁿 Flag for Għaxaq (MT-17)
🏴󠁭󠁴󠀰󠀹󠁿 Flag for Floriana (MT-09)
🏴󠁭󠁴󠀰󠀴󠁿 Flag for Birkirkara (MT-04)
🏴󠁭󠁴󠀳󠀵󠁿 Flag for Imtarfa (MT-35)
🏴󠁭󠁴󠀱󠀵󠁿 Flag for Għargħur (MT-15)
🏴󠁭󠁴󠀲󠀶󠁿 Flag for Marsa (MT-26)
🏴󠁭󠁴󠀰󠀶󠁿 Flag for Cospicua (MT-06)
🏴󠁭󠁲󠀱󠀵󠁿 Flag for Nouakchott Sud (MR-15)
🏴󠁭󠁭󠀱󠀵󠁿 Flag for Mon (MM-15)
🏴󠁭󠁴󠀰󠀱󠁿 Flag for Attard (MT-01)
🏴󠁭󠁴󠀲󠀲󠁿 Flag for Kerċem (MT-22)
🏴󠁭󠁴󠀳󠀳󠁿 Flag for Mqabba (MT-33)
🏴󠁭󠁴󠀵󠀳󠁿 Flag for Santa Luċija (MT-53)
🏴󠁥󠁴󠁴󠁩󠁿 Flag for Tigray (ET-TI)
🏴󠁭󠁴󠀴󠀰󠁿 Flag for Pembroke (MT-40)
🏴󠁴󠁲󠀰󠀳󠁿 Flag for Afyonkarahisar (TR-03)
🏴󠁭󠁴󠀴󠀴󠁿 Flag for Qrendi (MT-44)
🏴󠁭󠁵󠁰󠁬󠁿 Flag for Port Louis District (MU-PL)
🏴󠁭󠁴󠀶󠀱󠁿 Flag for Xagħra (MT-61)
🏴󠁭󠁴󠀶󠀴󠁿 Flag for Żabbar (MT-64)
👩🏿‍👶🏿‍👶🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁭󠁵󠁣󠁵󠁿 Flag for Curepipe (MU-CU)
🏴󠁭󠁵󠁰󠁡󠁿 Flag for Pamplemousses (MU-PA)
🏴󠁭󠁵󠁰󠁵󠁿 Flag for Port Louis (MU-PU)
🏴󠁭󠁴󠀵󠀸󠁿 Flag for Ta’ Xbiex (MT-58)
🏴󠁭󠁴󠀴󠀲󠁿 Flag for Qala (MT-42)
🏴󠁭󠁴󠀶󠀸󠁿 Flag for Żurrieq (MT-68)
🏴󠁭󠁴󠀴󠀹󠁿 Flag for San Ġwann (MT-49)
🏴󠁭󠁵󠁦󠁬󠁿 Flag for Flacq (MU-FL)
🏴󠁩󠁬󠁪󠁭󠁿 Flag for Jerusalem (IL-JM)
🏴󠁬󠁵󠁲󠁤󠁿 Flag for Redange (LU-RD)
🏴󠁭󠁴󠀵󠀰󠁿 Flag for Saint Lawrence (MT-50)
🏴󠁭󠁴󠀶󠀰󠁿 Flag for Valletta (MT-60)
🏴󠁭󠁴󠀴󠀷󠁿 Flag for Safi (MT-47)
🏴󠁭󠁴󠀵󠀴󠁿 Flag for Santa Venera (MT-54)
🏴󠁭󠁴󠀵󠀹󠁿 Flag for Tarxien (MT-59)
🏴󠁭󠁴󠀶󠀷󠁿 Flag for Żejtun (MT-67)
🏴󠁭󠁴󠀴󠀳󠁿 Flag for Qormi (MT-43)
🏴󠁭󠁴󠀵󠀷󠁿 Flag for Swieqi (MT-57)
🏴󠁭󠁴󠀶󠀶󠁿 Flag for Żebbuġ (MT-66)
🏴󠁭󠁵󠁢󠁬󠁿 Flag for Rivière Noire (MU-BL)
🏴󠁭󠁴󠀶󠀳󠁿 Flag for Xgħajra (MT-63)
🏴󠁭󠁴󠀵󠀵󠁿 Flag for Siġġiewi (MT-55)
🏴󠁭󠁴󠀵󠀶󠁿 Flag for Sliema (MT-56)
🏴󠁩󠁥󠁭󠁿 Flag for Munster (IE-M)
🏴󠁭󠁵󠁱󠁢󠁿 Flag for Quatre Bornes (MU-QB)
🏴󠁭󠁵󠁰󠁷󠁿 Flag for Plaines Wilhems (MU-PW)
🏴󠁭󠁸󠁧󠁵󠁡󠁿 Flag for Guanajuato (MX-GUA)
🔿 Upper Right Shadowed White Circle
👨🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁭󠁶󠁣󠁥󠁿 Flag for Central Province (MV-CE)
🏴󠁡󠁯󠁵󠁩󠁧󠁿 Flag for Uíge (AO-UIG)
🏴󠁭󠁷󠁳󠁿 Flag for Southern (MW-S)
🏴󠁭󠁷󠁣󠁿 Flag for Central (MW-C)
🏴󠁭󠁤󠁡󠁮󠁿 Flag for Anenii Noi (MD-AN)
👩🏼‍👨🏼‍👧🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁭󠁵󠁶󠁰󠁿 Flag for Vacoas-Phoenix (MU-VP)
󠀭 Tag Hyphen-Minus
🏴󠁭󠁸󠁣󠁡󠁭󠁿 Flag for Campeche (MX-CAM)
🏴󠁭󠁸󠁣󠁯󠁡󠁿 Flag for Coahuila (MX-COA)
🏴󠁪󠁰󠀲󠀶󠁿 Flag for Kyōto (JP-26)
🏴󠁡󠁯󠁣󠁣󠁵󠁿 Flag for Cuando Cubango (AO-CCU)
🏴󠁫󠁺󠁡󠁬󠁡󠁿 Flag for Almaty (KZ-ALA)
🏴󠁩󠁴󠀳󠀶󠁿 Flag for Friuli–Venezia Giulia (IT-36)
🏴󠁭󠁸󠁯󠁡󠁸󠁿 Flag for Oaxaca (MX-OAX)
🏴󠁭󠁸󠁨󠁩󠁤󠁿 Flag for Hidalgo (MX-HID)
⚧ Male with Stroke and Male and Female Sign
🏴󠁭󠁶󠁭󠁬󠁥󠁿 Flag for Malé (MV-MLE)
🏴󠁪󠁭󠀱󠀲󠁿 Flag for Manchester (JM-12)
🏴󠁩󠁲󠀱󠀸󠁿 Flag for Kohgiluyeh and Boyer-Ahmad (IR-18)
🏴󠁭󠁶󠁳󠁵󠁿 Flag for South Province (MV-SU)
🧟🏾‍♀️ Woman Zombie: Medium-Dark Skin Tone
🏴󠁭󠁵󠁳󠁡󠁿 Flag for Savanne (MU-SA)
🏴󠁭󠁸󠁺󠁡󠁣󠁿 Flag for Zacatecas (MX-ZAC)
🏴󠁮󠁡󠁥󠁲󠁿 Flag for Erongo (NA-ER)
🏴󠁭󠁸󠁶󠁥󠁲󠁿 Flag for Veracruz (MX-VER)
🏴󠁢󠁲󠁳󠁣󠁿 Flag for Santa Catarina (BR-SC)
🏴󠁭󠁺󠁴󠁿 Flag for Tete (MZ-T)
🏴󠁭󠁸󠁴󠁬󠁡󠁿 Flag for Tlaxcala (MX-TLA)
🏴󠁭󠁹󠀱󠀵󠁿 Flag for Labuan (MY-15)
🏴󠁭󠁺󠁭󠁰󠁭󠁿 Flag for Maputo (MZ-MPM)
🏴󠁭󠁹󠀰󠀹󠁿 Flag for Perlis (MY-09)
🏴󠁭󠁺󠁡󠁿 Flag for Niassa (MZ-A)
🏴󠁭󠁶󠁵󠁮󠁿 Flag for Upper North Province (MV-UN)
🏴󠁭󠁸󠁭󠁩󠁣󠁿 Flag for Michoacán (MX-MIC)
🏴󠁭󠁣󠁭󠁣󠁿 Flag for Monte Carlo (MC-MC)
🏴󠁭󠁸󠁮󠁬󠁥󠁿 Flag for Nuevo León (MX-NLE)
🏴󠁡󠁲󠁤󠁿 Flag for San Luis (AR-D)
👩🏻‍❤️‍👩🏾 Couple With Heart - Woman: Light Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁭󠁺󠁰󠁿 Flag for Cabo Delgado (MZ-P)
🀉 Mahjong Tile Three of Characters
🏴󠁭󠁺󠁩󠁿 Flag for Inhambane (MZ-I)
👩🏻‍👦🏻‍👶🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
🏴󠁭󠁺󠁳󠁿 Flag for Sofala (MZ-S)
🏴󠁭󠁸󠁳󠁩󠁮󠁿 Flag for Sinaloa (MX-SIN)
🏴󠁫󠁮󠁫󠁿 Flag for Saint Kitts (KN-K)
🏴󠁩󠁴󠀷󠀵󠁿 Flag for Apulia (IT-75)
🏴󠁭󠁺󠁮󠁿 Flag for Nampula (MZ-N)
🏴󠁭󠁣󠁳󠁯󠁿 Flag for La Source (MC-SO)
🏴󠁭󠁺󠁧󠁿 Flag for Gaza (MZ-G)
🏴󠁮󠁡󠁨󠁡󠁿 Flag for Hardap (NA-HA)
🏴󠁭󠁸󠁱󠁵󠁥󠁿 Flag for Querétaro (MX-QUE)
🏴󠁭󠁹󠀱󠀶󠁿 Flag for Putrajaya (MY-16)
🏴󠁮󠁡󠁣󠁡󠁿 Flag for Zambezi (NA-CA)
🏴󠁧󠁡󠀷󠁿 Flag for Ogooué-Lolo (GA-7)
🏴󠁭󠁺󠁢󠁿 Flag for Manica (MZ-B)
󠁠 Tag Grave Accent
🏴󠁭󠁹󠀰󠀵󠁿 Flag for Negeri Sembilan (MY-05)
🏴󠁭󠁹󠀰󠀴󠁿 Flag for Malacca (MY-04)
🏴󠁮󠁥󠀱󠁿 Flag for Agadez (NE-1)
🏴󠁮󠁡󠁯󠁤󠁿 Flag for Otjozondjupa (NA-OD)
🏴󠁮󠁥󠀵󠁿 Flag for Tahoua (NE-5)
🏴󠁮󠁧󠁫󠁯󠁿 Flag for Kogi (NG-KO)
⚭ Marriage Symbol
🏴󠁮󠁧󠁫󠁴󠁿 Flag for Katsina (NG-KT)
🏴󠁶󠁮󠀲󠀵󠁿 Flag for Quảng Trị (VN-25)
🏴󠁮󠁥󠀶󠁿 Flag for Tillabéri (NE-6)
🏴󠁮󠁡󠁫󠁨󠁿 Flag for Khomas (NA-KH)
🏴󠁮󠁡󠁯󠁳󠁿 Flag for Omusati (NA-OS)
🏴󠁭󠁵󠁲󠁲󠁿 Flag for Rivière du Rempart (MU-RR)
🏴󠁤󠁺󠀲󠀲󠁿 Flag for Sidi Bel Abbès (DZ-22)
🏴󠁮󠁡󠁫󠁵󠁿 Flag for Kunene (NA-KU)
🏴󠁮󠁧󠁪󠁩󠁿 Flag for Jigawa (NG-JI)
🏴󠁮󠁥󠀴󠁿 Flag for Maradi (NE-4)
🏴󠁮󠁥󠀳󠁿 Flag for Dosso (NE-3)
🏴󠁮󠁧󠁢󠁥󠁿 Flag for Benue (NG-BE)
🏴󠁮󠁥󠀷󠁿 Flag for Zinder (NE-7)
🏴󠁮󠁡󠁯󠁷󠁿 Flag for Ohangwena (NA-OW)
🏴󠁮󠁧󠁡󠁢󠁿 Flag for Abia (NG-AB)
🏴󠁮󠁡󠁫󠁡󠁿 Flag for Karas (NA-KA)
🏴󠁮󠁧󠁥󠁫󠁿 Flag for Ekiti (NG-EK)
🏴󠁮󠁡󠁯󠁮󠁿 Flag for Oshana (NA-ON)
🏴󠁮󠁧󠁥󠁢󠁿 Flag for Ebonyi (NG-EB)
🏴󠁮󠁧󠁫󠁤󠁿 Flag for Kaduna (NG-KD)
󠁕 Tag Latin Capital Letter U
🏴󠁮󠁥󠀸󠁿 Flag for Niamey (NE-8)
🏴󠁭󠁸󠁴󠁡󠁭󠁿 Flag for Tamaulipas (MX-TAM)
🏴󠁮󠁡󠁫󠁷󠁿 Flag for Kavango West (NA-KW)
🏴󠁮󠁧󠁢󠁹󠁿 Flag for Bayelsa (NG-BY)
🏴󠁮󠁥󠀲󠁿 Flag for Diffa (NE-2)
🏴󠁮󠁧󠁡󠁫󠁿 Flag for Akwa Ibom (NG-AK)
🏴󠁮󠁧󠁫󠁮󠁿 Flag for Kano (NG-KN)
🏴󠁮󠁡󠁯󠁴󠁿 Flag for Oshikoto (NA-OT)
󠁀 Tag Commercial at
🏴󠁮󠁧󠁡󠁮󠁿 Flag for Anambra (NG-AN)
🏴󠁵󠁡󠀱󠀸󠁿 Flag for Zhytomyrshchyna (UA-18)
🏴󠁮󠁩󠁣󠁩󠁿 Flag for Chinandega (NI-CI)
🏴󠁮󠁧󠁴󠁡󠁿 Flag for Taraba (NG-TA)
🏴󠁮󠁬󠁢󠁱󠀳󠁿 Flag for Sint Eustatius (NL-BQ3)
👨‍👶‍👦 Family: Man, Baby, Boy
🏴󠁮󠁧󠁺󠁡󠁿 Flag for Zamfara (NG-ZA)
🏴󠁮󠁧󠁰󠁬󠁿 Flag for Plateau (NG-PL)
🏴󠁮󠁧󠁫󠁷󠁿 Flag for Kwara (NG-KW)
🏴󠁮󠁩󠁮󠁳󠁿 Flag for Nueva Segovia (NI-NS)
🏴󠁪󠁭󠀰󠀸󠁿 Flag for Saint James (JM-08)
🏴󠁮󠁬󠁦󠁬󠁿 Flag for Flevoland (NL-FL)
🏴󠁮󠁩󠁡󠁳󠁿 Flag for Atlántico Sur (NI-AS)
🏴󠁮󠁩󠁭󠁤󠁿 Flag for Madriz (NI-MD)
🏴󠁵󠁳󠁭󠁡󠁿 Flag for Massachusetts (US-MA)
🏴󠁮󠁩󠁪󠁩󠁿 Flag for Jinotega (NI-JI)
🏴󠁧󠁴󠁰󠁲󠁿 Flag for El Progreso (GT-PR)
🏴󠁮󠁩󠁭󠁮󠁿 Flag for Managua (NI-MN)
🏴󠁮󠁩󠁡󠁮󠁿 Flag for Atlántico Norte (NI-AN)
🏴󠁮󠁬󠁧󠁥󠁿 Flag for Gelderland (NL-GE)
🏴󠁮󠁩󠁢󠁯󠁿 Flag for Boaco (NI-BO)
🏴󠁮󠁧󠁯󠁳󠁿 Flag for Osun (NG-OS)
🏴󠁮󠁧󠁩󠁭󠁿 Flag for Imo (NG-IM)
🏴󠁮󠁩󠁲󠁩󠁿 Flag for Rivas (NI-RI)
🏴󠁮󠁩󠁣󠁯󠁿 Flag for Chontales (NI-CO)
🏴󠁦󠁲󠁭󠁡󠁹󠁿 Flag for Mayotte (FR-MAY)
🏴󠁮󠁧󠁯󠁹󠁿 Flag for Oyo (NG-OY)
🏴󠁩󠁬󠁺󠁿 Flag for Northern District (IL-Z)
🏴󠁮󠁩󠁥󠁳󠁿 Flag for Estelí (NI-ES)
🏴󠁮󠁩󠁧󠁲󠁿 Flag for Granada (NI-GR)
🏴󠁮󠁩󠁭󠁴󠁿 Flag for Matagalpa (NI-MT)
🏴󠁮󠁩󠁣󠁡󠁿 Flag for Carazo (NI-CA)
🏴󠁮󠁧󠁮󠁡󠁿 Flag for Nasarawa (NG-NA)
🏴󠁮󠁲󠀰󠀳󠁿 Flag for Anetan (NR-03)
🏴󠁧󠁮󠁮󠁿 Flag for Nzérékoré Region (GN-N)
🏴󠁮󠁲󠀰󠀴󠁿 Flag for Anibare (NR-04)
🏴󠁮󠁯󠀲󠀲󠁿 Flag for Jan Mayen (NO-22)
🏴󠁮󠁯󠀰󠀹󠁿 Flag for Aust-Agder (NO-09)
🏴󠁮󠁯󠀰󠀲󠁿 Flag for Akershus (NO-02)
🏴󠁮󠁯󠀱󠀷󠁿 Flag for Nord-Trøndelag (NO-17)
🏴󠁮󠁯󠀰󠀸󠁿 Flag for Telemark (NO-08)
🏴󠁬󠁩󠀰󠀱󠁿 Flag for Balzers (LI-01)
🏴󠁮󠁰󠀳󠁿 Flag for Western (NP-3)
🏴󠁮󠁰󠀱󠁿 Flag for Central (NP-1)
🏴󠁮󠁰󠀴󠁿 Flag for Purwanchal (NP-4)
🏴󠁮󠁯󠀱󠀵󠁿 Flag for Møre og Romsdal (NO-15)
🏴󠁭󠁣󠁬󠁡󠁿 Flag for Larvotto (MC-LA)
🏴󠁮󠁯󠀰󠀵󠁿 Flag for Oppland (NO-05)
󠁶 Tag Latin Small Letter V
🏴󠁮󠁲󠀰󠀱󠁿 Flag for Aiwo (NR-01)
🏴󠁮󠁬󠁺󠁥󠁿 Flag for Zeeland (NL-ZE)
🏴󠁮󠁲󠀰󠀵󠁿 Flag for Baiti (NR-05)
🏴󠁮󠁯󠀰󠀶󠁿 Flag for Buskerud (NO-06)
🏴󠁮󠁯󠀰󠀴󠁿 Flag for Hedmark (NO-04)
🏴󠁮󠁯󠀰󠀷󠁿 Flag for Vestfold (NO-07)
🏴󠁮󠁯󠀱󠀸󠁿 Flag for Nordland (NO-18)
🏴󠁭󠁫󠀶󠀲󠁿 Flag for Prilep (MK-62)
🏴󠁮󠁬󠁣󠁷󠁿 Flag for Curaçao (NL-CW)
🏴󠁮󠁰󠀲󠁿 Flag for Madhya Pashchimanchal (NP-2)
🏴󠁮󠁯󠀱󠀶󠁿 Flag for Sør-Trøndelag (NO-16)
🏴󠁮󠁧󠁯󠁮󠁿 Flag for Ondo (NG-ON)
🏴󠁮󠁲󠀰󠀷󠁿 Flag for Buada (NR-07)
🏴󠁭󠁤󠁵󠁮󠁿 Flag for Ungheni (MD-UN)
🏴󠁮󠁯󠀰󠀱󠁿 Flag for Østfold (NO-01)
🏴󠁬󠁶󠀰󠀰󠀵󠁿 Flag for Aloja (LV-005)
🏴󠁮󠁲󠀰󠀶󠁿 Flag for Boe (NR-06)
👨🏼‍❤️‍👩🏾 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁮󠁯󠀰󠀳󠁿 Flag for Oslo (NO-03)
🏴󠁡󠁺󠁡󠁧󠁡󠁿 Flag for Agstafa (AZ-AGA)
🏴󠁤󠁥󠁭󠁶󠁿 Flag for Mecklenburg-Vorpommern (DE-MV)
🏴󠁮󠁯󠀱󠀹󠁿 Flag for Troms (NO-19)
👨‍❤️‍👨🏽 Couple With Heart - Man, Man: Medium Skin Tone
🏴󠁮󠁯󠀲󠀰󠁿 Flag for Finnmark (NO-20)
🏴󠁣󠁤󠁬󠁵󠁿 Flag for Lualaba (CD-LU)
🏴󠁮󠁧󠁥󠁤󠁿 Flag for Edo (NG-ED)
🏴󠁮󠁺󠁣󠁩󠁴󠁿 Flag for Chatham Islands (NZ-CIT)
🏴󠁧󠁮󠁫󠁿 Flag for Kankan Region (GN-K)
🏴󠁩󠁮󠁡󠁮󠁿 Flag for Andaman and Nicobar Islands (IN-AN)
👩🏿‍👩🏿‍👦🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
👨🏾‍❤️‍👩🏾 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁪󠁯󠁫󠁡󠁿 Flag for Karak (JO-KA)
🏴󠁯󠁭󠁺󠁵󠁿 Flag for Dhofar (OM-ZU)
🏴󠁤󠁥󠁳󠁨󠁿 Flag for Schleswig-Holstein (DE-SH)
🏴󠁯󠁭󠁳󠁪󠁿 Flag for Janub ash Sharqiyah (OM-SJ)
🏴󠁯󠁭󠁳󠁳󠁿 Flag for Shamal ash Sharqiyah (OM-SS)
🏴󠁰󠁡󠀳󠁿 Flag for Colón (PA-3)
🏴󠁮󠁲󠀱󠀰󠁿 Flag for Ijuw (NR-10)
🏴󠁮󠁺󠁷󠁫󠁯󠁿 Flag for Waikato (NZ-WKO)
👩🏿‍👧🏿‍👧🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁯󠁭󠁭󠁡󠁿 Flag for Muscat (OM-MA)
🏴󠁯󠁭󠁺󠁡󠁿 Flag for Ad Dhahirah (OM-ZA)
🏴󠁰󠁧󠁮󠁣󠁤󠁿 Flag for Port Moresby (PG-NCD)
🏴󠁯󠁭󠁢󠁳󠁿 Flag for Shamal al Batinah (OM-BS)
🏴󠁯󠁭󠁭󠁵󠁿 Flag for Musandam (OM-MU)
👩🏼‍❤️‍💋‍👨🏽 Kiss - Woman: Medium-Light Skin Tone, Man: Medium Skin Tone
🏴󠁮󠁺󠁧󠁩󠁳󠁿 Flag for Gisborne (NZ-GIS)
🕂 Cross Pommee
🏴󠁮󠁲󠀱󠀲󠁿 Flag for Nibok (NR-12)
🏴󠁯󠁭󠁢󠁪󠁿 Flag for Janub al Batinah (OM-BJ)
🏴󠁰󠁥󠁡󠁭󠁡󠁿 Flag for Amazonas (PE-AMA)
🏴󠁰󠁧󠁣󠁰󠁭󠁿 Flag for Central (PG-CPM)
🏴󠁰󠁥󠁩󠁣󠁡󠁿 Flag for Ica (PE-ICA)
🏴󠁰󠁥󠁬󠁭󠁡󠁿 Flag for Lima (PE-LMA)
🏴󠁰󠁥󠁬󠁡󠁭󠁿 Flag for Lambayeque (PE-LAM)
🏴󠁰󠁡󠀶󠁿 Flag for Herrera (PA-6)
🏴󠁢󠁩󠁧󠁩󠁿 Flag for Gitega (BI-GI)
🏴󠁰󠁥󠁣󠁡󠁬󠁿 Flag for El Callao (PE-CAL)
🏴󠁰󠁥󠁳󠁡󠁭󠁿 Flag for San Martín (PE-SAM)
🏴󠁰󠁥󠁨󠁵󠁶󠁿 Flag for Huancavelica (PE-HUV)
🏴󠁰󠁥󠁴󠁵󠁭󠁿 Flag for Tumbes (PE-TUM)
󠀮 Tag Full Stop
🏴󠁰󠁡󠀵󠁿 Flag for Darién (PA-5)
🏴󠁰󠁥󠁰󠁵󠁮󠁿 Flag for Puno (PE-PUN)
🏴󠁰󠁥󠁪󠁵󠁮󠁿 Flag for Junín (PE-JUN)
🏴󠁰󠁡󠀱󠁿 Flag for Bocas del Toro (PA-1)
🛪 Northeast-Pointing Airplane
🏴󠁰󠁥󠁰󠁡󠁳󠁿 Flag for Pasco (PE-PAS)
🏴󠁮󠁲󠀰󠀸󠁿 Flag for Denigomodu (NR-08)
🏴󠁰󠁥󠁡󠁮󠁣󠁿 Flag for Ancash (PE-ANC)
🖅 Flying Envelope
🏴󠁰󠁧󠁣󠁰󠁫󠁿 Flag for Chimbu (PG-CPK)
🏴󠁰󠁡󠀹󠁿 Flag for Veraguas (PA-9)
🏴󠁰󠁥󠁰󠁩󠁵󠁿 Flag for Piura (PE-PIU)
🏴󠁧󠁴󠁡󠁶󠁿 Flag for Alta Verapaz (GT-AV)
🏴󠁰󠁥󠁬󠁯󠁲󠁿 Flag for Loreto (PE-LOR)
🏴󠁰󠁥󠁭󠁯󠁱󠁿 Flag for Moquegua (PE-MOQ)
🏴󠁰󠁥󠁵󠁣󠁡󠁿 Flag for Ucayali (PE-UCA)
🏴󠁰󠁥󠁬󠁡󠁬󠁿 Flag for La Libertad (PE-LAL)
🏴󠁰󠁥󠁣󠁡󠁪󠁿 Flag for Cajamarca (PE-CAJ)
🏴󠁰󠁥󠁨󠁵󠁣󠁿 Flag for Huánuco (PE-HUC)
🏴󠁰󠁧󠁮󠁳󠁢󠁿 Flag for Bougainville (PG-NSB)
🏴󠁦󠁪󠁷󠁿 Flag for Western (FJ-W)
🏴󠁬󠁶󠀰󠀰󠀶󠁿 Flag for Alsunga (LV-006)
🏴󠁰󠁧󠁪󠁷󠁫󠁿 Flag for Jiwaka (PG-JWK)
🏴󠁡󠁲󠁡󠁿 Flag for Salta (AR-A)
🏴󠁰󠁫󠁩󠁳󠁿 Flag for Islamabad (PK-IS)
🏴󠁰󠁧󠁨󠁬󠁡󠁿 Flag for Hela (PG-HLA)
🏴󠁫󠁰󠀰󠀲󠁿 Flag for South Pyongan (KP-02)
🏴󠁰󠁧󠁷󠁰󠁤󠁿 Flag for Western (PG-WPD)
🏴󠁰󠁨󠀱󠀰󠁿 Flag for Northern Mindanao (PH-10)
🕱 Black Skull and Crossbones
🏴󠁦󠁲󠁰󠁡󠁣󠁿 Flag for Provence-Alpes-Côte-d’Azur (FR-PAC)
🏴󠁮󠁲󠀰󠀲󠁿 Flag for Anabar (NR-02)
🏴󠁰󠁨󠀱󠀳󠁿 Flag for Caraga (PH-13)
🏴󠁰󠁧󠁳󠁨󠁭󠁿 Flag for Southern Highlands (PG-SHM)
🏴󠁰󠁨󠀰󠀸󠁿 Flag for Eastern Visayas (PH-08)
🏴󠁰󠁨󠀴󠀰󠁿 Flag for Calabarzon (PH-40)
🏴󠁰󠁨󠀴󠀱󠁿 Flag for Mimaropa (PH-41)
🏴󠁰󠁧󠁳󠁡󠁮󠁿 Flag for Sandaun (PG-SAN)
🏴󠁰󠁨󠀰󠀹󠁿 Flag for Zamboanga Peninsula (PH-09)
🗶 Ballot Bold Script X
🏴󠁰󠁨󠀰󠀳󠁿 Flag for Central Luzon (PH-03)
🏴󠁰󠁧󠁭󠁰󠁭󠁿 Flag for Madang (PG-MPM)
🏴󠁰󠁨󠀱󠀲󠁿 Flag for Soccsksargen (PH-12)
👨🏽‍👩🏽‍👶🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
👩🏾‍👨🏾‍👧🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁰󠁧󠁥󠁳󠁷󠁿 Flag for East Sepik (PG-ESW)
🏴󠁰󠁧󠁭󠁰󠁬󠁿 Flag for Morobe (PG-MPL)
󠁫 Tag Latin Small Letter K
🏴󠁰󠁨󠀰󠀶󠁿 Flag for Western Visayas (PH-06)
🏴󠁰󠁧󠁭󠁢󠁡󠁿 Flag for Milne Bay (PG-MBA)
🏴󠁰󠁫󠁧󠁢󠁿 Flag for Gilgit-Baltistan (PK-GB)
🏴󠁩󠁴󠀵󠀲󠁿 Flag for Tuscany (IT-52)
🏴󠁰󠁨󠀱󠀱󠁿 Flag for Davao (PH-11)
🏴󠁡󠁵󠁱󠁬󠁤󠁿 Flag for Queensland (AU-QLD)
🏴󠁰󠁬󠁰󠁤󠁿 Flag for Podlaskie (PL-PD)
🏴󠁰󠁨󠀰󠀵󠁿 Flag for Bicol (PH-05)
🏴󠁰󠁫󠁫󠁰󠁿 Flag for Khyber Pakhtunkhwa (PK-KP)
🏴󠁰󠁬󠁬󠁢󠁿 Flag for Lubusz (PL-LB)
🏴󠁰󠁳󠁴󠁫󠁭󠁿 Flag for Tulkarm (PS-TKM)
🏴󠁰󠁬󠁰󠁭󠁿 Flag for Federal Capital Territory (PL-PM)
🏴󠁰󠁬󠁷󠁮󠁿 Flag for Warmian-Masuria (PL-WN)
󠁝 Tag Right Square Bracket
🏴󠁰󠁳󠁲󠁦󠁨󠁿 Flag for Rafah (PS-RFH)
🏴󠁰󠁳󠁮󠁢󠁳󠁿 Flag for Nablus (PS-NBS)
󠁋 Tag Latin Capital Letter K
🏴󠁰󠁳󠁪󠁥󠁮󠁿 Flag for Jenin (PS-JEN)
🏴󠁰󠁬󠁫󠁰󠁿 Flag for Kuyavian-Pomerania (PL-KP)
🏴󠁰󠁬󠁯󠁰󠁿 Flag for Opole (PL-OP)
🏴󠁰󠁬󠁳󠁬󠁿 Flag for Silesia (PL-SL)
🏴󠁰󠁫󠁰󠁢󠁿 Flag for Punjab (PK-PB)
🏴󠁭󠁸󠁹󠁵󠁣󠁿 Flag for Yucatán (MX-YUC)
🏴󠁭󠁹󠀰󠀱󠁿 Flag for Johor (MY-01)
🏴󠁰󠁬󠁰󠁫󠁿 Flag for Subcarpathia (PL-PK)
🏴󠁰󠁳󠁳󠁬󠁴󠁿 Flag for Salfit (PS-SLT)
🏴󠁰󠁬󠁺󠁰󠁿 Flag for West Pomerania (PL-ZP)
🏴󠁰󠁬󠁳󠁫󠁿 Flag for Świętokrzyskie (PL-SK)
🏴󠁰󠁳󠁴󠁢󠁳󠁿 Flag for Tubas (PS-TBS)
🏴󠁰󠁬󠁬󠁵󠁿 Flag for Lublin (PL-LU)
🏴󠁰󠁳󠁫󠁹󠁳󠁿 Flag for Khan Yunis (PS-KYS)
🏴󠁡󠁺󠁫󠁵󠁲󠁿 Flag for Kurdamir (AZ-KUR)
🏴󠁰󠁫󠁳󠁤󠁿 Flag for Sindh (PK-SD)
🏴󠁰󠁴󠀰󠀱󠁿 Flag for Aveiro (PT-01)
🏴󠁰󠁳󠁪󠁲󠁨󠁿 Flag for Jericho (PS-JRH)
🏴󠁰󠁳󠁨󠁢󠁮󠁿 Flag for Hebron (PS-HBN)
🏴󠁰󠁬󠁤󠁳󠁿 Flag for Lower Silesian (PL-DS)
🏴󠁰󠁬󠁭󠁺󠁿 Flag for Mazovia (PL-MZ)
🏴󠁰󠁳󠁱󠁱󠁡󠁿 Flag for Qalqilya (PS-QQA)
🏴󠁲󠁵󠁭󠁯󠁳󠁿 Flag for Moscow Province (RU-MOS)
🏴󠁰󠁬󠁬󠁤󠁿 Flag for Łódź (PL-LD)
🖘 Sideways White Left Pointing Index
🏴󠁰󠁹󠀱󠀱󠁿 Flag for Central (PY-11)
🏴󠁰󠁷󠀲󠀲󠀶󠁿 Flag for Ngchesar (PW-226)
🏴󠁰󠁴󠀱󠀷󠁿 Flag for Vila Real (PT-17)
🏴󠁰󠁷󠀲󠀱󠀴󠁿 Flag for Ngaraard (PW-214)
🏴󠁰󠁴󠀰󠀵󠁿 Flag for Castelo Branco (PT-05)
🏴󠁰󠁷󠀰󠀰󠀴󠁿 Flag for Airai (PW-004)
🏴󠁰󠁹󠀱󠀲󠁿 Flag for Ñeembucú (PY-12)
🏴󠁰󠁷󠀰󠀰󠀲󠁿 Flag for Aimeliik (PW-002)
🏴󠁰󠁴󠀰󠀶󠁿 Flag for Coimbra (PT-06)
🏴󠁫󠁰󠀰󠀶󠁿 Flag for North Hwanghae (KP-06)
🏴󠁰󠁹󠀱󠀵󠁿 Flag for Presidente Hayes (PY-15)
🏴󠁮󠁲󠀱󠀱󠁿 Flag for Meneng (NR-11)
🏴󠁰󠁴󠀱󠀲󠁿 Flag for Portalegre (PT-12)
🏴󠁮󠁧󠁥󠁮󠁿 Flag for Enugu (NG-EN)
🏴󠁰󠁨󠀰󠀲󠁿 Flag for Cagayan Valley (PH-02)
🏴󠁰󠁹󠀱󠀳󠁿 Flag for Amambay (PY-13)
🏴󠁰󠁷󠀲󠀲󠀲󠁿 Flag for Ngardmau (PW-222)
🏴󠁰󠁴󠀰󠀷󠁿 Flag for Évora (PT-07)
🏴󠁰󠁷󠀲󠀲󠀴󠁿 Flag for Ngatpang (PW-224)
🏴󠁰󠁹󠀱󠀴󠁿 Flag for Canindeyú (PY-14)
🏴󠁰󠁷󠀲󠀲󠀷󠁿 Flag for Ngeremlengui (PW-227)
🏴󠁰󠁴󠀱󠀶󠁿 Flag for Viana do Castelo (PT-16)
🏴󠁡󠁯󠁮󠁡󠁭󠁿 Flag for Namibe (AO-NAM)
🏴󠁰󠁷󠀰󠀱󠀰󠁿 Flag for Angaur (PW-010)
🏴󠁰󠁴󠀱󠀰󠁿 Flag for Leiria (PT-10)
🏴󠁰󠁴󠀰󠀹󠁿 Flag for Guarda (PT-09)
🏴󠁰󠁹󠀱󠀰󠁿 Flag for Alto Paraná (PY-10)
🏴󠁰󠁴󠀱󠀵󠁿 Flag for Setúbal (PT-15)
🏴󠁰󠁴󠀱󠀴󠁿 Flag for Santarém (PT-14)
🏴󠁰󠁡󠀲󠁿 Flag for Coclé (PA-2)
🏴󠁰󠁷󠀰󠀵󠀰󠁿 Flag for Hatohobei (PW-050)
🏴󠁰󠁴󠀰󠀴󠁿 Flag for Bragança (PT-04)
🏴󠁰󠁷󠀱󠀵󠀰󠁿 Flag for Koror (PW-150)
🏴󠁰󠁹󠀸󠁿 Flag for Misiones (PY-8)
🏴󠁰󠁹󠀲󠁿 Flag for San Pedro (PY-2)
🏴󠁲󠁯󠁤󠁪󠁿 Flag for Dolj (RO-DJ)
🏴󠁲󠁯󠁨󠁤󠁿 Flag for Hunedoara (RO-HD)
🏴󠁰󠁹󠀴󠁿 Flag for Guairá (PY-4)
🖁 Clamshell Mobile Phone
🖏 Turned Ok Hand Sign
🏴󠁲󠁯󠁢󠁨󠁿 Flag for Bihor (RO-BH)
🏴󠁰󠁹󠀶󠁿 Flag for Caazapá (PY-6)
🏴󠁲󠁯󠁣󠁪󠁿 Flag for Cluj (RO-CJ)
🏴󠁲󠁯󠁣󠁴󠁿 Flag for Constanța (RO-CT)
🏴󠁲󠁯󠁤󠁢󠁿 Flag for Dâmbovița (RO-DB)
🏴󠁤󠁪󠁤󠁩󠁿 Flag for Dikhil (DJ-DI)
🏴󠁲󠁯󠁧󠁬󠁿 Flag for Galați (RO-GL)
🏴󠁰󠁹󠀳󠁿 Flag for Cordillera (PY-3)
🏴󠁲󠁯󠁨󠁲󠁿 Flag for Harghita (RO-HR)
󠁎 Tag Latin Capital Letter N
🏴󠁱󠁡󠁭󠁳󠁿 Flag for Madinat ash Shamal (QA-MS)
🏴󠁱󠁡󠁺󠁡󠁿 Flag for Al Daayen (QA-ZA)
🏴󠁩󠁳󠀱󠁿 Flag for Capital (IS-1)
🏴󠁰󠁹󠀷󠁿 Flag for Itapúa (PY-7)
🏴󠁰󠁹󠁡󠁳󠁵󠁿 Flag for Asunción (PY-ASU)
🏴󠁰󠁹󠀱󠁿 Flag for Concepción (PY-1)
🏴󠁲󠁯󠁢󠁣󠁿 Flag for Bacău (RO-BC)
🏴󠁱󠁡󠁷󠁡󠁿 Flag for Al Wakrah (QA-WA)
🏴󠁰󠁹󠀵󠁿 Flag for Caaguazú (PY-5)
🏴󠁱󠁡󠁲󠁡󠁿 Flag for Al Rayyan (QA-RA)
🏴󠁰󠁹󠀹󠁿 Flag for Paraguarí (PY-9)
🏴󠁲󠁯󠁡󠁲󠁿 Flag for Arad (RO-AR)
🏴󠁰󠁹󠀱󠀹󠁿 Flag for Boquerón (PY-19)
🏴󠁱󠁡󠁫󠁨󠁿 Flag for Al Khor (QA-KH)
🏴󠁲󠁯󠁡󠁧󠁿 Flag for Argeș (RO-AG)
🏴󠁲󠁯󠁣󠁶󠁿 Flag for Covasna (RO-CV)
🏴󠁲󠁯󠁧󠁲󠁿 Flag for Giurgiu (RO-GR)
🏴󠁲󠁯󠁢󠁲󠁿 Flag for Brăila (RO-BR)
🀂 Mahjong Tile West Wind
🏴󠁲󠁯󠁶󠁳󠁿 Flag for Vaslui (RO-VS)
🏴󠁲󠁳󠀱󠀲󠁿 Flag for Šumadija (RS-12)
🏴󠁲󠁳󠀲󠀰󠁿 Flag for Nišava (RS-20)
🏴󠁰󠁧󠁮󠁰󠁰󠁿 Flag for Oro (PG-NPP)
🏴󠁲󠁯󠁰󠁨󠁿 Flag for Prahova (RO-PH)
🏴󠁲󠁯󠁴󠁬󠁿 Flag for Tulcea (RO-TL)
🏴󠁲󠁳󠀲󠀳󠁿 Flag for Jablanica (RS-23)
🏴󠁲󠁯󠁴󠁲󠁿 Flag for Teleorman (RO-TR)
🏴󠁲󠁳󠀰󠀰󠁿 Flag for Beograd (RS-00)
🏴󠁲󠁯󠁩󠁦󠁿 Flag for Ilfov (RO-IF)
🏴󠁲󠁳󠀱󠀱󠁿 Flag for Braničevo (RS-11)
🏴󠁲󠁯󠁩󠁳󠁿 Flag for Iași (RO-IS)
🏴󠁲󠁯󠁭󠁳󠁿 Flag for Mureş (RO-MS)
🏴󠁲󠁳󠀰󠀸󠁿 Flag for Mačva (RS-08)
󠁟 Tag Low Line
🏴󠁲󠁳󠀲󠀲󠁿 Flag for Pirot (RS-22)
🏴󠁲󠁳󠀱󠀷󠁿 Flag for Moravica (RS-17)
🏴󠁲󠁳󠀲󠀱󠁿 Flag for Toplica (RS-21)
🏴󠁲󠁯󠁯󠁴󠁿 Flag for Olt (RO-OT)
🏴󠁲󠁳󠀱󠀳󠁿 Flag for Pomoravlje (RS-13)
🏴󠁲󠁯󠁶󠁮󠁿 Flag for Vrancea (RO-VN)
🏴󠁲󠁯󠁭󠁨󠁿 Flag for Mehedinți (RO-MH)
🏴󠁲󠁳󠀱󠀶󠁿 Flag for Zlatibor (RS-16)
🏴󠁭󠁣󠁭󠁵󠁿 Flag for Moulins (MC-MU)
🏴󠁲󠁳󠀱󠀸󠁿 Flag for Raška (RS-18)
🏴󠁲󠁳󠀲󠀴󠁿 Flag for Pčinja (RS-24)
🏴󠁲󠁯󠁭󠁭󠁿 Flag for Maramureş (RO-MM)
🏴󠁨󠁵󠁰󠁳󠁿 Flag for Pécs (HU-PS)
🏴󠁲󠁯󠁳󠁶󠁿 Flag for Suceava (RO-SV)
🏴󠁲󠁯󠁮󠁴󠁿 Flag for Neamţ (RO-NT)
🏴󠁲󠁳󠀰󠀹󠁿 Flag for Kolubara (RS-09)
🏴󠁲󠁳󠀱󠀹󠁿 Flag for Rasina (RS-19)
🏴󠁲󠁯󠁩󠁬󠁿 Flag for Ialomița (RO-IL)
🏴󠁲󠁯󠁳󠁪󠁿 Flag for Sălaj (RO-SJ)
🏴󠁲󠁳󠀱󠀵󠁿 Flag for Zaječar (RS-15)
🏴󠁲󠁯󠁴󠁭󠁿 Flag for Timiș (RO-TM)
🏴󠁲󠁵󠁩󠁶󠁡󠁿 Flag for Ivanovo (RU-IVA)
🏴󠁲󠁵󠁫󠁲󠁳󠁿 Flag for Kursk (RU-KRS)
🏴󠁲󠁵󠁣󠁨󠁥󠁿 Flag for Chelyabinsk (RU-CHE)
🏴󠁬󠁲󠁧󠁫󠁿 Flag for Grand Kru (LR-GK)
🏴󠁲󠁵󠁫󠁡󠁭󠁿 Flag for Kamchatka Krai (RU-KAM)
🏴󠁲󠁵󠁫󠁬󠁵󠁿 Flag for Kaluga (RU-KLU)
🏴󠁲󠁵󠁫󠁹󠁡󠁿 Flag for Krasnoyarsk Krai (RU-KYA)
🏴󠁲󠁵󠁣󠁵󠁿 Flag for Chuvash (RU-CU)
🏴󠁲󠁵󠁫󠁩󠁲󠁿 Flag for Kirov (RU-KIR)
🏴󠁲󠁵󠁡󠁳󠁴󠁿 Flag for Astrakhan (RU-AST)
🏴󠁲󠁵󠁫󠁨󠁭󠁿 Flag for Khanty-Mansi (RU-KHM)
🏴󠁲󠁵󠁭󠁥󠁿 Flag for Mari El (RU-ME)
🏴󠁲󠁵󠁢󠁥󠁬󠁿 Flag for Belgorod (RU-BEL)
🏴󠁲󠁵󠁫󠁣󠁿 Flag for Karachay-Cherkess (RU-KC)
🏴󠁲󠁵󠁡󠁬󠁿 Flag for Altai (RU-AL)
🏴󠁲󠁵󠁬󠁩󠁰󠁿 Flag for Lipetsk (RU-LIP)
🏴󠁲󠁵󠁭󠁯󠁿 Flag for Mordovia (RU-MO)
🏴󠁲󠁵󠁫󠁯󠁿 Flag for Komi (RU-KO)
🏴󠁲󠁯󠁡󠁢󠁿 Flag for Alba (RO-AB)
🏴󠁩󠁮󠁵󠁰󠁿 Flag for Uttar Pradesh (IN-UP)
🏴󠁲󠁵󠁫󠁥󠁭󠁿 Flag for Kemerovo (RU-KEM)
👨🏾‍❤️‍👨🏻 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Light Skin Tone
🏴󠁲󠁵󠁫󠁲󠁿 Flag for Karelia (RU-KR)
🏴󠁡󠁺󠁫󠁡󠁬󠁿 Flag for Kalbajar (AZ-KAL)
👨🏻‍❤️‍💋‍👨🏻 Kiss - Man: Light Skin Tone, Man: Light Skin Tone
🏴󠁡󠁯󠁭󠁯󠁸󠁿 Flag for Moxico (AO-MOX)
🏴󠁲󠁵󠁩󠁲󠁫󠁿 Flag for Irkutsk (RU-IRK)
🏴󠁢󠁲󠁧󠁯󠁿 Flag for Goiás (BR-GO)
🏴󠁫󠁥󠀴󠀶󠁿 Flag for Wajir (KE-46)
🏴󠁲󠁵󠁫󠁧󠁮󠁿 Flag for Kurgan (RU-KGN)
🏴󠁰󠁥󠁴󠁡󠁣󠁿 Flag for Tacna (PE-TAC)
👩🏼‍❤️‍💋‍👩 Kiss - Woman: Medium-Light Skin Tone, Woman
🏴󠁲󠁵󠁲󠁹󠁡󠁿 Flag for Ryazan (RU-RYA)
🏴󠁲󠁵󠁴󠁡󠁭󠁿 Flag for Tambov (RU-TAM)
🏴󠁲󠁵󠁴󠁯󠁭󠁿 Flag for Tomsk (RU-TOM)
🏴󠁲󠁵󠁮󠁧󠁲󠁿 Flag for Novgorod (RU-NGR)
🏴󠁩󠁴󠀲󠀱󠁿 Flag for Piedmont (IT-21)
🏴󠁲󠁵󠁳󠁡󠁲󠁿 Flag for Saratov (RU-SAR)
🏴󠁲󠁵󠁮󠁶󠁳󠁿 Flag for Novosibirsk (RU-NVS)
🏴󠁲󠁵󠁰󠁮󠁺󠁿 Flag for Penza (RU-PNZ)
🏴󠁲󠁵󠁳󠁶󠁥󠁿 Flag for Sverdlovsk (RU-SVE)
🏴󠁲󠁯󠁣󠁬󠁿 Flag for Călărași (RO-CL)
🏴󠁲󠁵󠁴󠁹󠁵󠁿 Flag for Tyumen (RU-TYU)
🏴󠁲󠁵󠁹󠁡󠁮󠁿 Flag for Yamalo-Nenets Okrug (RU-YAN)
🏴󠁲󠁵󠁲󠁯󠁳󠁿 Flag for Rostov (RU-ROS)
🏴󠁩󠁮󠁤󠁤󠁿 Flag for Daman and Diu (IN-DD)
🏴󠁲󠁵󠁯󠁲󠁥󠁿 Flag for Orenburg (RU-ORE)
🏴󠁬󠁡󠁸󠁩󠁿 Flag for Xiangkhouang (LA-XI)
🗴 Ballot Script X
🏴󠁲󠁵󠁳󠁭󠁯󠁿 Flag for Smolensk (RU-SMO)
🏴󠁲󠁵󠁹󠁡󠁲󠁿 Flag for Yaroslavl (RU-YAR)
🏴󠁲󠁵󠁴󠁵󠁬󠁿 Flag for Tula (RU-TUL)
🏴󠁲󠁵󠁭󠁵󠁲󠁿 Flag for Murmansk (RU-MUR)
🏴󠁲󠁵󠁶󠁬󠁡󠁿 Flag for Vladimir (RU-VLA)
🏴󠁲󠁵󠁮󠁥󠁮󠁿 Flag for Nenets (RU-NEN)
🏴󠁲󠁵󠁮󠁩󠁺󠁿 Flag for Nizhny Novgorod (RU-NIZ)
🏴󠁲󠁵󠁴󠁶󠁥󠁿 Flag for Tver (RU-TVE)
🏴󠁲󠁵󠁰󠁳󠁫󠁿 Flag for Pskov (RU-PSK)
🏴󠁰󠁧󠁥󠁰󠁷󠁿 Flag for Enga (PG-EPW)
🏴󠁮󠁧󠁢󠁡󠁿 Flag for Bauchi (NG-BA)
🏴󠁲󠁵󠁳󠁡󠁫󠁿 Flag for Sakhalin (RU-SAK)
🏴󠁲󠁵󠁶󠁬󠁧󠁿 Flag for Vologda (RU-VLG)
🏴󠁲󠁵󠁴󠁹󠁿 Flag for Tuva (RU-TY)
🏴󠁳󠁣󠀰󠀲󠁿 Flag for Anse Boileau (SC-02)
🏴󠁳󠁡󠀰󠀹󠁿 Flag for Jizan (SA-09)
🏴󠁮󠁺󠁣󠁡󠁮󠁿 Flag for Canterbury (NZ-CAN)
🏴󠁲󠁵󠁺󠁡󠁢󠁿 Flag for Zabaykalsky Krai (RU-ZAB)
🏴󠁲󠁷󠀰󠀵󠁿 Flag for Southern (RW-05)
🏴󠁳󠁢󠁧󠁵󠁿 Flag for Guadalcanal (SB-GU)
🏴󠁳󠁢󠁣󠁥󠁿 Flag for Central (SB-CE)
🏴󠁳󠁢󠁷󠁥󠁿 Flag for Western (SB-WE)
🏴󠁰󠁴󠀰󠀳󠁿 Flag for Braga (PT-03)
🏴󠁳󠁡󠀱󠀰󠁿 Flag for Najran (SA-10)
🏴󠁣󠁡󠁰󠁥󠁿 Flag for Prince Edward Island (CA-PE)
🏴󠁳󠁢󠁭󠁬󠁿 Flag for Malaita (SB-ML)
🏴󠁳󠁡󠀰󠀷󠁿 Flag for Tabuk (SA-07)
🏴󠁳󠁡󠀱󠀴󠁿 Flag for Asir (SA-14)
🏴󠁳󠁡󠀱󠀲󠁿 Flag for Al Jawf (SA-12)
🏴󠁪󠁰󠀰󠀱󠁿 Flag for Hokkaidō (JP-01)
🏴󠁳󠁣󠀰󠀸󠁿 Flag for Beau Vallon (SC-08)
🏴󠁲󠁷󠀰󠀲󠁿 Flag for Eastern (RW-02)
🏴󠁳󠁣󠀰󠀷󠁿 Flag for Baie Sainte Anne (SC-07)
🏴󠁰󠁧󠁷󠁨󠁭󠁿 Flag for Western Highlands (PG-WHM)
🏴󠁮󠁺󠁯󠁴󠁡󠁿 Flag for Otago (NZ-OTA)
🏴󠁳󠁡󠀰󠀴󠁿 Flag for Eastern (SA-04)
🏴󠁳󠁣󠀰󠀶󠁿 Flag for Baie Lazare (SC-06)
🏴󠁳󠁢󠁩󠁳󠁿 Flag for Isabel (SB-IS)
🏴󠁳󠁢󠁣󠁨󠁿 Flag for Choiseul (SB-CH)
🏴󠁲󠁷󠀰󠀴󠁿 Flag for Western (RW-04)
🏴󠁳󠁢󠁣󠁴󠁿 Flag for Honiara (SB-CT)
🏴󠁲󠁷󠀰󠀳󠁿 Flag for Northern (RW-03)
🏴󠁰󠁷󠀳󠀷󠀰󠁿 Flag for Sonsorol (PW-370)
6️ Digit Six
🏴󠁳󠁣󠀰󠀴󠁿 Flag for Au Cap (SC-04)
🏴󠁳󠁢󠁲󠁢󠁿 Flag for Rennell and Bellona (SB-RB)
🏴󠁳󠁢󠁭󠁫󠁿 Flag for Makira-Ulawa (SB-MK)
🏴󠁳󠁡󠀰󠀶󠁿 Flag for Ha’il (SA-06)
🏴󠁳󠁡󠀰󠀸󠁿 Flag for Northern Borders (SA-08)
🏴󠁲󠁷󠀰󠀱󠁿 Flag for Kigali (RW-01)
🏴󠁳󠁤󠁧󠁺󠁿 Flag for Al Jazirah (SD-GZ)
🏴󠁳󠁣󠀱󠀹󠁿 Flag for Plaisance (SC-19)
🏴󠁳󠁤󠁤󠁳󠁿 Flag for South Darfur (SD-DS)
🏴󠁳󠁣󠀱󠀸󠁿 Flag for Mont Fleuri (SC-18)
🏴󠁳󠁣󠀲󠀱󠁿 Flag for Port Glaud (SC-21)
🏴󠁳󠁥󠁤󠁿 Flag for Södermanland (SE-D)
🏴󠁳󠁤󠁫󠁳󠁿 Flag for South Kurdufan (SD-KS)
🏴󠁳󠁤󠁧󠁫󠁿 Flag for West Kurdufan (SD-GK)
🏴󠁳󠁤󠁳󠁩󠁿 Flag for Sennar (SD-SI)
🏴󠁳󠁣󠀱󠀶󠁿 Flag for La Rivière Anglaise (SC-16)
🏴󠁳󠁤󠁫󠁨󠁿 Flag for Khartoum (SD-KH)
🏴󠁳󠁣󠀱󠀵󠁿 Flag for La Digue (SC-15)
🏴󠁳󠁤󠁮󠁯󠁿 Flag for Northern (SD-NO)
🏴󠁳󠁣󠀲󠀲󠁿 Flag for Saint Louis (SC-22)
🏴󠁳󠁣󠀱󠀴󠁿 Flag for Grand’Anse Praslin (SC-14)
🏴󠁲󠁵󠁶󠁧󠁧󠁿 Flag for Volgograd (RU-VGG)
🏴󠁳󠁣󠀲󠀴󠁿 Flag for Les Mamelles (SC-24)
🕈 Celtic Cross
🏴󠁳󠁤󠁤󠁥󠁿 Flag for East Darfur (SD-DE)
🏴󠁳󠁤󠁮󠁷󠁿 Flag for White Nile (SD-NW)
🏴󠁳󠁣󠀱󠀲󠁿 Flag for Glacis (SC-12)
🏴󠁳󠁤󠁫󠁮󠁿 Flag for North Kurdufan (SD-KN)
🏴󠁳󠁥󠁦󠁿 Flag for Jönköping (SE-F)
🏴󠁳󠁤󠁤󠁮󠁿 Flag for North Darfur (SD-DN)
🏴󠁳󠁥󠁥󠁿 Flag for Östergötland (SE-E)
🏴󠁳󠁣󠀱󠀳󠁿 Flag for Grand’Anse Mahé (SC-13)
🏴󠁳󠁥󠁡󠁢󠁿 Flag for Stockholm (SE-AB)
🏴󠁳󠁤󠁮󠁲󠁿 Flag for River Nile (SD-NR)
🏴󠁳󠁥󠁢󠁤󠁿 Flag for Norrbotten (SE-BD)
🏴󠁳󠁥󠁡󠁣󠁿 Flag for Västerbotten (SE-AC)
🏴󠁳󠁣󠀱󠀱󠁿 Flag for Cascade (SC-11)
🏴󠁳󠁣󠀱󠀷󠁿 Flag for Mont Buxton (SC-17)
🏴󠁳󠁤󠁫󠁡󠁿 Flag for Kassala (SD-KA)
🏴󠁳󠁤󠁤󠁣󠁿 Flag for Central Darfur (SD-DC)
🏴󠁳󠁤󠁤󠁷󠁿 Flag for West Darfur (SD-DW)
🏴󠁳󠁣󠀲󠀰󠁿 Flag for Pointe La Rue (SC-20)
🏴󠁳󠁤󠁧󠁤󠁿 Flag for Al Qadarif (SD-GD)
🏴󠁳󠁣󠀲󠀳󠁿 Flag for Takamaka (SC-23)
🏴󠁳󠁨󠁡󠁣󠁿 Flag for Ascension Island (SH-AC)
🏴󠁳󠁥󠁧󠁿 Flag for Kronoberg (SE-G)
🏴󠁳󠁩󠀰󠀱󠀰󠁿 Flag for Tišina (SI-010)
🏴󠁳󠁩󠀰󠀱󠀷󠁿 Flag for Črnomelj (SI-017)
🏴󠁳󠁩󠀰󠀰󠀲󠁿 Flag for Beltinci (SI-002)
🏴󠁳󠁥󠁵󠁿 Flag for Västmanland (SE-U)
🏴󠁳󠁩󠀰󠀱󠀳󠁿 Flag for Cerknica (SI-013)
🏴󠁳󠁩󠀰󠀱󠀶󠁿 Flag for Črna na Koroškem (SI-016)
🏴󠁳󠁥󠁫󠁿 Flag for Blekinge (SE-K)
🏴󠁳󠁧󠀰󠀴󠁿 Flag for South East (SG-04)
🏴󠁳󠁥󠁨󠁿 Flag for Kalmar (SE-H)
🏴󠁳󠁩󠀰󠀱󠀸󠁿 Flag for Destrnik (SI-018)
🏴󠁳󠁧󠀰󠀳󠁿 Flag for North West (SG-03)
🏴󠁳󠁨󠁨󠁬󠁿 Flag for Saint Helena (SH-HL)
🏴󠁳󠁩󠀰󠀰󠀹󠁿 Flag for Brežice (SI-009)
🏴󠁳󠁧󠀰󠀵󠁿 Flag for South West (SG-05)
🏴󠁳󠁩󠀰󠀰󠀳󠁿 Flag for Bled (SI-003)
🏴󠁳󠁣󠀰󠀳󠁿 Flag for Anse Etoile (SC-03)
🏴󠁳󠁥󠁴󠁿 Flag for Örebro (SE-T)
🏴󠁳󠁩󠀰󠀰󠀷󠁿 Flag for Brda (SI-007)
🏴󠁡󠁯󠁭󠁡󠁬󠁿 Flag for Malanje (AO-MAL)
🏴󠁳󠁩󠀰󠀱󠀵󠁿 Flag for Črenšovci (SI-015)
🏴󠁭󠁤󠁲󠁥󠁿 Flag for Rezina (MD-RE)
🏴󠁳󠁩󠀰󠀰󠀱󠁿 Flag for Ajdovščina (SI-001)
🏴󠁳󠁩󠀰󠀰󠀵󠁿 Flag for Borovnica (SI-005)
🏴󠁡󠁯󠁣󠁮󠁯󠁿 Flag for Cuanza Norte (AO-CNO)
🏴󠁳󠁩󠀰󠀰󠀶󠁿 Flag for Bovec (SI-006)
🏴󠁳󠁥󠁳󠁿 Flag for Värmland (SE-S)
🏴󠁳󠁩󠀰󠀱󠀲󠁿 Flag for Cerklje na Gorenjskem (SI-012)
🏴󠁳󠁩󠀰󠀱󠀴󠁿 Flag for Cerkno (SI-014)
🏴󠁳󠁧󠀰󠀲󠁿 Flag for North East (SG-02)
🏴󠁳󠁩󠀰󠀰󠀸󠁿 Flag for Brezovica (SI-008)
🏴󠁳󠁩󠀰󠀱󠀹󠁿 Flag for Divača (SI-019)
🏴󠁳󠁩󠀰󠀴󠀰󠁿 Flag for Izola (SI-040)
🏴󠁳󠁩󠀰󠀲󠀵󠁿 Flag for Dravograd (SI-025)
🏴󠁳󠁩󠀰󠀴󠀱󠁿 Flag for Jesenice (SI-041)
🏴󠁳󠁩󠀰󠀲󠀸󠁿 Flag for Gorišnica (SI-028)
🏴󠁳󠁩󠀰󠀲󠀹󠁿 Flag for Gornja Radgona (SI-029)
🏴󠁳󠁩󠀰󠀵󠀳󠁿 Flag for Kranjska Gora (SI-053)
🏴󠁳󠁩󠀰󠀲󠀴󠁿 Flag for Dornava (SI-024)
🏴󠁳󠁩󠀰󠀳󠀴󠁿 Flag for Hrastnik (SI-034)
🏴󠁳󠁩󠀰󠀳󠀰󠁿 Flag for Gornji Grad (SI-030)
🏴󠁳󠁩󠀰󠀴󠀹󠁿 Flag for Komen (SI-049)
🏴󠁳󠁩󠀰󠀵󠀱󠁿 Flag for Kozje (SI-051)
🏴󠁵󠁳󠁷󠁩󠁿 Flag for Wisconsin (US-WI)
🏴󠁳󠁩󠀰󠀳󠀶󠁿 Flag for Idrija (SI-036)
🏴󠁳󠁩󠀰󠀳󠀱󠁿 Flag for Gornji Petrovci (SI-031)
🏴󠁳󠁩󠀰󠀴󠀶󠁿 Flag for Kobarid (SI-046)
🏴󠁳󠁩󠀰󠀴󠀷󠁿 Flag for Kobilje (SI-047)
🏴󠁳󠁢󠁴󠁥󠁿 Flag for Temotu (SB-TE)
🏴󠁳󠁩󠀰󠀴󠀴󠁿 Flag for Kanal (SI-044)
🏴󠁳󠁩󠀰󠀲󠀱󠁿 Flag for Dobrova–Polhov Gradec (SI-021)
🏴󠁳󠁩󠀰󠀵󠀵󠁿 Flag for Kungota (SI-055)
🏴󠁳󠁩󠀰󠀳󠀲󠁿 Flag for Grosuplje (SI-032)
🏴󠁳󠁩󠀰󠀲󠀶󠁿 Flag for Duplek (SI-026)
🏴󠁳󠁩󠀰󠀴󠀲󠁿 Flag for Juršinci (SI-042)
🏴󠁳󠁩󠀰󠀵󠀴󠁿 Flag for Krško (SI-054)
🏴󠁳󠁩󠀰󠀳󠀳󠁿 Flag for Šalovci (SI-033)
🏴󠁳󠁩󠀰󠀳󠀹󠁿 Flag for Ivančna Gorica (SI-039)
🏴󠁳󠁩󠀰󠀴󠀸󠁿 Flag for Kočevje (SI-048)
🏴󠁳󠁩󠀰󠀳󠀸󠁿 Flag for Ilirska Bistrica (SI-038)
🏴󠁳󠁩󠀰󠀴󠀳󠁿 Flag for Kamnik (SI-043)
🏴󠁳󠁩󠀰󠀳󠀵󠁿 Flag for Hrpelje–Kozina (SI-035)
🏴󠁳󠁩󠀰󠀲󠀳󠁿 Flag for Domžale (SI-023)
🏴󠁲󠁵󠁵󠁬󠁹󠁿 Flag for Ulyanovsk (RU-ULY)
🏴󠁳󠁩󠀰󠀲󠀰󠁿 Flag for Dobrepolje (SI-020)
🏴󠁳󠁩󠀰󠀵󠀶󠁿 Flag for Kuzma (SI-056)
🏴󠁳󠁩󠀰󠀸󠀹󠁿 Flag for Pesnica (SI-089)
🏴󠁳󠁩󠀰󠀸󠀷󠁿 Flag for Ormož (SI-087)
🏴󠁳󠁩󠀰󠀷󠀴󠁿 Flag for Mežica (SI-074)
🏴󠁳󠁩󠀰󠀷󠀶󠁿 Flag for Mislinja (SI-076)
🏴󠁳󠁩󠀰󠀵󠀹󠁿 Flag for Lendava (SI-059)
🏴󠁳󠁩󠀰󠀹󠀳󠁿 Flag for Podvelka (SI-093)
🏴󠁳󠁩󠀰󠀶󠀶󠁿 Flag for Loški Potok (SI-066)
🏴󠁳󠁩󠀰󠀸󠀱󠁿 Flag for Muta (SI-081)
🏴󠁭󠁥󠀰󠀸󠁿 Flag for Herceg Novi (ME-08)
🏴󠁳󠁩󠀰󠀷󠀲󠁿 Flag for Mengeš (SI-072)
🏴󠁳󠁩󠀰󠀷󠀳󠁿 Flag for Metlika (SI-073)
🏴󠁳󠁩󠀰󠀷󠀷󠁿 Flag for Moravče (SI-077)
🏴󠁳󠁩󠀰󠀷󠀸󠁿 Flag for Moravske Toplice (SI-078)
🏴󠁳󠁩󠀰󠀹󠀴󠁿 Flag for Postojna (SI-094)
🏴󠁳󠁩󠀰󠀸󠀰󠁿 Flag for Murska Sobota (SI-080)
🏴󠁳󠁩󠀰󠀸󠀲󠁿 Flag for Naklo (SI-082)
🕻 Left Hand Telephone Receiver
🏴󠁳󠁩󠀰󠀶󠀴󠁿 Flag for Logatec (SI-064)
🏴󠁳󠁩󠀰󠀶󠀳󠁿 Flag for Ljutomer (SI-063)
🏴󠁳󠁩󠀰󠀹󠀱󠁿 Flag for Pivka (SI-091)
🏴󠁳󠁩󠀰󠀸󠀳󠁿 Flag for Nazarje (SI-083)
🏴󠁳󠁩󠀰󠀷󠀵󠁿 Flag for Miren–Kostanjevica (SI-075)
🏴󠁳󠁩󠀰󠀶󠀱󠁿 Flag for Ljubljana (SI-061)
🏴󠁳󠁩󠀰󠀷󠀰󠁿 Flag for Maribor (SI-070)
🏴󠁳󠁩󠀰󠀶󠀷󠁿 Flag for Luče (SI-067)
🏴󠁳󠁩󠀰󠀹󠀲󠁿 Flag for Podčetrtek (SI-092)
🏴󠁳󠁩󠀰󠀶󠀲󠁿 Flag for Ljubno (SI-062)
🏴󠁳󠁩󠀰󠀸󠀴󠁿 Flag for Nova Gorica (SI-084)
🏴󠁳󠁩󠀰󠀷󠀱󠁿 Flag for Medvode (SI-071)
🏴󠁳󠁩󠀰󠀶󠀵󠁿 Flag for Loška Dolina (SI-065)
🏴󠁳󠁩󠀰󠀸󠀸󠁿 Flag for Osilnica (SI-088)
🏴󠁳󠁩󠀰󠀷󠀹󠁿 Flag for Mozirje (SI-079)
🏴󠁳󠁩󠀰󠀶󠀸󠁿 Flag for Lukovica (SI-068)
🏴󠁳󠁩󠀰󠀶󠀰󠁿 Flag for Litija (SI-060)
🏴󠁳󠁩󠀰󠀵󠀷󠁿 Flag for Laško (SI-057)
🏴󠁳󠁩󠀰󠀶󠀹󠁿 Flag for Majšperk (SI-069)
🏴󠁧󠁨󠁣󠁰󠁿 Flag for Central (GH-CP)
🏴󠁳󠁩󠀱󠀳󠀱󠁿 Flag for Tržič (SI-131)
🏴󠁳󠁩󠀱󠀱󠀸󠁿 Flag for Šentilj (SI-118)
🏴󠁳󠁩󠀱󠀱󠀴󠁿 Flag for Slovenske Konjice (SI-114)
🏴󠁳󠁩󠀰󠀹󠀷󠁿 Flag for Puconci (SI-097)
🏴󠁳󠁩󠀰󠀹󠀸󠁿 Flag for Rače–Fram (SI-098)
🏴󠁳󠁩󠀱󠀰󠀵󠁿 Flag for Rogašovci (SI-105)
🏴󠁳󠁩󠀱󠀱󠀳󠁿 Flag for Slovenska Bistrica (SI-113)
🏴󠁳󠁩󠀱󠀰󠀷󠁿 Flag for Rogatec (SI-107)
🏴󠁳󠁩󠀰󠀹󠀶󠁿 Flag for Ptuj (SI-096)
🏴󠁳󠁩󠀱󠀱󠀹󠁿 Flag for Šentjernej (SI-119)
🏴󠁳󠁩󠀱󠀱󠀱󠁿 Flag for Sežana (SI-111)
🏴󠁳󠁩󠀱󠀱󠀲󠁿 Flag for Slovenj Gradec (SI-112)
🏴󠁳󠁩󠀱󠀱󠀵󠁿 Flag for Starše (SI-115)
🏴󠁳󠁩󠀱󠀱󠀶󠁿 Flag for Sveti Jurij (SI-116)
🏴󠁳󠁩󠀱󠀳󠀰󠁿 Flag for Trebnje (SI-130)
🏴󠁳󠁩󠀱󠀱󠀰󠁿 Flag for Sevnica (SI-110)
🏴󠁳󠁩󠀰󠀹󠀹󠁿 Flag for Radeče (SI-099)
🏴󠁳󠁩󠀱󠀲󠀱󠁿 Flag for Škocjan (SI-121)
🏴󠁳󠁩󠀱󠀲󠀴󠁿 Flag for Šmarje pri Jelšah (SI-124)
🏴󠁳󠁩󠀱󠀲󠀶󠁿 Flag for Šoštanj (SI-126)
🏴󠁳󠁩󠀱󠀲󠀷󠁿 Flag for Štore (SI-127)
🏴󠁳󠁩󠀱󠀰󠀴󠁿 Flag for Ribnica (SI-104)
🏴󠁳󠁩󠀱󠀰󠀶󠁿 Flag for Rogaška Slatina (SI-106)
🏴󠁳󠁩󠀱󠀲󠀹󠁿 Flag for Trbovlje (SI-129)
🏴󠁳󠁩󠀱󠀳󠀲󠁿 Flag for Turnišče (SI-132)
🏴󠁳󠁩󠀱󠀰󠀲󠁿 Flag for Radovljica (SI-102)
🏴󠁳󠁩󠀰󠀹󠀵󠁿 Flag for Preddvor (SI-095)
🏴󠁳󠁩󠀱󠀲󠀰󠁿 Flag for Šentjur (SI-120)
🏴󠁳󠁩󠀱󠀲󠀸󠁿 Flag for Tolmin (SI-128)
🏴󠁳󠁩󠀱󠀰󠀱󠁿 Flag for Radlje ob Dravi (SI-101)
🏴󠁳󠁩󠀱󠀰󠀸󠁿 Flag for Ruše (SI-108)
🏴󠁳󠁩󠀱󠀰󠀹󠁿 Flag for Semič (SI-109)
🏴󠁳󠁩󠀱󠀱󠀷󠁿 Flag for Šenčur (SI-117)
🏴󠁳󠁩󠀱󠀰󠀳󠁿 Flag for Ravne na Koroškem (SI-103)
🏴󠁳󠁩󠀱󠀲󠀳󠁿 Flag for Škofljica (SI-123)
🏴󠁳󠁩󠀱󠀶󠀹󠁿 Flag for Miklavž na Dravskem Polju (SI-169)
🏴󠁳󠁩󠀱󠀴󠀲󠁿 Flag for Zagorje ob Savi (SI-142)
🕅 Symbol for Marks Chapter
🏴󠁳󠁩󠀱󠀴󠀰󠁿 Flag for Vrhnika (SI-140)
🏴󠁳󠁩󠀱󠀷󠀰󠁿 Flag for Mirna Peč (SI-170)
🏴󠁳󠁩󠀱󠀵󠀹󠁿 Flag for Hajdina (SI-159)
🏴󠁳󠁩󠀱󠀴󠀱󠁿 Flag for Vuzenica (SI-141)
🏴󠁳󠁩󠀱󠀳󠀵󠁿 Flag for Videm (SI-135)
🏴󠁳󠁩󠀱󠀳󠀴󠁿 Flag for Velike Lašče (SI-134)
🏴󠁳󠁩󠀱󠀳󠀷󠁿 Flag for Vitanje (SI-137)
🏴󠁳󠁩󠀱󠀵󠀵󠁿 Flag for Dobrna (SI-155)
🏴󠁳󠁩󠀱󠀵󠀶󠁿 Flag for Dobrovnik (SI-156)
🏴󠁳󠁩󠀱󠀵󠀷󠁿 Flag for Dolenjske Toplice (SI-157)
🏴󠁳󠁩󠀱󠀷󠀱󠁿 Flag for Oplotnica (SI-171)
🏴󠁳󠁩󠀱󠀶󠀳󠁿 Flag for Jezersko (SI-163)
🏴󠁳󠁩󠀱󠀶󠀴󠁿 Flag for Komenda (SI-164)
🏴󠁳󠁩󠀱󠀶󠀵󠁿 Flag for Kostel (SI-165)
🏴󠁳󠁩󠀱󠀶󠀶󠁿 Flag for Križevci (SI-166)
🏴󠁳󠁩󠀱󠀶󠀱󠁿 Flag for Hodoš (SI-161)
🏴󠁳󠁩󠀱󠀶󠀸󠁿 Flag for Markovci (SI-168)
🏴󠁳󠁩󠀱󠀳󠀹󠁿 Flag for Vojnik (SI-139)
🏴󠁳󠁩󠀱󠀶󠀲󠁿 Flag for Horjul (SI-162)
🏴󠁳󠁩󠀱󠀵󠀳󠁿 Flag for Cerkvenjak (SI-153)
🏴󠁳󠁩󠀱󠀳󠀸󠁿 Flag for Vodice (SI-138)
🏴󠁳󠁩󠀱󠀳󠀶󠁿 Flag for Vipava (SI-136)
🏴󠁳󠁩󠀱󠀴󠀴󠁿 Flag for Zreče (SI-144)
🏴󠁳󠁩󠀱󠀵󠀲󠁿 Flag for Cankova (SI-152)
🏴󠁳󠁩󠀱󠀴󠀶󠁿 Flag for Železniki (SI-146)
🏴󠁳󠁩󠀱󠀶󠀰󠁿 Flag for Hoče–Slivnica (SI-160)
🏴󠁳󠁩󠀱󠀴󠀷󠁿 Flag for Žiri (SI-147)
🏴󠁳󠁩󠀱󠀵󠀰󠁿 Flag for Bloke (SI-150)
🏴󠁳󠁩󠀱󠀴󠀸󠁿 Flag for Benedikt (SI-148)
🏴󠁳󠁩󠀱󠀷󠀲󠁿 Flag for Podlehnik (SI-172)
🏴󠁳󠁩󠀱󠀷󠀴󠁿 Flag for Prebold (SI-174)
🏴󠁳󠁩󠀱󠀸󠀶󠁿 Flag for Trzin (SI-186)
🏴󠁳󠁩󠀱󠀸󠀸󠁿 Flag for Veržej (SI-188)
🏴󠁳󠁩󠀱󠀹󠀰󠁿 Flag for Žalec (SI-190)
🏴󠁳󠁩󠀱󠀸󠀰󠁿 Flag for Solčava (SI-180)
🏴󠁳󠁩󠀱󠀸󠀳󠁿 Flag for Šempeter–Vrtojba (SI-183)
🏴󠁳󠁩󠀲󠀰󠀵󠁿 Flag for Sveti Tomaž (SI-205)
🏴󠁳󠁩󠀱󠀷󠀹󠁿 Flag for Sodražica (SI-179)
🏴󠁳󠁩󠀱󠀹󠀸󠁿 Flag for Makole (SI-198)
🏴󠁳󠁩󠀱󠀹󠀳󠁿 Flag for Žužemberk (SI-193)
🏴󠁳󠁩󠀱󠀹󠀷󠁿 Flag for Kostanjevica na Krki (SI-197)
⛻ Japanese Bank Symbol
🏴󠁳󠁩󠀱󠀹󠀴󠁿 Flag for Šmartno pri Litiji (SI-194)
🏴󠁳󠁩󠀱󠀹󠀱󠁿 Flag for Žetale (SI-191)
🏴󠁳󠁩󠀱󠀸󠀹󠁿 Flag for Vransko (SI-189)
🏴󠁳󠁩󠀲󠀰󠀱󠁿 Flag for Renče–Vogrsko (SI-201)
🏴󠁳󠁩󠀱󠀷󠀶󠁿 Flag for Razkrižje (SI-176)
🏴󠁳󠁩󠀱󠀸󠀱󠁿 Flag for Sveta Ana (SI-181)
🏴󠁳󠁩󠀱󠀷󠀵󠁿 Flag for Prevalje (SI-175)
🏴󠁳󠁩󠀲󠀰󠀷󠁿 Flag for Gorje (SI-207)
❥ Rotated Heavy Black Heart Bullet
🏴󠁳󠁩󠀱󠀸󠀴󠁿 Flag for Tabor (SI-184)
🏴󠁭󠁹󠀱󠀳󠁿 Flag for Sarawak (MY-13)
🏴󠁳󠁩󠀱󠀷󠀳󠁿 Flag for Polzela (SI-173)
🏴󠁳󠁩󠀱󠀷󠀸󠁿 Flag for Selnica ob Dravi (SI-178)
🏴󠁳󠁩󠀲󠀰󠀰󠁿 Flag for Poljčane (SI-200)
🏴󠁳󠁩󠀱󠀹󠀹󠁿 Flag for Mokronog–Trebelno (SI-199)
🏴󠁳󠁩󠀱󠀸󠀵󠁿 Flag for Trnovska Vas (SI-185)
🏴󠁳󠁩󠀱󠀷󠀷󠁿 Flag for Ribnica na Pohorju (SI-177)
🏴󠁳󠁩󠀲󠀰󠀳󠁿 Flag for Straža (SI-203)
🏴󠁭󠁣󠁶󠁲󠁿 Flag for Vallon de la Rousse (MC-VR)
🏴󠁳󠁩󠀱󠀹󠀵󠁿 Flag for Apače (SI-195)
🏴󠁳󠁩󠀱󠀹󠀶󠁿 Flag for Cirkulane (SI-196)
🏴󠁳󠁭󠀰󠀹󠁿 Flag for Serravalle (SM-09)
🏴󠁳󠁩󠀲󠀰󠀹󠁿 Flag for Rečica ob Savinji (SI-209)
🏴󠁳󠁮󠁴󠁣󠁿 Flag for Tambacounda (SN-TC)
🏴󠁳󠁮󠁫󠁡󠁿 Flag for Kaffrine (SN-KA)
🏴󠁧󠁲󠁧󠁿 Flag for West Greece (GR-G)
🏴󠁳󠁩󠀲󠀱󠀱󠁿 Flag for Šentrupert (SI-211)
🏴󠁳󠁫󠁺󠁩󠁿 Flag for Žilina (SK-ZI)
🏴󠁳󠁭󠀰󠀵󠁿 Flag for Fiorentino (SM-05)
🏴󠁳󠁬󠁷󠁿 Flag for Western Area (SL-W)
🏴󠁳󠁮󠁴󠁨󠁿 Flag for Thiès (SN-TH)
🏴󠁳󠁫󠁴󠁣󠁿 Flag for Trenčín (SK-TC)
🏴󠁳󠁩󠀲󠀱󠀲󠁿 Flag for Mirna (SI-212)
🏴󠁲󠁯󠁶󠁬󠁿 Flag for Vâlcea (RO-VL)
🏴󠁳󠁫󠁫󠁩󠁿 Flag for Košice (SK-KI)
🏴󠁳󠁮󠁳󠁥󠁿 Flag for Sédhiou (SN-SE)
🏴󠁳󠁬󠁮󠁿 Flag for Northern (SL-N)
🏴󠁳󠁭󠀰󠀳󠁿 Flag for Domagnano (SM-03)
🏴󠁳󠁭󠀰󠀲󠁿 Flag for Chiesanuova (SM-02)
🏴󠁩󠁮󠁲󠁪󠁿 Flag for Rajasthan (IN-RJ)
🏴󠁳󠁮󠁦󠁫󠁿 Flag for Fatick (SN-FK)
🏴󠁳󠁭󠀰󠀸󠁿 Flag for Montegiardino (SM-08)
🏴󠁳󠁭󠀰󠀶󠁿 Flag for Borgo Maggiore (SM-06)
🏴󠁳󠁮󠁫󠁤󠁿 Flag for Kolda (SN-KD)
🏴󠁳󠁮󠁭󠁴󠁿 Flag for Matam (SN-MT)
🏴󠁳󠁮󠁤󠁢󠁿 Flag for Diourbel (SN-DB)
🏴󠁳󠁬󠁳󠁿 Flag for Southern (SL-S)
🏴󠁳󠁮󠁫󠁥󠁿 Flag for Kédougou (SN-KE)
󠀿 Tag Question Mark
🏴󠁳󠁫󠁢󠁣󠁿 Flag for Banská Bystrica (SK-BC)
🏴󠁳󠁮󠁬󠁧󠁿 Flag for Louga (SN-LG)
🏴󠁳󠁭󠀰󠀴󠁿 Flag for Faetano (SM-04)
🏴󠁳󠁭󠀰󠀱󠁿 Flag for Acquaviva (SM-01)
🏴󠁳󠁮󠁫󠁬󠁿 Flag for Kaolack (SN-KL)
🏴󠁳󠁫󠁰󠁶󠁿 Flag for Prešov (SK-PV)
🏴󠁳󠁫󠁮󠁩󠁿 Flag for Nitra (SK-NI)
🏴󠁩󠁴󠀷󠀸󠁿 Flag for Calabria (IT-78)
🏴󠁫󠁲󠀱󠀱󠁿 Flag for Seoul (KR-11)
🏴󠁳󠁭󠀰󠀷󠁿 Flag for San Marino (SM-07)
🏴󠁳󠁫󠁴󠁡󠁿 Flag for Trnava (SK-TA)
🏴󠁳󠁲󠁢󠁲󠁿 Flag for Brokopondo (SR-BR)
🏴󠁳󠁯󠁭󠁵󠁿 Flag for Mudug (SO-MU)
🏴󠁳󠁲󠁳󠁡󠁿 Flag for Saramacca (SR-SA)
🏴󠁳󠁯󠁧󠁡󠁿 Flag for Galguduud (SO-GA)
🏴󠁳󠁳󠁢󠁷󠁿 Flag for Western Bahr el Ghazal (SS-BW)
🏴󠁳󠁲󠁳󠁩󠁿 Flag for Sipaliwini (SR-SI)
🏴󠁳󠁲󠁭󠁡󠁿 Flag for Marowijne (SR-MA)
🏴󠁳󠁯󠁷󠁯󠁿 Flag for Woqooyi Galbeed (SO-WO)
🏴󠁳󠁯󠁴󠁯󠁿 Flag for Togdheer (SO-TO)
🏴󠁳󠁯󠁢󠁲󠁿 Flag for Bari (SO-BR)
🏴󠁳󠁳󠁥󠁷󠁿 Flag for Western Equatoria (SS-EW)
🏴󠁳󠁲󠁰󠁲󠁿 Flag for Para (SR-PR)
🏴󠁳󠁳󠁥󠁥󠁿 Flag for Eastern Equatoria (SS-EE)
🏴󠁳󠁲󠁰󠁭󠁿 Flag for Paramaribo (SR-PM)
🏴󠁳󠁳󠁮󠁵󠁿 Flag for Upper Nile (SS-NU)
🏴󠁳󠁮󠁺󠁧󠁿 Flag for Ziguinchor (SN-ZG)
🏴󠁳󠁯󠁨󠁩󠁿 Flag for Hiran (SO-HI)
🏴󠁳󠁲󠁷󠁡󠁿 Flag for Wanica (SR-WA)
🏴󠁳󠁴󠁰󠁿 Flag for Príncipe (ST-P)
🏴󠁳󠁲󠁣󠁲󠁿 Flag for Coronie (SR-CR)
🏴󠁳󠁯󠁪󠁤󠁿 Flag for Middle Juba (SO-JD)
󠀬 Tag Comma
🏴󠁳󠁯󠁧󠁥󠁿 Flag for Gedo (SO-GE)
🏴󠁳󠁲󠁣󠁭󠁿 Flag for Commewijne (SR-CM)
🏴󠁭󠁮󠀰󠀶󠀴󠁿 Flag for Govisümber (MN-064)
🏴󠁳󠁯󠁳󠁡󠁿 Flag for Sanaag (SO-SA)
🏴󠁳󠁳󠁷󠁲󠁿 Flag for Warrap (SS-WR)
🏴󠁳󠁯󠁡󠁷󠁿 Flag for Awdal (SO-AW)
🏴󠁳󠁯󠁪󠁨󠁿 Flag for Lower Juba (SO-JH)
🏴󠁳󠁯󠁮󠁵󠁿 Flag for Nugal (SO-NU)
🏴󠁳󠁯󠁳󠁤󠁿 Flag for Middle Shebelle (SO-SD)
🏴󠁳󠁲󠁮󠁩󠁿 Flag for Nickerie (SR-NI)
🏴󠁳󠁯󠁳󠁨󠁿 Flag for Lower Shebelle (SO-SH)
🏴󠁳󠁯󠁢󠁫󠁿 Flag for Bakool (SO-BK)
🏴󠁳󠁶󠁣󠁨󠁿 Flag for Chalatenango (SV-CH)
🏴󠁳󠁶󠁣󠁵󠁿 Flag for Cuscatlán (SV-CU)
🏴󠁳󠁺󠁳󠁨󠁿 Flag for Shiselweni (SZ-SH)
🏴󠁳󠁶󠁳󠁯󠁿 Flag for Sonsonate (SV-SO)
🏴󠁳󠁶󠁣󠁡󠁿 Flag for Cabañas (SV-CA)
🖒 Reversed Thumbs Up Sign
🏴󠁳󠁶󠁰󠁡󠁿 Flag for La Paz (SV-PA)
🏴󠁳󠁹󠁨󠁭󠁿 Flag for Hama (SY-HM)
🏴󠁳󠁹󠁩󠁤󠁿 Flag for Idlib (SY-ID)
🏴󠁳󠁺󠁬󠁵󠁿 Flag for Lubombo (SZ-LU)
🏴󠁴󠁤󠁥󠁯󠁿 Flag for Ennedi-Ouest (TD-EO)
🏴󠁳󠁶󠁡󠁨󠁿 Flag for Ahuachapán (SV-AH)
🏴󠁳󠁹󠁴󠁡󠁿 Flag for Tartus (SY-TA)
🏴󠁳󠁹󠁨󠁩󠁿 Flag for Homs (SY-HI)
🏴󠁳󠁺󠁭󠁡󠁿 Flag for Manzini (SZ-MA)
🏴󠁳󠁶󠁵󠁮󠁿 Flag for La Unión (SV-UN)
🏴󠁴󠁤󠁥󠁥󠁿 Flag for Ennedi-Est (TD-EE)
🏴󠁴󠁤󠁢󠁯󠁿 Flag for Borkou (TD-BO)
🏴󠁴󠁤󠁢󠁡󠁿 Flag for Batha (TD-BA)
🏴󠁳󠁹󠁤󠁩󠁿 Flag for Damascus (SY-DI)
🏴󠁳󠁹󠁳󠁵󠁿 Flag for As-Suwayda (SY-SU)
🏴󠁴󠁤󠁫󠁡󠁿 Flag for Kanem (TD-KA)
🏴󠁳󠁹󠁨󠁡󠁿 Flag for Al-Hasakah (SY-HA)
🏴󠁳󠁹󠁨󠁬󠁿 Flag for Aleppo (SY-HL)
🏴󠁳󠁶󠁬󠁩󠁿 Flag for La Libertad (SV-LI)
🏴󠁳󠁶󠁭󠁯󠁿 Flag for Morazán (SV-MO)
🏴󠁴󠁤󠁧󠁲󠁿 Flag for Guéra (TD-GR)
🏴󠁳󠁹󠁱󠁵󠁿 Flag for Quneitra (SY-QU)
🏴󠁴󠁤󠁣󠁢󠁿 Flag for Chari-Baguirmi (TD-CB)
🏴󠁳󠁹󠁤󠁲󠁿 Flag for Daraa (SY-DR)
🏴󠁴󠁤󠁢󠁧󠁿 Flag for Bahr el Gazel (TD-BG)
🏴󠁳󠁺󠁨󠁨󠁿 Flag for Hhohho (SZ-HH)
🏴󠁳󠁶󠁳󠁡󠁿 Flag for Santa Ana (SV-SA)
🏴󠁳󠁹󠁲󠁡󠁿 Flag for Ar-Raqqah (SY-RA)
🏴󠁳󠁹󠁲󠁤󠁿 Flag for Rif Dimashq (SY-RD)
🏴󠁳󠁹󠁬󠁡󠁿 Flag for Latakia (SY-LA)
🏴󠁴󠁨󠀱󠀴󠁿 Flag for Phra Nakhon Si Ayutthaya (TH-14)
󠁌 Tag Latin Capital Letter L
🏴󠁴󠁨󠀱󠀰󠁿 Flag for Bangkok (TH-10)
🏴󠁴󠁤󠁴󠁩󠁿 Flag for Tibesti (TD-TI)
🏴󠁴󠁤󠁬󠁣󠁿 Flag for Lac (TD-LC)
🏴󠁴󠁧󠁳󠁿 Flag for Savanes (TG-S)
🏴󠁴󠁨󠀲󠀶󠁿 Flag for Nakhon Nayok (TH-26)
🏴󠁴󠁤󠁮󠁤󠁿 Flag for N’Djamena (TD-ND)
󠁄 Tag Latin Capital Letter D
🏴󠁴󠁤󠁭󠁣󠁿 Flag for Moyen-Chari (TD-MC)
🏴󠁴󠁨󠀲󠀰󠁿 Flag for Chon Buri (TH-20)
🏴󠁴󠁤󠁭󠁯󠁿 Flag for Mayo-Kebbi Ouest (TD-MO)
🏴󠁴󠁧󠁣󠁿 Flag for Centrale (TG-C)
🏴󠁴󠁨󠀳󠀱󠁿 Flag for Buri Ram (TH-31)
🏴󠁴󠁤󠁴󠁡󠁿 Flag for Tandjilé (TD-TA)
🏴󠁴󠁤󠁯󠁤󠁿 Flag for Ouaddaï (TD-OD)
🏴󠁴󠁨󠀳󠀲󠁿 Flag for Surin (TH-32)
🏴󠁴󠁤󠁳󠁡󠁿 Flag for Salamat (TD-SA)
🏴󠁴󠁤󠁳󠁩󠁿 Flag for Sila (TD-SI)
🏴󠁴󠁧󠁰󠁿 Flag for Plateaux (TG-P)
🏴󠁴󠁤󠁬󠁯󠁿 Flag for Logone Occidental (TD-LO)
🏴󠁴󠁤󠁬󠁲󠁿 Flag for Logone Oriental (TD-LR)
🏴󠁴󠁨󠀱󠀷󠁿 Flag for Sing Buri (TH-17)
🏴󠁴󠁨󠀳󠀰󠁿 Flag for Nakhon Ratchasima (TH-30)
🏴󠁴󠁨󠀱󠀸󠁿 Flag for Chai Nat (TH-18)
🏴󠁴󠁨󠀲󠀴󠁿 Flag for Chachoengsao (TH-24)
🏴󠁴󠁤󠁭󠁡󠁿 Flag for Mandoul (TD-MA)
🏴󠁴󠁨󠀱󠀵󠁿 Flag for Ang Thong (TH-15)
🏴󠁴󠁤󠁷󠁦󠁿 Flag for Wadi Fira (TD-WF)
🏴󠁴󠁨󠀱󠀹󠁿 Flag for Saraburi (TH-19)
🏴󠁴󠁨󠀱󠀱󠁿 Flag for Samut Prakan (TH-11)
🏴󠁴󠁨󠀲󠀱󠁿 Flag for Rayong (TH-21)
🏴󠁴󠁨󠀲󠀲󠁿 Flag for Chanthaburi (TH-22)
🏴󠁴󠁨󠀱󠀳󠁿 Flag for Pathum Thani (TH-13)
🏴󠁴󠁨󠀲󠀵󠁿 Flag for Prachin Buri (TH-25)
🏴󠁴󠁨󠀲󠀷󠁿 Flag for Sa Kaeo (TH-27)
🏴󠁴󠁤󠁭󠁥󠁿 Flag for Mayo-Kebbi Est (TD-ME)
🏴󠁴󠁨󠀱󠀲󠁿 Flag for Nonthaburi (TH-12)
🏴󠁴󠁨󠀵󠀵󠁿 Flag for Nan (TH-55)
🏴󠁴󠁨󠀳󠀴󠁿 Flag for Ubon Ratchathani (TH-34)
🏴󠁴󠁨󠀷󠀲󠁿 Flag for Suphanburi (TH-72)
🏴󠁴󠁨󠀶󠀰󠁿 Flag for Nakhon Sawan (TH-60)
🏴󠁴󠁨󠀶󠀷󠁿 Flag for Phetchabun (TH-67)
🏴󠁴󠁨󠀷󠀱󠁿 Flag for Kanchanaburi (TH-71)
🏴󠁴󠁨󠀵󠀴󠁿 Flag for Phrae (TH-54)
🏴󠁴󠁨󠀶󠀳󠁿 Flag for Tak (TH-63)
🏴󠁴󠁨󠀶󠀴󠁿 Flag for Sukhothai (TH-64)
🏴󠁴󠁨󠀵󠀸󠁿 Flag for Mae Hong Son (TH-58)
🏴󠁴󠁨󠀴󠀸󠁿 Flag for Nakhon Phanom (TH-48)
🏴󠁴󠁨󠀵󠀱󠁿 Flag for Lamphun (TH-51)
🏴󠁴󠁨󠀳󠀹󠁿 Flag for Nong Bua Lam Phu (TH-39)
🏴󠁴󠁨󠀵󠀶󠁿 Flag for Phayao (TH-56)
🏴󠁴󠁨󠀶󠀲󠁿 Flag for Kamphaeng Phet (TH-62)
🏴󠁴󠁨󠀴󠀵󠁿 Flag for Roi Et (TH-45)
🏴󠁴󠁨󠀵󠀷󠁿 Flag for Chiang Rai (TH-57)
🏴󠁴󠁨󠀴󠀴󠁿 Flag for Maha Sarakham (TH-44)
🏴󠁴󠁨󠀴󠀰󠁿 Flag for Khon Kaen (TH-40)
🏴󠁴󠁨󠀷󠀳󠁿 Flag for Nakhon Pathom (TH-73)
🏴󠁴󠁨󠀷󠀰󠁿 Flag for Ratchaburi (TH-70)
🏴󠁴󠁨󠀴󠀱󠁿 Flag for Udon Thani (TH-41)
🏴󠁴󠁨󠀳󠀵󠁿 Flag for Yasothon (TH-35)
🏴󠁴󠁨󠀳󠀷󠁿 Flag for Amnat Charoen (TH-37)
🏴󠁴󠁨󠀷󠀴󠁿 Flag for Samut Sakhon (TH-74)
🏴󠁴󠁨󠀶󠀱󠁿 Flag for Uthai Thani (TH-61)
🏴󠁴󠁨󠀴󠀳󠁿 Flag for Nong Khai (TH-43)
🏴󠁴󠁨󠀴󠀶󠁿 Flag for Kalasin (TH-46)
🏴󠁴󠁨󠀴󠀲󠁿 Flag for Loei (TH-42)
🏴󠁴󠁨󠀵󠀲󠁿 Flag for Lampang (TH-52)
🏴󠁴󠁨󠀴󠀹󠁿 Flag for Mukdahan (TH-49)
🏴󠁴󠁨󠀳󠀸󠁿 Flag for Bueng Kan (TH-38)
🏴󠁴󠁨󠀳󠀳󠁿 Flag for Si Sa Ket (TH-33)
🏴󠁴󠁨󠀵󠀳󠁿 Flag for Uttaradit (TH-53)
🏴󠁴󠁨󠀴󠀷󠁿 Flag for Sakon Nakhon (TH-47)
🏴󠁴󠁨󠀶󠀶󠁿 Flag for Phichit (TH-66)
🏴󠁴󠁨󠀵󠀰󠁿 Flag for Chiang Mai (TH-50)
🏴󠁴󠁨󠀶󠀵󠁿 Flag for Phitsanulok (TH-65)
🏴󠁴󠁪󠁳󠁵󠁿 Flag for Sughd (TJ-SU)
🏴󠁴󠁨󠀸󠀴󠁿 Flag for Surat Thani (TH-84)
🏴󠁡󠁦󠁳󠁡󠁲󠁿 Flag for Sar-e Pol (AF-SAR)
🏴󠁴󠁬󠁬󠁩󠁿 Flag for Liquiçá (TL-LI)
🏴󠁴󠁨󠀹󠀱󠁿 Flag for Satun (TH-91)
🀠 Mahjong Tile Eight of Circles
🏴󠁴󠁬󠁭󠁴󠁿 Flag for Manatuto (TL-MT)
🏴󠁴󠁪󠁫󠁴󠁿 Flag for Khatlon (TJ-KT)
🏴󠁴󠁬󠁡󠁮󠁿 Flag for Ainaro (TL-AN)
🏴󠁪󠁰󠀳󠀴󠁿 Flag for Hiroshima (JP-34)
🏴󠁴󠁭󠁤󠁿 Flag for Daşoguz (TM-D)
🏴󠁴󠁨󠀷󠀷󠁿 Flag for Prachuap Khiri Khan (TH-77)
🏴󠁴󠁨󠀷󠀶󠁿 Flag for Phetchaburi (TH-76)
🏴󠁴󠁨󠀸󠀲󠁿 Flag for Phang Nga (TH-82)
🏴󠁴󠁨󠀹󠀵󠁿 Flag for Yala (TH-95)
🏴󠁴󠁨󠁳󠁿 Flag for Pattaya (TH-S)
🏴󠁦󠁲󠁬󠁲󠁥󠁿 Flag for La Réunion (FR-LRE)
👨🏽‍👩🏽‍👧🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁴󠁨󠀹󠀲󠁿 Flag for Trang (TH-92)
🏴󠁴󠁨󠀹󠀶󠁿 Flag for Narathiwat (TH-96)
🏴󠁴󠁨󠀸󠀵󠁿 Flag for Ranong (TH-85)
🏴󠁴󠁬󠁢󠁡󠁿 Flag for Baucau (TL-BA)
🏴󠁴󠁬󠁶󠁩󠁿 Flag for Viqueque (TL-VI)
🏴󠁴󠁪󠁤󠁵󠁿 Flag for Dushanbe (TJ-DU)
🏴󠁴󠁬󠁡󠁬󠁿 Flag for Aileu (TL-AL)
🏴󠁴󠁬󠁢󠁯󠁿 Flag for Bobonaro (TL-BO)
🏴󠁴󠁨󠀹󠀴󠁿 Flag for Pattani (TH-94)
🏴󠁴󠁬󠁯󠁥󠁿 Flag for Oecusse (TL-OE)
🏴󠁴󠁨󠀹󠀰󠁿 Flag for Songkhla (TH-90)
🏴󠁴󠁪󠁲󠁡󠁿 Flag for Nohiyahoi Tobei Jumhurí (TJ-RA)
🏴󠁴󠁮󠀳󠀴󠁿 Flag for Siliana (TN-34)
🏴󠁴󠁮󠀳󠀱󠁿 Flag for Béja (TN-31)
🏴󠁬󠁴󠀱󠀶󠁿 Flag for Kaunas (LT-16)
🏴󠁴󠁮󠀸󠀲󠁿 Flag for Medenine (TN-82)
🏴󠁴󠁮󠀶󠀱󠁿 Flag for Sfax (TN-61)
🏴󠁴󠁮󠀸󠀳󠁿 Flag for Tataouine (TN-83)
🏴󠁴󠁯󠀰󠀵󠁿 Flag for Vavaʻu (TO-05)
🏴󠁴󠁯󠀰󠀲󠁿 Flag for Haʻapai (TO-02)
🏴󠁴󠁲󠀱󠀳󠁿 Flag for Bitlis (TR-13)
🏴󠁴󠁮󠀱󠀲󠁿 Flag for Ariana (TN-12)
🏴󠁴󠁮󠀵󠀳󠁿 Flag for Mahdia (TN-53)
🏴󠁴󠁲󠀰󠀷󠁿 Flag for Antalya (TR-07)
🏴󠁴󠁲󠀰󠀹󠁿 Flag for Aydın (TR-09)
🏴󠁴󠁲󠀰󠀴󠁿 Flag for Ağrı (TR-04)
🏴󠁴󠁲󠀰󠀵󠁿 Flag for Amasya (TR-05)
🏴󠁴󠁲󠀱󠀰󠁿 Flag for Balıkesir (TR-10)
🏴󠁴󠁮󠀴󠀲󠁿 Flag for Kasserine (TN-42)
🏴󠁴󠁮󠀵󠀲󠁿 Flag for Monastir (TN-52)
🏴󠁴󠁮󠀸󠀱󠁿 Flag for Gabès (TN-81)
🏴󠁴󠁲󠀱󠀲󠁿 Flag for Bingöl (TR-12)
🏴󠁴󠁲󠀱󠀴󠁿 Flag for Bolu (TR-14)
🏴󠁴󠁯󠀰󠀳󠁿 Flag for Niuas (TO-03)
🏴󠁴󠁮󠀳󠀲󠁿 Flag for Jendouba (TN-32)
🏴󠁴󠁮󠀴󠀱󠁿 Flag for Kairouan (TN-41)
🏴󠁴󠁲󠀰󠀸󠁿 Flag for Artvin (TR-08)
🏴󠁴󠁮󠀵󠀱󠁿 Flag for Sousse (TN-51)
🏴󠁴󠁮󠀳󠀳󠁿 Flag for Kef (TN-33)
🏴󠁮󠁲󠀰󠀹󠁿 Flag for Ewa (NR-09)
🏴󠁴󠁮󠀲󠀲󠁿 Flag for Zaghouan (TN-22)
🏴󠁴󠁮󠀲󠀱󠁿 Flag for Nabeul (TN-21)
🏴󠁴󠁮󠀷󠀲󠁿 Flag for Tozeur (TN-72)
🏴󠁴󠁮󠀱󠀴󠁿 Flag for Manouba (TN-14)
🏴󠁴󠁯󠀰󠀱󠁿 Flag for ʻEua (TO-01)
🏴󠁴󠁲󠀰󠀲󠁿 Flag for Adıyaman (TR-02)
🏴󠁴󠁲󠀱󠀱󠁿 Flag for Bilecik (TR-11)
🏴󠁴󠁮󠀲󠀳󠁿 Flag for Bizerte (TN-23)
🏴󠁴󠁯󠀰󠀴󠁿 Flag for Tongatapu (TO-04)
🏴󠁴󠁮󠀴󠀳󠁿 Flag for Sidi Bouzid (TN-43)
🏴󠁴󠁮󠀷󠀳󠁿 Flag for Kebili (TN-73)
🏴󠁴󠁲󠀴󠀷󠁿 Flag for Mardin (TR-47)
🏴󠁴󠁲󠀵󠀱󠁿 Flag for Niğde (TR-51)
🏴󠁴󠁲󠀲󠀰󠁿 Flag for Denizli (TR-20)
🏴󠁭󠁴󠀴󠀵󠁿 Flag for Victoria (MT-45)
🏴󠁰󠁡󠁮󠁢󠁿 Flag for Ngöbe-Buglé (PA-NB)
🏴󠁴󠁲󠀵󠀳󠁿 Flag for Rize (TR-53)
🏴󠁴󠁲󠀴󠀶󠁿 Flag for Kahramanmaraş (TR-46)
🏴󠁴󠁲󠀴󠀸󠁿 Flag for Muğla (TR-48)
🏴󠁴󠁲󠀵󠀲󠁿 Flag for Ordu (TR-52)
🏴󠁴󠁲󠀱󠀷󠁿 Flag for Çanakkale (TR-17)
🏴󠁴󠁲󠀲󠀷󠁿 Flag for Gaziantep (TR-27)
🏴󠁴󠁲󠀳󠀷󠁿 Flag for Kastamonu (TR-37)
🏴󠁴󠁲󠀱󠀹󠁿 Flag for Çorum (TR-19)
🏴󠁴󠁲󠀲󠀲󠁿 Flag for Edirne (TR-22)
🏴󠁴󠁲󠀲󠀳󠁿 Flag for Elazığ (TR-23)
🏴󠁴󠁲󠀳󠀲󠁿 Flag for Isparta (TR-32)
🏴󠁴󠁲󠀳󠀱󠁿 Flag for Hatay (TR-31)
🏴󠁴󠁲󠀱󠀶󠁿 Flag for Bursa (TR-16)
🏴󠁴󠁲󠀴󠀵󠁿 Flag for Manisa (TR-45)
🏴󠁴󠁲󠀲󠀵󠁿 Flag for Erzurum (TR-25)
🏴󠁴󠁲󠀴󠀴󠁿 Flag for Malatya (TR-44)
🏴󠁴󠁲󠀳󠀰󠁿 Flag for Hakkâri (TR-30)
🏴󠁴󠁲󠀱󠀵󠁿 Flag for Burdur (TR-15)
🏴󠁴󠁲󠀵󠀶󠁿 Flag for Siirt (TR-56)
󠁸 Tag Latin Small Letter X
🏴󠁴󠁲󠀳󠀹󠁿 Flag for Kırklareli (TR-39)
🏴󠁴󠁲󠀴󠀰󠁿 Flag for Kırşehir (TR-40)
🏴󠁴󠁲󠀵󠀴󠁿 Flag for Sakarya (TR-54)
🏴󠁴󠁲󠀲󠀶󠁿 Flag for Eskişehir (TR-26)
🏴󠁴󠁲󠀵󠀵󠁿 Flag for Samsun (TR-55)
🏴󠁴󠁲󠀲󠀱󠁿 Flag for Diyarbakır (TR-21)
🏴󠁴󠁲󠀳󠀳󠁿 Flag for Mersin (TR-33)
🏴󠁴󠁲󠀱󠀸󠁿 Flag for Çankırı (TR-18)
🏴󠁴󠁲󠀷󠀱󠁿 Flag for Kırıkkale (TR-71)
🏴󠁴󠁴󠁴󠁵󠁰󠁿 Flag for Tunapuna-Piarco (TT-TUP)
🏴󠁴󠁲󠀶󠀲󠁿 Flag for Tunceli (TR-62)
🏴󠁴󠁴󠁰󠁴󠁦󠁿 Flag for Point Fortin (TT-PTF)
🏴󠁴󠁲󠀶󠀸󠁿 Flag for Aksaray (TR-68)
🏴󠁴󠁲󠀷󠀷󠁿 Flag for Yalova (TR-77)
🏴󠁴󠁴󠁣󠁨󠁡󠁿 Flag for Chaguanas (TT-CHA)
🏴󠁴󠁴󠁳󠁪󠁬󠁿 Flag for San Juan-Laventille (TT-SJL)
🏴󠁴󠁴󠁳󠁦󠁯󠁿 Flag for San Fernando (TT-SFO)
🏴󠁴󠁴󠁡󠁲󠁩󠁿 Flag for Arima (TT-ARI)
🏴󠁴󠁲󠀷󠀹󠁿 Flag for Kilis (TR-79)
🏴󠁴󠁲󠀷󠀶󠁿 Flag for Iğdır (TR-76)
🏴󠁴󠁴󠁴󠁯󠁢󠁿 Flag for Tobago (TT-TOB)
🏴󠁴󠁲󠀶󠀹󠁿 Flag for Bayburt (TR-69)
🏴󠁴󠁲󠀷󠀸󠁿 Flag for Karabük (TR-78)
🏴󠁬󠁲󠁣󠁭󠁿 Flag for Grand Cape Mount (LR-CM)
🏴󠁴󠁲󠀲󠀴󠁿 Flag for Erzincan (TR-24)
🏴󠁴󠁴󠁰󠁲󠁴󠁿 Flag for Princes Town (TT-PRT)
🏴󠁴󠁲󠀶󠀵󠁿 Flag for Van (TR-65)
🏴󠁴󠁲󠀵󠀷󠁿 Flag for Sinop (TR-57)
🏴󠁴󠁲󠀶󠀶󠁿 Flag for Yozgat (TR-66)
🏴󠁴󠁲󠀷󠀵󠁿 Flag for Ardahan (TR-75)
🏴󠁴󠁲󠀷󠀴󠁿 Flag for Bartın (TR-74)
🏴󠁴󠁴󠁭󠁲󠁣󠁿 Flag for Mayaro-Rio Claro (TT-MRC)
🏴󠁴󠁲󠀶󠀴󠁿 Flag for Uşak (TR-64)
🏴󠁴󠁲󠀶󠀷󠁿 Flag for Zonguldak (TR-67)
🏴󠁴󠁴󠁤󠁭󠁮󠁿 Flag for Diego Martin (TT-DMN)
🏴󠁴󠁲󠀵󠀸󠁿 Flag for Sivas (TR-58)
🏴󠁴󠁴󠁣󠁴󠁴󠁿 Flag for Couva-Tabaquite-Talparo (TT-CTT)
🏴󠁴󠁴󠁳󠁩󠁰󠁿 Flag for Siparia (TT-SIP)
🏴󠁴󠁴󠁰󠁥󠁤󠁿 Flag for Penal-Debe (TT-PED)
🏴󠁴󠁲󠀷󠀰󠁿 Flag for Karaman (TR-70)
🏴󠁴󠁲󠀵󠀹󠁿 Flag for Tekirdağ (TR-59)
🏴󠁴󠁲󠀷󠀳󠁿 Flag for Şırnak (TR-73)
🏴󠁴󠁲󠀶󠀳󠁿 Flag for Şanlıurfa (TR-63)
🏴󠁴󠁲󠀶󠀰󠁿 Flag for Tokat (TR-60)
👨🏼‍👩🏼‍👦🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁴󠁺󠀰󠀵󠁿 Flag for Kagera (TZ-05)
🏴󠁴󠁷󠁴󠁮󠁮󠁿 Flag for Tainan (TW-TNN)
🏴󠁴󠁷󠁣󠁹󠁩󠁿 Flag for Chiayi County (TW-CYI)
🏴󠁴󠁷󠁰󠁩󠁦󠁿 Flag for Pingtung (TW-PIF)
🏴󠁴󠁷󠁮󠁷󠁴󠁿 Flag for New Taipei (TW-NWT)
🏴󠁴󠁷󠁩󠁬󠁡󠁿 Flag for Yilan (TW-ILA)
🏴󠁴󠁲󠀴󠀹󠁿 Flag for Muş (TR-49)
🏴󠁴󠁷󠁴󠁡󠁯󠁿 Flag for Taoyuan (TW-TAO)
🏴󠁡󠁧󠀰󠀳󠁿 Flag for Saint George (AG-03)
🏴󠁴󠁺󠀰󠀹󠁿 Flag for Kilimanjaro (TZ-09)
🏴󠁴󠁷󠁴󠁸󠁧󠁿 Flag for Taichung (TW-TXG)
🏴󠁴󠁶󠁮󠁫󠁦󠁿 Flag for Nukufetau (TV-NKF)
🏴󠁴󠁺󠀰󠀳󠁿 Flag for Dodoma (TZ-03)
🏴󠁴󠁷󠁫󠁩󠁮󠁿 Flag for Kinmen (TW-KIN)
🏴󠁴󠁺󠀰󠀶󠁿 Flag for North Pemba (TZ-06)
🏴󠁴󠁺󠀰󠀸󠁿 Flag for Kigoma (TZ-08)
👨🏻‍👶🏻‍👧🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
🏴󠁴󠁺󠀰󠀴󠁿 Flag for Iringa (TZ-04)
🏴󠁭󠁴󠀵󠀲󠁿 Flag for Sannat (MT-52)
🏴󠁴󠁷󠁬󠁩󠁥󠁿 Flag for Lienchiang (TW-LIE)
🏴󠁴󠁶󠁮󠁭󠁡󠁿 Flag for Nanumea (TV-NMA)
🏴󠁴󠁷󠁭󠁩󠁡󠁿 Flag for Miaoli (TW-MIA)
🏴󠁴󠁶󠁶󠁡󠁩󠁿 Flag for Vaitupu (TV-VAI)
🏴󠁴󠁷󠁹󠁵󠁮󠁿 Flag for Yunlin (TW-YUN)
🏴󠁴󠁷󠁴󠁴󠁴󠁿 Flag for Taitung (TW-TTT)
🏴󠁴󠁷󠁨󠁵󠁡󠁿 Flag for Hualien (TW-HUA)
🏴󠁴󠁷󠁣󠁹󠁱󠁿 Flag for Chiayi (TW-CYQ)
👨🏾‍👩🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁴󠁶󠁮󠁵󠁩󠁿 Flag for Nui (TV-NUI)
🏴󠁴󠁷󠁫󠁥󠁥󠁿 Flag for Keelung (TW-KEE)
🏴󠁴󠁺󠀰󠀱󠁿 Flag for Arusha (TZ-01)
🏴󠁲󠁯󠁣󠁳󠁿 Flag for Caraș-Severin (RO-CS)
🏴󠁴󠁺󠀱󠀳󠁿 Flag for Mara (TZ-13)
🏴󠁴󠁺󠀱󠀰󠁿 Flag for South Pemba (TZ-10)
🏴󠁴󠁺󠀲󠀶󠁿 Flag for Manyara (TZ-26)
🏴󠁴󠁺󠀱󠀹󠁿 Flag for Pwani (TZ-19)
🏴󠁵󠁡󠀰󠀷󠁿 Flag for Volyn (UA-07)
🏴󠁴󠁺󠀲󠀰󠁿 Flag for Rukwa (TZ-20)
🏴󠁵󠁡󠀰󠀹󠁿 Flag for Luhanshchyna (UA-09)
🏴󠁴󠁺󠀲󠀲󠁿 Flag for Shinyanga (TZ-22)
🏴󠁴󠁺󠀲󠀱󠁿 Flag for Ruvuma (TZ-21)
🏴󠁵󠁡󠀴󠀸󠁿 Flag for Mykolayivschyna (UA-48)
🏴󠁵󠁡󠀲󠀳󠁿 Flag for Zaporizhzhya (UA-23)
🏴󠁵󠁡󠀲󠀱󠁿 Flag for Zakarpattia (UA-21)
🏴󠁴󠁺󠀱󠀴󠁿 Flag for Mbeya (TZ-14)
🏴󠁴󠁺󠀲󠀳󠁿 Flag for Singida (TZ-23)
🏴󠁴󠁺󠀲󠀴󠁿 Flag for Tabora (TZ-24)
🏴󠁴󠁺󠀱󠀲󠁿 Flag for Lindi (TZ-12)
🏴󠁴󠁺󠀱󠀷󠁿 Flag for Mtwara (TZ-17)
🏴󠁴󠁺󠀳󠀰󠁿 Flag for Simiyu (TZ-30)
🏴󠁵󠁡󠀵󠀶󠁿 Flag for Rivnenshchyna (UA-56)
🕲 No Piracy
🏴󠁵󠁡󠀵󠀳󠁿 Flag for Poltavshchyna (UA-53)
🏴󠁵󠁡󠀴󠀰󠁿 Flag for Sevastopol (UA-40)
🏴󠁤󠁭󠀰󠀴󠁿 Flag for Saint George (DM-04)
🏴󠁫󠁭󠁭󠁿 Flag for Mohéli (KM-M)
🏴󠁴󠁺󠀱󠀸󠁿 Flag for Mwanza (TZ-18)
🏴󠁫󠁺󠁢󠁡󠁹󠁿 Flag for Bayqongyr (KZ-BAY)
🏴󠁴󠁷󠁣󠁨󠁡󠁿 Flag for Changhua (TW-CHA)
🏴󠁧󠁷󠁮󠁿 Flag for Norte (GW-N)
🏴󠁵󠁡󠀰󠀵󠁿 Flag for Vinnychchyna (UA-05)
🏴󠁵󠁡󠀵󠀱󠁿 Flag for Odeshchyna (UA-51)
🏴󠁴󠁺󠀲󠀸󠁿 Flag for Katavi (TZ-28)
🏴󠁵󠁡󠀳󠀲󠁿 Flag for Kyivshchyna (UA-32)
🏴󠁴󠁺󠀱󠀵󠁿 Flag for Zanzibar Urban/West (TZ-15)
🏴󠁭󠁮󠀰󠀴󠀹󠁿 Flag for Selenge (MN-049)
🏴󠁴󠁺󠀲󠀹󠁿 Flag for Njombe (TZ-29)
🏴󠁴󠁺󠀲󠀷󠁿 Flag for Geita (TZ-27)
🏴󠁳󠁧󠀰󠀱󠁿 Flag for Central Singapore (SG-01)
🏴󠁵󠁭󠀹󠀵󠁿 Flag for Palmyra Atoll (UM-95)
🏴󠁵󠁡󠀶󠀵󠁿 Flag for Khersonshchyna (UA-65)
🏴󠁭󠁹󠀰󠀳󠁿 Flag for Kelantan (MY-03)
🏴󠁵󠁡󠀷󠀴󠁿 Flag for Chernihivshchyna (UA-74)
🏴󠁵󠁡󠀷󠀱󠁿 Flag for Cherkashchyna (UA-71)
🏴󠁵󠁭󠀸󠀱󠁿 Flag for Baker Island (UM-81)
🏴󠁲󠁵󠁫󠁧󠁤󠁿 Flag for Kaliningrad (RU-KGD)
🏴󠁵󠁡󠀶󠀱󠁿 Flag for Ternopilshchyna (UA-61)
🏴󠁵󠁭󠀷󠀱󠁿 Flag for Midway Atoll (UM-71)
🏴󠁬󠁶󠁲󠁩󠁸󠁿 Flag for Riga (LV-RIX)
🏴󠁵󠁡󠀵󠀹󠁿 Flag for Sumshchyna (UA-59)
🏴󠁵󠁳󠁣󠁴󠁿 Flag for Connecticut (US-CT)
️ Variation Selector-16
🏴󠁵󠁧󠁥󠁿 Flag for Eastern (UG-E)
🏴󠁵󠁭󠀸󠀴󠁿 Flag for Howland Island (UM-84)
🏴󠁩󠁮󠁰󠁢󠁿 Flag for Punjab (IN-PB)
🏴󠁵󠁭󠀶󠀷󠁿 Flag for Johnston Atoll (UM-67)
🏴󠁵󠁧󠁷󠁿 Flag for Western (UG-W)
🏴󠁩󠁥󠁵󠁿 Flag for Ulster (IE-U)
🏴󠁵󠁡󠀶󠀳󠁿 Flag for Kharkivshchyna (UA-63)
🏴󠁵󠁡󠀷󠀷󠁿 Flag for Chernivtsi Oblast (UA-77)
🏴󠁵󠁳󠁦󠁬󠁿 Flag for Florida (US-FL)
🏴󠁵󠁡󠀶󠀸󠁿 Flag for Khmelnychchyna (UA-68)
🏴󠁲󠁵󠁩󠁮󠁿 Flag for Ingushetia (RU-IN)
🏴󠁵󠁧󠁮󠁿 Flag for Northern (UG-N)
🏴󠁵󠁳󠁩󠁡󠁿 Flag for Iowa (US-IA)
♹ Recycling Symbol for Type-7 Plastics
🏴󠁵󠁭󠀷󠀹󠁿 Flag for Wake Island (UM-79)
🏴󠁵󠁳󠁡󠁬󠁿 Flag for Alabama (US-AL)
🏴󠁵󠁭󠀷󠀶󠁿 Flag for Navassa Island (UM-76)
🏴󠁮󠁧󠁮󠁩󠁿 Flag for Niger (NG-NI)
🏴󠁴󠁲󠀰󠀱󠁿 Flag for Adana (TR-01)
🏴󠁵󠁳󠁭󠁥󠁿 Flag for Maine (US-ME)
🕀 Circled Cross Pommee
🏴󠁣󠁡󠁡󠁢󠁿 Flag for Alberta (CA-AB)
🏴󠁥󠁧󠁡󠁬󠁸󠁿 Flag for Alexandria (EG-ALX)
🏴󠁵󠁭󠀸󠀶󠁿 Flag for Jarvis Island (UM-86)
☥ Ankh
🏴󠁵󠁡󠀱󠀲󠁿 Flag for Dnipropetrovshchyna (UA-12)
🏴󠁣󠁯󠁭󠁥󠁴󠁿 Flag for Meta (CO-MET)
🏴󠁡󠁯󠁨󠁵󠁩󠁿 Flag for Huíla (AO-HUI)
🎘 Musical Keyboard with Jacks
🏴󠁳󠁩󠀲󠀰󠀴󠁿 Flag for Sveta Trojica v Slovenskih Goricah (SI-204)
👨🏾‍👨🏾‍👦🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁵󠁭󠀸󠀹󠁿 Flag for Kingman Reef (UM-89)
🏴󠁵󠁹󠁡󠁲󠁿 Flag for Artigas (UY-AR)
🏴󠁵󠁹󠁣󠁡󠁿 Flag for Canelones (UY-CA)
🏴󠁭󠁸󠁰󠁵󠁥󠁿 Flag for Puebla (MX-PUE)
🏴󠁵󠁳󠁰󠁡󠁿 Flag for Pennsylvania (US-PA)
🏴󠁴󠁨󠀸󠀰󠁿 Flag for Nakhon Si Thammarat (TH-80)
👨‍👩‍👦‍👧 Family: Man, Woman, Boy, Girl
🏴󠁵󠁳󠁵󠁴󠁿 Flag for Utah (US-UT)
🏴󠁲󠁵󠁫󠁯󠁳󠁿 Flag for Kostroma (RU-KOS)
🏴󠁵󠁳󠁯󠁫󠁿 Flag for Oklahoma (US-OK)
🏴󠁧󠁲󠁢󠁿 Flag for Central Macedonia (GR-B)
👩🏽‍❤️‍👨🏿 Couple With Heart - Woman: Medium Skin Tone, Man: Dark Skin Tone
🏴󠁵󠁳󠁨󠁩󠁿 Flag for Hawaii (US-HI)
🏴󠁵󠁹󠁭󠁡󠁿 Flag for Maldonado (UY-MA)
🏴󠁵󠁺󠁮󠁧󠁿 Flag for Namangan (UZ-NG)
🏴󠁵󠁺󠁪󠁩󠁿 Flag for Jizzakh (UZ-JI)
🏴󠁶󠁣󠀰󠀲󠁿 Flag for Saint Andrew (VC-02)
🏴󠁶󠁥󠁢󠁿 Flag for Anzoátegui (VE-B)
🏴󠁶󠁥󠁤󠁿 Flag for Aragua (VE-D)
👨‍👶‍👧 Family: Man, Baby, Girl
🏴󠁵󠁺󠁱󠁲󠁿 Flag for Karakalpakstan (UZ-QR)
🏴󠁵󠁹󠁳󠁯󠁿 Flag for Soriano (UY-SO)
🏴󠁵󠁹󠁰󠁡󠁿 Flag for Paysandú (UY-PA)
🏴󠁵󠁹󠁣󠁯󠁿 Flag for Colonia (UY-CO)
🏴󠁶󠁣󠀰󠀱󠁿 Flag for Charlotte (VC-01)
🏴󠁰󠁷󠀲󠀱󠀲󠁿 Flag for Melekeok (PW-212)
🏴󠁵󠁺󠁴󠁯󠁿 Flag for Tashkent Province (UZ-TO)
🏴󠁵󠁺󠁢󠁵󠁿 Flag for Bukhara (UZ-BU)
🏴󠁵󠁳󠁭󠁤󠁿 Flag for Maryland (US-MD)
🏴󠁶󠁥󠁡󠁿 Flag for Capital (VE-A)
🏴󠁵󠁺󠁡󠁮󠁿 Flag for Andijan (UZ-AN)
🏴󠁵󠁹󠁴󠁡󠁿 Flag for Tacuarembó (UY-TA)
🏴󠁭󠁤󠁴󠁥󠁿 Flag for Telenești (MD-TE)
🏴󠁵󠁳󠁳󠁣󠁿 Flag for South Carolina (US-SC)
🏴󠁵󠁹󠁭󠁯󠁿 Flag for Montevideo (UY-MO)
🏴󠁵󠁹󠁦󠁳󠁿 Flag for Flores (UY-FS)
🏴󠁵󠁹󠁴󠁴󠁿 Flag for Treinta y Tres (UY-TT)
🏴󠁵󠁹󠁳󠁡󠁿 Flag for Salto (UY-SA)
🏴󠁶󠁣󠀰󠀶󠁿 Flag for Grenadines (VC-06)
🏴󠁵󠁺󠁱󠁡󠁿 Flag for Qashqadaryo (UZ-QA)
🏴󠁵󠁺󠁴󠁫󠁿 Flag for Tashkent (UZ-TK)
🏴󠁵󠁺󠁳󠁩󠁿 Flag for Sirdaryo (UZ-SI)
🏴󠁵󠁹󠁲󠁮󠁿 Flag for Río Negro (UY-RN)
🏴󠁵󠁹󠁲󠁯󠁿 Flag for Rocha (UY-RO)
🏴󠁵󠁹󠁬󠁡󠁿 Flag for Lavalleja (UY-LA)
🏴󠁵󠁺󠁳󠁡󠁿 Flag for Samarqand (UZ-SA)
🏴󠁶󠁣󠀰󠀳󠁿 Flag for Saint David (VC-03)
🏴󠁵󠁺󠁦󠁡󠁿 Flag for Fergana (UZ-FA)
🏴󠁵󠁺󠁳󠁵󠁿 Flag for Surxondaryo (UZ-SU)
🏴󠁵󠁹󠁤󠁵󠁿 Flag for Durazno (UY-DU)
🏴󠁵󠁺󠁮󠁷󠁿 Flag for Navoiy (UZ-NW)
🏴󠁵󠁹󠁣󠁬󠁿 Flag for Cerro Largo (UY-CL)
🏴󠁳󠁩󠀰󠀳󠀷󠁿 Flag for Ig (SI-037)
🏴󠁶󠁥󠁭󠁿 Flag for Miranda (VE-M)
🏴󠁶󠁮󠀲󠀲󠁿 Flag for Nghệ An (VN-22)
🏴󠁵󠁳󠁧󠁵󠁿 Flag for Guam (US-GU)
🏴󠁶󠁮󠀱󠀸󠁿 Flag for Ninh Bình (VN-18)
🏴󠁶󠁥󠁫󠁿 Flag for Lara (VE-K)
🏴󠁮󠁺󠁷󠁧󠁮󠁿 Flag for Wellington (NZ-WGN)
🏴󠁶󠁮󠀲󠀹󠁿 Flag for Quảng Ngãi (VN-29)
🏴󠁶󠁮󠀲󠀰󠁿 Flag for Thái Bình (VN-20)
🏴󠁶󠁮󠀰󠀴󠁿 Flag for Cao Bằng (VN-04)
👨🏼‍👧🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁶󠁮󠀱󠀳󠁿 Flag for Quảng Ninh (VN-13)
🏴󠁶󠁮󠀰󠀹󠁿 Flag for Lạng Sơn (VN-09)
🏴󠁶󠁮󠀰󠀷󠁿 Flag for Tuyên Quang (VN-07)
🏴󠁧󠁭󠁬󠁿 Flag for Lower River Division (GM-L)
🏴󠁶󠁮󠀲󠀱󠁿 Flag for Thanh Hóa (VN-21)
🏴󠁧󠁥󠁴󠁢󠁿 Flag for Tbilisi (GE-TB)
🏴󠁶󠁮󠀱󠀴󠁿 Flag for Hòa Bình (VN-14)
🏴󠁶󠁮󠀰󠀵󠁿 Flag for Sơn La (VN-05)
🏴󠁤󠁺󠀱󠀳󠁿 Flag for Tlemcen (DZ-13)
🏴󠁶󠁥󠁥󠁿 Flag for Barinas (VE-E)
🏴󠁶󠁥󠁨󠁿 Flag for Cojedes (VE-H)
🏴󠁶󠁮󠀲󠀸󠁿 Flag for Kon Tum (VN-28)
󠀰 Tag Digit Zero
🏴󠁶󠁥󠁳󠁿 Flag for Táchira (VE-S)
🀨 Mahjong Tile Autumn
👩🏼‍👦🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁶󠁮󠀲󠀳󠁿 Flag for Hà Tĩnh (VN-23)
🏴󠁶󠁮󠀰󠀶󠁿 Flag for Yên Bái (VN-06)
🏴󠁶󠁥󠁵󠁿 Flag for Yaracuy (VE-U)
🏴󠁶󠁮󠀰󠀳󠁿 Flag for Hà Giang (VN-03)
🏴󠁶󠁮󠀳󠀵󠁿 Flag for Lâm Đồng (VN-35)
🏴󠁶󠁮󠀶󠀷󠁿 Flag for Nam Định (VN-67)
🏴󠁶󠁮󠀵󠀸󠁿 Flag for Bình Phước (VN-58)
🏴󠁶󠁮󠀶󠀱󠁿 Flag for Hải Dương (VN-61)
🏴󠁶󠁮󠀵󠀰󠁿 Flag for Bến Tre (VN-50)
🏴󠁶󠁮󠀷󠀰󠁿 Flag for Vĩnh Phúc (VN-70)
🏴󠁶󠁮󠀷󠀳󠁿 Flag for Hậu Giang (VN-73)
🏴󠁶󠁮󠀷󠀱󠁿 Flag for Điện Biên (VN-71)
🏴󠁶󠁥󠁦󠁿 Flag for Bolívar (VE-F)
🏴󠁶󠁮󠀳󠀷󠁿 Flag for Tây Ninh (VN-37)
🏴󠁶󠁮󠁤󠁮󠁿 Flag for Da Nang (VN-DN)
🏴󠁭󠁷󠁮󠁿 Flag for Northern (MW-N)
🏴󠁶󠁮󠀵󠀷󠁿 Flag for Bình Dương (VN-57)
🏴󠁶󠁮󠀵󠀶󠁿 Flag for Bắc Ninh (VN-56)
🏴󠁶󠁮󠀶󠀳󠁿 Flag for Hà Nam (VN-63)
🏴󠁶󠁮󠀶󠀹󠁿 Flag for Thái Nguyên (VN-69)
🏴󠁶󠁮󠀳󠀲󠁿 Flag for Phú Yên (VN-32)
🏴󠁶󠁮󠀴󠀱󠁿 Flag for Long An (VN-41)
🏴󠁶󠁮󠀵󠀳󠁿 Flag for Bắc Kạn (VN-53)
🏴󠁶󠁮󠀵󠀹󠁿 Flag for Cà Mau (VN-59)
🏴󠁶󠁮󠀳󠀱󠁿 Flag for Bình Định (VN-31)
🏴󠁶󠁮󠀳󠀳󠁿 Flag for Đắk Lắk (VN-33)
🏴󠁶󠁮󠀵󠀵󠁿 Flag for Bạc Liêu (VN-55)
🏴󠁶󠁮󠀳󠀰󠁿 Flag for Gia Lai (VN-30)
🏴󠁶󠁮󠀴󠀷󠁿 Flag for Kiên Giang (VN-47)
🏴󠁶󠁮󠀵󠀴󠁿 Flag for Bắc Giang (VN-54)
🏴󠁶󠁮󠀴󠀵󠁿 Flag for Đồng Tháp (VN-45)
🏴󠁭󠁵󠁣󠁣󠁿 Flag for Cargados Carajos (MU-CC)
🏴󠁶󠁮󠀳󠀹󠁿 Flag for Đồng Nai (VN-39)
🏴󠁶󠁮󠀳󠀴󠁿 Flag for Khánh Hòa (VN-34)
🏴󠁶󠁮󠀶󠀸󠁿 Flag for Phú Thọ (VN-68)
🏴󠁶󠁮󠀷󠀲󠁿 Flag for Đắk Nông (VN-72)
🏴󠁶󠁮󠀴󠀳󠁿 Flag for Bà Rịa–Vũng Tàu (VN-43)
🏴󠁶󠁮󠀵󠀲󠁿 Flag for Sóc Trăng (VN-52)
🏴󠁶󠁮󠀳󠀶󠁿 Flag for Ninh Thuận (VN-36)
🏴󠁶󠁮󠀴󠀶󠁿 Flag for Tiền Giang (VN-46)
🏴󠁶󠁮󠁣󠁴󠁿 Flag for Can Tho (VN-CT)
🏴󠁶󠁮󠀴󠀰󠁿 Flag for Bình Thuận (VN-40)
🏴󠁷󠁦󠁵󠁶󠁿 Flag for Uvea (WF-UV)
🏴󠁹󠁥󠁭󠁲󠁿 Flag for Al Mahrah (YE-MR)
🏴󠁷󠁳󠁧󠁥󠁿 Flag for Gaga’emauga (WS-GE)
🏴󠁹󠁥󠁨󠁵󠁿 Flag for Al Hudaydah (YE-HU)
🏴󠁹󠁥󠁬󠁡󠁿 Flag for Lahij (YE-LA)
🏴󠁹󠁥󠁤󠁨󠁿 Flag for Dhamar (YE-DH)
🏴󠁷󠁳󠁡󠁴󠁿 Flag for Atua (WS-AT)
🏴󠁷󠁳󠁳󠁡󠁿 Flag for Satupa’itea (WS-SA)
🏴󠁷󠁳󠁶󠁦󠁿 Flag for Va’a-o-Fonoti (WS-VF)
🏴󠁹󠁥󠁡󠁭󠁿 Flag for Amran (YE-AM)
🏴󠁶󠁵󠁳󠁥󠁥󠁿 Flag for Shefa (VU-SEE)
🏴󠁹󠁥󠁲󠁡󠁿 Flag for Raymah (YE-RA)
🏴󠁷󠁳󠁰󠁡󠁿 Flag for Palauli (WS-PA)
🏴󠁶󠁵󠁴󠁡󠁥󠁿 Flag for Tafea (VU-TAE)
🏴󠁹󠁥󠁨󠁪󠁿 Flag for Hajjah (YE-HJ)
🏴󠁶󠁮󠁨󠁰󠁿 Flag for Haiphong (VN-HP)
🏴󠁶󠁵󠁰󠁡󠁭󠁿 Flag for Penama (VU-PAM)
👨🏻‍👨🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone
🏴󠁷󠁳󠁴󠁵󠁿 Flag for Tuamasaga (WS-TU)
🏴󠁹󠁥󠁳󠁨󠁿 Flag for Shabwah (YE-SH)
🏴󠁶󠁵󠁴󠁯󠁢󠁿 Flag for Torba (VU-TOB)
👨🏻‍👩🏻‍👧🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
👨🏽‍👩🏽‍👶🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
󠁹 Tag Latin Small Letter Y
🏴󠁰󠁡󠁫󠁹󠁿 Flag for Guna Yala (PA-KY)
🏴󠁩󠁲󠀰󠀳󠁿 Flag for Ardabil (IR-03)
⚷ Chiron
🏴󠁹󠁥󠁡󠁤󠁿 Flag for ’Adan (YE-AD)
🏴󠁹󠁥󠁭󠁷󠁿 Flag for Al Mahwit (YE-MW)
🏴󠁹󠁥󠁢󠁡󠁿 Flag for Al Bayda (YE-BA)
🏴󠁹󠁥󠁤󠁡󠁿 Flag for Dhale (YE-DA)
🏴󠁹󠁥󠁡󠁢󠁿 Flag for Abyan (YE-AB)
🏴󠁲󠁵󠁢󠁡󠁿 Flag for Bashkortostan (RU-BA)
👨🏾‍👦🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁺󠁭󠀰󠀱󠁿 Flag for Western (ZM-01)
🏴󠁺󠁡󠁥󠁣󠁿 Flag for Eastern Cape (ZA-EC)
🏴󠁺󠁭󠀱󠀰󠁿 Flag for Muchinga (ZM-10)
🏴󠁺󠁷󠁭󠁡󠁿 Flag for Manicaland (ZW-MA)
🏴󠁺󠁷󠁢󠁵󠁿 Flag for Bulawayo (ZW-BU)
🏴󠁺󠁷󠁭󠁷󠁿 Flag for Mashonaland West (ZW-MW)
🏴󠁺󠁭󠀰󠀴󠁿 Flag for Luapula (ZM-04)
🏴󠁺󠁭󠀰󠀵󠁿 Flag for Northern (ZM-05)
🏴󠁺󠁭󠀰󠀶󠁿 Flag for North-Western (ZM-06)
🏴󠁺󠁭󠀰󠀳󠁿 Flag for Eastern (ZM-03)
🏴󠁺󠁡󠁦󠁳󠁿 Flag for Free (ZA-FS)
🏴󠁺󠁷󠁭󠁳󠁿 Flag for Matabeleland South (ZW-MS)
🏴󠁹󠁥󠁴󠁡󠁿 Flag for Taiz (YE-TA)
🏴󠁷󠁦󠁳󠁧󠁿 Flag for Sigave (WF-SG)
🏴󠁺󠁭󠀰󠀸󠁿 Flag for Copperbelt (ZM-08)
🏴󠁺󠁭󠀰󠀷󠁿 Flag for Southern (ZM-07)
🏴󠁺󠁭󠀰󠀹󠁿 Flag for Lusaka (ZM-09)
🏴󠁴󠁲󠀴󠀱󠁿 Flag for Kocaeli (TR-41)
🏴󠁭󠁫󠀷󠀸󠁿 Flag for Centar Župa (MK-78)
🏴󠁺󠁷󠁭󠁮󠁿 Flag for Matabeleland North (ZW-MN)
🏴󠁺󠁡󠁭󠁰󠁿 Flag for Mpumalanga (ZA-MP)
🏴󠁺󠁡󠁧󠁴󠁿 Flag for Gauteng (ZA-GT)
👨🏻‍👧🏻‍👦🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁰󠁳󠁮󠁧󠁺󠁿 Flag for North Gaza (PS-NGZ)
🏴󠁺󠁷󠁭󠁥󠁿 Flag for Mashonaland East (ZW-ME)
🏴󠁺󠁷󠁭󠁶󠁿 Flag for Masvingo (ZW-MV)
🏴󠁺󠁡󠁬󠁰󠁿 Flag for Limpopo (ZA-LP)
🏴󠁺󠁡󠁮󠁣󠁿 Flag for Northern Cape (ZA-NC)
🏴󠁮󠁺󠁳󠁴󠁬󠁿 Flag for Southland (NZ-STL)
🏴󠁺󠁭󠀰󠀲󠁿 Flag for Central (ZM-02)
🏴󠁲󠁳󠁶󠁯󠁿 Flag for Vojvodina (RS-VO)
🏴󠁺󠁷󠁨󠁡󠁿 Flag for Harare (ZW-HA)
🏴󠁷󠁳󠁡󠁡󠁿 Flag for A’ana (WS-AA)
🏴󠁴󠁶󠁮󠁩󠁴󠁿 Flag for Niutao (TV-NIT)
🏴󠁵󠁹󠁳󠁪󠁿 Flag for San José (UY-SJ)
🏴󠁬󠁴󠀲󠀰󠁿 Flag for Klaipėdos Municipality (LT-20)
󠀺 Tag Colon
🏴󠁲󠁵󠁫󠁤󠁡󠁿 Flag for Krasnodar Krai (RU-KDA)
🏴󠁨󠁲󠀰󠀳󠁿 Flag for Sisak-Moslavina (HR-03)
🏴󠁪󠁰󠀰󠀷󠁿 Flag for Fukushima (JP-07)
🏴󠁩󠁲󠀲󠀱󠁿 Flag for Mazandaran (IR-21)
🏴󠁤󠁪󠁡󠁲󠁿 Flag for Arta (DJ-AR)
🏴󠁣󠁡󠁭󠁢󠁿 Flag for Manitoba (CA-MB)
🏴󠁥󠁧󠁷󠁡󠁤󠁿 Flag for New Valley (EG-WAD)
🌢 Black Droplet
🏴󠁶󠁮󠁨󠁮󠁿 Flag for Hanoi (VN-HN)
🏴󠁲󠁵󠁰󠁲󠁩󠁿 Flag for Primorsky Krai (RU-PRI)
🏴󠁮󠁬󠁵󠁴󠁿 Flag for Utrecht (NL-UT)
🏴󠁴󠁨󠀸󠀱󠁿 Flag for Krabi (TH-81)
🏴󠁰󠁬󠁷󠁰󠁿 Flag for Greater Poland (PL-WP)
👨🏽‍👨🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone
👩🏽‍👨🏽‍👶🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁣󠁹󠀰󠀳󠁿 Flag for Larnaca (CY-03)
🏴󠁣󠁹󠀰󠀶󠁿 Flag for Kyrenia (CY-06)
🏴󠁤󠁪󠁤󠁪󠁿 Flag for Djibouti (DJ-DJ)
🏴󠁤󠁺󠀴󠀵󠁿 Flag for Naama (DZ-45)
🏴󠁡󠁯󠁬󠁮󠁯󠁿 Flag for Lunda Norte (AO-LNO)
🏴󠁡󠁯󠁬󠁳󠁵󠁿 Flag for Lunda Sul (AO-LSU)
🏴󠁰󠁧󠁭󠁲󠁬󠁿 Flag for Manus (PG-MRL)
🏴󠁩󠁲󠀳󠀱󠁿 Flag for North Khorasan (IR-31)
🖟 Sideways White Down Pointing Index
👩‍❤️‍👩🏿 Couple With Heart - Woman, Woman: Dark Skin Tone
🏴󠁵󠁳󠁮󠁨󠁿 Flag for New Hampshire (US-NH)
🕿 Black Touchtone Telephone
🏴󠁥󠁥󠀵󠀹󠁿 Flag for Lääne-Viru (EE-59)
🏴󠁭󠁹󠀰󠀸󠁿 Flag for Perak (MY-08)
👩🏼‍❤️‍💋‍👨🏻 Kiss - Woman: Medium-Light Skin Tone, Man: Light Skin Tone
🏴󠁨󠁵󠁢󠁵󠁿 Flag for Budapest (HU-BU)
🏴󠁧󠁡󠀸󠁿 Flag for Ogooué-Maritime (GA-8)
🏴󠁷󠁳󠁧󠁩󠁿 Flag for Gaga’ifomauga (WS-GI)
🖞 Sideways White Up Pointing Index
🏴󠁦󠁩󠀱󠀸󠁿 Flag for Uusimaa (FI-18)
👨🏽‍❤️‍💋‍👨 Kiss - Man: Medium Skin Tone, Man
👩🏼‍👨🏼‍👦🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁭󠁺󠁱󠁿 Flag for Zambezia (MZ-Q)
🏴󠁰󠁳󠁤󠁥󠁢󠁿 Flag for Deir al-Balah (PS-DEB)
🖚 Sideways Black Left Pointing Index
👨‍❤️‍👨🏾 Couple With Heart - Man, Man: Medium-Dark Skin Tone
🀕 Mahjong Tile Six of Bamboos
🏴󠁮󠁩󠁳󠁪󠁿 Flag for Río San Juan (NI-SJ)
󠁂 Tag Latin Capital Letter B
🏴󠁶󠁥󠁯󠁿 Flag for Nueva Esparta (VE-O)
🏴󠁰󠁹󠀱󠀶󠁿 Flag for Alto Paraguay (PY-16)
🏴󠁹󠁥󠁳󠁵󠁿 Flag for Arkhabil Suqutra (YE-SU)
🏴󠁧󠁲󠁣󠁿 Flag for West Macedonia (GR-C)
🏴󠁬󠁶󠀰󠀶󠀷󠁿 Flag for Ogre (LV-067)
👨‍❤️‍💋‍👩🏽 Kiss - Man, Woman: Medium Skin Tone
🏴󠁡󠁯󠁨󠁵󠁡󠁿 Flag for Huambo (AO-HUA)
🏴󠁵󠁡󠀲󠀶󠁿 Flag for Prykarpattia (UA-26)
🏴󠁥󠁣󠁨󠁿 Flag for Chimborazo (EC-H)
🏴󠁡󠁯󠁣󠁵󠁳󠁿 Flag for Cuanza Sul (AO-CUS)
🏴󠁥󠁥󠀳󠀷󠁿 Flag for Harju (EE-37)
🏴󠁩󠁮󠁧󠁪󠁿 Flag for Gujarat (IN-GJ)
👨🏾‍👩🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🖉 Lower Left Pencil
👨🏻‍👨🏻‍👶🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
👨🏿‍❤️‍💋‍👩🏽 Kiss - Man: Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁰󠁬󠁭󠁡󠁿 Flag for Lesser Poland (PL-MA)
🏴󠁦󠁲󠁣󠁰󠁿 Flag for Clipperton Island (FR-CP)
👨🏽‍👧🏽‍👶🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁮󠁲󠀱󠀴󠁿 Flag for Yaren (NR-14)
🏴󠁭󠁫󠀲󠀵󠁿 Flag for Demir Hisar (MK-25)
🏴󠁡󠁵󠁡󠁣󠁴󠁿 Flag for Australian Capital Territory (AU-ACT)
⛍ Disabled Car
🏴󠁡󠁯󠁢󠁩󠁥󠁿 Flag for Bié (AO-BIE)
👩‍❤️‍👩🏻 Couple With Heart - Woman, Woman: Light Skin Tone
🀆 Mahjong Tile White Dragon
🏴󠁤󠁥󠁨󠁢󠁿 Flag for Bremen (DE-HB)
🎜 Beamed Ascending Musical Notes
🏴󠁵󠁳󠁭󠁳󠁿 Flag for Mississippi (US-MS)
🏴󠁣󠁯󠁣󠁨󠁯󠁿 Flag for Chocó (CO-CHO)
🏴󠁴󠁲󠀸󠀱󠁿 Flag for Düzce (TR-81)
👩🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁣󠁨󠁶󠁤󠁿 Flag for Vaud (CH-VD)
🏴󠁩󠁮󠁴󠁧󠁿 Flag for Telangana (IN-TG)
👩🏼‍❤️‍💋‍👩🏻 Kiss - Woman: Medium-Light Skin Tone, Woman: Light Skin Tone
🏴󠁭󠁡󠀰󠀸󠁿 Flag for Grand Casablanca (MA-08)
👩‍👨‍👶‍👦 Family: Woman, Man, Baby, Boy
🏴󠁩󠁴󠀲󠀳󠁿 Flag for Aosta Valley (IT-23)
🏴󠁰󠁥󠁡󠁰󠁵󠁿 Flag for Apurímac (PE-APU)
🏴󠁭󠁸󠁳󠁯󠁮󠁿 Flag for Sonora (MX-SON)
🏴󠁥󠁴󠁳󠁮󠁿 Flag for Southern Nations, Nationalities, and Peoples (ET-SN)
🏴󠁫󠁷󠁨󠁡󠁿 Flag for Hawalli (KW-HA)
🏴󠁥󠁣󠁧󠁿 Flag for Guayas (EC-G)
🏴󠁰󠁥󠁭󠁤󠁤󠁿 Flag for Madre de Dios (PE-MDD)
👨🏻‍👦🏻‍👦🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
🏴󠁡󠁯󠁣󠁡󠁢󠁿 Flag for Cabinda (AO-CAB)
🏴󠁥󠁴󠁯󠁲󠁿 Flag for Oromia (ET-OR)
🏴󠁭󠁲󠀰󠀷󠁿 Flag for Adrar (MR-07)
🏴󠁣󠁩󠁳󠁭󠁿 Flag for Sassandra-Marahoué (CI-SM)
🏴󠁬󠁩󠀰󠀸󠁿 Flag for Schellenberg (LI-08)
🏴󠁶󠁣󠀰󠀵󠁿 Flag for Saint Patrick (VC-05)
👨🏿‍👩🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁵󠁧󠁣󠁿 Flag for Central (UG-C)
👩🏽‍❤️‍💋‍👩🏼 Kiss - Woman: Medium Skin Tone, Woman: Medium-Light Skin Tone
👨🏽‍👨🏽‍👧🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁵󠁳󠁷󠁹󠁿 Flag for Wyoming (US-WY)
🏴󠁴󠁷󠁨󠁳󠁺󠁿 Flag for Hsinchu (TW-HSZ)
🏴󠁬󠁶󠀱󠀰󠀰󠁿 Flag for Vaiņode (LV-100)
🏴󠁣󠁦󠁶󠁫󠁿 Flag for Vakaga (CF-VK)
👨🏼‍👩🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁡󠁯󠁢󠁧󠁵󠁿 Flag for Benguela (AO-BGU)
🏴󠁮󠁧󠁳󠁯󠁿 Flag for Sokoto (NG-SO)
👩🏽‍❤️‍👩🏼 Couple With Heart - Woman: Medium Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁦󠁲󠁩󠁤󠁦󠁿 Flag for Île-de-France (FR-IDF)
👨🏾‍👩🏾‍👧🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁳󠁩󠀱󠀲󠀲󠁿 Flag for Škofja Loka (SI-122)
🏴󠁭󠁹󠀰󠀶󠁿 Flag for Pahang (MY-06)
🏴󠁨󠁮󠁩󠁢󠁿 Flag for Bay Islands (HN-IB)
👩🏻‍👩🏻‍👦🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
🏴󠁶󠁥󠁪󠁿 Flag for Guárico (VE-J)
🏴󠁪󠁭󠀱󠀴󠁿 Flag for Saint Catherine (JM-14)
🏴󠁬󠁲󠁢󠁧󠁿 Flag for Bong (LR-BG)
🏴󠁣󠁯󠁳󠁵󠁣󠁿 Flag for Sucre (CO-SUC)
👩🏻‍❤️‍💋‍👨🏼 Kiss - Woman: Light Skin Tone, Man: Medium-Light Skin Tone
🏴󠁣󠁧󠀱󠀱󠁿 Flag for Bouenza (CG-11)
🏴󠁬󠁳󠁣󠁿 Flag for Leribe (LS-C)
5️ Digit Five
🏴󠁭󠁸󠁭󠁥󠁸󠁿 Flag for Mexico State (MX-MEX)
🏴󠁰󠁥󠁡󠁲󠁥󠁿 Flag for Arequipa (PE-ARE)
🏴󠁶󠁥󠁰󠁿 Flag for Portuguesa (VE-P)
🏴󠁡󠁯󠁢󠁧󠁯󠁿 Flag for Bengo (AO-BGO)
🖶 Printer Icon
👩‍👨‍👶 Family: Woman, Man, Baby
👩🏿‍👩🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁬󠁫󠀳󠁿 Flag for Southern (LK-3)
🏴󠁶󠁥󠁲󠁿 Flag for Sucre (VE-R)
👩🏻‍❤️‍💋‍👩🏻 Kiss - Woman: Light Skin Tone, Woman: Light Skin Tone
👩🏽‍👨🏽‍👧🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
8️ Digit Eight
👨‍❤️‍💋‍👨🏼 Kiss - Man, Man: Medium-Light Skin Tone
🏴󠁮󠁩󠁬󠁥󠁿 Flag for León (NI-LE)
🏴󠁣󠁡󠁮󠁴󠁿 Flag for Northwest Territories (CA-NT)
🏴󠁰󠁡󠀴󠁿 Flag for Chiriquí (PA-4)
🏴󠁭󠁶󠁮󠁯󠁿 Flag for North Province (MV-NO)
🏴󠁲󠁵󠁭󠁡󠁧󠁿 Flag for Magadan (RU-MAG)
👩🏼‍👩🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🗲 Lightning Mood
🏴󠁭󠁫󠀶󠀱󠁿 Flag for Plasnica (MK-61)
👨‍👨‍👦‍👶 Family: Man, Man, Boy, Baby
🏴󠁣󠁯󠁡󠁮󠁴󠁿 Flag for Antioquia (CO-ANT)
🏴󠁥󠁳󠁡󠁲󠁿 Flag for Aragon (ES-AR)
🏴󠁵󠁳󠁶󠁡󠁿 Flag for Virginia (US-VA)
🏴󠁭󠁣󠁳󠁤󠁿 Flag for Sainte-Dévote Chapel (MC-SD)
🏴󠁨󠁲󠀰󠀵󠁿 Flag for Varaždin (HR-05)
👩🏻‍👨🏻‍👶🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
👩🏽‍👨🏽‍👧🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁮󠁯󠀱󠀲󠁿 Flag for Hordaland (NO-12)
🏴󠁮󠁬󠁮󠁨󠁿 Flag for North Holland (NL-NH)
🏴󠁦󠁲󠁰󠁤󠁬󠁿 Flag for Pays-de-la-Loire (FR-PDL)
🏴󠁶󠁥󠁬󠁿 Flag for Mérida (VE-L)
🏴󠁴󠁺󠀱󠀶󠁿 Flag for Morogoro (TZ-16)
🖴 Hard Disk
🏴󠁶󠁥󠁣󠁿 Flag for Apure (VE-C)
🖮 Wired Keyboard
🏴󠁨󠁵󠁥󠁧󠁿 Flag for Eger (HU-EG)
🏴󠁵󠁳󠁬󠁡󠁿 Flag for Louisiana (US-LA)
🏴󠁩󠁴󠀳󠀴󠁿 Flag for Veneto (IT-34)
🏴󠁥󠁳󠁡󠁳󠁿 Flag for Asturias (ES-AS)
🏴󠁵󠁳󠁡󠁫󠁿 Flag for Alaska (US-AK)
🏴󠁩󠁲󠀱󠀷󠁿 Flag for Kermanshah (IR-17)
👨🏼‍👦🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁤󠁭󠀰󠀵󠁿 Flag for Saint John (DM-05)
🏴󠁭󠁸󠁴󠁡󠁢󠁿 Flag for Tabasco (MX-TAB)
🏴󠁢󠁲󠁲󠁳󠁿 Flag for Rio Grande do Sul (BR-RS)
🏴󠁳󠁩󠀱󠀳󠀳󠁿 Flag for Velenje (SI-133)
🗫 Three Speech Bubbles
👩🏼‍❤️‍👨🏾 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁦󠁲󠁢󠁬󠁿 Flag for St. Barthélemy (FR-BL)
🏴󠁮󠁺󠁡󠁵󠁫󠁿 Flag for Auckland (NZ-AUK)
👩‍❤️‍💋‍👩🏼 Kiss - Woman, Woman: Medium-Light Skin Tone
🏴󠁫󠁲󠀴󠀷󠁿 Flag for North Gyeongsang (KR-47)
🏴󠁧󠁴󠁲󠁥󠁿 Flag for Retalhuleu (GT-RE)
🏴󠁦󠁩󠀰󠀶󠁿 Flag for Tavastia Proper (FI-06)
👩🏻‍❤️‍👩🏻 Couple With Heart - Woman: Light Skin Tone, Woman: Light Skin Tone
🏴󠁴󠁮󠀱󠀱󠁿 Flag for Tunis (TN-11)
🏴󠁣󠁤󠁥󠁱󠁿 Flag for Équateur (CD-EQ)
🏴󠁪󠁭󠀰󠀵󠁿 Flag for Saint Mary (JM-05)
🏴󠁭󠁸󠁧󠁲󠁯󠁿 Flag for Guerrero (MX-GRO)
🏴󠁧󠁴󠁪󠁵󠁿 Flag for Jutiapa (GT-JU)
🏴󠁺󠁷󠁭󠁣󠁿 Flag for Mashonaland Central (ZW-MC)
󠁪 Tag Latin Small Letter J
🏴󠁴󠁲󠀳󠀸󠁿 Flag for Kayseri (TR-38)
🏴󠁣󠁯󠁮󠁡󠁲󠁿 Flag for Nariño (CO-NAR)
🏴󠁢󠁲󠁣󠁥󠁿 Flag for Ceará (BR-CE)
🏴󠁶󠁵󠁳󠁡󠁭󠁿 Flag for Sanma (VU-SAM)
🏴󠁧󠁡󠀵󠁿 Flag for Nyanga (GA-5)
🏴󠁴󠁮󠀷󠀱󠁿 Flag for Gafsa (TN-71)
🏴󠁳󠁩󠀱󠀵󠀴󠁿 Flag for Dobje (SI-154)
🏴󠁭󠁹󠀱󠀲󠁿 Flag for Sabah (MY-12)
🏴󠁣󠁮󠀵󠀴󠁿 Flag for Tibet (CN-54)
🏴󠁰󠁧󠁧󠁰󠁫󠁿 Flag for Gulf (PG-GPK)
🏴󠁪󠁭󠀰󠀳󠁿 Flag for Saint Thomas (JM-03)
🏴󠁴󠁺󠀰󠀲󠁿 Flag for Dar es Salaam (TZ-02)
🏴󠁶󠁵󠁭󠁡󠁰󠁿 Flag for Malampa (VU-MAP)
👨🏼‍❤️‍💋‍👨🏻 Kiss - Man: Medium-Light Skin Tone, Man: Light Skin Tone
⛖ Black Two-Way Left Way Traffic
🏴󠁳󠁩󠀲󠀱󠀳󠁿 Flag for Ankaran (SI-213)
👨‍👩‍👦‍👶 Family: Man, Woman, Boy, Baby
🏴󠁣󠁡󠁱󠁣󠁿 Flag for Quebec (CA-QC)
👨🏽‍❤️‍💋‍👨🏻 Kiss - Man: Medium Skin Tone, Man: Light Skin Tone
󠁙 Tag Latin Capital Letter Y
🏴󠁥󠁧󠁧󠁺󠁿 Flag for Giza (EG-GZ)
🏴󠁧󠁤󠀰󠀱󠁿 Flag for Saint Andrew (GD-01)
🏴󠁰󠁨󠀰󠀷󠁿 Flag for Central Visayas (PH-07)
🏴󠁥󠁣󠁥󠁿 Flag for Esmeraldas (EC-E)
🏴󠁣󠁤󠁮󠁵󠁿 Flag for Nord-Ubangi (CD-NU)
🏴󠁫󠁥󠀲󠀵󠁿 Flag for Marsabit (KE-25)
🏴󠁳󠁶󠁵󠁳󠁿 Flag for Usulután (SV-US)
🏴󠁴󠁬󠁤󠁩󠁿 Flag for Dili (TL-DI)
🏴󠁣󠁩󠁺󠁺󠁿 Flag for Zanzan (CI-ZZ)
🏴󠁤󠁺󠀰󠀱󠁿 Flag for Adrar (DZ-01)
👨🏾‍👨🏾‍👶🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁬󠁶󠀰󠀶󠀰󠁿 Flag for Mazsalaca (LV-060)
🏴󠁳󠁫󠁢󠁬󠁿 Flag for Bratislava (SK-BL)
🏴󠁴󠁨󠀸󠀶󠁿 Flag for Chumphon (TH-86)
🏴󠁴󠁨󠀷󠀵󠁿 Flag for Samut Songkhram (TH-75)
👨‍❤️‍💋‍👩🏿 Kiss - Man, Woman: Dark Skin Tone
🏴󠁶󠁮󠀰󠀱󠁿 Flag for Lai Châu (VN-01)
🏴󠁴󠁨󠀳󠀶󠁿 Flag for Chaiyaphum (TH-36)
🏴󠁥󠁳󠁣󠁬󠁿 Flag for Castile and León (ES-CL)
🕪 Right Speaker with Three Sound Waves
🕫 Bullhorn
🗋 Empty Document
👨🏿‍❤️‍💋‍👩🏻 Kiss - Man: Dark Skin Tone, Woman: Light Skin Tone
👩🏽‍👩🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁩󠁴󠀴󠀵󠁿 Flag for Emilia-Romagna (IT-45)
🏴󠁶󠁥󠁩󠁿 Flag for Falcón (VE-I)
🏴󠁬󠁳󠁡󠁿 Flag for Maseru (LS-A)
🏴󠁴󠁲󠀴󠀳󠁿 Flag for Kütahya (TR-43)
🏴󠁷󠁳󠁶󠁳󠁿 Flag for Vaisigano (WS-VS)
👨🏿‍👩🏿‍👦🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁡󠁭󠁡󠁶󠁿 Flag for Armavir (AM-AV)
🏴󠁵󠁳󠁭󠁴󠁿 Flag for Montana (US-MT)
👨🏼‍👩🏼‍👧🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁫󠁲󠀲󠀹󠁿 Flag for Gwangju City (KR-29)
🕇 Heavy Latin Cross
🏴󠁳󠁡󠀱󠀱󠁿 Flag for Al Bahah (SA-11)
🏴󠁥󠁧󠁣󠁿 Flag for Cairo (EG-C)
🏴󠁰󠁴󠀳󠀰󠁿 Flag for Madeira (PT-30)
🏴󠁬󠁴󠁰󠁮󠁿 Flag for Panevėžys County (LT-PN)
🏴󠁪󠁰󠀴󠀶󠁿 Flag for Kagoshima (JP-46)
🏴󠁳󠁩󠀰󠀵󠀲󠁿 Flag for Kranj (SI-052)
🏴󠁳󠁩󠀱󠀶󠀷󠁿 Flag for Lovrenc na Pohorju (SI-167)
🏴󠁮󠁬󠁦󠁲󠁿 Flag for Friesland (NL-FR)
🏴󠁫󠁩󠁬󠁿 Flag for Line Islands (KI-L)
🏴󠁵󠁡󠀱󠀴󠁿 Flag for Donechchyna (UA-14)
🏴󠁶󠁥󠁶󠁿 Flag for Zulia (VE-V)
🏴󠁦󠁩󠀰󠀱󠁿 Flag for Åland Islands (FI-01)
👩‍👨‍👶‍👧 Family: Woman, Man, Baby, Girl
🏴󠁵󠁳󠁯󠁨󠁿 Flag for Ohio (US-OH)
🏴󠁶󠁮󠀲󠀷󠁿 Flag for Quảng Nam (VN-27)
👨🏿‍❤️‍💋‍👩🏼 Kiss - Man: Dark Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁩󠁲󠀰󠀲󠁿 Flag for West Azarbaijan (IR-02)
👨‍❤️‍👩🏻 Couple With Heart - Man, Woman: Light Skin Tone
🏴󠁣󠁨󠁧󠁬󠁿 Flag for Glarus (CH-GL)
👩🏽‍❤️‍👩🏾 Couple With Heart - Woman: Medium Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁤󠁺󠀲󠀱󠁿 Flag for Skikda (DZ-21)
🏴󠁵󠁳󠁶󠁩󠁿 Flag for U.S. Virgin Islands (US-VI)
🏴󠁳󠁡󠀰󠀱󠁿 Flag for Riyadh (SA-01)
🏴󠁤󠁺󠀰󠀸󠁿 Flag for Béchar (DZ-08)
🏴󠁰󠁡󠁥󠁭󠁿 Flag for Emberá (PA-EM)
👨🏻‍❤️‍👨🏼 Couple With Heart - Man: Light Skin Tone, Man: Medium-Light Skin Tone
🏴󠁮󠁬󠁡󠁷󠁿 Flag for Aruba (NL-AW)
🧟🏻‍♂️ Man Zombie: Light Skin Tone
🏴󠁹󠁥󠁩󠁢󠁿 Flag for Ibb (YE-IB)
󠁺 Tag Latin Small Letter Z
🏴󠁡󠁭󠁬󠁯󠁿 Flag for Lori (AM-LO)
🏴󠁢󠁺󠁢󠁺󠁿 Flag for Belize (BZ-BZ)
🏴󠁥󠁣󠁳󠁤󠁿 Flag for Santo Domingo de los Tsáchilas (EC-SD)
🏴󠁩󠁴󠀶󠀵󠁿 Flag for Abruzzo (IT-65)
👩🏻‍❤️‍👩🏽 Couple With Heart - Woman: Light Skin Tone, Woman: Medium Skin Tone
🏴󠁴󠁺󠀰󠀷󠁿 Flag for Zanzibar North (TZ-07)
🏴󠁲󠁵󠁹󠁥󠁶󠁿 Flag for Jewish (RU-YEV)
🏴󠁶󠁮󠀲󠀶󠁿 Flag for Thừa Thiên–Huế (VN-26)
🏴󠁧󠁹󠁥󠁢󠁿 Flag for East Berbice-Corentyne (GY-EB)
🏴󠁬󠁵󠁣󠁡󠁿 Flag for Capellen (LU-CA)
🏴󠁭󠁴󠀲󠀵󠁿 Flag for Luqa (MT-25)
🏴󠁴󠁨󠀹󠀳󠁿 Flag for Phatthalung (TH-93)
🏴󠁹󠁥󠁨󠁤󠁿 Flag for Hadramaut (YE-HD)
🏴󠁲󠁵󠁫󠁬󠁿 Flag for Kalmykia (RU-KL)
🏴󠁫󠁲󠀲󠀶󠁿 Flag for Busan (KR-26)
🏴󠁥󠁧󠁳󠁩󠁮󠁿 Flag for North Sinai (EG-SIN)
🏴󠁢󠁢󠀰󠀸󠁿 Flag for Saint Michael (BB-08)
🀖 Mahjong Tile Seven of Bamboos
🀡 Mahjong Tile Nine of Circles
🏴󠁳󠁩󠀰󠀲󠀷󠁿 Flag for Gorenja Vas–Poljane (SI-027)
🏴󠁣󠁧󠀱󠀲󠁿 Flag for Pool (CG-12)
🏴󠁮󠁧󠁤󠁥󠁿 Flag for Delta (NG-DE)
🏴󠁨󠁵󠁳󠁺󠁿 Flag for Szabolcs-Szatmár-Bereg (HU-SZ)
🕩 Right Speaker with One Sound Wave
🏴󠁬󠁴󠀳󠀰󠁿 Flag for Pakruojis (LT-30)
👩🏾‍❤️‍💋‍👨🏽 Kiss - Woman: Medium-Dark Skin Tone, Man: Medium Skin Tone
👨🏻‍👧🏻‍👧🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
🏴󠁳󠁩󠀰󠀸󠀶󠁿 Flag for Odranci (SI-086)
🏴󠁵󠁳󠁷󠁡󠁿 Flag for Washington (US-WA)
👨🏿‍👩🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone
👨🏿‍👦🏿‍👦🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁵󠁡󠀴󠀳󠁿 Flag for Crimea (UA-43)
👨🏾‍👩🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁬󠁶󠀰󠀴󠀶󠁿 Flag for Koknese (LV-046)
👩🏿‍❤️‍👩🏿 Couple With Heart - Woman: Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁹󠁥󠁪󠁡󠁿 Flag for Al Jawf (YE-JA)
🀩 Mahjong Tile Winter
🏴󠁵󠁡󠀳󠀰󠁿 Flag for Kiev (UA-30)
🔾 Lower Right Shadowed White Circle
🏴󠁭󠁤󠁣󠁳󠁿 Flag for Căușeni (MD-CS)
🏴󠁫󠁨󠀲󠀰󠁿 Flag for Svay Rieng (KH-20)
🀙 Mahjong Tile One of Circles
🏴󠁣󠁧󠀱󠀶󠁿 Flag for Pointe-Noire (CG-16)
🏴󠁲󠁵󠁯󠁭󠁳󠁿 Flag for Omsk (RU-OMS)
👨🏻‍👨🏻‍👶🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
🏴󠁡󠁭󠁡󠁧󠁿 Flag for Aragatsotn (AM-AG)
🏴󠁬󠁶󠀰󠀰󠀹󠁿 Flag for Ape (LV-009)
🏴󠁬󠁶󠀰󠀴󠀱󠁿 Flag for Jelgava Municipality (LV-041)
🏴󠁭󠁵󠁲󠁯󠁿 Flag for Rodrigues (MU-RO)
🏴󠁡󠁭󠁡󠁲󠁿 Flag for Ararat (AM-AR)
🏴󠁭󠁺󠁬󠁿 Flag for Maputo Province (MZ-L)
🏴󠁹󠁥󠁭󠁡󠁿 Flag for Ma’rib (YE-MA)
🏴󠁭󠁴󠀶󠀲󠁿 Flag for Xewkija (MT-62)
🏴󠁭󠁲󠀱󠀰󠁿 Flag for Guidimaka (MR-10)
👨🏾‍👩🏾‍👦🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁴󠁤󠁨󠁬󠁿 Flag for Hadjer-Lamis (TD-HL)
🗰 Mood Bubble
🏴󠁪󠁰󠀲󠀱󠁿 Flag for Gifu (JP-21)
👨‍❤️‍👩🏿 Couple With Heart - Man, Woman: Dark Skin Tone
🏴󠁭󠁫󠀰󠀲󠁿 Flag for Aračinovo (MK-02)
🏴󠁳󠁩󠀰󠀴󠀵󠁿 Flag for Kidričevo (SI-045)
🀘 Mahjong Tile Nine of Bamboos
🏴󠁦󠁩󠀱󠀴󠁿 Flag for Northern Ostrobothnia (FI-14)
🏴󠁢󠁱󠁳󠁥󠁿 Flag for Sint Eustatius (BQ-SE)
🏴󠁪󠁰󠀱󠀱󠁿 Flag for Saitama (JP-11)
🏴󠁩󠁮󠁡󠁳󠁿 Flag for Assam (IN-AS)
🀧 Mahjong Tile Summer
🀔 Mahjong Tile Five of Bamboos
👨🏾‍👩🏾‍👶🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👨🏽‍👩🏽‍👦🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁣󠁯󠁤󠁣󠁿 Flag for Capital District (CO-DC)
🏴󠁳󠁩󠀱󠀲󠀵󠁿 Flag for Šmartno ob Paki (SI-125)
🏴󠁣󠁵󠀹󠀹󠁿 Flag for Isla de la Juventud (CU-99)
🏴󠁪󠁭󠀰󠀲󠁿 Flag for Saint Andrew (JM-02)
🀦 Mahjong Tile Spring
󠁈 Tag Latin Capital Letter H
👩🏼‍❤️‍👩🏼 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
🗹 Ballot Box with Bold Check
🀗 Mahjong Tile Eight of Bamboos
🏴󠁨󠁵󠁨󠁶󠁿 Flag for Hódmezővásárhely (HU-HV)
🏴󠁡󠁭󠁧󠁲󠁿 Flag for Gegharkunik (AM-GR)
🏴󠁡󠁲󠁨󠁿 Flag for Chaco (AR-H)
🏴󠁡󠁭󠁫󠁴󠁿 Flag for Kotayk (AM-KT)
🏴󠁵󠁳󠁭󠁩󠁿 Flag for Michigan (US-MI)
🏴󠁭󠁶󠁳󠁣󠁿 Flag for South Central Province (MV-SC)
🏴󠁬󠁴󠀰󠀲󠁿 Flag for Alytus Municipality (LT-02)
🏴󠁬󠁶󠀱󠀰󠀶󠁿 Flag for Ventspils Municipality (LV-106)
🏴󠁢󠁡󠁢󠁩󠁨󠁿 Flag for Federation of Bosnia and Herzegovina (BA-BIH)
🏴󠁡󠁺󠁸󠁶󠁤󠁿 Flag for Khojavend (AZ-XVD)
🏴󠁳󠁥󠁯󠁿 Flag for Västra Götaland (SE-O)
🏴󠁫󠁺󠁹󠁵󠁺󠁿 Flag for South Kazakhstan (KZ-YUZ)
🏴󠁶󠁮󠀶󠀶󠁿 Flag for Hưng Yên (VN-66)
🏴󠁣󠁮󠀴󠀴󠁿 Flag for Guangdong (CN-44)
👨🏻‍👨🏻‍👧🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
👩🏼‍👧🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🀣 Mahjong Tile Orchid
🏴󠁲󠁳󠀱󠀰󠁿 Flag for Podunavlje (RS-10)
👩🏼‍👩🏼‍👧🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁵󠁺󠁸󠁯󠁿 Flag for Xorazm (UZ-XO)
⚯ Unmarried Partnership Symbol
🏴󠁡󠁬󠀱󠀲󠁿 Flag for Vlorë County (AL-12)
🏴󠁧󠁡󠀴󠁿 Flag for Ngounié (GA-4)
👨🏼‍👨🏼‍👧🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁴󠁨󠀲󠀳󠁿 Flag for Trat (TH-23)
🏴󠁲󠁵󠁳󠁥󠁿 Flag for North Ossetia-Alania (RU-SE)
🏴󠁤󠁥󠁮󠁩󠁿 Flag for Lower Saxony (DE-NI)
🏴󠁲󠁯󠁢󠁿 Flag for Bucharest (RO-B)
🏴󠁡󠁬󠀰󠀲󠁿 Flag for Durrës County (AL-02)
🏴󠁧󠁴󠁳󠁭󠁿 Flag for San Marcos (GT-SM)
🏴󠁲󠁵󠁢󠁵󠁿 Flag for Buryat (RU-BU)
👨🏽‍👨🏽‍👧🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
👨🏿‍👨🏿‍👧🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁫󠁲󠀴󠀸󠁿 Flag for South Gyeongsang (KR-48)
👨🏾‍👨🏾‍👧🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁣󠁬󠁲󠁭󠁿 Flag for Santiago Metropolitan (CL-RM)
🏴󠁴󠁨󠀸󠀳󠁿 Flag for Phuket (TH-83)
🏴󠁦󠁲󠁰󠁭󠁿 Flag for St. Pierre & Miquelon (FR-PM)
🏴󠁣󠁦󠁵󠁫󠁿 Flag for Ouaka (CF-UK)
👨🏼‍👧🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🖝 Black Right Pointing Backhand Index
🏴󠁳󠁩󠀲󠀰󠀲󠁿 Flag for Središče ob Dravi (SI-202)
🏴󠁲󠁯󠁢󠁺󠁿 Flag for Buzău (RO-BZ)
🀊 Mahjong Tile Four of Characters
🏶 Black Rosette
🏴󠁫󠁥󠀳󠀰󠁿 Flag for Nairobi County (KE-30)
🏴󠁴󠁭󠁬󠁿 Flag for Lebap (TM-L)
󠀽 Tag Equals Sign
🏴󠁴󠁴󠁳󠁧󠁥󠁿 Flag for Sangre Grande (TT-SGE)
🏴󠁡󠁲󠁣󠁿 Flag for Buenos Aires (AR-C)
🏴󠁦󠁩󠀱󠀹󠁿 Flag for Southwest Finland (FI-19)
👨🏻‍👨🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone
🏴󠁲󠁵󠁳󠁡󠁭󠁿 Flag for Samara (RU-SAM)
🏴󠁲󠁵󠁶󠁯󠁲󠁿 Flag for Voronezh (RU-VOR)
󠁢 Tag Latin Small Letter B
🏴󠁰󠁳󠁢󠁴󠁨󠁿 Flag for Bethlehem (PS-BTH)
👨🏻‍👩🏻‍👶🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
🏴󠁫󠁥󠀱󠀷󠁿 Flag for Kisumu (KE-17)
👨🏽‍👨🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone
🀓 Mahjong Tile Four of Bamboos
🀑 Mahjong Tile Two of Bamboos
👨🏽‍👨🏽‍👶🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
🕆 White Latin Cross
🏴󠁵󠁳󠁵󠁭󠁿 Flag for U.S. Outlying Islands (US-UM)
🗱 Lightning Mood Bubble
👩🏾‍❤️‍💋‍👨🏾 Kiss - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁤󠁥󠁮󠁷󠁿 Flag for North Rhine-Westphalia (DE-NW)
👩🏿‍👧🏿‍👦🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
󠁻 Tag Left Curly Bracket
🏴󠁮󠁺󠁭󠁢󠁨󠁿 Flag for Marl (NZ-MBH)
👨🏼‍👩🏼‍👦🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁶󠁥󠁮󠁿 Flag for Monagas (VE-N)
🏴󠁶󠁥󠁺󠁿 Flag for Amazonas (VE-Z)
1️ Digit One
👩🏽‍👦🏽‍👦🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👨🏼‍👨🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁲󠁵󠁫󠁫󠁿 Flag for Khakassia (RU-KK)
🏴󠁫󠁧󠁧󠁯󠁿 Flag for Osh (KG-GO)
🏴󠁳󠁩󠀲󠀱󠀰󠁿 Flag for Sveti Jurij v Slovenskih Goricah (SI-210)
👩‍👧‍👶 Family: Woman, Girl, Baby
🏴󠁨󠁴󠁮󠁯󠁿 Flag for Nord-Ouest (HT-NO)
👩‍❤️‍💋‍👨🏽 Kiss - Woman, Man: Medium Skin Tone
🏴󠁵󠁳󠁧󠁡󠁿 Flag for Georgia (US-GA)
👨🏿‍👨🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁵󠁳󠁫󠁹󠁿 Flag for Kentucky (US-KY)
👩‍👨‍👦 Family: Woman, Man, Boy
󠀶 Tag Digit Six
👨‍❤️‍👨🏻 Couple With Heart - Man, Man: Light Skin Tone
🏴󠁤󠁺󠀲󠀸󠁿 Flag for M’Sila (DZ-28)
👨🏼‍👨🏼‍👶🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩‍❤️‍👨🏿 Couple With Heart - Woman, Man: Dark Skin Tone
🏴󠁡󠁬󠀰󠀸󠁿 Flag for Lezhë County (AL-08)
🏴󠁡󠁬󠀱󠀰󠁿 Flag for Shkodër County (AL-10)
🏴󠁲󠁯󠁳󠁭󠁿 Flag for Satu Mare (RO-SM)
👨🏽‍👩🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁩󠁮󠁳󠁫󠁿 Flag for Sikkim (IN-SK)
🏴󠁰󠁧󠁥󠁨󠁧󠁿 Flag for Eastern Highlands (PG-EHG)
👨🏾‍👨🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁺󠁡󠁷󠁣󠁿 Flag for Western Cape (ZA-WC)
🏴󠁡󠁬󠀱󠀱󠁿 Flag for Tirana County (AL-11)
🖺 Document with Text and Picture
󠁤 Tag Latin Small Letter D
🏴󠁥󠁳󠁣󠁢󠁿 Flag for Cantabria (ES-CB)
🏴󠁳󠁳󠁵󠁹󠁿 Flag for Unity (SS-UY)
👨🏻‍👩🏻‍👦🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
🗙 Cancellation X
👩🏾‍👶🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏽‍👶🏽‍👧🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👩🏾‍👶🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
📾 Portable Stereo
👩🏾‍👶🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩🏾‍👨🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁮󠁺󠁨󠁫󠁢󠁿 Flag for Hawke’s Bay (NZ-HKB)
👩🏿‍👨🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁲󠁵󠁵󠁤󠁿 Flag for Udmurt (RU-UD)
🖣 Black Down Pointing Backhand Index
👨🏿‍👨🏿‍👶🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁳󠁥󠁣󠁿 Flag for Uppsala (SE-C)
🏴󠁵󠁳󠁤󠁣󠁿 Flag for Washington DC (US-DC)
🏴󠁶󠁮󠀴󠀴󠁿 Flag for An Giang (VN-44)
🀋 Mahjong Tile Five of Characters
👩🏽‍👶🏽‍👦🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁩󠁴󠀸󠀸󠁿 Flag for Sardinia (IT-88)
👩🏼‍👨🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏽‍👨🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁴󠁬󠁥󠁲󠁿 Flag for Ermera (TL-ER)
🏴󠁨󠁲󠀰󠀸󠁿 Flag for Primorje-Gorski Kotar (HR-08)
👩🏾‍👨🏾‍👦🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏻‍👨🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone
👩🏾‍👨🏾‍👦🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏽‍👨🏽‍👦🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁯󠁭󠁤󠁡󠁿 Flag for Ad Dakhiliyah (OM-DA)
🗛 Decrease Font Size Symbol
🏴󠁭󠁡󠀰󠀴󠁿 Flag for Oriental (MA-04)
👩🏻‍👨🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone
👩🏻‍👨🏻‍👦🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
🏴󠁳󠁩󠀱󠀴󠀳󠁿 Flag for Zavrč (SI-143)
👩🏽‍👨🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁵󠁳󠁷󠁶󠁿 Flag for West Virginia (US-WV)
👩🏽‍👨🏽‍👦🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👩🏼‍👨🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏽‍👨🏽‍👦🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁡󠁥󠁡󠁪󠁿 Flag for Ajman (AE-AJ)
🏴󠁲󠁵󠁫󠁨󠁡󠁿 Flag for Khabarovsk Krai (RU-KHA)
🏴󠁰󠁨󠀱󠀴󠁿 Flag for Muslim Mindanao (PH-14)
👩🏼‍👨🏼‍👧🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏾‍👨🏾‍👧🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏼‍👨🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁡󠁬󠀰󠀹󠁿 Flag for Dibër County (AL-09)
🛉 Boys Symbol
🏴󠁥󠁳󠁩󠁢󠁿 Flag for Balearic Islands (ES-IB)
🏴󠁩󠁱󠁫󠁩󠁿 Flag for Kirkuk (IQ-KI)
👩🏽‍👨🏽‍👧🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁨󠁵󠁳󠁴󠁿 Flag for Salgótarján (HU-ST)
🏴󠁴󠁲󠀳󠀶󠁿 Flag for Kars (TR-36)
👩🏽‍👦🏽‍👶🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁢󠁳󠁣󠁳󠁿 Flag for Central Andros (BS-CS)
☬ Adi Shakti
👩🏿‍👨🏿‍👧🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁭󠁫󠀲󠀴󠁿 Flag for Demir Kapija (MK-24)
🏴󠁭󠁴󠀳󠀱󠁿 Flag for Mġarr (MT-31)
🏴󠁫󠁺󠁺󠁡󠁰󠁿 Flag for West Kazakhstan (KZ-ZAP)
👩🏻‍👨🏻‍👧🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
🏴󠁡󠁵󠁴󠁡󠁳󠁿 Flag for Tasmania (AU-TAS)
👩🏽‍👨🏽‍👶🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👨🏾‍👶🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🗁 Open Folder
👩🏻‍👨🏻‍👶🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
👨‍👨‍👶‍👧 Family: Man, Man, Baby, Girl
🏴󠁭󠁹󠀰󠀲󠁿 Flag for Kedah (MY-02)
👩🏽‍👨🏽‍👶🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
🀪 Mahjong Tile Joker
👩🏻‍👨🏻‍👶🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🏴󠁭󠁥󠀰󠀶󠁿 Flag for Cetinje (ME-06)
👩🏼‍👩🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏿‍👨🏿‍👶🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
👩🏼‍👨🏼‍👶🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏿‍👨🏿‍👶🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁮󠁬󠁯󠁶󠁿 Flag for Overijssel (NL-OV)
🏴󠁨󠁴󠁳󠁥󠁿 Flag for Sud-Est (HT-SE)
👩🏿‍👩🏿‍👦🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁲󠁵󠁳󠁰󠁥󠁿 Flag for Saint Petersburg (RU-SPE)
👩🏾‍👩🏾‍👦🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁰󠁳󠁧󠁺󠁡󠁿 Flag for Gaza (PS-GZA)
🏴󠁰󠁡󠀸󠁿 Flag for Panamá (PA-8)
👩🏽‍👩🏽‍👦🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👩🏾‍👦🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👦🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
👩🏾‍👩🏾‍👦🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👨🏾‍👩🏾‍👦🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏻‍👩🏻‍👦🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
🏴󠁩󠁤󠁪󠁷󠁿 Flag for Java (ID-JW)
🗸 Light Check Mark
🏴󠁬󠁣󠀱󠀱󠁿 Flag for Vieux Fort (LC-11)
👨🏾‍👦🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🛈 Circled Information Source
👩🏻‍👩🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone
👨🏾‍👨🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁵󠁳󠁡󠁳󠁿 Flag for American Samoa (US-AS)
👩🏾‍👦🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👨🏾‍👩🏾‍👧🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩🏻‍👩🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone
🛊 Girls Symbol
👩🏾‍👩🏾‍👧🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🖾 Frame with an X
👩🏾‍👩🏾‍👧🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👧🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁴󠁲󠀲󠀸󠁿 Flag for Giresun (TR-28)
🏴󠁮󠁧󠁫󠁥󠁿 Flag for Kebbi (NG-KE)
👨🏻‍❤️‍💋‍👩🏼 Kiss - Man: Light Skin Tone, Woman: Medium-Light Skin Tone
👩🏿‍👧🏿‍👶🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁡󠁵󠁮󠁳󠁷󠁿 Flag for New South Wales (AU-NSW)
⛾ Cup On Black Square
🏴󠁣󠁮󠀳󠀴󠁿 Flag for Anhui (CN-34)
👩🏾‍👩🏾‍👶🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩🏻‍👩🏻‍👶🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
👩🏼‍👩🏼‍👶🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏽‍👩🏽‍👶🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
👩🏼‍👦🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏾‍👩🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👨‍❤️‍👨🏿 Couple With Heart - Man, Man: Dark Skin Tone
🏴󠁧󠁹󠁵󠁴󠁿 Flag for Upper Takutu-Upper Essequibo (GY-UT)
👩🏿‍👩🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁥󠁲󠁧󠁢󠁿 Flag for Gash-Barka (ER-GB)
👩🏽‍👩🏽‍👶🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
👩🏿‍👩🏿‍👶🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
👩🏼‍👩🏼‍👶🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏻‍👩🏻‍👶🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
🏴󠁬󠁡󠁢󠁫󠁿 Flag for Bokeo (LA-BK)
👩🏿‍👩🏿‍👶🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁡󠁬󠀰󠀷󠁿 Flag for Kukës County (AL-07)
🏴󠁴󠁭󠁭󠁿 Flag for Mary (TM-M)
🏴󠁰󠁷󠀳󠀵󠀰󠁿 Flag for Peleliu (PW-350)
🏴󠁬󠁲󠁢󠁭󠁿 Flag for Bomi (LR-BM)
🗍 Empty Pages
👩🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏻‍👨🏻‍👧🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
🏴󠁵󠁳󠁭󠁮󠁿 Flag for Minnesota (US-MN)
👩🏿‍👶🏿‍👧🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁭󠁴󠀶󠀵󠁿 Flag for Żebbuġ Gozo (MT-65)
🏴󠁴󠁲󠀸󠀰󠁿 Flag for Osmaniye (TR-80)
🏴󠁤󠁺󠀳󠀹󠁿 Flag for El Oued (DZ-39)
🗐 Pages
👩🏾‍👩🏾‍👶🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁩󠁤󠁭󠁬󠁿 Flag for Maluku Islands (ID-ML)
🖽 Frame with Tiles
🏴󠁴󠁺󠀲󠀵󠁿 Flag for Tanga (TZ-25)
🏴󠁤󠁫󠀸󠀳󠁿 Flag for Southern Denmark (DK-83)
👩🏿‍👩🏿‍👶🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
👩🏿‍👨🏿‍👧🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
👨🏽‍👧🏽‍👧🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁭󠁥󠀱󠀷󠁿 Flag for Rožaje (ME-17)
🏴󠁢󠁯󠁳󠁿 Flag for Santa Cruz (BO-S)
👨🏼‍❤️‍💋‍👨 Kiss - Man: Medium-Light Skin Tone, Man
🏴󠁡󠁬󠀰󠀴󠁿 Flag for Fier County (AL-04)
🏴󠁩󠁮󠁫󠁡󠁿 Flag for Karnataka (IN-KA)
🏴󠁳󠁣󠀰󠀹󠁿 Flag for Bel Air (SC-09)
🏴󠁭󠁸󠁣󠁨󠁰󠁿 Flag for Chiapas (MX-CHP)
🏴󠁩󠁮󠁴󠁮󠁿 Flag for Tamil Nadu (IN-TN)
🏴󠁬󠁲󠁲󠁧󠁿 Flag for River Gee (LR-RG)
🏴󠁰󠁴󠀰󠀲󠁿 Flag for Beja (PT-02)
🏴󠁭󠁫󠀸󠀵󠁿 Flag for Skopje (MK-85)
👨🏼‍❤️‍💋‍👩 Kiss - Man: Medium-Light Skin Tone, Woman
🏴󠁴󠁬󠁣󠁯󠁿 Flag for Cova Lima (TL-CO)
🏴󠁰󠁫󠁪󠁫󠁿 Flag for Azad Kashmir (PK-JK)
🏴󠁧󠁴󠁧󠁵󠁿 Flag for Guatemala (GT-GU)
🀝 Mahjong Tile Five of Circles
🗅 Empty Note
👩🏿‍👨🏿‍👦🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁣󠁵󠀰󠀳󠁿 Flag for Havana (CU-03)
🏴󠁬󠁣󠀰󠀸󠁿 Flag for Micoud (LC-08)
🏴󠁲󠁵󠁯󠁲󠁬󠁿 Flag for Oryol (RU-ORL)
👨🏿‍👨🏿‍👦🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
☶ Trigram for Mountain
🏴󠁣󠁮󠀱󠀵󠁿 Flag for Inner Mongolia (CN-15)
🏴󠁣󠁭󠁥󠁮󠁿 Flag for Far North (CM-EN)
🏴󠁦󠁲󠁢󠁦󠁣󠁿 Flag for Bourgogne-Franche-Comté (FR-BFC)
🏴󠁢󠁲󠁲󠁪󠁿 Flag for Rio de Janeiro (BR-RJ)
🏴󠁴󠁪󠁧󠁢󠁿 Flag for Gorno-Badakhshan (TJ-GB)
👨🏽‍👩🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁰󠁡󠀱󠀰󠁿 Flag for West Panamá (PA-10)
🏴󠁩󠁴󠀳󠀲󠁿 Flag for Trentino-South Tyrol (IT-32)
🏴󠁭󠁨󠁴󠁿 Flag for Ratak Chain (MH-T)
👨🏿‍👨🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁮󠁺󠁷󠁴󠁣󠁿 Flag for West Coast (NZ-WTC)
⛞ Falling Diagonal In White Circle In Black Square
🗠 Stock Chart
󠁴 Tag Latin Small Letter T
🏴󠁰󠁳󠁪󠁥󠁭󠁿 Flag for Jerusalem (PS-JEM)
🕴🏾‍♀️ Woman in Business Suit Levitating: Medium-Dark Skin Tone
🏴󠁲󠁵󠁰󠁥󠁲󠁿 Flag for Perm Krai (RU-PER)
👩‍👩‍👶 Family: Woman, Woman, Baby
󠁔 Tag Latin Capital Letter T
👩🏻‍❤️‍💋‍👩🏿 Kiss - Woman: Light Skin Tone, Woman: Dark Skin Tone
🏴󠁬󠁢󠁪󠁬󠁿 Flag for Mount Lebanon (LB-JL)
👩‍👩‍👶‍👶 Family: Woman, Woman, Baby, Baby
🏴󠁣󠁩󠁬󠁧󠁿 Flag for Lagunes (CI-LG)
🏴󠁡󠁵󠁷󠁡󠁿 Flag for Western Australia (AU-WA)
🏴󠁬󠁶󠀰󠀵󠀹󠁿 Flag for Madona (LV-059)
👩🏼‍👶🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🗖 Maximize
🏴󠁡󠁧󠀰󠀴󠁿 Flag for Saint John (AG-04)
🗮 Left Anger Bubble
🏴󠁦󠁲󠁭󠁦󠁿 Flag for St. Martin (FR-MF)
🏴󠁳󠁣󠀰󠀱󠁿 Flag for Anse aux Pins (SC-01)
👨‍👩‍👶 Family: Man, Woman, Baby
🏴󠁥󠁳󠁭󠁣󠁿 Flag for Murcia Region (ES-MC)
🏴󠁤󠁥󠁢󠁷󠁿 Flag for Baden-Württemberg (DE-BW)
🏴󠁵󠁳󠁴󠁮󠁿 Flag for Tennessee (US-TN)
🏴󠁤󠁥󠁢󠁥󠁿 Flag for Berlin (DE-BE)
🗧 Three Rays Right
🏴󠁴󠁭󠁢󠁿 Flag for Balkan (TM-B)
🗦 Three Rays Left
👩🏿‍👧🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁤󠁥󠁢󠁹󠁿 Flag for Bavaria (DE-BY)
🗔 Desktop Window
🏴󠁴󠁷󠁨󠁳󠁱󠁿 Flag for Hsinchu County (TW-HSQ)
🏴󠁬󠁴󠀵󠀸󠁿 Flag for Vilnius (LT-58)
󠁳 Tag Latin Small Letter S
👩🏻‍❤️‍💋‍👩🏾 Kiss - Woman: Light Skin Tone, Woman: Medium-Dark Skin Tone
🗏 Page
🏴󠁣󠁬󠁶󠁳󠁿 Flag for Valparaíso (CL-VS)
🏴󠁣󠁲󠁨󠁿 Flag for Heredia (CR-H)
👩🏽‍👧🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁷󠁳󠁡󠁬󠁿 Flag for Aiga-i-le-Tai (WS-AL)
🧕‍♀️ Woman With Headscarf
🗗 Overlap
🏴󠁮󠁧󠁢󠁯󠁿 Flag for Borno (NG-BO)
 Apple Logo
🗥 Three Rays Below
🖔 Reversed Victory Hand
🗤 Three Rays Above
🏴󠁵󠁳󠁮󠁪󠁿 Flag for New Jersey (US-NJ)
🏴󠁨󠁵󠁳󠁳󠁿 Flag for Szekszárd (HU-SS)
🖸 Optical Disc Icon
🏴󠁮󠁧󠁧󠁯󠁿 Flag for Gombe (NG-GO)
🏴󠁴󠁷󠁰󠁥󠁮󠁿 Flag for Penghu (TW-PEN)
👩🏽‍👶🏽‍👶🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁭󠁴󠀴󠀶󠁿 Flag for Rabat (MT-46)
👨🏼‍👨🏼‍👶🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁭󠁵󠁭󠁯󠁿 Flag for Moka (MU-MO)
🏴󠁫󠁥󠀳󠀱󠁿 Flag for Nakuru (KE-31)
🏴󠁡󠁧󠀱󠀱󠁿 Flag for Redonda (AG-11)
👨🏻‍👨🏻‍👧🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁤󠁺󠀲󠀹󠁿 Flag for Mascara (DZ-29)
🗚 Increase Font Size Symbol
🏴󠁡󠁧󠀰󠀶󠁿 Flag for Saint Paul (AG-06)
🏴󠁣󠁺󠀵󠀳󠁿 Flag for Pardubický kraj (CZ-53)
🏴󠁵󠁳󠁶󠁴󠁿 Flag for Vermont (US-VT)
🏴󠁶󠁥󠁧󠁿 Flag for Carabobo (VE-G)
🧟🏽‍♂️ Man Zombie: Medium Skin Tone
🖵 Screen
🏴󠁣󠁺󠀴󠀲󠁿 Flag for Ústecký kraj (CZ-42)
🏴󠁭󠁤󠁳󠁮󠁿 Flag for Transnistria (MD-SN)
🏴󠁫󠁩󠁧󠁿 Flag for Gilbert Islands (KI-G)
󠀨 Tag Left Parenthesis
👩🏽‍👧🏽‍👶🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁡󠁧󠀰󠀵󠁿 Flag for Saint Mary (AG-05)
🀀 Mahjong Tile East Wind
🏴󠁯󠁭󠁷󠁵󠁿 Flag for Al Wusta (OM-WU)
👩🏽‍👩🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone
👨🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁮󠁩󠁭󠁳󠁿 Flag for Masaya (NI-MS)
🗉 Note Page
🏴󠁩󠁲󠀰󠀷󠁿 Flag for Tehran (IR-07)
🏴󠁭󠁹󠀱󠀴󠁿 Flag for Kuala Lumpur (MY-14)
🗕 Minimize
🏴󠁲󠁵󠁤󠁡󠁿 Flag for Dagestan (RU-DA)
🏴󠁶󠁮󠀵󠀱󠁿 Flag for Trà Vinh (VN-51)
🏴󠁭󠁤󠁧󠁡󠁿 Flag for Gagauzia (MD-GA)
🏴󠁫󠁨󠀴󠁿 Flag for Kampong Chhnang (KH-4)
👩🏽‍👶🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁥󠁣󠁺󠁿 Flag for Zamora-Chinchipe (EC-Z)
󠀪 Tag Asterisk
🏴󠁫󠁥󠀱󠀹󠁿 Flag for Kwale (KE-19)
🏴󠁰󠁥󠁡󠁹󠁡󠁿 Flag for Ayacucho (PE-AYA)
🏴󠁤󠁫󠀸󠀱󠁿 Flag for Northern Denmark (DK-81)
🏴󠁡󠁧󠀰󠀸󠁿 Flag for Saint Philip (AG-08)
🏴󠁭󠁴󠀲󠀹󠁿 Flag for Mdina (MT-29)
🏴󠁴󠁧󠁫󠁿 Flag for Kara (TG-K)
🏴󠁤󠁭󠀰󠀶󠁿 Flag for Saint Joseph (DM-06)
🏴󠁮󠁬󠁬󠁩󠁿 Flag for Limburg (NL-LI)
🏴󠁦󠁲󠁡󠁲󠁡󠁿 Flag for Auvergne-Rhône-Alpes (FR-ARA)
🏴󠁴󠁲󠀴󠀲󠁿 Flag for Konya (TR-42)
🏲 Black Pennant
🏴󠁨󠁵󠁣󠁳󠁿 Flag for Csongrád (HU-CS)
🗌 Empty Page
👨🏿‍👶🏿‍👧🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🗈 Note
󠁥 Tag Latin Small Letter E
🖷 Fax Icon
👩🏾‍👧🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏼‍👶🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁴󠁷󠁮󠁡󠁮󠁿 Flag for Nantou (TW-NAN)
🏴󠁩󠁴󠀲󠀵󠁿 Flag for Lombardy (IT-25)
🏴󠁳󠁳󠁢󠁮󠁿 Flag for Northern Bahr el Ghazal (SS-BN)
🗎 Document
🏴󠁣󠁯󠁶󠁩󠁤󠁿 Flag for Vichada (CO-VID)
🏴󠁬󠁫󠀵󠁿 Flag for Eastern (LK-5)
🏴󠁡󠁦󠁺󠁡󠁢󠁿 Flag for Zabul (AF-ZAB)
🏴󠁭󠁹󠀱󠀰󠁿 Flag for Selangor (MY-10)
🏴󠁳󠁯󠁢󠁹󠁿 Flag for Bay, Somalia (SO-BY)
🏴󠁬󠁵󠁥󠁳󠁿 Flag for Esch-sur-Alzette (LU-ES)
🏴󠁡󠁦󠁰󠁩󠁡󠁿 Flag for Paktia (AF-PIA)
🏴󠁢󠁳󠁢󠁹󠁿 Flag for Berry Islands (BS-BY)
🏴󠁮󠁧󠁯󠁧󠁿 Flag for Ogun (NG-OG)
🏴󠁮󠁺󠁮󠁳󠁮󠁿 Flag for Nelson (NZ-NSN)
🏴󠁡󠁥󠁲󠁫󠁿 Flag for Ras al-Khaimah (AE-RK)
🏴󠁵󠁳󠁡󠁺󠁿 Flag for Arizona (US-AZ)
󠁰 Tag Latin Small Letter P
🀌 Mahjong Tile Six of Characters
🏴󠁪󠁰󠀴󠀴󠁿 Flag for Ōita (JP-44)
🏴󠁴󠁶󠁮󠁫󠁬󠁿 Flag for Nukulaelae (TV-NKL)
👨🏼‍👨🏼‍👧🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏼‍❤️‍👨🏻 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Light Skin Tone
🏴󠁵󠁳󠁮󠁣󠁿 Flag for North Carolina (US-NC)
󠀳 Tag Digit Three
󠀵 Tag Digit Five
🏴󠁢󠁧󠀰󠀴󠁿 Flag for Veliko Tarnovo (BG-04)
🏴󠁢󠁲󠁭󠁳󠁿 Flag for Mato Grosso do Sul (BR-MS)
🏴󠁩󠁴󠀷󠀷󠁿 Flag for Basilicata (IT-77)
🏴󠁬󠁹󠁪󠁩󠁿 Flag for Jafara (LY-JI)
🏴󠁡󠁦󠁵󠁲󠁵󠁿 Flag for Urozgan (AF-URU)
🏴󠁥󠁴󠁳󠁯󠁿 Flag for Somali (ET-SO)
⛥ Right-Handed Interlaced Pentagram
🏴󠁮󠁬󠁮󠁢󠁿 Flag for North Brabant (NL-NB)
👩🏽‍👩🏽‍👧🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
👨🏻‍👦🏻‍👧🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
🏴󠁡󠁦󠁬󠁡󠁧󠁿 Flag for Laghman (AF-LAG)
🏴󠁺󠁡󠁮󠁷󠁿 Flag for North West (ZA-NW)
🗆 Empty Note Page
🏴󠁣󠁦󠁢󠁫󠁿 Flag for Basse-Kotto (CF-BK)
⚉ Black Circle with Two White Dots
🏴󠁡󠁦󠁮󠁵󠁲󠁿 Flag for Nuristan (AF-NUR)
👨🏾‍👨🏾‍👦🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
󠀣 Tag Number Sign
🏴󠁧󠁴󠁳󠁲󠁿 Flag for Santa Rosa (GT-SR)
🗀 Folder
󠁞 Tag Circumflex Accent
🏴󠁮󠁬󠁧󠁲󠁿 Flag for Groningen (NL-GR)
👩🏻‍👨🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone
🏴󠁡󠁦󠁰󠁫󠁡󠁿 Flag for Paktika (AF-PKA)
🀛 Mahjong Tile Three of Circles
🏴󠁷󠁳󠁦󠁡󠁿 Flag for Fa’asaleleaga (WS-FA)
👨‍👶 Family: Man, Baby
🏴󠁢󠁲󠁭󠁴󠁿 Flag for Mato Grosso (BR-MT)
👨🏿‍👨🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁳󠁶󠁳󠁶󠁿 Flag for San Vicente (SV-SV)
🏴󠁰󠁥󠁬󠁩󠁭󠁿 Flag for Lima Region (PE-LIM)
🏴󠁣󠁮󠀱󠀳󠁿 Flag for Hebei (CN-13)
🏴󠁮󠁺󠁢󠁯󠁰󠁿 Flag for Bay of Plenty (NZ-BOP)
🧟🏿‍♀️ Woman Zombie: Dark Skin Tone
🏴󠁩󠁮󠁨󠁲󠁿 Flag for Haryana (IN-HR)
🏴󠁳󠁩󠀱󠀰󠀰󠁿 Flag for Radenci (SI-100)
󠁱 Tag Latin Small Letter Q
🏴󠁳󠁩󠀱󠀵󠀱󠁿 Flag for Braslovče (SI-151)
🏴󠁩󠁲󠀳󠀲󠁿 Flag for Alborz (IR-32)
👨🏼‍👨🏼‍👶🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👨🏻‍👨🏻‍👶🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
󠁒 Tag Latin Capital Letter R
🏴󠁳󠁤󠁮󠁢󠁿 Flag for Blue Nile (SD-NB)
🗷 Ballot Box with Bold Script X
🏴󠁺󠁡󠁮󠁬󠁿 Flag for KwaZulu-Natal (ZA-NL)
🏴󠁵󠁳󠁩󠁤󠁿 Flag for Idaho (US-ID)
🏴󠁧󠁲󠁪󠁿 Flag for Peloponnese (GR-J)
🏴󠁢󠁩󠁭󠁷󠁿 Flag for Mwaro (BI-MW)
🏴󠁭󠁴󠀴󠀸󠁿 Flag for St. Julian’s (MT-48)
🏴󠁥󠁳󠁣󠁥󠁿 Flag for Ceuta (ES-CE)
🏴󠁭󠁸󠁣󠁯󠁬󠁿 Flag for Colima (MX-COL)
🖻 Document with Picture
🏴󠁣󠁡󠁮󠁬󠁿 Flag for Newfoundland and Labrador (CA-NL)
🏴󠁮󠁬󠁳󠁸󠁿 Flag for Sint Maarten (NL-SX)
🏴󠁮󠁧󠁡󠁤󠁿 Flag for Adamawa (NG-AD)
👩‍👩‍👧‍👶 Family: Woman, Woman, Girl, Baby
👩🏼‍👨🏼‍👧🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁰󠁧󠁥󠁢󠁲󠁿 Flag for East New Britain (PG-EBR)
🏴󠁬󠁫󠀹󠁿 Flag for Sabaragamuwa (LK-9)
🏴󠁬󠁶󠀰󠀱󠀰󠁿 Flag for Auce (LV-010)
👩🏽‍👩🏽‍👦🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👩🏿‍👨🏿‍👧🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁳󠁴󠁳󠁿 Flag for São Tomé (ST-S)
🏴󠁣󠁯󠁣󠁵󠁮󠁿 Flag for Cundinamarca (CO-CUN)
🏴󠁲󠁵󠁳󠁴󠁡󠁿 Flag for Stavropol Krai (RU-STA)
🏴󠁬󠁹󠁢󠁵󠁿 Flag for Butnan (LY-BU)
🏴󠁭󠁵󠁧󠁰󠁿 Flag for Grand Port (MU-GP)
👩🏻‍👨🏻‍👧🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁬󠁲󠁧󠁧󠁿 Flag for Grand Gedeh (LR-GG)
🏴󠁰󠁨󠀱󠀵󠁿 Flag for Cordillera Administrative (PH-15)
🏴󠁣󠁡󠁳󠁫󠁿 Flag for Saskatchewan (CA-SK)
👩🏻‍👩🏻‍👧🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
👨🏻‍❤️‍👩🏽 Couple With Heart - Man: Light Skin Tone, Woman: Medium Skin Tone
👨🏼‍👨🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🤵‍♀️ Woman in Tuxedo
👨🏾‍👨🏾‍👶🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏾‍👧🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👨🏽‍❤️‍💋‍👩 Kiss - Man: Medium Skin Tone, Woman
🏴󠁭󠁡󠀱󠀳󠁿 Flag for Souss-Massa-Drâa (MA-13)
🏴󠁩󠁴󠀷󠀲󠁿 Flag for Campania (IT-72)
🏴󠁡󠁦󠁳󠁡󠁭󠁿 Flag for Samangan (AF-SAM)
🏴󠁩󠁮󠁡󠁰󠁿 Flag for Andhra Pradesh (IN-AP)
👨🏿‍👩🏿‍👧🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁫󠁲󠀴󠀹󠁿 Flag for Jeju (KR-49)
🏴󠁬󠁶󠀰󠀳󠀷󠁿 Flag for Inčukalns (LV-037)
🏴󠁧󠁥󠁫󠁡󠁿 Flag for Kakheti (GE-KA)
🏴󠁩󠁲󠀲󠀴󠁿 Flag for Hamadan (IR-24)
👨‍👩‍👶‍👧 Family: Man, Woman, Baby, Girl
🏴󠁲󠁵󠁡󠁤󠁿 Flag for Adygea (RU-AD)
👩🏿‍👩🏿‍👧🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁲󠁢󠁡󠁿 Flag for Bahia (BR-BA)
🏴󠁲󠁳󠀱󠀴󠁿 Flag for Bor (RS-14)
🧕🏼‍♂️ Man With Headscarf: Medium-Light Skin Tone
🏴󠁴󠁶󠁮󠁭󠁧󠁿 Flag for Nanumanga (TV-NMG)
🧟🏽‍♀️ Woman Zombie: Medium Skin Tone
👨🏽‍👦🏽‍👦🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👩🏽‍👧🏽‍👧🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
🕬 Bullhorn with Sound Waves
🏴󠁳󠁥󠁮󠁿 Flag for Halland (SE-N)
🏴󠁣󠁨󠁴󠁩󠁿 Flag for Ticino (CH-TI)
👩🏻‍👶🏻‍👶🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
󠁯 Tag Latin Small Letter O
🏴󠁡󠁥󠁡󠁺󠁿 Flag for Abu Dhabi (AE-AZ)
🏴󠁳󠁩󠀱󠀹󠀲󠁿 Flag for Žirovnica (SI-192)
🏴󠁩󠁮󠁣󠁴󠁿 Flag for Chhattisgarh (IN-CT)
👩🏻‍👩🏻‍👧🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
👩🏾‍👧🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁭󠁬󠁢󠁫󠁯󠁿 Flag for Bamako (ML-BKO)
🏴󠁡󠁦󠁮󠁩󠁭󠁿 Flag for Nimruz (AF-NIM)
🏴󠁭󠁸󠁲󠁯󠁯󠁿 Flag for Quintana Roo (MX-ROO)
☟ White Down Pointing Index
🏴󠁴󠁧󠁭󠁿 Flag for Maritime (TG-M)
🏴󠁡󠁥󠁦󠁵󠁿 Flag for Fujairah (AE-FU)
🧟🏼‍♀️ Woman Zombie: Medium-Light Skin Tone
🏴󠁩󠁳󠀳󠁿 Flag for Western (IS-3)
👩🏿‍👩🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone
⛗ White Two-Way Left Way Traffic
🏴󠁨󠁲󠀰󠀴󠁿 Flag for Karlovac (HR-04)
🏴󠁴󠁮󠀱󠀳󠁿 Flag for Ben Arous (TN-13)
🏴󠁨󠁵󠁧󠁳󠁿 Flag for Győr-Moson-Sopron (HU-GS)
🏴󠁡󠁦󠁰󠁡󠁲󠁿 Flag for Parwan (AF-PAR)
🏴󠁰󠁧󠁷󠁢󠁫󠁿 Flag for West New Britain (PG-WBK)
🏴󠁧󠁹󠁵󠁤󠁿 Flag for Upper Demerara-Berbice (GY-UD)
🏴󠁤󠁥󠁲󠁰󠁿 Flag for Rhineland-Palatinate (DE-RP)
👩🏽‍❤️‍💋‍👩🏾 Kiss - Woman: Medium Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁥󠁴󠁡󠁦󠁿 Flag for Afar (ET-AF)
🏴󠁡󠁦󠁮󠁡󠁮󠁿 Flag for Nangarhar (AF-NAN)
🏴󠁢󠁮󠁢󠁭󠁿 Flag for Brunei-Muara (BN-BM)
󠀷 Tag Digit Seven
🏴󠁭󠁣󠁭󠁯󠁿 Flag for Monaco-Ville (MC-MO)
🕴🏻‍♀️ Woman in Business Suit Levitating: Light Skin Tone
🏴󠁳󠁯󠁢󠁮󠁿 Flag for Banaadir (SO-BN)
🏴󠁳󠁳󠁥󠁣󠁿 Flag for Central Equatoria (SS-EC)
🏴󠁡󠁦󠁫󠁨󠁯󠁿 Flag for Khost (AF-KHO)
🏴󠁢󠁳󠁢󠁰󠁿 Flag for Black Point (BS-BP)
🏴󠁥󠁲󠁤󠁫󠁿 Flag for Southern Red Sea (ER-DK)
🏴󠁳󠁮󠁳󠁬󠁿 Flag for Saint-Louis (SN-SL)
🏴󠁢󠁺󠁯󠁷󠁿 Flag for Orange Walk (BZ-OW)
7️ Digit Seven
󠀹 Tag Digit Nine
🏴󠁭󠁭󠀱󠀷󠁿 Flag for Shan (MM-17)
🏴󠁬󠁡󠁫󠁨󠁿 Flag for Khammouane (LA-KH)
🖭 Tape Cartridge
🧟🏻‍♀️ Woman Zombie: Light Skin Tone
*️ Asterisk
🏴󠁪󠁰󠀱󠀸󠁿 Flag for Fukui (JP-18)
🏴󠁣󠁨󠁢󠁥󠁿 Flag for Bern (CH-BE)
🏴󠁫󠁲󠀲󠀷󠁿 Flag for Daegu (KR-27)
👨🏻‍👩🏻‍👶🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🏴󠁩󠁲󠀱󠀵󠁿 Flag for Kerman (IR-15)
🧕🏽‍♂️ Man With Headscarf: Medium Skin Tone
🏴󠁯󠁭󠁢󠁵󠁿 Flag for Al Buraimi (OM-BU)
🏴󠁩󠁮󠁤󠁮󠁿 Flag for Dadra and Nagar Haveli (IN-DN)
👩🏼‍❤️‍👩🏿 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Dark Skin Tone
👩‍❤️‍👨🏽 Couple With Heart - Woman, Man: Medium Skin Tone
🏴󠁡󠁥󠁤󠁵󠁿 Flag for Dubai (AE-DU)
👩🏻‍👩🏻‍👦🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
👨🏻‍👩🏻‍👦🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
🖯 One Button Mouse
👨🏽‍❤️‍👩🏾 Couple With Heart - Man: Medium Skin Tone, Woman: Medium-Dark Skin Tone
🖪 Black Hard Shell Floppy Disk
🖳 Old Personal Computer
👩🏼‍👨🏼‍👦🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👨🏻‍👩🏻‍👧🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
⚑ Black Flag
🏴󠁵󠁳󠁮󠁶󠁿 Flag for Nevada (US-NV)
👨🏻‍👩🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone
👩🏽‍👧🏽‍👦🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
󠁍 Tag Latin Capital Letter M
🏴󠁵󠁳󠁴󠁸󠁿 Flag for Texas (US-TX)
🏴󠁵󠁳󠁰󠁲󠁿 Flag for Puerto Rico (US-PR)
🏴󠁢󠁲󠁥󠁳󠁿 Flag for Espírito Santo (BR-ES)
🏴󠁪󠁰󠀱󠀳󠁿 Flag for Tokyo (JP-13)
🏴󠁷󠁦󠁡󠁬󠁿 Flag for Alo (WF-AL)
🏴󠁭󠁵󠁡󠁧󠁿 Flag for Agaléga (MU-AG)
🏴󠁰󠁷󠀱󠀰󠀰󠁿 Flag for Kayangel (PW-100)
🏴󠁡󠁦󠁬󠁯󠁧󠁿 Flag for Logar (AF-LOG)
🕃 Notched Left Semicircle with Three Dots
👨🏻‍❤️‍👨🏾 Couple With Heart - Man: Light Skin Tone, Man: Medium-Dark Skin Tone
🀍 Mahjong Tile Seven of Characters
👩🏾‍❤️‍💋‍👨 Kiss - Woman: Medium-Dark Skin Tone, Man
🖰 Two Button Mouse
🏴󠁣󠁺󠀷󠀲󠁿 Flag for Zlínský kraj (CZ-72)
🏴󠁣󠁯󠁴󠁯󠁬󠁿 Flag for Tolima (CO-TOL)
👩🏾‍👨🏾‍👶🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁡󠁦󠁤󠁡󠁹󠁿 Flag for Daykundi (AF-DAY)
󠀾 Tag Greater-Than Sign
🏴󠁣󠁨󠁧󠁥󠁿 Flag for Geneva (CH-GE)
👨🏿‍👩🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone
󠁭 Tag Latin Small Letter M
🏴󠁡󠁦󠁫󠁮󠁲󠁿 Flag for Kunar (AF-KNR)
🏴󠁣󠁤󠁢󠁵󠁿 Flag for Bas-Uélé (CD-BU)
🏴󠁶󠁥󠁸󠁿 Flag for Vargas (VE-X)
🏴󠁢󠁲󠁰󠁢󠁿 Flag for Paraíba (BR-PB)
🏴󠁵󠁳󠁳󠁤󠁿 Flag for South Dakota (US-SD)
🖧 Three Networked Computers
🗇 Empty Note Pad
🏴󠁩󠁲󠀲󠀰󠁿 Flag for Lorestan (IR-20)
🧟🏾‍♂️ Man Zombie: Medium-Dark Skin Tone
🏴󠁥󠁥󠀳󠀹󠁿 Flag for Hiiu (EE-39)
🏴󠁳󠁩󠀱󠀵󠀸󠁿 Flag for Grad (SI-158)
🏴󠁳󠁶󠁳󠁭󠁿 Flag for San Miguel (SV-SM)
🏴󠁴󠁲󠀶󠀱󠁿 Flag for Trabzon (TR-61)
🏴󠁢󠁲󠁳󠁰󠁿 Flag for São Paulo (BR-SP)
🏴󠁳󠁩󠀱󠀸󠀷󠁿 Flag for Velika Polana (SI-187)
🏴󠁢󠁤󠁣󠁿 Flag for Dhaka Division (BD-C)
🏴󠁤󠁫󠀸󠀲󠁿 Flag for Central Denmark (DK-82)
🏴󠁡󠁲󠁹󠁿 Flag for Jujuy (AR-Y)
🏴󠁩󠁴󠀶󠀲󠁿 Flag for Lazio (IT-62)
🏴󠁢󠁤󠁦󠁿 Flag for Rangpur Division (BD-F)
🏴󠁡󠁲󠁢󠁿 Flag for Buenos Aires Province (AR-B)
🏴󠁢󠁦󠀱󠀱󠁿 Flag for Plateau-Central (BF-11)
🏴󠁲󠁵󠁡󠁲󠁫󠁿 Flag for Arkhangelsk (RU-ARK)
🏴󠁢󠁧󠀰󠀵󠁿 Flag for Vidin (BG-05)
🏴󠁢󠁧󠀰󠀳󠁿 Flag for Varna (BG-03)
🏴󠁢󠁦󠀰󠀵󠁿 Flag for Centre-Nord (BF-05)
🏴󠁡󠁬󠀰󠀳󠁿 Flag for Elbasan County (AL-03)
🏴󠁢󠁦󠀰󠀷󠁿 Flag for Centre-Sud (BF-07)
♜ Black Chess Rook
🏴󠁡󠁦󠁢󠁤󠁳󠁿 Flag for Badakhshan (AF-BDS)
👨🏿‍👩🏿‍👦🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁧󠁤󠀰󠀶󠁿 Flag for Saint Patrick (GD-06)
👩🏽‍❤️‍💋‍👨🏽 Kiss - Woman: Medium Skin Tone, Man: Medium Skin Tone
👩🏾‍👩🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
♘ White Chess Knight
🏴󠁩󠁲󠀱󠀶󠁿 Flag for Kurdistan (IR-16)
👩🏿‍👶🏿‍👦🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁧󠀰󠀸󠁿 Flag for Dobrich (BG-08)
🏴󠁢󠁦󠀰󠀴󠁿 Flag for Centre-Est (BF-04)
🏴󠁢󠁧󠀰󠀷󠁿 Flag for Gabrovo (BG-07)
👨🏽‍❤️‍👩🏿 Couple With Heart - Man: Medium Skin Tone, Woman: Dark Skin Tone
🏴󠁳󠁩󠀰󠀵󠀰󠁿 Flag for Koper (SI-050)
🏴󠁢󠁤󠁧󠁿 Flag for Sylhet Division (BD-G)
🏴󠁵󠁳󠁣󠁡󠁿 Flag for California (US-CA)
👨🏿‍❤️‍👨🏿 Couple With Heart - Man: Dark Skin Tone, Man: Dark Skin Tone
🀇 Mahjong Tile One of Characters
👩🏽‍❤️‍👨🏻 Couple With Heart - Woman: Medium Skin Tone, Man: Light Skin Tone
🏴󠁡󠁵󠁮󠁴󠁿 Flag for Northern Territory (AU-NT)
🏴󠁢󠁦󠀰󠀶󠁿 Flag for Centre-Ouest (BF-06)
🏴󠁢󠁥󠁢󠁲󠁵󠁿 Flag for Brussels (BE-BRU)
🏴󠁤󠁺󠀱󠀶󠁿 Flag for Algiers (DZ-16)
🏴󠁢󠁦󠀰󠀸󠁿 Flag for Est (BF-08)
🏴󠁡󠁺󠁳󠁭󠁿 Flag for Sumqayit (AZ-SM)
👨🏻‍❤️‍💋‍👩🏿 Kiss - Man: Light Skin Tone, Woman: Dark Skin Tone
👨🏽‍👨🏽‍👦🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁢󠁯󠁴󠁿 Flag for Tarija (BO-T)
🏴󠁳󠁩󠀰󠀵󠀸󠁿 Flag for Lenart (SI-058)
🏴󠁰󠁫󠁢󠁡󠁿 Flag for Balochistan (PK-BA)
⛭ Gear Without Hub
👩‍❤️‍💋‍👩🏽 Kiss - Woman, Woman: Medium Skin Tone
👨🏿‍❤️‍👩🏻 Couple With Heart - Man: Dark Skin Tone, Woman: Light Skin Tone
🏴󠁲󠁵󠁴󠁡󠁿 Flag for Tatarstan (RU-TA)
🏴󠁢󠁤󠁨󠁿 Flag for Mymensingh Division (BD-H)
⚀ Die Face-1
🏴󠁣󠁬󠁬󠁩󠁿 Flag for Libertador General Bernardo O’Higgins (CL-LI)
👨🏼‍👩🏼‍👶🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨🏽‍👨🏽‍👶🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👨🏼‍👨🏼‍👦🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏾‍❤️‍👩🏽 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Medium Skin Tone
👨🏻‍👨🏻‍👦🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
🏴󠁢󠁧󠀱󠀱󠁿 Flag for Lovech (BG-11)
🏴󠁢󠁦󠀰󠀲󠁿 Flag for Cascades (BF-02)
🏴󠁢󠁧󠀱󠀴󠁿 Flag for Pernik (BG-14)
👨🏾‍❤️‍💋‍👩🏾 Kiss - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
🖩 Pocket Calculator
🏴󠁢󠁧󠀱󠀰󠁿 Flag for Kyustendil (BG-10)
🏴󠁢󠁧󠀱󠀳󠁿 Flag for Pazardzhik (BG-13)
👨🏿‍👩🏿‍👧🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁰󠁡󠀷󠁿 Flag for Los Santos (PA-7)
👩🏽‍❤️‍💋‍👨🏼 Kiss - Woman: Medium Skin Tone, Man: Medium-Light Skin Tone
🏴󠁢󠁦󠀰󠀱󠁿 Flag for Boucle du Mouhoun (BF-01)
👩🏾‍👨🏾‍👶🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁡󠁭󠁶󠁤󠁿 Flag for Vayots Dzor (AM-VD)
🏴󠁢󠁳󠁬󠁩󠁿 Flag for Long Island (BS-LI)
🏴󠁢󠁦󠀰󠀳󠁿 Flag for Centre (BF-03)
👨🏽‍👶🏽‍👶🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
☳ Trigram for Thunder
🏴󠁡󠁯󠁣󠁮󠁮󠁿 Flag for Cunene (AO-CNN)
🏴󠁥󠁳󠁣󠁮󠁿 Flag for Canary Islands (ES-CN)
👩‍👨‍👧‍👧 Family: Woman, Man, Girl, Girl
🏴󠁢󠁤󠁥󠁿 Flag for Rajshahi Division (BD-E)
👩🏼‍👩🏼‍👶🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨🏿‍❤️‍👩🏿 Couple With Heart - Man: Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁢󠁲󠁭󠁧󠁿 Flag for Minas Gerais (BR-MG)
🏴󠁢󠁧󠀱󠀷󠁿 Flag for Razgrad (BG-17)
󠀦 Tag Ampersand
🏴󠁢󠁡󠁳󠁲󠁰󠁿 Flag for Republika Srpska (BA-SRP)
🏴󠁢󠁧󠀱󠀵󠁿 Flag for Pleven (BG-15)
🏴󠁤󠁺󠀳󠀴󠁿 Flag for Bordj Bou Arréridj (DZ-34)
🏴󠁢󠁧󠀱󠀶󠁿 Flag for Plovdiv (BG-16)
🏴󠁲󠁵󠁣󠁨󠁵󠁿 Flag for Chukotka Okrug (RU-CHU)
🏴󠁢󠁦󠀱󠀰󠁿 Flag for Nord (BF-10)
👩‍👶‍👶 Family: Woman, Baby, Baby
🏴󠁢󠁢󠀰󠀹󠁿 Flag for Saint Peter (BB-09)
🏴󠁢󠁤󠁤󠁿 Flag for Khulna Division (BD-D)
👨🏿‍❤️‍👨 Couple With Heart - Man: Dark Skin Tone, Man
🏴󠁣󠁩󠁶󠁢󠁿 Flag for Vallée du Bandama (CI-VB)
🏴󠁡󠁴󠀳󠁿 Flag for Lower Austria (AT-3)
🏴󠁦󠁲󠁴󠁦󠁿 Flag for French Southern Territories (FR-TF)
🧕🏼‍♀️ Woman With Headscarf: Medium-Light Skin Tone
🏴󠁳󠁡󠀰󠀵󠁿 Flag for Al-Qassim (SA-05)
☓ Saltire
󠀯 Tag Solidus
🏴󠁣󠁡󠁢󠁣󠁿 Flag for British Columbia (CA-BC)
🏴󠁢󠁧󠀰󠀱󠁿 Flag for Blagoevgrad (BG-01)
🀎 Mahjong Tile Eight of Characters
🏴󠁥󠁳󠁡󠁮󠁿 Flag for Andalusia (ES-AN)
🖙 Sideways White Right Pointing Index
🏴󠁢󠁧󠀲󠀳󠁿 Flag for Sofia District (BG-23)
👨🏽‍👨🏽‍👧🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁢󠁧󠀲󠀵󠁿 Flag for Targovishte (BG-25)
🏴󠁡󠁺󠁺󠁡󠁮󠁿 Flag for Zangilan (AZ-ZAN)
🏴󠁢󠁧󠀲󠀲󠁿 Flag for Sofia (BG-22)
🏴󠁪󠁭󠀰󠀱󠁿 Flag for Kingston (JM-01)
🏴󠁮󠁧󠁹󠁯󠁿 Flag for Yobe (NG-YO)
🏴󠁢󠁤󠁡󠁿 Flag for Barisal (BD-A)
👨🏻‍❤️‍👩 Couple With Heart - Man: Light Skin Tone, Woman
🛲 Diesel Locomotive
👨🏼‍👨🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
♯ Music Sharp Sign
👨🏻‍❤️‍💋‍👩🏾 Kiss - Man: Light Skin Tone, Woman: Medium-Dark Skin Tone
👨🏻‍👩🏻‍👶🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
🏴󠁡󠁺󠁺󠁡󠁲󠁿 Flag for Zardab (AZ-ZAR)
🏴󠁢󠁢󠀰󠀳󠁿 Flag for Saint George (BB-03)
👩🏽‍👦🏽‍👧🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁶󠁣󠀰󠀴󠁿 Flag for Saint George (VC-04)
󠀼 Tag Less-Than Sign
🏴󠁢󠁢󠀱󠀰󠁿 Flag for Saint Philip (BB-10)
🏴󠁡󠁦󠁷󠁡󠁲󠁿 Flag for Maidan Wardak (AF-WAR)
👩🏻‍👶🏻‍👦🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
󠁜 Tag Reverse Solidus
🏴󠁢󠁹󠁢󠁲󠁿 Flag for Brest (BY-BR)
👨🏾‍❤️‍👨🏽 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Medium Skin Tone
🏴󠁦󠁲󠁭󠁱󠁿 Flag for Martinique (FR-MQ)
🧕🏽‍♀️ Woman With Headscarf: Medium Skin Tone
󠁑 Tag Latin Capital Letter Q
🏴󠁡󠁺󠁳󠁫󠁲󠁿 Flag for Shamkir (AZ-SKR)
♧ White Club Suit
🏴󠁩󠁳󠀸󠁿 Flag for Southern (IS-8)
🏴󠁢󠁢󠀰󠀷󠁿 Flag for Saint Lucy (BB-07)
🏴󠁭󠁣󠁳󠁲󠁿 Flag for Saint Roman (MC-SR)
♺ Recycling Symbol for Generic Materials
🏴󠁢󠁧󠀲󠀸󠁿 Flag for Yambol (BG-28)
🏴󠁫󠁧󠁢󠁿 Flag for Batken (KG-B)
🏴󠁪󠁭󠀰󠀴󠁿 Flag for Portland (JM-04)
🏴󠁵󠁳󠁩󠁮󠁿 Flag for Indiana (US-IN)
🏴󠁬󠁩󠀰󠀷󠁿 Flag for Schaan (LI-07)
🏴󠁢󠁢󠀰󠀶󠁿 Flag for Saint Joseph (BB-06)
👨🏽‍👩🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone
👨‍👩‍👶‍👦 Family: Man, Woman, Baby, Boy
🏴󠁦󠁲󠁢󠁲󠁥󠁿 Flag for Bretagne (FR-BRE)
🏴󠁢󠁢󠀰󠀵󠁿 Flag for Saint John (BB-05)
🏴󠁬󠁫󠀱󠁿 Flag for Western (LK-1)
🏴󠁢󠁧󠀲󠀶󠁿 Flag for Haskovo (BG-26)
👩🏽‍👩🏽‍👧🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
👨🏿‍👩🏿‍👶🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🖆 Pen Over Stamped Envelope
🏴󠁲󠁯󠁢󠁴󠁿 Flag for Botoşani (RO-BT)
🏴󠁢󠁢󠀰󠀴󠁿 Flag for Saint James (BB-04)
🏴󠁢󠁩󠁢󠁢󠁿 Flag for Bubanza (BI-BB)
🏴󠁣󠁯󠁱󠁵󠁩󠁿 Flag for Quindío (CO-QUI)
👨‍👨‍👶‍👶 Family: Man, Man, Baby, Baby
👨‍❤️‍👩🏽 Couple With Heart - Man, Woman: Medium Skin Tone
👩🏻‍❤️‍👩 Couple With Heart - Woman: Light Skin Tone, Woman
󠁧 Tag Latin Small Letter G
👨🏾‍❤️‍👩🏼 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁢󠁨󠀱󠀷󠁿 Flag for Northern (BH-17)
👨🏻‍👦🏻‍👶🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
👩🏻‍❤️‍👨🏿 Couple With Heart - Woman: Light Skin Tone, Man: Dark Skin Tone
🏴󠁲󠁯󠁳󠁢󠁿 Flag for Sibiu (RO-SB)
🏴󠁢󠁢󠀰󠀲󠁿 Flag for Saint Andrew (BB-02)
🏴󠁢󠁨󠀱󠀴󠁿 Flag for Southern (BH-14)
👨🏽‍❤️‍💋‍👩🏽 Kiss - Man: Medium Skin Tone, Woman: Medium Skin Tone
👨🏽‍❤️‍👩 Couple With Heart - Man: Medium Skin Tone, Woman
👩🏿‍👶🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone
👩‍❤️‍💋‍👨🏿 Kiss - Woman, Man: Dark Skin Tone
🏴󠁢󠁨󠀱󠀵󠁿 Flag for Muharraq (BH-15)
👩🏾‍👩🏾‍👶🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🗵 Ballot Box with Script X
🏴󠁤󠁺󠀲󠀵󠁿 Flag for Constantine (DZ-25)
🏴󠁡󠁵󠁶󠁩󠁣󠁿 Flag for Victoria (AU-VIC)
🏴󠁦󠁲󠁮󠁣󠁿 Flag for New Caledonia (FR-NC)
👨‍❤️‍👩🏼 Couple With Heart - Man, Woman: Medium-Light Skin Tone
☩ Cross of Jerusalem
🏴󠁡󠁺󠁹󠁥󠁿 Flag for Yevlakh (AZ-YE)
👨🏿‍👩🏿‍👧🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🧕🏾‍♂️ Man With Headscarf: Medium-Dark Skin Tone
🏴󠁡󠁺󠁹󠁥󠁶󠁿 Flag for Yevlakh District (AZ-YEV)
♤ White Spade Suit
🀐 Mahjong Tile One of Bamboos
⚥ Male and Female Sign
🕴🏿‍♀️ Woman in Business Suit Levitating: Dark Skin Tone
👩🏿‍👦🏿‍👧🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁹󠁥󠁳󠁤󠁿 Flag for Sa’dah (YE-SD)
🏴󠁡󠁺󠁳󠁡󠁬󠁿 Flag for Salyan (AZ-SAL)
👩🏼‍👩🏼‍👦🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁡󠁺󠁹󠁡󠁲󠁿 Flag for Yardymli (AZ-YAR)
🏴󠁬󠁲󠁭󠁯󠁿 Flag for Montserrado (LR-MO)
♰ West Syriac Cross
🏴󠁢󠁨󠀱󠀳󠁿 Flag for Capital (BH-13)
🏴󠁤󠁥󠁨󠁨󠁿 Flag for Hamburg (DE-HH)
🏴󠁡󠁺󠁺󠁡󠁱󠁿 Flag for Zaqatala (AZ-ZAQ)
👨🏾‍❤️‍👩 Couple With Heart - Man: Medium-Dark Skin Tone, Woman
🏴󠁡󠁺󠁸󠁡󠁿 Flag for Stepanakert (AZ-XA)
👨🏽‍❤️‍👨🏼 Couple With Heart - Man: Medium Skin Tone, Man: Medium-Light Skin Tone
🧕🏿‍♂️ Man With Headscarf: Dark Skin Tone
🏴󠁨󠁴󠁮󠁥󠁿 Flag for Nord-Est (HT-NE)
🏴󠁡󠁦󠁰󠁡󠁮󠁿 Flag for Panjshir (AF-PAN)
🏴󠁬󠁶󠀰󠀲󠀴󠁿 Flag for Dagda (LV-024)
🏴󠁳󠁮󠁤󠁫󠁿 Flag for Dakar (SN-DK)
🗊 Note Pad
🏴󠁭󠁶󠁮󠁣󠁿 Flag for North Central Province (MV-NC)
🏴󠁡󠁤󠀰󠀲󠁿 Flag for Canillo (AD-02)
🏴󠁥󠁧󠁰󠁴󠁳󠁿 Flag for Port Said (EG-PTS)
🏴󠁬󠁶󠀰󠀱󠀲󠁿 Flag for Babīte (LV-012)
🏴󠁢󠁲󠁰󠁡󠁿 Flag for Pará (BR-PA)
👩🏿‍👨🏿‍👶🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁪󠁰󠀴󠀱󠁿 Flag for Saga (JP-41)
🏴󠁭󠁥󠀰󠀳󠁿 Flag for Berane (ME-03)
⚈ Black Circle with White Dot Right
⚋ Monogram for Yin
👨🏿‍❤️‍💋‍👨🏽 Kiss - Man: Dark Skin Tone, Man: Medium Skin Tone
🏴󠁤󠁯󠀳󠀷󠁿 Flag for El Valle (DO-37)
🏴󠁣󠁮󠀲󠀲󠁿 Flag for Jilin (CN-22)
🏴󠁣󠁮󠀵󠀳󠁿 Flag for Yunnan (CN-53)
👨🏿‍👧🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁵󠁳󠁤󠁥󠁿 Flag for Delaware (US-DE)
🏴󠁭󠁥󠀲󠀲󠁿 Flag for Gusinje (ME-22)
🏴󠁳󠁥󠁸󠁿 Flag for Gävleborg (SE-X)
🤵🏻‍♀️ Woman in Tuxedo: Light Skin Tone
🏴󠁭󠁴󠀵󠀱󠁿 Flag for St. Paul’s Bay (MT-51)
🏴󠁣󠁺󠀳󠀱󠁿 Flag for Jihočeský kraj (CZ-31)
🏴󠁡󠁦󠁢󠁤󠁧󠁿 Flag for Badghis (AF-BDG)
🏴󠁰󠁴󠀱󠀳󠁿 Flag for Porto (PT-13)
🏴󠁭󠁶󠁵󠁳󠁿 Flag for Upper South Province (MV-US)
⚚ Staff of Hermes
🏴󠁧󠁲󠁭󠁿 Flag for Crete (GR-M)
🏴󠁴󠁴󠁰󠁯󠁳󠁿 Flag for Port of Spain (TT-POS)
🏴󠁥󠁧󠁢󠁮󠁳󠁿 Flag for Beni Suef (EG-BNS)
 Shibuya
🏴󠁭󠁸󠁭󠁯󠁲󠁿 Flag for Morelos (MX-MOR)
🏴󠁭󠁡󠀱󠀰󠁿 Flag for Doukkala-Abda (MA-10)
🏴󠁫󠁮󠁮󠁿 Flag for Nevis (KN-N)
🏴󠁴󠁬󠁭󠁦󠁿 Flag for Manufahi (TL-MF)
🏴󠁧󠁥󠁡󠁪󠁿 Flag for Adjara (GE-AJ)
👩‍❤️‍💋‍👨🏼 Kiss - Woman, Man: Medium-Light Skin Tone
🏴󠁥󠁣󠁴󠁿 Flag for Tungurahua (EC-T)
🏴󠁵󠁳󠁭󠁯󠁿 Flag for Missouri (US-MO)
🏴󠁮󠁧󠁬󠁡󠁿 Flag for Lagos (NG-LA)
🏴󠁩󠁮󠁴󠁲󠁿 Flag for Tripura (IN-TR)
🏴󠁡󠁤󠀰󠀳󠁿 Flag for Encamp (AD-03)
🏴󠁵󠁹󠁲󠁶󠁿 Flag for Rivera (UY-RV)
🏴󠁧󠁡󠀱󠁿 Flag for Estuaire (GA-1)
👩🏼‍👩🏼‍👦🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁭󠁬󠀶󠁿 Flag for Tombouctou (ML-6)
🖄 Envelope with Lightning
🏴󠁬󠁶󠀰󠀳󠀶󠁿 Flag for Ilūkste (LV-036)
👨🏾‍👩🏾‍👶🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
♃ Jupiter
🏴󠁵󠁳󠁩󠁬󠁿 Flag for Illinois (US-IL)
🏴󠁡󠁦󠁫󠁡󠁰󠁿 Flag for Kapisa (AF-KAP)
🏴󠁤󠁥󠁴󠁨󠁿 Flag for Thuringia (DE-TH)
🗢 Lips
🏴󠁢󠁱󠁳󠁡󠁿 Flag for Saba (BQ-SA)
🏴󠁳󠁥󠁩󠁿 Flag for Gotland (SE-I)
👨🏼‍👩🏼‍👧🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁥󠁧󠁳󠁨󠁧󠁿 Flag for Sohag (EG-SHG)
🗘 Clockwise Right and Left Semicircle Arrows
🖢 Black Up Pointing Backhand Index
👨‍❤️‍💋‍👨🏽 Kiss - Man, Man: Medium Skin Tone
🖦 Keyboard and Mouse
⛿ White Flag with Horizontal Middle Black Stripe
🏴󠁣󠁯󠁳󠁡󠁰󠁿 Flag for San Andrés & Providencia (CO-SAP)
🏴󠁦󠁲󠁣󠁯󠁲󠁿 Flag for Corse (FR-COR)
🏴󠁡󠁦󠁫󠁡󠁮󠁿 Flag for Kandahar (AF-KAN)
9️ Digit Nine
👨‍❤️‍💋‍👨🏿 Kiss - Man, Man: Dark Skin Tone
🏴󠁪󠁰󠀲󠀷󠁿 Flag for Ōsaka (JP-27)
🏴󠁴󠁬󠁬󠁡󠁿 Flag for Lautém (TL-LA)
🖿 Black Folder
🕨 Right Speaker
🏴󠁬󠁹󠁭󠁩󠁿 Flag for Misrata (LY-MI)
🏴󠁬󠁢󠁢󠁡󠁿 Flag for Beirut (LB-BA)
🏴󠁧󠁤󠀰󠀵󠁿 Flag for Saint Mark (GD-05)
🏴󠁡󠁦󠁫󠁡󠁢󠁿 Flag for Kabul (AF-KAB)
🏴󠁶󠁥󠁷󠁿 Flag for Federal Dependencies (VE-W)
🏴󠁮󠁺󠁴󠁡󠁳󠁿 Flag for Tasman (NZ-TAS)
🏴󠁩󠁮󠁭󠁨󠁿 Flag for Maharashtra (IN-MH)
🏴󠁲󠁵󠁡󠁭󠁵󠁿 Flag for Amur (RU-AMU)
🏴󠁪󠁰󠀴󠀲󠁿 Flag for Nagasaki (JP-42)
👩🏼‍👩🏼‍👧🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
⚇ White Circle with Two Dots
🏴󠁳󠁥󠁺󠁿 Flag for Jämtland (SE-Z)
🧟🏼‍♂️ Man Zombie: Medium-Light Skin Tone
🏴󠁭󠁸󠁢󠁣󠁮󠁿 Flag for Baja California (MX-BCN)
🏴󠁣󠁯󠁡󠁭󠁡󠁿 Flag for Amazonas (CO-AMA)
🏴󠁣󠁮󠀹󠀲󠁿 Flag for Macau SAR China (CN-92)
👨🏿‍👨🏿‍👦🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
⃣ Combining Enclosing Keycap
󠁷 Tag Latin Small Letter W
4️ Digit Four
🏴󠁡󠁴󠀱󠁿 Flag for Burgenland (AT-1)
🏴󠁡󠁦󠁨󠁥󠁲󠁿 Flag for Herat (AF-HER)
🏴󠁣󠁬󠁡󠁰󠁿 Flag for Arica y Parinacota (CL-AP)
🏴󠁰󠁳󠁲󠁢󠁨󠁿 Flag for Ramallah and al-Bireh (PS-RBH)
🏴󠁳󠁩󠀱󠀴󠀹󠁿 Flag for Bistrica ob Sotli (SI-149)
🏴󠁩󠁲󠀰󠀶󠁿 Flag for Bushehr (IR-06)
#️ Number Sign
󠁵 Tag Latin Small Letter U
🀟 Mahjong Tile Seven of Circles
🏱 White Pennant
👨🏻‍👶🏻‍👦🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
🏴󠁭󠁬󠀸󠁿 Flag for Kidal (ML-8)
👩🏽‍❤️‍👩🏿 Couple With Heart - Woman: Medium Skin Tone, Woman: Dark Skin Tone
🏴󠁮󠁬󠁢󠁱󠀲󠁿 Flag for Saba (NL-BQ2)
🏴󠁣󠁬󠁡󠁮󠁿 Flag for Antofagasta (CL-AN)
🏴󠁧󠁥󠁡󠁢󠁿 Flag for Abkhazia (GE-AB)
🏴󠁣󠁨󠁳󠁨󠁿 Flag for Schaffhausen (CH-SH)
🏴󠁡󠁦󠁧󠁨󠁡󠁿 Flag for Ghazni (AF-GHA)
🏴󠁢󠁷󠁧󠁡󠁿 Flag for Gaborone (BW-GA)
👩🏽‍👩🏽‍👶🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👩🏿‍👨🏿‍👦🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🖂 Back of Envelope
🀃 Mahjong Tile North Wind
👩🏻‍👦🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone
👨🏼‍👩🏼‍👶🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏾‍❤️‍👨🏻 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Light Skin Tone
🏴󠁣󠁯󠁶󠁡󠁣󠁿 Flag for Valle del Cauca (CO-VAC)
🏴󠁮󠁧󠁲󠁩󠁿 Flag for Rivers (NG-RI)
👩‍👩‍👦‍👧 Family: Woman, Woman, Boy, Girl
🏴󠁡󠁦󠁧󠁨󠁯󠁿 Flag for Ghōr (AF-GHO)
🏴󠁥󠁳󠁶󠁣󠁿 Flag for Valencian Community (ES-VC)
🏴󠁢󠁲󠁰󠁥󠁿 Flag for Pernambuco (BR-PE)
👩🏽‍❤️‍💋‍👨🏻 Kiss - Woman: Medium Skin Tone, Man: Light Skin Tone
🏴󠁥󠁳󠁣󠁴󠁿 Flag for Catalonia (ES-CT)
🏴󠁣󠁮󠀱󠀱󠁿 Flag for Beijing (CN-11)
👨🏽‍👨🏽‍👦🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👨🏽‍❤️‍💋‍👨🏿 Kiss - Man: Medium Skin Tone, Man: Dark Skin Tone
🏴󠁣󠁮󠀲󠀳󠁿 Flag for Heilongjiang (CN-23)
🏴󠁤󠁯󠀴󠀰󠁿 Flag for Ozama (DO-40)
🏴󠁴󠁷󠁴󠁰󠁥󠁿 Flag for Taipei (TW-TPE)
🌣 White Sun
👨🏻‍❤️‍👩🏼 Couple With Heart - Man: Light Skin Tone, Woman: Medium-Light Skin Tone
🕁 Cross Pommee with Half-Circle Below
🏴󠁴󠁭󠁡󠁿 Flag for Ahal (TM-A)
🏴󠁩󠁮󠁭󠁮󠁿 Flag for Manipur (IN-MN)
🏴󠁣󠁨󠁴󠁧󠁿 Flag for Thurgau (CH-TG)
🏴󠁮󠁬󠁤󠁲󠁿 Flag for Drenthe (NL-DR)
🏴󠁭󠁭󠀰󠀳󠁿 Flag for Magway (MM-03)
🏴󠁡󠁦󠁦󠁲󠁡󠁿 Flag for Farah (AF-FRA)
👨🏻‍❤️‍💋‍👨🏾 Kiss - Man: Light Skin Tone, Man: Medium-Dark Skin Tone
👨‍👦‍👧 Family: Man, Boy, Girl
🏴󠁭󠁫󠀶󠀴󠁿 Flag for Radoviš (MK-64)
󠁦 Tag Latin Small Letter F
🏴󠁰󠁷󠀲󠀲󠀸󠁿 Flag for Ngiwal (PW-228)
👨‍👶‍👶 Family: Man, Baby, Baby
󠀸 Tag Digit Eight
👨🏽‍👩🏽‍👦🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁢󠁳󠁣󠁩󠁿 Flag for Cat Island (BS-CI)
👨🏻‍👩🏻‍👦🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
🏴󠁮󠁲󠀱󠀳󠁿 Flag for Uaboe (NR-13)
👩🏾‍👨🏾‍👧🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
✐ Upper Right Pencil
✎ Lower Right Pencil
🖜 Black Left Pointing Backhand Index
🏴󠁫󠁥󠀱󠀸󠁿 Flag for Kitui (KE-18)
👩🏼‍👶🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🀜 Mahjong Tile Four of Circles
🏴󠁫󠁺󠁡󠁳󠁴󠁿 Flag for Astana (KZ-AST)
🏴󠁩󠁮󠁷󠁢󠁿 Flag for West Bengal (IN-WB)
🏴󠁳󠁬󠁥󠁿 Flag for Eastern (SL-E)
🀞 Mahjong Tile Six of Circles
☷ Trigram for Earth
󠁊 Tag Latin Capital Letter J
🏴󠁩󠁲󠀱󠀴󠁿 Flag for Fars (IR-14)
󠀩 Tag Right Parenthesis
🗟 Page with Circled Text
🖓 Reversed Thumbs Down Sign
🗪 Two Speech Bubbles
☿️ Mercury
🏴󠁣󠁨󠁺󠁧󠁿 Flag for Zug (CH-ZG)
🏴󠁡󠁦󠁢󠁧󠁬󠁿 Flag for Baghlan (AF-BGL)
👨🏾‍❤️‍👨 Couple With Heart - Man: Medium-Dark Skin Tone, Man
🏴󠁵󠁡󠀳󠀵󠁿 Flag for Kirovohradschyna (UA-35)
☰ Trigram for Heaven
🏴󠁬󠁩󠀰󠀵󠁿 Flag for Planken (LI-05)
⚘ Flower
󠁿 Cancel Tag
󠀱 Tag Digit One
󠀴 Tag Digit Four
🏴󠁧󠁹󠁢󠁡󠁿 Flag for Barima-Waini (GY-BA)
🏴󠁡󠁦󠁢󠁡󠁬󠁿 Flag for Balkh (AF-BAL)
🏴󠁩󠁱󠁢󠁢󠁿 Flag for Babylon (IQ-BB)
🏴󠁣󠁮󠀶󠀱󠁿 Flag for Shaanxi (CN-61)
🖬 Soft Shell Floppy Disk
♫ Beamed Eighth Notes
🏴󠁡󠁥󠁵󠁱󠁿 Flag for Umm al-Quwain (AE-UQ)
🏴󠁤󠁺󠀱󠀹󠁿 Flag for Sétif (DZ-19)
🏴󠁤󠁥󠁢󠁢󠁿 Flag for Brandenburg (DE-BB)
🛇 Prohibited Sign
🏴󠁲󠁵󠁳󠁡󠁿 Flag for Sakha (RU-SA)
🏴󠁣󠁭󠁳󠁵󠁿 Flag for South (CM-SU)
🏴󠁩󠁮󠁪󠁫󠁿 Flag for Jammu and Kashmir (IN-JK)
🏴󠁤󠁺󠀰󠀳󠁿 Flag for Laghouat (DZ-03)
🏴󠁡󠁥󠁳󠁨󠁿 Flag for Sharjah (AE-SH)
👩🏻‍👩🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone
🏴󠁩󠁳󠀴󠁿 Flag for Westfjords (IS-4)
🏴󠁣󠁭󠁯󠁵󠁿 Flag for West (CM-OU)
🏴󠁤󠁥󠁳󠁬󠁿 Flag for Saarland (DE-SL)
🏴󠁭󠁫󠀶󠀵󠁿 Flag for Rankovce (MK-65)
👨🏼‍👨🏼‍👦🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🤵🏿‍♀️ Woman in Tuxedo: Dark Skin Tone
󠁚 Tag Latin Capital Letter Z
🏴󠁬󠁹󠁭󠁪󠁿 Flag for Marj (LY-MJ)
⛐ Car Sliding
🏴󠁦󠁩󠀰󠀸󠁿 Flag for Central Finland (FI-08)
👩🏼‍👩🏼‍👦🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁬󠁴󠀵󠀷󠁿 Flag for Vilniaus Municipality (LT-57)
🏴󠁳󠁩󠀲󠀰󠀸󠁿 Flag for Log–Dragomer (SI-208)
👩🏽‍❤️‍👩🏻 Couple With Heart - Woman: Medium Skin Tone, Woman: Light Skin Tone
⛊ Turned Black Shogi Piece
🏴󠁬󠁹󠁪󠁵󠁿 Flag for Jufra (LY-JU)
🀅 Mahjong Tile Green Dragon
🏴󠁧󠁷󠁳󠁿 Flag for Sul (GW-S)
🤵🏾‍♀️ Woman in Tuxedo: Medium-Dark Skin Tone
󠁣 Tag Latin Small Letter C
🧕🏿‍♀️ Woman With Headscarf: Dark Skin Tone
🀏 Mahjong Tile Nine of Characters
⛕ Alternate One-Way Left Way Traffic
🏴󠁨󠁲󠀱󠀰󠁿 Flag for Virovitica-Podravina (HR-10)
🏴󠁣󠁮󠀳󠀳󠁿 Flag for Zhejiang (CN-33)
🏴󠁶󠁥󠁴󠁿 Flag for Trujillo (VE-T)
👨🏻‍❤️‍👨🏻 Couple With Heart - Man: Light Skin Tone, Man: Light Skin Tone
🏴󠁳󠁣󠀱󠀰󠁿 Flag for Bel Ombre (SC-10)
☜ White Left Pointing Index
🧕🏾‍♀️ Woman With Headscarf: Medium-Dark Skin Tone
🏴󠁵󠁳󠁡󠁲󠁿 Flag for Arkansas (US-AR)
🏴󠁵󠁹󠁦󠁤󠁿 Flag for Florida (UY-FD)
🏴󠁳󠁯󠁳󠁯󠁿 Flag for Sool (SO-SO)
👩🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁡󠁦󠁢󠁡󠁭󠁿 Flag for Bamyan (AF-BAM)
🏴󠁢󠁩󠁣󠁩󠁿 Flag for Cibitoke (BI-CI)
🏴󠁥󠁣󠁦󠁿 Flag for Cañar (EC-F)
🧕‍♂️ Man With Headscarf
🕭 Ringing Bell
🏴󠁭󠁸󠁮󠁡󠁹󠁿 Flag for Nayarit (MX-NAY)
👩🏻‍👦🏻‍👦🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
󠀡 Tag Exclamation Mark
🤵🏽‍♀️ Woman in Tuxedo: Medium Skin Tone
🏴󠁭󠁬󠀱󠁿 Flag for Kayes (ML-1)
🏴󠁧󠁲󠁩󠁿 Flag for Attica (GR-I)
🏴󠁮󠁺󠁴󠁫󠁩󠁿 Flag for Taranaki (NZ-TKI)
🏴󠁩󠁲󠀳󠀰󠁿 Flag for Razavi Khorasan (IR-30)
🗬 Left Thought Bubble
🏴󠁮󠁡󠁯󠁨󠁿 Flag for Omaheke (NA-OH)
󠁩 Tag Latin Small Letter I
♗ White Chess Bishop
🛧 Up-Pointing Airplane
🕼 Telephone Receiver with Page
🏴󠁣󠁵󠀰󠀱󠁿 Flag for Pinar del Río (CU-01)
♵ Recycling Symbol for Type-3 Plastics
☞ White Right Pointing Index
🏴󠁧󠁴󠁳󠁡󠁿 Flag for Sacatepéquez (GT-SA)
🏴󠁣󠁹󠀰󠀴󠁿 Flag for Famagusta (CY-04)
🏴󠁹󠁥󠁳󠁡󠁿 Flag for Amanat Al Asimah (YE-SA)
🏴󠁹󠁥󠁳󠁮󠁿 Flag for Sana’a (YE-SN)
👨🏿‍👨🏿‍👧🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁨󠁵󠁫󠁶󠁿 Flag for Kaposvár (HU-KV)
🏴󠁡󠁺󠁡󠁢󠁳󠁿 Flag for Absheron (AZ-ABS)
🏴󠁫󠁥󠀰󠀱󠁿 Flag for Baringo (KE-01)
🖎 Left Writing Hand
👨🏻‍👨🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone
🏴󠁬󠁡󠁳󠁶󠁿 Flag for Savannakhet (LA-SV)
󠁲 Tag Latin Small Letter R
🏴󠁥󠁣󠁸󠁿 Flag for Cotopaxi (EC-X)
👩🏻‍👧🏻‍👧🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
🏴󠁭󠁥󠀰󠀲󠁿 Flag for Bar (ME-02)
🏴󠁭󠁫󠀷󠀵󠁿 Flag for Tearce (MK-75)
🏴󠁡󠁦󠁦󠁹󠁢󠁿 Flag for Faryab (AF-FYB)
🏴󠁭󠁴󠀲󠀰󠁿 Flag for Senglea (MT-20)
☛🏻 Black Right Pointing Index + Emoji Modifier Fitzpatrick Type-1-2
☞🏻 White Right Pointing Index + Emoji Modifier Fitzpatrick Type-1-2
☟🏻 White Down Pointing Index + Emoji Modifier Fitzpatrick Type-1-2
🖑🏻 Reversed Raised Hand with Fingers Splayed + Emoji Modifier Fitzpatrick Type-1-2
☚🏻 Black Left Pointing Index + Emoji Modifier Fitzpatrick Type-1-2
🖎🏻 Left Writing Hand + Emoji Modifier Fitzpatrick Type-1-2
🖓🏻 Reversed Thumbs Down Sign + Emoji Modifier Fitzpatrick Type-1-2
🖔🏻 Reversed Victory Hand + Emoji Modifier Fitzpatrick Type-1-2
🖒🏻 Reversed Thumbs Up Sign + Emoji Modifier Fitzpatrick Type-1-2
☜🏻 White Left Pointing Index + Emoji Modifier Fitzpatrick Type-1-2
🖓🏼 Reversed Thumbs Down Sign + Emoji Modifier Fitzpatrick Type-3
☛🏼 Black Right Pointing Index + Emoji Modifier Fitzpatrick Type-3
🖑🏼 Reversed Raised Hand with Fingers Splayed + Emoji Modifier Fitzpatrick Type-3
🖔🏼 Reversed Victory Hand + Emoji Modifier Fitzpatrick Type-3
☜🏼 White Left Pointing Index + Emoji Modifier Fitzpatrick Type-3
🖒🏼 Reversed Thumbs Up Sign + Emoji Modifier Fitzpatrick Type-3
☞🏼 White Right Pointing Index + Emoji Modifier Fitzpatrick Type-3
🖎🏼 Left Writing Hand + Emoji Modifier Fitzpatrick Type-3
☚🏼 Black Left Pointing Index + Emoji Modifier Fitzpatrick Type-3
☟🏼 White Down Pointing Index + Emoji Modifier Fitzpatrick Type-3
🖑🏽 Reversed Raised Hand with Fingers Splayed + Emoji Modifier Fitzpatrick Type-4
☜🏽 White Left Pointing Index + Emoji Modifier Fitzpatrick Type-4
🖒🏽 Reversed Thumbs Up Sign + Emoji Modifier Fitzpatrick Type-4
☞🏽 White Right Pointing Index + Emoji Modifier Fitzpatrick Type-4
🖔🏽 Reversed Victory Hand + Emoji Modifier Fitzpatrick Type-4
☟🏽 White Down Pointing Index + Emoji Modifier Fitzpatrick Type-4
☛🏽 Black Right Pointing Index + Emoji Modifier Fitzpatrick Type-4
☚🏽 Black Left Pointing Index + Emoji Modifier Fitzpatrick Type-4
🖓🏽 Reversed Thumbs Down Sign + Emoji Modifier Fitzpatrick Type-4
🖎🏽 Left Writing Hand + Emoji Modifier Fitzpatrick Type-4
🖒🏾 Reversed Thumbs Up Sign + Emoji Modifier Fitzpatrick Type-5
🖑🏾 Reversed Raised Hand with Fingers Splayed + Emoji Modifier Fitzpatrick Type-5
☚🏾 Black Left Pointing Index + Emoji Modifier Fitzpatrick Type-5
☟🏾 White Down Pointing Index + Emoji Modifier Fitzpatrick Type-5
🖔🏾 Reversed Victory Hand + Emoji Modifier Fitzpatrick Type-5
☛🏾 Black Right Pointing Index + Emoji Modifier Fitzpatrick Type-5
☞🏾 White Right Pointing Index + Emoji Modifier Fitzpatrick Type-5
☜🏾 White Left Pointing Index + Emoji Modifier Fitzpatrick Type-5
🖓🏾 Reversed Thumbs Down Sign + Emoji Modifier Fitzpatrick Type-5
🖎🏾 Left Writing Hand + Emoji Modifier Fitzpatrick Type-5
☚🏿 Black Left Pointing Index + Emoji Modifier Fitzpatrick Type-6
☛🏿 Black Right Pointing Index + Emoji Modifier Fitzpatrick Type-6
☜🏿 White Left Pointing Index + Emoji Modifier Fitzpatrick Type-6
🖓🏿 Reversed Thumbs Down Sign + Emoji Modifier Fitzpatrick Type-6
☟🏿 White Down Pointing Index + Emoji Modifier Fitzpatrick Type-6
🖎🏿 Left Writing Hand + Emoji Modifier Fitzpatrick Type-6
🖔🏿 Reversed Victory Hand + Emoji Modifier Fitzpatrick Type-6
☞🏿 White Right Pointing Index + Emoji Modifier Fitzpatrick Type-6
🖒🏿 Reversed Thumbs Up Sign + Emoji Modifier Fitzpatrick Type-6
🖑🏿 Reversed Raised Hand with Fingers Splayed + Emoji Modifier Fitzpatrick Type-6
"""

rofi = Popen(
    args=[
        'rofi',
        '-dmenu',
        '-i',
        '-p',
        ' 😀   ',
        '-kb-custom-1',
        'Alt+c'
    ],
    stdin=PIPE,
    stdout=PIPE
)
(stdout, stderr) = rofi.communicate(input=emojis.encode('utf-8'))

if rofi.returncode == 1:
    exit()
else:
    emoji = stdout.split()[0]
    if rofi.returncode == 0:
        Popen(
            args=[
                'xdotool',
                'type',
                '--clearmodifiers',
                emoji.decode('utf-8')
            ]
        )
    elif rofi.returncode == 10:
        xsel = Popen(
            args=[
                'xsel',
                '-i',
                '-b'
            ],
            stdin=PIPE
        )
        xsel.communicate(input=emoji)
