# Comic Book Database
# Not sure what we're gonna do here yet.
# Right now, just read our simple database (in csv format) and spit out some junk.
import dataReader

comics = dataReader.getComics()
if comics is not None:
    for c in comics:
        print(c["title"] + " " + c["number"])
        