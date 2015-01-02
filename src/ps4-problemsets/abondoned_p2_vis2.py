from pandas import *
from ggplot import *

import pandasql

#
# headers for the booth station mapping data
# 
# Note: remote maps to the unit from the turnstile data set
#
remote_booth_station_headers = ["remote","booth","station","linename","division"]

#
# Reference data that relates the turnstile units to their station etc.
#
# Note: to answer this question I need the following reference set of data
# ordinarilly I would read this in from a csv file but as I can't control the
# data files on the udacity server side I have hard coded the values inline
#
#
remote_booth_station = [("R001","A060","WHITEHALL ST","R1","BMT"),\
("R001","A058","WHITEHALL ST","R1","BMT"),\
("R001","R101S","SOUTH FERRY","R1","IRT"),\
("R002","A077","FULTON ST","ACJZ2345","BMT"),\
("R002","A081","FULTON ST","ACJZ2345","BMT"),\
("R002","A082","FULTON ST","ACJZ2345","BMT"),\
("R003","J025","CYPRESS HILLS","J","BMT"),\
("R004","J028","ELDERTS LANE","JZ","BMT"),\
("R005","J030","FOREST PARKWAY","J","BMT"),\
("R006","J031","WOODHAVEN BLVD","JZ","BMT"),\
("R006","J032","WOODHAVEN BLVD","JZ","BMT"),\
("R007","J034","104 ST","JZ","BMT"),\
("R008","J035","111 ST","J","BMT"),\
("R009","J037","121 ST","JZ","BMT"),\
("R010","N062A","42 ST-PA BUS TE","ACENQRS1237","IND"),\
("R010","N060","42 ST-PA BUS TE","ACENQRS1237","IND"),\
("R011","N063A","42 ST-PA BUS TE","ACENQRS1237","IND"),\
("R011","N062","42 ST-PA BUS TE","ACENQRS1237","IND"),\
("R011","N063","42 ST-PA BUS TE","ACENQRS1237","IND"),\
("R012","N067","34 ST-PENN STA","ACE","IND"),\
("R012","N065","34 ST-PENN STA","ACE","IND"),\
("R012","N068","34 ST-PENN STA","ACE","IND"),\
("R012","N070","34 ST-PENN STA","ACE","IND"),\
("R012","N072","34 ST-PENN STA","ACE","IND"),\
("R013","N071","34 ST-PENN STA","ACE","IND"),\
("R013","N069","34 ST-PENN STA","ACE","IND"),\
("R013","N073","34 ST-PENN STA","ACE","IND"),\
("R014","N095","FULTON ST","ACJZ2345","IND"),\
("R014","R205","FULTON ST","ACJZ2345","IRT"),\
("R014","R206","FULTON ST","2345ACJZ","IRT"),\
("R014","R208","FULTON ST","2345ACJZ","IRT"),\
("R014","R205A","FULTON ST","2345ACJZ","IRT"),\
("R015","N303","5 AVE-53 ST","EM","IND"),\
("R015","N304","5 AVE-53 ST","EM","IND"),\
("R016","N305A","LEXINGTON-53 ST","EM6","IND"),\
("R017","N306","LEXINGTON-53 ST","EM6","IND"),\
("R017","N305","LEXINGTON-53 ST","EM6","IND"),\
("R018","N324","ROOSEVELT AVE","EFMR7","IND"),\
("R018","N323","ROOSEVELT AVE","EFMR7","IND"),\
("R018","R525","74 ST-BROADWAY","EFMR7","IRT"),\
("R019","N343","JAMAICA-179 ST","F","IND"),\
("R019","N342","JAMAICA-179 ST","F","IND"),\
("R020","N500","47-50 ST-ROCK","BDFM","IND"),\
("R020","N501","47-50 ST-ROCK","BDFM","IND"),\
("R020","N501A","47-50 ST-ROCK","BDFM","IND"),\
("R021","N503","42 ST-BRYANT PK","BDFM7","IND"),\
("R021","N502","42 ST-BRYANT PK","BDFM7","IND"),\
("R021","N504","42 ST-BRYANT PK","BDFM7","IND"),\
("R022","N506","34 ST-HERALD SQ","BDFMNQR","IND"),\
("R022","A022","34 ST-HERALD SQ","BDFMNQR","BMT"),\
("R022","N505","34 ST-HERALD SQ","BDFMNQR","IND"),\
("R023","N507","34 ST-HERALD SQ","BDFMNQR","IND"),\
("R023","A025","34 ST-HERALD SQ","BDFMNQR","BMT"),\
("R024","N605","SUTPHIN BLVD","EJZ","IND"),\
("R025","N606","JAMAICA CENTER","EJZ","IND"),\
("R025","N607","JAMAICA CENTER","EJZ","IND"),\
("R027","R111","WALL ST","23","IRT"),\
("R027","R110","WALL ST","23","IRT"),\
("R027","R112","WALL ST","23","IRT"),\
("R027","R112A","WALL ST","23","IRT"),\
("R028","R113A","FULTON ST","2345ACJZ","IRT"),\
("R028","R113","FULTON ST","2345ACJZ","IRT"),\
("R028","R114","FULTON ST","2345ACJZ","IRT"),\
("R029","R115","PARK PLACE","23ACE","IRT"),\
("R029","N094","WORLD TRADE CTR","23ACE","IND"),\
("R029","N091","CHAMBERS ST","ACE23","IND"),\
("R029","N092","CHAMBERS ST","ACE23","IND"),\
("R030","R116","CHAMBERS ST","123","IRT"),\
("R031","R141","34 ST-PENN STA","123","IRT"),\
("R031","R135","34 ST-PENN STA","123","IRT"),\
("R031","R137","34 ST-PENN STA","123","IRT"),\
("R031","R139","34 ST-PENN STA","123","IRT"),\
("R032","R145","42 ST-TIMES SQ","1237ACENQRS","IRT"),\
("R032","A021","42 ST-TIMES SQ","1237ACENQRS","BMT"),\
("R032","R143","42 ST-TIMES SQ","ACENQRS1237","IRT"),\
("R032","R146","42 ST-TIMES SQ","1237ACENQRS","IRT"),\
("R033","R151","42 ST-TIMES SQ","1237ACENQRS","IRT"),\
("R033","R148","42 ST-TIMES SQ","1237ACENQRS","IRT"),\
("R033","R150","42 ST-TIMES SQ","1237ACENQRS","IRT"),\
("R033","R153","42 ST-TIMES SQ","1237ACENQRS","IRT"),\
("R033","R147","42 ST-TIMES SQ","1237ACENQRS","IRT"),\
("R034","R174","125 ST","1","IRT"),\
("R035","R182","168 ST-BROADWAY","1AC","IRT"),\
("R035","N012","168 ST-BROADWAY","1AC","IND"),\
("R035","N013","168 ST-BROADWAY","AC1","IND"),\
("R036","R186","DYCKMAN ST","1","IRT"),\
("R037","R188","207 ST","1","IRT"),\
("R038","R190","215 ST","1","IRT"),\
("R039","R192","MARBLE HILL-225","1","IRT"),\
("R040","R194","231 ST","1","IRT"),\
("R041","R201","BOWLING GREEN","45","IRT"),\
("R041","R200A","BOWLING GREEN","45","IRT"),\
("R042","R202","BOWLING GREEN","45","IRT"),\
("R043","R203","WALL ST","45","IRT"),\
("R043","R203A","WALL ST","45","IRT"),\
("R043","R204","WALL ST","45","IRT"),\
("R043","R204A","WALL ST","45","IRT"),\
("R044","R210","BROOKLYN BRIDGE","456JZ","IRT"),\
("R044","A069","CHAMBERS ST","456JZ","BMT"),\
("R044","A071","CHAMBERS ST","JZ456","BMT"),\
("R044","R210A","BROOKLYN BRIDGE","JZ456","IRT"),\
("R045","R236","42 ST-GRD CNTRL","4567S","IRT"),\
("R045","R233","42 ST-GRD CNTRL","4567S","IRT"),\
("R046","R238","42 ST-GRD CNTRL","4567S","IRT"),\
("R046","R237","42 ST-GRD CNTRL","4567S","IRT"),\
("R046","R238A","42 ST-GRD CNTRL","4567S","IRT"),\
("R047","R240","42 ST-GRD CNTRL","4567S","IRT"),\
("R047","R237B","42 ST-GRD CNTRL","4567S","IRT"),\
("R048","R241A","42 ST-GRD CNTRL","4567S","IRT"),\
("R049","R243","51 ST","6","IRT"),\
("R049","R242","51 ST","6","IRT"),\
("R049","R242A","51 ST","6","IRT"),\
("R050","R244","59 ST","456NQR","IRT"),\
("R050","R244A","59 ST","456NQR","IRT"),\
("R050","A004","LEXINGTON AVE","456NQR","BMT"),\
("R051","R245","59 ST","456NQR","IRT"),\
("R051","R245A","59 ST","456NQR","IRT"),\
("R051","A002","LEXINGTON AVE","456NQR","BMT"),\
("R052","R294","WOODLAWN ROAD","4","IRT"),\
("R053","R311","149 ST-3 AVE","25","IRT"),\
("R053","R310","149 ST-3 AVE","25","IRT"),\
("R054","R501","5 AVE-BRYANT PK","7BDFM","IRT"),\
("R054","R500","5 AVE-BRYANT PK","7BDFM","IRT"),\
("R055","R533","MAIN ST","7","IRT"),\
("R055","R534","MAIN ST","7","IRT"),\
("R056","R608","NEVINS ST","2345","IRT"),\
("R056","R609","NEVINS ST","2345","IRT"),\
("R057","R610","ATLANTIC AVE","2345BDNQR","IRT"),\
("R057","B001","ATLANTIC AVE","2345BDNQR","BMT"),\
("R057","B002","ATLANTIC AVE","BDNQR2345","BMT"),\
("R057","C009","PACIFIC ST","BDNQR2345","BMT"),\
("R058","R617","BERGEN ST","23","IRT"),\
("R058","R618","BERGEN ST","23","IRT"),\
("R059","R619","GRAND ARMY PLAZ","23","IRT"),\
("R060","R621","EASTERN PKWY","23","IRT"),\
("R061","R623","NOSTRAND AVE","3","IRT"),\
("R062","R626","CROWN HTS-UTICA","34","IRT"),\
("R062","R625","CROWN HTS-UTICA","34","IRT"),\
("R063","R627","SUTTER AVE","3","IRT"),\
("R064","R628","SARATOGA AVE","3","IRT"),\
("R065","R629","ROCKAWAY AVE","3","IRT"),\
("R066","R630","JUNIUS ST","3","IRT"),\
("R067","R632","PENNSYLVANIA AV","3","IRT"),\
("R068","R633","VAN SICLEN AVE","3","IRT"),\
("R069","R634","NEW LOTS AVE","3","IRT"),\
("R070","S101","ST. GEORGE","1","SRT"),\
("R070","S101A","ST. GEORGE","1","SRT"),\
("R076","MCC07","2 BDWY CUST SRV","45","IRT"),\
("R079","A006","5 AVE-59 ST","NQR","BMT"),\
("R079","A007","5 AVE-59 ST","NQR","BMT"),\
("R080","A010","57 ST-7 AVE","NQR","BMT"),\
("R080","A011","57 ST-7 AVE","NQR","BMT"),\
("R081","A015","49 ST-7 AVE","NQR","BMT"),\
("R081","A013","49 ST-7 AVE","NQR","BMT"),\
("R081","A014","49 ST-7 AVE","NQR","BMT"),\
("R081","A016","49 ST-7 AVE","NQR","BMT"),\
("R082","A029","28 ST-BROADWAY","NR","BMT"),\
("R082","A027","28 ST-BROADWAY","NR","BMT"),\
("R083","A031","23 ST-5 AVE","NR","BMT"),\
("R083","A030","23 ST-5 AVE","NR","BMT"),\
("R084","R158","59 ST-COLUMBUS","1ABCD","IRT"),\
("R084","N049","59 ST-COLUMBUS","1ABCD","IND"),\
("R084","N051","59 ST-COLUMBUS","ABCD1","IND"),\
("R085","A038","8 ST-B'WAY NYU","NR","BMT"),\
("R085","A039","8 ST-B'WAY NYU","NR","BMT"),\
("R086","A041","PRINCE ST-B'WAY","NR","BMT"),\
("R086","A042","PRINCE ST-B'WAY","NR","BMT"),\
("R087","A047","MURRAY ST-B'WAY","R","BMT"),\
("R088","A050","CORTLANDT ST","R","BMT"),\
("R088","A052","CORTLANDT ST","R","BMT"),\
("R088","A051","CORTLANDT ST","R","BMT"),\
("R088","A053","CORTLANDT ST","R","BMT"),\
("R089","C003","JAY ST-METROTEC","R","BMT"),\
("R089","C004","JAY ST-METROTEC","R","BMT"),\
("R090","R510","BEEBE-39 AVE","NQ","BMT"),\
("R091","R511","WASHINGTON-36 A","NQ","BMT"),\
("R092","R512","BROADWAY-31 ST","NQ","BMT"),\
("R093","R513","GRAND-30 AVE","NQ","BMT"),\
("R094","R514","HOYT ST-ASTORIA","NQ","BMT"),\
("R095","R515","DITMARS BL-31 S","NQ","BMT"),\
("R096","R526","82 ST-JACKSON H","7","IRT"),\
("R097","R528","JUNCTION BLVD","7","IRT"),\
("R098","B016","CHURCH AVE","BQ","BMT"),\
("R098","B015","CHURCH AVE","BQ","BMT"),\
("R099","C008","DEKALB AVE","BDNQR","BMT"),\
("R100","K026","METROPOLITAN AV","M","BMT"),\
("R101","N020","145 ST","ABCD","IND"),\
("R101","N019","145 ST","ABCD","IND"),\
("R102","N026","125 ST","ACBD","IND"),\
("R102","N025","125 ST","ACBD","IND"),\
("R103","N124","BROADWAY-ENY","ACJLZ","IND"),\
("R104","N207","167 ST","BD","IND"),\
("R104","N206","167 ST","BD","IND"),\
("R105","R127","14 ST","123FLM","IRT"),\
("R105","R128","14 ST","123FLM","IRT"),\
("R106","R418","CASTLE HILL AVE","6","IRT"),\
("R107","R420","WESTCHESTER SQ","6","IRT"),\
("R108","R602","BOROUGH HALL/CT","2345R","IRT"),\
("R108","C001","BOROUGH HALL/CT","2345R","BMT"),\
("R108","R601A","BOROUGH HALL/CT","R2345","IRT"),\
("R108","R604","BOROUGH HALL/CT","2345R","IRT"),\
("R109","R639","CHURCH AVE","25","IRT"),\
("R110","R645","FLATBUSH AVE","25","IRT"),\
("R110","R646","FLATBUSH AVE","25","IRT"),\
("R110","R647","FLATBUSH AVE","25","IRT"),\
("R111","N076","23 ST","CE","IND"),\
("R111","N075","23 ST","CE","IND"),\
("R111","N077","23 ST","CE","IND"),\
("R112","N217","FORDHAM ROAD","BD","IND"),\
("R112","N218","FORDHAM ROAD","BD","IND"),\
("R113","N301","7 AVE-53 ST","BDE","IND"),\
("R113","N300","7 AVE-53 ST","BDE","IND"),\
("R114","N339A","PARSONS BLVD","F","IND"),\
("R114","N339","PARSONS BLVD","F","IND"),\
("R115","N340","169 ST","F","IND"),\
("R115","N340A","169 ST","F","IND"),\
("R116","R154","50 ST","1","IRT"),\
("R116","R155","50 ST","1","IRT"),\
("R117","R197","242 ST","1","IRT"),\
("R118","A066","CANAL ST","JNQRZ6","BMT"),\
("R119","R289","FORDHAM ROAD","4","IRT"),\
("R120","R415","MORRISON AVE","6","IRT"),\
("R121","R509","QUEENSBORO PLZ","7NQ","IRT"),\
("R122","R527","90 ST-ELMHURST","7","IRT"),\
("R123","R622","FRANKLIN AVE","2345S","IRT"),\
("R124","R624","KINGSTON AVE","3","IRT"),\
("R125","A083","BROAD ST","JZ","BMT"),\
("R125","A084","BROAD ST","JZ","BMT"),\
("R125","A085","BROAD ST","JZ","BMT"),\
("R126","N010","175 ST","A","IND"),\
("R126","N011","175 ST","A","IND"),\
("R127","N103","JAY ST-METROTEC","ACF","IND"),\
("R127","N102","JAY ST-METROTEC","ACF","IND"),\
("R128","N338B","SUTPHIN BLVD","F","IND"),\
("R128","N338","SUTPHIN BLVD","F","IND"),\
("R129","N532","BERGEN ST","FG","IND"),\
("R129","N531","BERGEN ST","FG","IND"),\
("R129","N533","BERGEN ST","FG","IND"),\
("R130","N557","KINGS HIGHWAY","F","IND"),\
("R130","N558","KINGS HIGHWAY","F","IND"),\
("R131","R227","23 ST","6","IRT"),\
("R131","R227A","23 ST","6","IRT"),\
("R131","R226","23 ST","6","IRT"),\
("R131","R226A","23 ST","6","IRT"),\
("R132","R258","125 ST","456","IRT"),\
("R133","R293","MOSHOLU PARKWAY","4","IRT"),\
("R134","R507","HUNTERS PT AVE","7","IRT"),\
("R135","R643","NEWKIRK AVE","25","IRT"),\
("R135","R644","NEWKIRK AVE","25","IRT"),\
("R136","B027","SHEEPSHEAD BAY","BQ","BMT"),\
("R136","B028","SHEEPSHEAD BAY","BQ","BMT"),\
("R137","H026","MYRTLE AVE","LM","BMT"),\
("R137","H027","MYRTLE AVE","LM","BMT"),\
("R138","N080","W 4 ST-WASH SQ","ABCDEFM","IND"),\
("R138","N083","W 4 ST-WASH SQ","ABCDEFM","IND"),\
("R139","N089","CANAL ST","ACE","IND"),\
("R139","N090","CANAL ST","ACE","IND"),\
("R140","N309A","QUEENS PLAZA","EMR","IND"),\
("R140","N310","QUEENS PLAZA","EMR","IND"),\
("R141","N333A","FOREST HILLS-71","EFMR","IND"),\
("R141","N333","FOREST HILLS-71","EFMR","IND"),\
("R141","N333B","FOREST HILLS-71","EFMR","IND"),\
("R142","A061","ESSEX ST","FJMZ","BMT"),\
("R142","N525","DELANCEY ST","FJMZ","IND"),\
("R142","N526","DELANCEY ST","FJMZ","IND"),\
("R143","R228","28 ST","6","IRT"),\
("R143","R229","28 ST","6","IRT"),\
("R143","R230","28 ST","6","IRT"),\
("R144","R251","96 ST","6","IRT"),\
("R145","R336","WAKEFIELD-241","2","IRT"),\
("R146","R412","HUNTS POINT AVE","6","IRT"),\
("R147","R523","61 ST/WOODSIDE","7","IRT"),\
("R148","B014","PARKSIDE AVE","BQ","BMT"),\
("R149","B019","NEWKIRK AVE","BQ","BMT"),\
("R150","B025","AVE U","BQ","BMT"),\
("R151","G001","STILLWELL AVE","DFNQ","BMT"),\
("R151","G009","STILLWELL AVE","DFNQ","BMT"),\
("R152","H041","ROCKAWAY PKY","L","BMT"),\
("R153","N120","UTICA AVE","AC","IND"),\
("R153","N120A","UTICA AVE","AC","IND"),\
("R154","N213","TREMONT AVE","BD","IND"),\
("R154","N214","TREMONT AVE","BD","IND"),\
("R155","N221","KINGSBRIDGE RD","BD","IND"),\
("R155","N220","KINGSBRIDGE RD","BD","IND"),\
("R156","N222","BEDFORD PARK BL","BD","IND"),\
("R156","N223","BEDFORD PARK BL","BD","IND"),\
("R157","N224","NORWOOD-205 ST","D","IND"),\
("R157","N225","NORWOOD-205 ST","D","IND"),\
("R158","N336","UNION TPK-KEW G","EF","IND"),\
("R158","N335","UNION TPK-KEW G","EF","IND"),\
("R159","R173","116 ST-COLUMBIA","1","IRT"),\
("R160","R219","ASTOR PLACE","6","IRT"),\
("R160","R220","ASTOR PLACE","6","IRT"),\
("R161","R290","KINGSBRIDGE RD","4","IRT"),\
("R162","R414","ELDER AVE","6","IRT"),\
("R163","N512","14 ST-6 AVE","FLM123","IND"),\
("R163","H003","6 AVE","FLM123","BMT"),\
("R163","N510","14 ST-6 AVE","FLM123","IND"),\
("R163","N511","14 ST-6 AVE","FLM123","IND"),\
("R163","N513","14 ST-6 AVE","FLM123","IND"),\
("R164","R160A","66 ST-LINCOLN","1","IRT"),\
("R164","R159","66 ST-LINCOLN","1","IRT"),\
("R164","R160","66 ST-LINCOLN","1","IRT"),\
("R165","S102","TOMPKINSVILLE","1","SRT"),\
("R166","R162","79 ST","1","IRT"),\
("R166","R163","79 ST","1","IRT"),\
("R167","R164","86 ST","1","IRT"),\
("R167","R165","86 ST","1","IRT"),\
("R167","R166","86 ST","1","IRT"),\
("R168","R168A","96 ST","123","IRT"),\
("R168","R168","96 ST","123","IRT"),\
("R169","R176","137 ST-CITY COL","1","IRT"),\
("R169","R175","137 ST-CITY COL","1","IRT"),\
("R170","A035","14 ST-UNION SQ","LNQR456","BMT"),\
("R170","R221","14 ST-UNION SQ","LNQR456","IRT"),\
("R170","A033","14 ST-UNION SQ","456LNQR","BMT"),\
("R170","A034","14 ST-UNION SQ","LNQR456","BMT"),\
("R170","A036","14 ST-UNION SQ","LNQR456","BMT"),\
("R170","A037","14 ST-UNION SQ","LNRQ456","BMT"),\
("R171","B004","7 AVE","BQ","BMT"),\
("R172","B029","BRIGHTON BEACH","BQ","BMT"),\
("R172","B031","BRIGHTON BEACH","BQ","BMT"),\
("R173","N002A","INWOOD-207 ST","A","IND"),\
("R173","N001","INWOOD-207 ST","A","IND"),\
("R174","N007A","181 ST","A","IND"),\
("R174","N009","181 ST","A","IND"),\
("R175","H001","8 AVE","ACEL","BMT"),\
("R175","N078","14 ST","ACEL","IND"),\
("R176","R231","33 ST","6","IRT"),\
("R176","R231A","33 ST","6","IRT"),\
("R176","R232","33 ST","6","IRT"),\
("R176","R232A","33 ST","6","IRT"),\
("R177","R246","68ST-HUNTER COL","6","IRT"),\
("R178","R248","77 ST","6","IRT"),\
("R178","R247","77 ST","6","IRT"),\
("R179","R250","86 ST","456","IRT"),\
("R179","R249","86 ST","456","IRT"),\
("R180","R252","103 ST","6","IRT"),\
("R181","R253","110 ST","6","IRT"),\
("R181","R254","110 ST","6","IRT"),\
("R182","R256","116 ST","6","IRT"),\
("R182","R257","116 ST","6","IRT"),\
("R183","R291","BEDFORD PARK BL","4","IRT"),\
("R184","B018","CORTELYOU ROAD","BQ","BMT"),\
("R185","N003","DYCKMAN-200 ST","A","IND"),\
("R186","N043","86 ST","BC","IND"),\
("R186","N042","86 ST","BC","IND"),\
("R187","N044","81 ST-MUSEUM","BC","IND"),\
("R187","N045","81 ST-MUSEUM","BC","IND"),\
("R188","N057","50 ST","CE","IND"),\
("R188","N056","50 ST","CE","IND"),\
("R189","R125","CHRISTOPHER ST","1","IRT"),\
("R189","R126","CHRISTOPHER ST","1","IRT"),\
("R190","R131","23 ST","1","IRT"),\
("R190","R132","23 ST","1","IRT"),\
("R191","R170","103 ST","1","IRT"),\
("R192","R172","110 ST-CATHEDRL","1","IRT"),\
("R192","R171","110 ST-CATHEDRL","1","IRT"),\
("R193","R180","157 ST","1","IRT"),\
("R193","R179","157 ST","1","IRT"),\
("R194","R217A","BLEECKER ST","6DF","IRT"),\
("R195","N203","161 ST-YANKEE","BD4","IND"),\
("R195","N204","161 ST-YANKEE","BD4","IND"),\
("R195","N205","161 ST-YANKEE","BD4","IND"),\
("R195","R262","161 ST-YANKEE","BD4","IRT"),\
("R195","R262A","161 ST-YANKEE","4BD","IRT"),\
("R195","R262B","161 ST-YANKEE","4BD","IRT"),\
("R196","B012","PROSPECT PARK","BQS","BMT"),\
("R196","B013","PROSPECT PARK","BQS","BMT"),\
("R197","C018","36 ST","DNR","BMT"),\
("R198","N116","NOSTRAND AVE","AC","IND"),\
("R198","N117","NOSTRAND AVE","AC","IND"),\
("R199","N119","KINGSTON-THROOP","C","IND"),\
("R199","N118","KINGSTON-THROOP","C","IND"),\
("R200","N128","EUCLID AVE","AC","IND"),\
("R201","N329","WOODHAVEN BLVD","MR","IND"),\
("R201","N329A","WOODHAVEN BLVD","MR","IND"),\
("R202","N330B","63 DR-REGO PARK","MR","IND"),\
("R202","N330C","63 DR-REGO PARK","MR","IND"),\
("R203","N509","23 ST-6 AVE","FM","IND"),\
("R204","N546","CHURCH AVE","FG","IND"),\
("R204","N545","CHURCH AVE","FG","IND"),\
("R205","R261","149 ST-GR CONC","245","IRT"),\
("R205","R260","149 ST-GR CONC","245","IRT"),\
("R206","R304","125 ST","23","IRT"),\
("R206","R305","125 ST","23","IRT"),\
("R207","R306","135 ST","23","IRT"),\
("R207","R307","135 ST","23","IRT"),\
("R208","R529","103 ST-CORONA","7","IRT"),\
("R209","R636","STERLING ST","25","IRT"),\
("R210","R641","BEVERLY ROAD","25","IRT"),\
("R211","B024","KINGS HIGHWAY","BQ","BMT"),\
("R211","B023","KINGS HIGHWAY","BQ","BMT"),\
("R211","B024A","KINGS HIGHWAY","BQ","BMT"),\
("R212","C021","59 ST","NR","BMT"),\
("R212","C022","59 ST","NR","BMT"),\
("R213","C023","BAY RIDGE AVE","R","BMT"),\
("R214","C024","77 ST","R","BMT"),\
("R215","C025","86 ST","R","BMT"),\
("R215","C026","86 ST","R","BMT"),\
("R216","C027","BAY RIDGE-95 ST","R","BMT"),\
("R216","C028","BAY RIDGE-95 ST","R","BMT"),\
("R217","N108","HOYT/SCHERMER","ACG","IND"),\
("R218","N325A","ELMHURST AVE","MR","IND"),\
("R219","N331","67 AVE","MR","IND"),\
("R219","N332","67 AVE","MR","IND"),\
("R220","N535","CARROLL ST","FG","IND"),\
("R220","N534","CARROLL ST","FG","IND"),\
("R221","R283","167 ST","4","IRT"),\
("R222","R417","E 177 ST-PARKCH","6","IRT"),\
("R223","R519","46 ST-BLISS ST","7","IRT"),\
("R223","R520","46 ST-BLISS ST","7","IRT"),\
("R224","R600","CLARK ST","23","IRT"),\
("R225","R606","HOYT ST","23","IRT"),\
("R226","R728","GUN HILL ROAD","5","IRT"),\
("R227","A055","RECTOR ST","R","BMT"),\
("R227","A054","RECTOR ST","R","BMT"),\
("R228","B021","AVE J","BQ","BMT"),\
("R229","B022","AVE M","BQ","BMT"),\
("R230","B026","NECK ROAD","BQ","BMT"),\
("R231","C010","UNION ST","R","BMT"),\
("R231","C011","UNION ST","R","BMT"),\
("R232","C019","45 ST","R","BMT"),\
("R233","C020","53 ST","R","BMT"),\
("R234","E004","50 ST","D","BMT"),\
("R235","H009","BEDFORD AVE","L","BMT"),\
("R236","H023","DEKALB AVE","L","BMT"),\
("R237","N215","182-183 ST","BD","IND"),\
("R238","N315","STEINWAY ST","MR","IND"),\
("R238","N314","STEINWAY ST","MR","IND"),\
("R239","N405","GREENPOINT AVE","G","IND"),\
("R239","N403","GREENPOINT AVE","G","IND"),\
("R240","N520","GRAND ST","BD","IND"),\
("R241","N542","15 ST-PROSPECT","FG","IND"),\
("R241","N541","15 ST-PROSPECT","FG","IND"),\
("R242","N549","18 AVE","F","IND"),\
("R242","N550","18 AVE","F","IND"),\
("R243","R284","170 ST","4","IRT"),\
("R244","R287","BURNSIDE AVE","4","IRT"),\
("R245","R416","ST LAWRENCE AVE","6","IRT"),\
("R246","C014","PROSPECT AVE","R","BMT"),\
("R247","E005","55 ST","D","BMT"),\
("R248","H007","1 AVE","L","BMT"),\
("R248","H008","1 AVE","L","BMT"),\
("R249","H014","GRAHAM AVE","L","BMT"),\
("R249","H013","GRAHAM AVE","L","BMT"),\
("R250","H016","GRAND ST","L","BMT"),\
("R250","H015","GRAND ST","L","BMT"),\
("R251","N040","96 ST","BC","IND"),\
("R251","N039","96 ST","BC","IND"),\
("R252","N100","HIGH ST","AC","IND"),\
("R252","N101","HIGH ST","AC","IND"),\
("R253","N210","174-175 ST","BD","IND"),\
("R253","N212","174-175 ST","BD","IND"),\
("R254","N327","GRAND AV-NEWTON","MR","IND"),\
("R255","N337","VAN WYCK BLVD","EF","IND"),\
("R256","N408A","NASSAU AV","G","IND"),\
("R257","N529","EAST BROADWAY","F","IND"),\
("R257","N528","EAST BROADWAY","F","IND"),\
("R258","N537","4 AVE","DFGMNR","IND"),\
("R258","C012","9 ST","DFGMNR","BMT"),\
("R259","N602","ROOSEVELT IS","F","IND"),\
("R260","R183","181 ST","1","IRT"),\
("R261","R518","40 ST-LOWERY ST","7","IRT"),\
("R262","B017","BEVERLEY ROAD","BQ","BMT"),\
("R263","B020","AVE H","BQ","BMT"),\
("R264","B032","OCEAN PARKWAY","Q","BMT"),\
("R264","B034","OCEAN PARKWAY","Q","BMT"),\
("R265","H017","MONTROSE AVE","L","BMT"),\
("R266","H028","HALSEY ST","L","BMT"),\
("R266","H030","HALSEY ST","L","BMT"),\
("R267","N316","46 ST","MR","IND"),\
("R267","N316A","46 ST","MR","IND"),\
("R267","N317","46 ST","MR","IND"),\
("R268","N409","METROPOLITAN AV","GL","IND"),\
("R268","H012","LORIMER ST","GL","BMT"),\
("R269","N417","BEDFORD/NOSTRAN","G","IND"),\
("R269","N418","BEDFORD/NOSTRAN","G","IND"),\
("R270","N536","SMITH-9 ST","FG","IND"),\
("R271","N561","AVE X","F","IND"),\
("R272","R133","28 ST","1","IRT"),\
("R272","R134","28 ST","1","IRT"),\
("R273","R178","145 ST","1","IRT"),\
("R273","R177","145 ST","1","IRT"),\
("R274","R185","191 ST","1","IRT"),\
("R275","R288","183 ST","4","IRT"),\
("R276","R504","VERNON/JACKSON","7","IRT"),\
("R276","R503","VERNON/JACKSON","7","IRT"),\
("R276","R506","VERNON/JACKSON","7","IRT"),\
("R277","R635","PRESIDENT ST","25","IRT"),\
("R278","C016","25 ST","R","BMT"),\
("R279","H022","JEFFERSON ST","L","BMT"),\
("R280","N006A","190 ST","A","IND"),\
("R281","N046","72 ST","BC","IND"),\
("R282","N086","SPRING ST","CE","IND"),\
("R282","N087","SPRING ST","CE","IND"),\
("R283","N110","LAFAYETTE AVE","C","IND"),\
("R284","N111","CLINTON-WASH AV","C","IND"),\
("R284","N112A","CLINTON-WASH AV","C","IND"),\
("R285","N196","FAR ROCKAWAY","A","IND"),\
("R286","N415","MYRTLE-WILLOUGH","G","IND"),\
("R286","N416","MYRTLE-WILLOUGH","G","IND"),\
("R287","N419","CLASSON AVE","G","IND"),\
("R288","N539A","7 AV-PARK SLOPE","FG","IND"),\
("R289","N543","FT HAMILTON PKY","FG","IND"),\
("R289","N544","FT HAMILTON PKY","FG","IND"),\
("R290","R123","HOUSTON ST","1","IRT"),\
("R290","R121","HOUSTON ST","1","IRT"),\
("R290","R122","HOUSTON ST","1","IRT"),\
("R290","R124","HOUSTON ST","1","IRT"),\
("R291","R516","33 ST/RAWSON ST","7","IRT"),\
("R291","R517","33 ST/RAWSON ST","7","IRT"),\
("R292","R729","BAYCHESTER AVE","5","IRT"),\
("R293","R138","34 ST-PENN STA","123ACE","IRT"),\
("R293","R142","34 ST-PENN STA","123ACE","IRT"),\
("R294","H019","MORGAN AVE","L","BMT"),\
("R295","H032","WILSON AVE","L","BMT"),\
("R296","N016A","163 ST-AMSTERDM","C","IND"),\
("R297","N113","FRANKLIN AVE","ACS","IND"),\
("R297","N114","FRANKLIN AVE","ACS","IND"),\
("R298","N318","NORTHERN BLVD","MR","IND"),\
("R298","N319","NORTHERN BLVD","MR","IND"),\
("R299","N412","BROADWAY","G","IND"),\
("R300","N523","2 AVE","F","IND"),\
("R300","N521","2 AVE","F","IND"),\
("R301","N530","YORK ST","F","IND"),\
("R302","N600","57 ST","F","IND"),\
("R303","N603","21 ST","F","IND"),\
("R304","R103","RECTOR ST","1","IRT"),\
("R304","R102","RECTOR ST","1","IRT"),\
("R305","R107","CORTLANDT ST","1","IRT"),\
("R305","R106","CORTLANDT ST","1","IRT"),\
("R305","R108","CORTLANDT ST","1","IRT"),\
("R305","R109","CORTLANDT ST","1","IRT"),\
("R306","R196","238 ST","1","IRT"),\
("R307","R259","138 ST-GR CONC","45","IRT"),\
("R308","R285","MT EDEN AVE","4","IRT"),\
("R309","R286","176 ST","4","IRT"),\
("R310","R530","111 ST","7","IRT"),\
("R311","A064","BOWERY","JZ","BMT"),\
("R312","G011","W 8 ST-AQUARIUM","FQ","BMT"),\
("R312","G015","W 8 ST-AQUARIUM","FQ","BMT"),\
("R313","H033","BUSHWICK AVE","L","BMT"),\
("R314","N037","103 ST","BC","IND"),\
("R315","N202","155 ST","BD","IND"),\
("R316","N414","FLUSHING AVE","G","IND"),\
("R316","N414A","FLUSHING AVE","G","IND"),\
("R317","N420B","CLINTON-WASH AV","G","IND"),\
("R318","N422","FULTON ST","G","IND"),\
("R319","N601","LEXINGTON AVE","F","IND"),\
("R320","R119","CANAL ST","1","IRT"),\
("R320","R120","CANAL ST","1","IRT"),\
("R321","R129","18 ST","1","IRT"),\
("R321","R130","18 ST","1","IRT"),\
("R322","R215","SPRING ST","6","IRT"),\
("R322","R216","SPRING ST","6","IRT"),\
("R323","R301","110 ST-CPN","23","IRT"),\
("R324","R303","116 ST","23","IRT"),\
("R324","R302","116 ST","23","IRT"),\
("R325","R413","WHITLOCK AVE","6","IRT"),\
("R326","R419","ZEREGA AVE","6","IRT"),\
("R327","R521","52 ST-LINCOLN","7","IRT"),\
("R328","R532","METS-WILLETS PT","7","IRT"),\
("R328","R532G","METS-WILLETS PT","7","IRT"),\
("R328","R532H","METS-WILLETS PT","7","IRT"),\
("R329","R726","MORRIS PARK","5","IRT"),\
("R330","H005","3 AVE","L","BMT"),\
("R330","H006","3 AVE","L","BMT"),\
("R331","N017","155 ST","C","IND"),\
("R332","N024","135 ST","BC","IND"),\
("R332","N023","135 ST","BC","IND"),\
("R332","N022","135 ST","BC","IND"),\
("R333","N030","116 ST","BC","IND"),\
("R333","N029","116 ST","BC","IND"),\
("R334","N035","CATHEDRL-110 ST","BC","IND"),\
("R334","N034","CATHEDRL-110 ST","BC","IND"),\
("R335","N191","BEACH 67 ST","A","IND"),\
("R336","N192","BEACH 60 ST","A","IND"),\
("R337","N193","BEACH 44 ST","A","IND"),\
("R338","N194","BEACH 36 ST","A","IND"),\
("R339","N312","36 ST","MR","IND"),\
("R339","N311","36 ST","MR","IND"),\
("R340","N322","65 ST","MR","IND"),\
("R341","N334B","75 AVE","EF","IND"),\
("R342","N604","JAMAICA-VAN WYC","E","IND"),\
("R343","R117","FRANKLIN ST","1","IRT"),\
("R343","R118","FRANKLIN ST","1","IRT"),\
("R344","R308","145 ST","3","IRT"),\
("R345","R309","148 ST-LENOX","3","IRT"),\
("R346","R508","COURT SQ","7","IRT"),\
("R347","R524","69 ST-FISK AVE","7","IRT"),\
("R348","H035","ATLANTIC AVE","L","BMT"),\
("R349","H037","SUTTER AVE","L","BMT"),\
("R350","H038","LIVONIA AVE","L","BMT"),\
("R352","J003","HEWES ST","JM","BMT"),\
("R353","J005","LORIMER ST","JM","BMT"),\
("R354","N137","OXFORD-104 ST","A","IND"),\
("R355","N139","GREENWOOD-111","A","IND"),\
("R355","N138","GREENWOOD-111","A","IND"),\
("R356","N141","LEFFERTS BLVD","A","IND"),\
("R357","N181","AQUEDUCT-N CNDT","A","IND"),\
("R358","N195","BEACH 25 ST","A","IND"),\
("R359","N307","COURT SQ-23 ST","EMG","IND"),\
("R359","N400","COURT SQ","EMG","IND"),\
("R359","N400A","COURT SQ","EMG","IND"),\
("R360","N401","VAN ALSTON-21ST","G","IND"),\
("R361","R328","PELHAM PARKWAY","25","IRT"),\
("R361","R327","PELHAM PARKWAY","25","IRT"),\
("R362","R329","ALLERTON AVE","25","IRT"),\
("R363","R330","BURKE AVE","25","IRT"),\
("R364","R331","GUN HILL ROAD","25","IRT"),\
("R365","R332","219 ST","25","IRT"),\
("R366","R333","225 ST","25","IRT"),\
("R367","R334","233 ST","25","IRT"),\
("R368","E001","9 AVE","D","BMT"),\
("R369","E003","FT HAMILTON PKY","D","BMT"),\
("R370","E009","71 ST","D","BMT"),\
("R371","E011","79 ST","D","BMT"),\
("R372","E012","18 AVE","D","BMT"),\
("R373","E013","20 AVE","D","BMT"),\
("R374","E014","BAY PARKWAY","D","BMT"),\
("R375","H039","NEW LOTS AVE","L","BMT"),\
("R376","H040","EAST 105 ST","L","BMT"),\
("R377","J007","FLUSHING AVE","JM","BMT"),\
("R378","J009","MYRTLE AVE","JMZ","BMT"),\
("R379","J012","KOSCIUSZKO ST","J","BMT"),\
("R380","J013","GATES AVE","JZ","BMT"),\
("R381","J016","HALSEY ST","J","BMT"),\
("R382","N129","GRANT AVE","A","IND"),\
("R383","N131","HUDSON-80 ST","A","IND"),\
("R383","N130","HUDSON-80 ST","A","IND"),\
("R384","N133","BOYD-88 ST","A","IND"),\
("R385","N134","ROCKAWAY BLVD","A","IND"),\
("R385","N135","ROCKAWAY BLVD","A","IND"),\
("R386","R322","174 ST","25","IRT"),\
("R386","R321","174 ST","25","IRT"),\
("R387","R323","E TREMONT AVE","25","IRT"),\
("R387","R323A","E TREMONT AVE","25","IRT"),\
("R388","R325","E 180 ST","25","IRT"),\
("R389","R326","BRONX PARK EAST","25","IRT"),\
("R390","D002","8 AVE","N","BMT"),\
("R391","D003","FT HAMILTON PKY","N","BMT"),\
("R391","D004","FT HAMILTON PKY","N","BMT"),\
("R392","D008","18 AVE","N","BMT"),\
("R393","D009","20 AVE","N","BMT"),\
("R394","D010","BAY PKY-22 AVE","N","BMT"),\
("R394","D011","BAY PKY-22 AVE","N","BMT"),\
("R395","D012","KINGS HIGHWAY","N","BMT"),\
("R396","D015","AVE U","N","BMT"),\
("R397","D016","86 ST","N","BMT"),\
("R398","D005","NEW UTRECHT AVE","ND","BMT"),\
("R398","D006","NEW UTRECHT AVE","ND","BMT"),\
("R399","E015","25 AVE","D","BMT"),\
("R400","E016","BAY 50 ST","D","BMT"),\
("R401","K017","CENTRAL AVE","M","BMT"),\
("R402","K022","SENECA AVE","M","BMT"),\
("R403","K024","FOREST AVE","M","BMT"),\
("R404","K025","FRESH POND ROAD","M","BMT"),\
("R405","R312","JACKSON AVE","25","IRT"),\
("R406","R314","PROSPECT AVE","25","IRT"),\
("R406","R315","PROSPECT AVE","25","IRT"),\
("R407","R316","INTERVALE-163","25","IRT"),\
("R408","R318","SIMPSON ST","25","IRT"),\
("R408","R317","SIMPSON ST","25","IRT"),\
("R409","R320","FREEMAN ST","25","IRT"),\
("R409","R319","FREEMAN ST","25","IRT"),\
("R410","X001","NYC & CO - 7 AV","1","IRT"),\
("R411","B009","PARK PLACE","S","BMT"),\
("R412","B010","BOTANIC GARDEN","S2345","BMT"),\
("R413","K019","KNICKERBOCKER","M","BMT"),\
("R414","N182","HOWARD BCH-JFK","A","IND"),\
("R414","N182A","HOWARD BCH-JFK","A","IND"),\
("R415","N183","BROAD CHANNEL","AS","IND"),\
("R416","N184","BEACH 90 ST","AS","IND"),\
("R417","N185","BEACH 98 ST","AS","IND"),\
("R418","N186","BEACH 105 ST","AS","IND"),\
("R419","N187","ROCKAWAY PK 116","AS","IND"),\
("R420","N548","DITMAS AVE","F","IND"),\
("R420","N547","DITMAS AVE","F","IND"),\
("R421","N551","AVE I","F","IND"),\
("R422","N553","22 AVE-BAY PKY","F","IND"),\
("R423","N555","AVE N","F","IND"),\
("R423","N554","AVE N","F","IND"),\
("R424","N556","AVE P","F","IND"),\
("R425","N559","AVE U","F","IND"),\
("R426","N562","NEPTUNE AVE","F","IND"),\
("R427","R421","MIDDLETOWN ROAD","6","IRT"),\
("R428","R422","BUHRE AVE","6","IRT"),\
("R429","R423","PELHAM BAY PARK","6","IRT"),\
("R430","R727","PELHAM PARKWAY","5","IRT"),\
("R431","R730","DYRE AVE","5","IRT"),\
("R432","J017","CHAUNCEY ST","JZ","BMT"),\
("R433","J020","ALABAMA AVE","J","BMT"),\
("R434","J021","VAN SICLEN AVE","JZ","BMT"),\
("R435","J022","CLEVELAND ST","J","BMT"),\
("R436","J023","NORWOOD AVE","JZ","BMT"),\
("R437","J024","CRESCENT ST","JZ","BMT"),\
("R438","N121B","RALPH AVE","C","IND"),\
("R439","N122","ROCKAWAY AVE","C","IND"),\
("R439","N123B","ROCKAWAY AVE","C","IND"),\
("R440","N125","LIBERTY AVE","C","IND"),\
("R441","N126","VAN SICLEN AVE","C","IND"),\
("R442","N127","SHEPHERD AVE","C","IND"),\
("R443","N209","170 ST","BD","IND"),\
("R443","N208","170 ST","BD","IND"),\
("R444","R335","NEREID AVE","25","IRT"),\
("R445","R401","138 ST-3 AVE","6","IRT"),\
("R446","R402","BROOK AVE","6","IRT"),\
("R446","R403","BROOK AVE","6","IRT"),\
("R447","R404","CYPRESS AVE","6","IRT"),\
("R447","R405","CYPRESS AVE","6","IRT"),\
("R448","R406","E 143 ST","6","IRT"),\
("R448","R407","E 143 ST","6","IRT"),\
("R449","R408","E 149 ST","6","IRT"),\
("R449","R409","E 149 ST","6","IRT"),\
("R450","R410","LONGWOOD AVE","6","IRT"),\
("R450","R411","LONGWOOD AVE","6","IRT"),\
("R451","R637","WINTHROP ST","25","IRT"),\
("R452","R161B","72 ST","123","IRT"),\
("R452","R161A","72 ST","123","IRT"),\
("R453","N508","23 ST-6 AVE","FM","IND"),\
("R454","C015","PROSPECT AVE","R","BMT"),\
("R455","C017","25 ST","R","BMT"),\
("R456","R605","HOYT ST","23","IRT"),\
("R457","MCB1","METROCARD BUS 1","23","BMT"),\
("R458","MCB2","METROCARD BUS 2","23","BMT"),\
("R459","OB01","ORCHARD BEACH","6","IND"),\
("R460","J002","MARCY AVE","JMZ","BMT"),\
("R460","J001","MARCY AVE","JMZ","BMT"),\
("R461","N519","BROADWAY/LAFAY","BDFQ6","IND"),\
("R461","N519A","BROADWAY/LAFAY","BDFQ6","IND"),\
("R462","A043","CANAL ST","JNQRZ6","BMT"),\
("R462","A044","CANAL ST","JNQRZ6","BMT"),\
("R463","A046","CANAL ST","JNQRZ6","BMT"),\
("R463","R214","CANAL ST","JNQRZ6","IRT"),\
("R464","N181A","AQUEDUCT TRACK","A","IND"),\
("R465","MCV1","METROCARD VAN-1","1","BMT"),\
("R466","MCV2","METROCARD VAN-2","1","BMT"),\
("R467","MCV3","METROCARD VAN-3","1","BMT"),\
("R468","TRAM1","RIT-MANHATTAN","R","RIT"),\
("R469","TRAM2","RIT-ROOSEVELT","R","RIT"),\
("R470","X002","ELTINGVILLE PK","Z","SRT"),\
("R526","LI001","LIB-HEMPSTEAD","F","LIB"),\
("R532","WCCTR","WEST COUNTY CTR","5","BEE"),\
("R535","JFK01","JFK HOWARD BCH","A","IND"),\
("R535","JFK02","JFK HOWARD BCH","A","IND"),\
("R536","JFK03","JFK JAMAICA CT1","E","IND"),\
("R537","JFK04","JFK JAMAICA CT2","E","IND"),\
("R538","LGA01","LGA AIRPORT CTB","7","IRT"),\
("R540","PTH08","PATH WTC","1","PTH"),\
("R540","PTH21","PATH WTC 2","1","PTH"),\
("R541","PTH13","THIRTY ST","1","PTH"),\
("R541","PTH17","THIRTY THIRD ST","1","PTH"),\
("R542","PTH12","TWENTY THIRD ST","1","PTH"),\
("R543","PTH05","EXCHANGE PLACE","1","PTH"),\
("R544","PTH02","HARRISON","1","PTH"),\
("R545","PTH11","14TH STREET","1","PTH"),\
("R546","PTH06","PAVONIA/NEWPORT","1","PTH"),\
("R547","PTH10","9TH STREET","1","PTH"),\
("R548","PTH09","CHRISTOPHER ST","1","PTH"),\
("R549","PTH01","NEWARK HW BMEBE","1","PTH"),\
("R549","PTH18","NEWARK BM BW","1","PTH"),\
("R549","PTH19","NEWARK C","1","PTH"),\
("R549","PTH20","NEWARK HM HE","1","PTH"),\
("R550","PTH07","CITY / BUS","1","PTH"),\
("R550","PTH16","LACKAWANNA","1","PTH"),\
("R551","PTH04","GROVE STREET","1","PTH"),\
("R552","PTH03","JOURNAL SQUARE","1","PTH")]

def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''


    #
    # First we create a dataframe for our reference data that maps
    # remotes to booths to stations
    #
    remote_booth_station_df = DataFrame(remote_booth_station,\
                                    columns=remote_booth_station_headers)
                                
    #
    # Now we do something very dodgy!
    #
    # The data includes multiple booths for each remote, our turnstile data
    # however is reported at the remote level (not booth level) so we will
    # assume the remote reports an aggregate across all of its booths.
    #
    # We can therefore simplify the reference data, removing booth. This will
    # prevent double reporting when we join with the turnstile data                                
    #                                
    q = """
        SELECT DISTINCT remote, station, linename
        FROM remote_booth_station_df
        """
                                    
                                    
    remote_station_df = pandasql.sqldf(q, locals()) 
                                   
    # o.k. this is a dodgy place to do this logic but hey
    #
    # pandasql doesn't like the first unnamed column
    # I don't need it so bin it
    turnstile_weather = turnstile_weather.drop([turnstile_weather.columns[0]], axis=1)


    #
    # Now we need the daily average of turnstile entries per unit (remote)
    #
    q = """
        SELECT unit, avg(entries) AS avg_entries
        FROM
        (SELECT  unit, DATEn, sum(ENTRIESn_hourly) AS entries
        FROM turnstile_weather
        GROUP BY unit, DATEn)
        GROUP BY unit
        """

    
    turnstile_weather_daily_avg = pandasql.sqldf(q, locals()) 

    #
    # Finally we are in a position to join the weather data with our station
    # reference data
    #
    q = """
        SELECT r.linename, r.station, sum(t.avg_entries) as avg_entries
        FROM turnstile_weather_daily_avg t
        INNER JOIN remote_station_df r
        ON t.unit = r.remote
        GROUP BY linename, station
        """
        
    # Execute your SQL command against the pandas frame
    station_avgentries_by_line = pandasql.sqldf(q, locals())

    q = """
        SELECT * FROM station_avgentries_by_line ORDER BY avg_entries
        """

    # Execute your SQL command against the pandas frame
    ordered_station_avgentries_by_line = pandasql.sqldf(q, locals())
        
    
    print ordered_station_avgentries_by_line 
    
    
    """
    plot = ggplot(aes(x='factor(station)',weight='avg_entries'), data=p) + \
     scale_x_discrete('station') +\
     geom_bar()
    """ 
    #plot = qplot('station', 'avg_entries', data=p, stat="bar")     
    
    plot = ggplot(ordered_station_avgentries_by_line, aes(x = 'linename', y='avg_entries')) +\
            geom_bar(aes(weight='avg_entries', stat="bar")) +\
            ggtitle('NYC subway ridership') + xlab('Linename') + ylab('Avg Entries')
            


    #plot = ggplot(p, aes(x = 'linename', y='avg_entries')) +\
    #        geom_bar(aes(position="stack"), stat = "identity") +\
    #        ggtitle('NYC subway ridership') + xlab('Linename') + ylab('Avg Entries')  


    
    """
    plot = ggplot(station_avgentries_by_line,aes(x='linename',weight='avg_entries')) + \
            ggtitle("Average NYC Subway Turnstile Entries by Hour of the Day") +\
            ylab("Average Entries") +\
            xlab("Linename") +\
            geom_bar() +\
            theme(legend_title = element_text(colour="chocolate", size=16, face="bold"))
            """


    return plot

"""



    plot = # your code here
    return plot
"""

#print plot_weather_data(pandas.read_csv("./turnstile_data_master_with_weather.csv"))
print plot_weather_data(pandas.read_csv("./turnstile_data_master_with_weather.csv"))
