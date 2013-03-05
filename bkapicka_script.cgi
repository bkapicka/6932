#!/usr/bin/python
import sys

from rdflib import Graph
from rdflib import URIRef, Literal, BNode
from rdflib import Namespace, RDF

def main():
        
    try:
        print "Content-type: text/html"
        print """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
        <head>
                <link rel="stylesheet" type="text/css" href="http://web.mit.edu/~lkagal/Public/table.css" />
                <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                <title>Example of Use of RDFLib within CGI</title>
        </head>
        <body>
"""     
            
        # foaf uri
        foafuri = "http://dig.csail.mit.edu/2008/webdav/timbl/foaf.rdf"

        # create a graph
        store = Graph()
        store.parse(foafuri)
            
        # Create a namespace object for the Friend of a friend namespace.
        FOAF = Namespace("http://xmlns.com/foaf/0.1/")
    
        # Create a namespace object for the RDFS namespace
        RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
        
        for person in store.objects(URIRef(foafuri), FOAF["maker"]):
            print "<h2>FOAF URI:", person, "</h2>"
            #for friend in store.objects(person, FOAF["knows"]):
            #    print "FOAF Person:", friend, "<br/>"

            print "<table  id='customers' width='40%'>  <col width='40%' /> <tr> <th>Friend URI</th> </tr>"
            for obj in store.objects(person, FOAF["knows"]):
                print "<tr><td>", obj, "</td> </tr>"
            print "</table>"
        print "</body> </html>"

    except:
        print "<hr>Oops. An error occurred!</hr>"
        cgi.print_exception()
        print "</body> </html>"

if __name__ == "__main__":
    main()

