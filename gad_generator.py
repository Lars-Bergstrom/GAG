#!/usr/bin/env python

import time
import sqlite3
from gff_reader import GffReader
from fasta_reader import FastaReader
from feature_tbl_writer import FeatureTblWriter

start_time = time.time()

con = sqlite3.connect('real_files/tbl_db.sqlite')

print("Reading gff...")
gff_reader = GffReader()
gff_reader.read_into_db('real_files/454Scaffolds.gff3', con)

print(time.time() - start_time, "seconds")

print("Reading fasta...")
fasta_reader = FastaReader()
fasta_reader.read_into_db("real_files/454Scaffolds.fna", con)

print(time.time() - start_time, "seconds")

print("Writing tbl database...")
test_writer = FeatureTblWriter()
test_writer.write_to_db(con)
c = con.cursor()
#c.execute('SELECT * FROM tbl')
#for row in c.fetchall():
#    print(row)

con.commit()

print(time.time() - start_time, "seconds")
