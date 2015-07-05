## csv2xml.py
## Abstract: Convert .csv file to .xml file with each csv field given xml tags
## Created by: Taylor C. Johnson
## Created on: 20150212
## Last modified on: 20150213
## Version: 10.2.2

import os.path, csv, Tkinter, tkFileDialog

## ---- Global Variables ----

## List of columns in the Location.csv (used for ESRI Story Map, but *could* change)
columns = ["Name", "Caption", "URL", "Site", "Date", "Month_Text", "Time"]
## List of xml tags - in order of how they will be written to output .xml file
outCSVrows = ['<?xml version="1.0" encoding="utf-8"?>', '<collection>']

## ---- Global Functions ----

## Takes important Location.csv columns and compares them to actual headers in .csv file.
## Returns data dictionary with {'important column': 'index value'}
def defCoIndex(columns, headers):
    colDict = {}
    for c in columns:
        for i, head in enumerate(headers):
            if head.lower() == c.lower():
                colDict[head]=i
                break
    return colDict

## ---- Execution Code ----
try:
    root = Tkinter.Tk()
    root.withdraw()

    ## tkFileDialog to obtain .csv file
    inCSV = tkFileDialog.askopenfilename()
    outCSV = os.path.dirname(inCSV) + '/photoCollection.xml'

    with open(inCSV) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        coIndices = defCoIndex(columns, headers)
        for row in f_csv:
            outCSVrows.append('\t<image>')
            for c in columns:
                outCSVrows.append('\t\t<'+c.lower()+'>'+row[coIndices.get(c)]+'</'+c.lower()+'>')
##                if c == "Caption":
##                    outCSVrows.append('\t\t<'+c.lower()+'>'+row[coIndices.get(c)]
##                                      +' <button class="btn btn-default" id="start" data-toggle="modal" data-target="#imageModal" data-site="'
##                                      +row[coIndices.get("Site")]+'">PHOTOS</button></'+c.lower()+'>')
##                else:
##                    outCSVrows.append('\t\t<'+c.lower()+'>'+row[coIndices.get(c)]+'</'+c.lower()+'>')
            outCSVrows.append('\t</image>')
    outCSVrows.append('</collection>')

    with open(outCSV, 'w') as o:
        for el in outCSVrows:
            o.write(el+'\n')

finally:
    print("\nScript Complete")
