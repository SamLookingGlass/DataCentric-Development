{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":109,"column":16},"end":{"row":109,"column":17},"action":"insert","lines":[" "],"id":2064}],[{"start":{"row":109,"column":17},"end":{"row":109,"column":18},"action":"remove","lines":["S"],"id":2065}],[{"start":{"row":109,"column":17},"end":{"row":109,"column":18},"action":"insert","lines":["s"],"id":2066}],[{"start":{"row":108,"column":0},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":2067},{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":109,"column":0},"end":{"row":120,"column":14},"action":"insert","lines":["db[PHOTOS].insert({","            'image_url' : images_upload_set.url(filename),","            'image_name' : filename, ","            'image_caption' : caption,","            'image_tags' : tags,","            'uploaded_on' : timestamp(),","            'deleted': 0,","            'deleted_on' : \"null\",","            # Converts filesize to mb 3sf","            'file_size' : round((filesize/1000000),3),","            'file_type' : file_extension,","            })"],"id":2068}],[{"start":{"row":99,"column":15},"end":{"row":99,"column":21},"action":"remove","lines":["update"],"id":2069},{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"insert","lines":["i"]},{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"insert","lines":["n"]},{"start":{"row":99,"column":17},"end":{"row":99,"column":18},"action":"insert","lines":["s"]},{"start":{"row":99,"column":18},"end":{"row":99,"column":19},"action":"insert","lines":["e"]},{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"insert","lines":["r"]},{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":98,"column":0},"end":{"row":107,"column":10},"action":"remove","lines":["    selected_album = db[ALBUMS].insert({\"_id\": ObjectId(albumid)})","    db[ALBUMS].insert(","        {'_id':ObjectId(albumid)},","        { '$set':","            {","                'album_name': album_name,","                'album_description': album_description,","                'edited_on': timestamp(),","            }","        })"],"id":2070},{"start":{"row":97,"column":4},"end":{"row":98,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":9},"action":"remove","lines":["HOTOS"],"id":2071},{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"insert","lines":["A"]}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"remove","lines":["A"],"id":2072}],[{"start":{"row":99,"column":3},"end":{"row":99,"column":4},"action":"remove","lines":["P"],"id":2073}],[{"start":{"row":99,"column":3},"end":{"row":99,"column":4},"action":"insert","lines":["A"],"id":2074},{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"insert","lines":["L"]},{"start":{"row":99,"column":5},"end":{"row":99,"column":6},"action":"insert","lines":["B"]},{"start":{"row":99,"column":6},"end":{"row":99,"column":7},"action":"insert","lines":["U"]},{"start":{"row":99,"column":7},"end":{"row":99,"column":8},"action":"insert","lines":["M"]},{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"remove","lines":["s"],"id":2075}],[{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"insert","lines":["S"],"id":2076}],[{"start":{"row":100,"column":13},"end":{"row":100,"column":22},"action":"remove","lines":["image_url"],"id":2077},{"start":{"row":100,"column":13},"end":{"row":100,"column":14},"action":"insert","lines":["a"]},{"start":{"row":100,"column":14},"end":{"row":100,"column":15},"action":"insert","lines":["l"]},{"start":{"row":100,"column":15},"end":{"row":100,"column":16},"action":"insert","lines":["b"]},{"start":{"row":100,"column":16},"end":{"row":100,"column":17},"action":"insert","lines":["u"]},{"start":{"row":100,"column":17},"end":{"row":100,"column":18},"action":"insert","lines":["m"]},{"start":{"row":100,"column":18},"end":{"row":100,"column":19},"action":"insert","lines":["_"]},{"start":{"row":100,"column":19},"end":{"row":100,"column":20},"action":"insert","lines":["n"]},{"start":{"row":100,"column":20},"end":{"row":100,"column":21},"action":"insert","lines":["a"]},{"start":{"row":100,"column":21},"end":{"row":100,"column":22},"action":"insert","lines":["m"]},{"start":{"row":100,"column":22},"end":{"row":100,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":100,"column":27},"end":{"row":100,"column":58},"action":"remove","lines":["images_upload_set.url(filename)"],"id":2078},{"start":{"row":100,"column":27},"end":{"row":100,"column":37},"action":"insert","lines":["album_name"]}],[{"start":{"row":101,"column":13},"end":{"row":101,"column":23},"action":"remove","lines":["image_name"],"id":2079},{"start":{"row":101,"column":13},"end":{"row":101,"column":14},"action":"insert","lines":["a"]},{"start":{"row":101,"column":14},"end":{"row":101,"column":15},"action":"insert","lines":["l"]},{"start":{"row":101,"column":15},"end":{"row":101,"column":16},"action":"insert","lines":["b"]},{"start":{"row":101,"column":16},"end":{"row":101,"column":17},"action":"insert","lines":["u"]},{"start":{"row":101,"column":17},"end":{"row":101,"column":18},"action":"insert","lines":["m"]}],[{"start":{"row":101,"column":13},"end":{"row":101,"column":18},"action":"remove","lines":["album"],"id":2080},{"start":{"row":101,"column":13},"end":{"row":101,"column":30},"action":"insert","lines":["album_description"]}],[{"start":{"row":101,"column":34},"end":{"row":101,"column":42},"action":"remove","lines":["filename"],"id":2081},{"start":{"row":101,"column":34},"end":{"row":101,"column":35},"action":"insert","lines":["a"]},{"start":{"row":101,"column":35},"end":{"row":101,"column":36},"action":"insert","lines":["l"]},{"start":{"row":101,"column":36},"end":{"row":101,"column":37},"action":"insert","lines":["b"]},{"start":{"row":101,"column":37},"end":{"row":101,"column":38},"action":"insert","lines":["u"]},{"start":{"row":101,"column":38},"end":{"row":101,"column":39},"action":"insert","lines":["m"]}],[{"start":{"row":101,"column":34},"end":{"row":101,"column":39},"action":"remove","lines":["album"],"id":2082},{"start":{"row":101,"column":34},"end":{"row":101,"column":51},"action":"insert","lines":["album_description"]}],[{"start":{"row":101,"column":52},"end":{"row":101,"column":53},"action":"remove","lines":[" "],"id":2083},{"start":{"row":101,"column":52},"end":{"row":102,"column":0},"action":"insert","lines":["",""]},{"start":{"row":102,"column":0},"end":{"row":102,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":102,"column":12},"end":{"row":102,"column":14},"action":"insert","lines":["''"],"id":2084}],[{"start":{"row":102,"column":13},"end":{"row":102,"column":14},"action":"insert","lines":["c"],"id":2085},{"start":{"row":102,"column":14},"end":{"row":102,"column":15},"action":"insert","lines":["r"]},{"start":{"row":102,"column":15},"end":{"row":102,"column":16},"action":"insert","lines":["e"]},{"start":{"row":102,"column":16},"end":{"row":102,"column":17},"action":"insert","lines":["a"]},{"start":{"row":102,"column":17},"end":{"row":102,"column":18},"action":"insert","lines":["t"]},{"start":{"row":102,"column":18},"end":{"row":102,"column":19},"action":"insert","lines":["e"]},{"start":{"row":102,"column":19},"end":{"row":102,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":102,"column":13},"end":{"row":102,"column":20},"action":"remove","lines":["created"],"id":2086},{"start":{"row":102,"column":13},"end":{"row":102,"column":23},"action":"insert","lines":["created_on"]}],[{"start":{"row":102,"column":24},"end":{"row":102,"column":25},"action":"insert","lines":[":"],"id":2087}],[{"start":{"row":102,"column":25},"end":{"row":102,"column":26},"action":"insert","lines":[" "],"id":2088},{"start":{"row":102,"column":26},"end":{"row":102,"column":27},"action":"insert","lines":["t"]},{"start":{"row":102,"column":27},"end":{"row":102,"column":28},"action":"insert","lines":["u"]}],[{"start":{"row":102,"column":27},"end":{"row":102,"column":28},"action":"remove","lines":["u"],"id":2089}],[{"start":{"row":102,"column":27},"end":{"row":102,"column":28},"action":"insert","lines":["u"],"id":2090}],[{"start":{"row":102,"column":27},"end":{"row":102,"column":28},"action":"remove","lines":["u"],"id":2091}],[{"start":{"row":102,"column":26},"end":{"row":102,"column":27},"action":"remove","lines":["t"],"id":2092},{"start":{"row":102,"column":26},"end":{"row":102,"column":37},"action":"insert","lines":["timestamp()"]}],[{"start":{"row":102,"column":37},"end":{"row":102,"column":38},"action":"insert","lines":[","],"id":2094}],[{"start":{"row":100,"column":12},"end":{"row":101,"column":52},"action":"remove","lines":["'album_name' : album_name,","            'album_description' : album_description,"],"id":2095},{"start":{"row":100,"column":8},"end":{"row":100,"column":12},"action":"remove","lines":["    "]},{"start":{"row":100,"column":4},"end":{"row":100,"column":8},"action":"remove","lines":["    "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"remove","lines":["    "]},{"start":{"row":99,"column":19},"end":{"row":100,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":101,"column":12},"end":{"row":102,"column":0},"action":"insert","lines":["",""],"id":2096},{"start":{"row":102,"column":0},"end":{"row":102,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":101,"column":12},"end":{"row":102,"column":52},"action":"insert","lines":["'album_name' : album_name,","            'album_description' : album_description,"],"id":2097}],[{"start":{"row":103,"column":13},"end":{"row":103,"column":26},"action":"remove","lines":["image_caption"],"id":2098},{"start":{"row":103,"column":13},"end":{"row":103,"column":14},"action":"insert","lines":["e"]},{"start":{"row":103,"column":14},"end":{"row":103,"column":15},"action":"insert","lines":["d"]},{"start":{"row":103,"column":15},"end":{"row":103,"column":16},"action":"insert","lines":["i"]},{"start":{"row":103,"column":16},"end":{"row":103,"column":17},"action":"insert","lines":["t"]},{"start":{"row":103,"column":17},"end":{"row":103,"column":18},"action":"insert","lines":["e"]},{"start":{"row":103,"column":18},"end":{"row":103,"column":19},"action":"insert","lines":["d"]},{"start":{"row":103,"column":19},"end":{"row":103,"column":20},"action":"insert","lines":[")"]},{"start":{"row":103,"column":20},"end":{"row":103,"column":21},"action":"insert","lines":["o"]},{"start":{"row":103,"column":21},"end":{"row":103,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":103,"column":21},"end":{"row":103,"column":22},"action":"remove","lines":["n"],"id":2099},{"start":{"row":103,"column":20},"end":{"row":103,"column":21},"action":"remove","lines":["o"]},{"start":{"row":103,"column":19},"end":{"row":103,"column":20},"action":"remove","lines":[")"]}],[{"start":{"row":103,"column":19},"end":{"row":103,"column":20},"action":"insert","lines":["_"],"id":2100},{"start":{"row":103,"column":20},"end":{"row":103,"column":21},"action":"insert","lines":["o"]},{"start":{"row":103,"column":21},"end":{"row":103,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":103,"column":26},"end":{"row":103,"column":33},"action":"remove","lines":["caption"],"id":2101},{"start":{"row":103,"column":26},"end":{"row":103,"column":27},"action":"insert","lines":["\""]},{"start":{"row":103,"column":27},"end":{"row":103,"column":28},"action":"insert","lines":["\""]}],[{"start":{"row":103,"column":27},"end":{"row":103,"column":28},"action":"insert","lines":["N"],"id":2102},{"start":{"row":103,"column":28},"end":{"row":103,"column":29},"action":"insert","lines":["u"]},{"start":{"row":103,"column":29},"end":{"row":103,"column":30},"action":"insert","lines":["l"]},{"start":{"row":103,"column":30},"end":{"row":103,"column":31},"action":"insert","lines":["l"]}],[{"start":{"row":104,"column":13},"end":{"row":104,"column":23},"action":"remove","lines":["image_tags"],"id":2103},{"start":{"row":104,"column":13},"end":{"row":104,"column":14},"action":"insert","lines":["d"]},{"start":{"row":104,"column":14},"end":{"row":104,"column":15},"action":"insert","lines":["e"]},{"start":{"row":104,"column":15},"end":{"row":104,"column":16},"action":"insert","lines":["l"]},{"start":{"row":104,"column":16},"end":{"row":104,"column":17},"action":"insert","lines":["e"]},{"start":{"row":104,"column":17},"end":{"row":104,"column":18},"action":"insert","lines":["t"]},{"start":{"row":104,"column":18},"end":{"row":104,"column":19},"action":"insert","lines":["e"]},{"start":{"row":104,"column":19},"end":{"row":104,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":104,"column":13},"end":{"row":104,"column":20},"action":"remove","lines":["deleted"],"id":2104},{"start":{"row":104,"column":13},"end":{"row":104,"column":23},"action":"insert","lines":["deleted_on"]}],[{"start":{"row":104,"column":27},"end":{"row":104,"column":31},"action":"remove","lines":["tags"],"id":2105},{"start":{"row":104,"column":27},"end":{"row":104,"column":28},"action":"insert","lines":["\""]},{"start":{"row":104,"column":28},"end":{"row":104,"column":29},"action":"insert","lines":["N"]},{"start":{"row":104,"column":29},"end":{"row":104,"column":30},"action":"insert","lines":["u"]},{"start":{"row":104,"column":30},"end":{"row":104,"column":31},"action":"insert","lines":["l"]},{"start":{"row":104,"column":31},"end":{"row":104,"column":32},"action":"insert","lines":["l"]}],[{"start":{"row":104,"column":32},"end":{"row":104,"column":33},"action":"insert","lines":["\""],"id":2106}],[{"start":{"row":104,"column":20},"end":{"row":104,"column":23},"action":"remove","lines":["_on"],"id":2107}],[{"start":{"row":105,"column":13},"end":{"row":105,"column":21},"action":"remove","lines":["uploaded"],"id":2108},{"start":{"row":105,"column":13},"end":{"row":105,"column":14},"action":"insert","lines":["d"]},{"start":{"row":105,"column":14},"end":{"row":105,"column":15},"action":"insert","lines":["e"]},{"start":{"row":105,"column":15},"end":{"row":105,"column":16},"action":"insert","lines":["l"]},{"start":{"row":105,"column":16},"end":{"row":105,"column":17},"action":"insert","lines":["e"]},{"start":{"row":105,"column":17},"end":{"row":105,"column":18},"action":"insert","lines":["t"]},{"start":{"row":105,"column":18},"end":{"row":105,"column":19},"action":"insert","lines":["e"]},{"start":{"row":105,"column":19},"end":{"row":105,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":105,"column":27},"end":{"row":105,"column":38},"action":"remove","lines":["timestamp()"],"id":2109},{"start":{"row":105,"column":27},"end":{"row":105,"column":33},"action":"insert","lines":["\"Null\""]}],[{"start":{"row":108,"column":4},"end":{"row":110,"column":41},"action":"remove","lines":["        # Converts filesize to mb 3sf","            'file_size' : round((filesize/1000000),3),","            'file_type' : file_extension,"],"id":2110},{"start":{"row":108,"column":0},"end":{"row":108,"column":4},"action":"remove","lines":["    "]},{"start":{"row":107,"column":34},"end":{"row":108,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":107,"column":34},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":2111},{"start":{"row":108,"column":0},"end":{"row":108,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":108,"column":12},"end":{"row":108,"column":14},"action":"insert","lines":["''"],"id":2112}],[{"start":{"row":108,"column":13},"end":{"row":108,"column":14},"action":"insert","lines":["i"],"id":2113},{"start":{"row":108,"column":14},"end":{"row":108,"column":15},"action":"insert","lines":["m"]},{"start":{"row":108,"column":15},"end":{"row":108,"column":16},"action":"insert","lines":["a"]},{"start":{"row":108,"column":16},"end":{"row":108,"column":17},"action":"insert","lines":["g"]},{"start":{"row":108,"column":17},"end":{"row":108,"column":18},"action":"insert","lines":["e"]},{"start":{"row":108,"column":18},"end":{"row":108,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":108,"column":20},"end":{"row":108,"column":21},"action":"insert","lines":[" "],"id":2114},{"start":{"row":108,"column":21},"end":{"row":108,"column":22},"action":"insert","lines":[":"]}],[{"start":{"row":108,"column":22},"end":{"row":108,"column":23},"action":"insert","lines":[" "],"id":2115}],[{"start":{"row":108,"column":23},"end":{"row":108,"column":39},"action":"insert","lines":["[\"blank\", \"red\"]"],"id":2116}],[{"start":{"row":108,"column":39},"end":{"row":108,"column":40},"action":"insert","lines":[","],"id":2117}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "],"id":2118},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"insert","lines":["    "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"insert","lines":["    "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":4},"action":"insert","lines":["    "]},{"start":{"row":107,"column":0},"end":{"row":107,"column":4},"action":"insert","lines":["    "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":4},"action":"insert","lines":["    "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":97,"column":4},"end":{"row":98,"column":0},"action":"remove","lines":["",""],"id":2119},{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"remove","lines":["    "]},{"start":{"row":96,"column":61},"end":{"row":97,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":102,"column":16},"end":{"row":102,"column":35},"action":"remove","lines":["'deleted' : \"Null\","],"id":2120},{"start":{"row":102,"column":12},"end":{"row":102,"column":16},"action":"remove","lines":["    "]},{"start":{"row":102,"column":8},"end":{"row":102,"column":12},"action":"remove","lines":["    "]},{"start":{"row":102,"column":4},"end":{"row":102,"column":8},"action":"remove","lines":["    "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"remove","lines":["    "]},{"start":{"row":101,"column":37},"end":{"row":102,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":103,"column":16},"end":{"row":103,"column":29},"action":"remove","lines":["'deleted': 0,"],"id":2121}],[{"start":{"row":102,"column":16},"end":{"row":103,"column":0},"action":"insert","lines":["",""],"id":2122},{"start":{"row":103,"column":0},"end":{"row":103,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":102,"column":16},"end":{"row":102,"column":29},"action":"insert","lines":["'deleted': 0,"],"id":2123}],[{"start":{"row":104,"column":12},"end":{"row":104,"column":16},"action":"remove","lines":["    "],"id":2124},{"start":{"row":104,"column":8},"end":{"row":104,"column":12},"action":"remove","lines":["    "]},{"start":{"row":104,"column":4},"end":{"row":104,"column":8},"action":"remove","lines":["    "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"remove","lines":["    "]},{"start":{"row":103,"column":38},"end":{"row":104,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":103,"column":38},"end":{"row":104,"column":38},"action":"remove","lines":["","                'deleted_on' : \"null\","],"id":2125}],[{"start":{"row":106,"column":0},"end":{"row":107,"column":0},"action":"insert","lines":["",""],"id":2126},{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":108,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["<document or array of documents>,","   {","     writeConcern: <document>,","     ordered: <boolean>","   }"],"id":2127}],[{"start":{"row":112,"column":4},"end":{"row":113,"column":0},"action":"insert","lines":["",""],"id":2128},{"start":{"row":113,"column":0},"end":{"row":113,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":104,"column":41},"end":{"row":104,"column":42},"action":"remove","lines":["\""],"id":2129},{"start":{"row":104,"column":40},"end":{"row":104,"column":41},"action":"remove","lines":["d"]},{"start":{"row":104,"column":39},"end":{"row":104,"column":40},"action":"remove","lines":["e"]},{"start":{"row":104,"column":38},"end":{"row":104,"column":39},"action":"remove","lines":["r"]},{"start":{"row":104,"column":37},"end":{"row":104,"column":38},"action":"remove","lines":["\""]},{"start":{"row":104,"column":36},"end":{"row":104,"column":37},"action":"remove","lines":[" "]},{"start":{"row":104,"column":35},"end":{"row":104,"column":36},"action":"remove","lines":[","]},{"start":{"row":104,"column":34},"end":{"row":104,"column":35},"action":"remove","lines":["\""]},{"start":{"row":104,"column":33},"end":{"row":104,"column":34},"action":"remove","lines":["k"]},{"start":{"row":104,"column":32},"end":{"row":104,"column":33},"action":"remove","lines":["n"]},{"start":{"row":104,"column":31},"end":{"row":104,"column":32},"action":"remove","lines":["a"]},{"start":{"row":104,"column":30},"end":{"row":104,"column":31},"action":"remove","lines":["l"]},{"start":{"row":104,"column":29},"end":{"row":104,"column":30},"action":"remove","lines":["b"]}],[{"start":{"row":104,"column":28},"end":{"row":104,"column":29},"action":"remove","lines":["\""],"id":2130}],[{"start":{"row":104,"column":28},"end":{"row":104,"column":29},"action":"insert","lines":["0"],"id":2131}],[{"start":{"row":104,"column":28},"end":{"row":104,"column":29},"action":"insert","lines":["'"],"id":2132}],[{"start":{"row":104,"column":30},"end":{"row":104,"column":31},"action":"insert","lines":["'"],"id":2133},{"start":{"row":104,"column":31},"end":{"row":104,"column":32},"action":"insert","lines":[":"]}],[{"start":{"row":104,"column":32},"end":{"row":104,"column":34},"action":"insert","lines":["\"\""],"id":2134}],[{"start":{"row":104,"column":33},"end":{"row":104,"column":34},"action":"insert","lines":["0"],"id":2135}],[{"start":{"row":104,"column":34},"end":{"row":104,"column":35},"action":"remove","lines":["\""],"id":2136}],[{"start":{"row":104,"column":34},"end":{"row":104,"column":35},"action":"insert","lines":["'"],"id":2137}],[{"start":{"row":104,"column":32},"end":{"row":104,"column":33},"action":"remove","lines":["\""],"id":2138}],[{"start":{"row":104,"column":32},"end":{"row":104,"column":33},"action":"insert","lines":["'"],"id":2139}],[{"start":{"row":104,"column":27},"end":{"row":104,"column":28},"action":"insert","lines":["'"],"id":2140}],[{"start":{"row":104,"column":27},"end":{"row":104,"column":28},"action":"remove","lines":["'"],"id":2141}],[{"start":{"row":104,"column":27},"end":{"row":104,"column":28},"action":"insert","lines":["\""],"id":2142}],[{"start":{"row":104,"column":37},"end":{"row":104,"column":38},"action":"insert","lines":["\""],"id":2143}],[{"start":{"row":108,"column":0},"end":{"row":113,"column":3},"action":"remove","lines":["<document or array of documents>,","   {","     writeConcern: <document>,","     ordered: <boolean>","   }","   "],"id":2144},{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"remove","lines":["",""]},{"start":{"row":106,"column":0},"end":{"row":107,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":18},"end":{"row":106,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":107,"column":44},"end":{"row":107,"column":63},"action":"remove","lines":[", albumid = albumid"],"id":2145}],[{"start":{"row":93,"column":20},"end":{"row":93,"column":29},"action":"remove","lines":["<albumid>"],"id":2146}],[{"start":{"row":93,"column":20},"end":{"row":93,"column":21},"action":"remove","lines":["/"],"id":2147}],[{"start":{"row":93,"column":20},"end":{"row":93,"column":29},"action":"remove","lines":["edit_form"],"id":2148},{"start":{"row":93,"column":20},"end":{"row":93,"column":37},"action":"insert","lines":["create_album_form"]}],[{"start":{"row":102,"column":28},"end":{"row":102,"column":29},"action":"insert","lines":["'"],"id":2149}],[{"start":{"row":102,"column":27},"end":{"row":102,"column":28},"action":"insert","lines":["'"],"id":2150}],[{"start":{"row":104,"column":28},"end":{"row":104,"column":37},"action":"remove","lines":["['0':'0']"],"id":2151}],[{"start":{"row":104,"column":28},"end":{"row":104,"column":29},"action":"insert","lines":["A"],"id":2152},{"start":{"row":104,"column":29},"end":{"row":104,"column":30},"action":"insert","lines":["r"]},{"start":{"row":104,"column":30},"end":{"row":104,"column":31},"action":"insert","lines":["r"]},{"start":{"row":104,"column":31},"end":{"row":104,"column":32},"action":"insert","lines":["a"]},{"start":{"row":104,"column":32},"end":{"row":104,"column":33},"action":"insert","lines":["y"]}],[{"start":{"row":95,"column":17},"end":{"row":95,"column":18},"action":"insert","lines":["s"],"id":2153},{"start":{"row":95,"column":18},"end":{"row":95,"column":19},"action":"insert","lines":["t"]},{"start":{"row":95,"column":19},"end":{"row":95,"column":20},"action":"insert","lines":["r"]},{"start":{"row":95,"column":20},"end":{"row":95,"column":21},"action":"insert","lines":["("]}],[{"start":{"row":95,"column":51},"end":{"row":95,"column":52},"action":"insert","lines":[")"],"id":2154}],[{"start":{"row":96,"column":24},"end":{"row":96,"column":25},"action":"insert","lines":["s"],"id":2155},{"start":{"row":96,"column":25},"end":{"row":96,"column":26},"action":"insert","lines":["t"]},{"start":{"row":96,"column":26},"end":{"row":96,"column":27},"action":"insert","lines":["r"]},{"start":{"row":96,"column":27},"end":{"row":96,"column":28},"action":"insert","lines":["("]}],[{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"insert","lines":[")"],"id":2156}],[{"start":{"row":104,"column":27},"end":{"row":104,"column":34},"action":"remove","lines":["\"Array\""],"id":2157}],[{"start":{"row":104,"column":27},"end":{"row":104,"column":28},"action":"insert","lines":["["],"id":2158},{"start":{"row":104,"column":28},"end":{"row":104,"column":29},"action":"insert","lines":["]"]}],[{"start":{"row":45,"column":27},"end":{"row":45,"column":28},"action":"insert","lines":["\\"],"id":2160}],[{"start":{"row":45,"column":27},"end":{"row":45,"column":28},"action":"remove","lines":["\\"],"id":2161},{"start":{"row":45,"column":26},"end":{"row":45,"column":27},"action":"remove","lines":[")"]},{"start":{"row":45,"column":25},"end":{"row":45,"column":26},"action":"remove","lines":[")"]},{"start":{"row":45,"column":24},"end":{"row":45,"column":25},"action":"remove","lines":["s"]},{"start":{"row":45,"column":23},"end":{"row":45,"column":24},"action":"remove","lines":["t"]},{"start":{"row":45,"column":22},"end":{"row":45,"column":23},"action":"remove","lines":["l"]},{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"remove","lines":["u"]},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"remove","lines":["s"]},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"remove","lines":["e"]},{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"remove","lines":["r"]},{"start":{"row":45,"column":17},"end":{"row":45,"column":18},"action":"remove","lines":["("]},{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"remove","lines":["s"]},{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"remove","lines":["p"]},{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"remove","lines":["m"]},{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"remove","lines":["u"]},{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"remove","lines":["d"]},{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"remove","lines":["("]},{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"remove","lines":["t"]},{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"remove","lines":["n"]},{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"remove","lines":["i"]},{"start":{"row":45,"column":7},"end":{"row":45,"column":8},"action":"remove","lines":["r"]},{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"remove","lines":["p"]},{"start":{"row":45,"column":5},"end":{"row":45,"column":6},"action":"remove","lines":[" "]}],[{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"remove","lines":["#"],"id":2162},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "]},{"start":{"row":44,"column":33},"end":{"row":45,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":45,"column":28},"end":{"row":45,"column":33},"action":"remove","lines":["index"],"id":2163},{"start":{"row":45,"column":28},"end":{"row":45,"column":29},"action":"insert","lines":["h"]},{"start":{"row":45,"column":29},"end":{"row":45,"column":30},"action":"insert","lines":["o"]},{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["m"]},{"start":{"row":45,"column":31},"end":{"row":45,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":28},"end":{"row":45,"column":32},"action":"remove","lines":["home"],"id":2164}],[{"start":{"row":45,"column":28},"end":{"row":45,"column":29},"action":"insert","lines":["i"],"id":2165},{"start":{"row":45,"column":29},"end":{"row":45,"column":30},"action":"insert","lines":["n"]},{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["d"]},{"start":{"row":45,"column":31},"end":{"row":45,"column":32},"action":"insert","lines":["e"]},{"start":{"row":45,"column":32},"end":{"row":45,"column":33},"action":"insert","lines":["x"]}],[{"start":{"row":51,"column":28},"end":{"row":51,"column":35},"action":"remove","lines":["layout1"],"id":2167},{"start":{"row":51,"column":28},"end":{"row":51,"column":42},"action":"insert","lines":["display_albums"]}]]},"ace":{"folds":[],"scrolltop":446.5,"scrollleft":0,"selection":{"start":{"row":51,"column":42},"end":{"row":51,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":36,"state":"start","mode":"ace/mode/python"}},"timestamp":1567054352846,"hash":"c603aaf01d0761368cef1e426a63630438e8e9fa"}