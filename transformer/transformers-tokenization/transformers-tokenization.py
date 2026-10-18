class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        I am considering texts as my given dataset
        """
        vocab = set()
        for text in texts:
            words = text.lower().split()
            vocab.update(words)
        vocab = sorted(vocab)
        
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token] = 1
        self.word_to_id[self.bos_token] = 2
        self.word_to_id[self.eos_token] = 3
        i=4
        for word in vocab:
            self.word_to_id[word] = i
            i+=1

        self.id_to_word = {v:k for k, v in self.word_to_id.items()}
        self.vocab_size = len(self.word_to_id)
    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        encoded = []
        words = text.lower().split()
        for word in words:
            if word not in self.word_to_id:
                encoded.append(self.word_to_id[self.unk_token])
            else:
                 encoded.append(self.word_to_id[word])
        return encoded    

    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        decoded = []
        for id in ids:
            if id not in self.id_to_word:
                decoded.append(self.unk_token)
            else:
                decoded.append(self.id_to_word[id])
        return " ".join(decoded)            