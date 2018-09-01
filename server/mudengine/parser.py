
#Parses coommands with basic structure:
#VERB ADVERB DIRECT_OBJECT PREPOSITION OBJ_OF_PREPOSITION
class Parser:
    def __init__(self, verbs, nouns, adverbs):
        self.verb_map = verbs
        self.noun_map = nouns
        self.adverbs = adverbs

        #get single depth list of all verbs and synonyms
        self.flat_verbs = [
            verb
            for li in self.verb_map.items()
            for verb in li
        ]
        self.flat_nouns = [
            noun
            for li in self.noun_map.items()
            for noun in li
        ]

    def parse(self, string):
        normalized_string = string.strip().lower()
        word_list = normalized_string.split(" ")

        #parition by verbs
        paritions = []
        last_index = -1
        for index, word in enumerate(word_list):
            if word in self.flat_nouns:
                if last_index != -1:
                    paritions.append(word_list[last_index:index])
                last_index = index
        paritions.append(word_list[last_index:len(word_list)])

        return [self.parse_clause(part) for part in paritions]

    def parse_clause(self, word_list):
        command = {"verb":word_list[0]}
        for word in word_list[1:]:
            if ("adverb" not in command.keys()
            and word in self.adverbs
            ):
                command["adverb"] = word

            if "do" not in command.keys():
                if word in self.flat_nouns:
                    command["do"] = word
            elif "oop" not in command.keys():
                if word in self.flat_nouns:
                    command["oop"] = word

        return command


class Command:
    def __init__(
        self,
        verb,
        adverb=None, 
        do=None,
        oop=None
    ):
        self.verb = verb
        self.adverb = adverb
        self.do = do
        self.oop = oop

    def validate(self):
        pass