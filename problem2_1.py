from mrjob.job import MRJob
from mrjob.step import MRStep
import re

DATA_RE = re.compile(r"[\w.-]+")


class MRProb2_1(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_sepL,
                   reducer=self.reducer_get_min)
        ]

    def mapper_get_sepL(self, _, line):
        # yield each sepal length
        sep_L = float(DATA_RE.findall(line)[0])
        yield ("sepal length", sep_L)

    def reducer_get_min(self, key, values):
        # get min of the sepal lengths
        yield ("min sepal length", min(values))


if __name__ == '__main__':
    MRProb2_1.run()