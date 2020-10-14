from mrjob.job import MRJob
from mrjob.step import MRStep
import re

DATA_RE = re.compile(r"[\w.-]+")


class MRProb2_3(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_dif_not_setosa,
                   reducer=self.reducer_get_avg)
        ]

    def mapper_get_dif_not_setosa(self, _, line):
        # yield each sepal and petal length
        data = DATA_RE.findall(line)
        if "Iris-setosa" not in data:
            sep_L = float(data[0])
            pet_L = float(data[2])
            yield ("length diff", round(sep_L - pet_L, 1))

    def reducer_get_avg(self, key, values):
        # get max of the petal widths
        size, total = 0, 0
        for val in values:
            size += 1
            total += val
        yield ("non setosa length diff avg", round(round(total, 1) / float(size), 3))


if __name__ == '__main__':
    MRProb2_3.run()
