from mrjob.job import MRJob
from mrjob.step import MRStep
import re

DATA_RE = re.compile(r"[\w.-]+")


class MRProb2_2(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_petW,
                   reducer=self.reducer_get_max)
        ]

    def mapper_get_petW(self, _, line):
        # yield each petal width
        pet_W = float(DATA_RE.findall(line)[3])
        yield ("sepal length", pet_W)

    def reducer_get_max(self, key, values):
        # get max of the petal widths
        yield ("max petal width", max(values))


if __name__ == '__main__':
    MRProb2_2.run()