from nltk.chat.util import Chat,reflections

pairs = [
    [
        r"My name is (.*)",
        ["Hello %1. How are you today?","How may I help you?"]
    ],
    [
        r"(.*) name?",
        ["I am a Chatbot. I don't have a particular name"]
    ],
    [
        r"How are you?",
        ["I am fine.","I am always happy to help"]
    ],
    [
        r"I am doing good",
        ["Nice to hear that"]
    ],
    [
        r"Hi|Hello|Hey|hi|hello",
        ["Hey there","hello"]
    ],
    [
        r"(.*) created?",
        ["I was made by a computer programmer"]
    ],
    [
        r"(.*) investments|money?",
        ["There are many options to invest money like mutual funds, regional banks, etc."]
    ],
    [
        r"(.*) stocks?",
        ["There are many companies to invest your money in."]
    ],
    [
        r"(.*) companies (.*) money?",
        ["Amazon,Tesla"]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I don't have real-time weather information, but you might want to check a weather app or website."]
    ],
    [
        r"quit",
        ["Goodbye. It was nice talking to you!"]
    ],
    [
        r"(.*) (favorite|like) (.*) food?",
        ["I'm a computer program, so I don't eat food, but I'd love to learn about your favorite dishes!"]
    ],
    [
        r"tell me (.*) joke",
        ["Why don't scientists trust atoms? Because they make up everything!",
         "What do you call a bear with no teeth? A gummy bear!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem, happy to help!"]
    ],
    [
        r"(.*) (programming|coding) (.*)",
        ["Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
         "There are many programming languages like Python, Java, C++, and JavaScript."]
    ],
    [
        r"(.*) (artificial intelligence|AI) (.*)",
        ["Artificial Intelligence is the simulation of human intelligence processes by machines.",
         "AI includes technologies like machine learning, natural language processing, and computer vision."]
    ],
    [
        r"(.*) (study|learn) (.*)",
        ["Learning is a lifelong process. What particular subject interests you?"]
    ],
    [
        r"(.*) (book|read) recommendation",
        ["There are many great books depending on your interests. Some classics include '1984', 'To Kill a Mockingbird', and 'The Great Gatsby'."]
    ],
    [
        r"(.*) (movie|film) (.*) watch",
        ["There are many great movies across different genres. What type of films do you enjoy?"]
    ],
    [
        r"(.*) (help|assist) (.*) (assignment|homework|project) (.*)",
        ["I'd be happy to help you with your assignment. What specific questions do you have?"]
    ]
]

def chat():
    print("Hello I am a chatbot.Type 'quit' to exit")
    obj = Chat(pairs,reflections)
    obj.converse()
chat()