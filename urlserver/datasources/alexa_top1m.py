from . import BaseDataSource


class DataSource(BaseDataSource):
    """ Return the rank in the top 1 million domains from Alexa """

    dump_testdata = "tests/testdata/alexa-top1m.csv"
    dump_url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
    dump_compression = "zip"
    dump_compression_params = ("top-1m.csv", )
    dump_format = "csv"
    dump_batch_size = 100000

    def import_row(self, i, row):
        """ Maps a raw data row into a list of (key, values) pairs """
        return [(row[1], {"alexa_top1m": int(row[0])})]
