import csv
import os
from gmsdict2csv import list_csv

mock_lists = [
    ['datalist01', 'item11', 'item12', 'item13'],
    ['datalist02', '0', 'itemN', '20'],
    ['datalist03', 'Git', 'Repo', 'Data']
]


class TestListCsv:
    def test_csv(self):
        for l in mock_lists:
            list_csv(datalist=l, path='Downloads', file=l[0])
            with open(f"{os.path.expanduser('~')}/Downloads/{l[0]}.csv", newline='') as f:
                reader = csv.reader(f, delimiter=' ', quotechar='|')
                for rows in reader:
                    assert l == rows

