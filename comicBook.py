import sys
sys.path.append("C:\\users\\millersm\\mu_code")
# sys.path.append("C:\\users\\millersm\\mu_code\\data")
# sys.path.append("C:\\users\\millersm\\mu_code\\modules")

import dataReader

comics = dataReader.getComics()
if comics is not None:
    for c in comics:
        print(c["title"] + " " + c["number"])
        