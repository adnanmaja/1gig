class Mahasiswa:
    def __init__(self, nama, umur, fakultas, ipk, di_skors):
        self.nama = nama
        self.umur = umur
        self.fakultas = fakultas
        self.ipk = ipk
        self.di_skors = di_skors

    def to_dict(self):
        return{
            "nama": self.nama,
            "umur": self.umur,
            "fakultas": self.fakultas,
            "ipk": self.ipk,
            "di_skors": self.di_skors
        }


    @property
    def pinter(self):
        if self.ipk >= 3.5:
            return  True
        else:
            return  False


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer