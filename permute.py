import itertools

scans = ["Sequential Scan", "Index Scan", "Index-only Scan","Bitmap Scan", "TID Scan"]
joins = ["Nested-Loop Join", "Hash Join", "Merge Join"]
others = ["Hashed Aggregation","Materialization", "Explicit Sort"]
HA = ["Hashed Aggregation"]
MA = ["Materialization"]
ES = ["Explicit Sort"]
selected_scans = []
selected_joins = []

selected_es = ["Explicit Sort"]
selected_ma = ["Materialization"]
selected_ha = ["Hashed Aggregation"]

scan_flag = False
join_flag = False

PARAM_DICT = {"Bitmap Scan": "enable_bitmapscan",
               "Index Scan": "enable_indexscan",
               "Index-only Scan": "enable_indexonlyscan",
               "Sequential Scan": "enable_seqscan",
               "TID Scan": "enable_tidscan",
               "Hash Join": "enable_hashjoin",
               "Merge Join": "enable_mergejoin",
               "Nested-Loop Join": "enable_nestloop",
               "Hashed Aggregation": "enable_hashagg",
               "Materialization": "enable_material",
               "Explicit Sort": "enable_sort"
              }

POSTGRES_CONFIG_DICT = { "enable_bitmapscan": True,
                        "enable_hashagg": True,
                        "enable_hashjoin": True,
                        "enable_indexscan" : True,
                        "enable_indexonlyscan" : True,
                        "enable_material": True,
                        "enable_mergejoin": True,
                        "enable_nestloop": True,
                        "enable_seqscan": True,
                        "enable_sort": True,
                        "enable_tidscan": True
                         }

permutations = []

params = ["Merge Join", 'Hashed Aggregation']
for p in params:
    if p in scans:
        selected_scans.append(p)
    elif p in joins:
        selected_joins.append(p)
    elif p in HA:
        selected_ha.append(" ")
    elif p in MA:
        selected_ma.append(" ")
    elif p in ES:
        selected_es.append(" ")

if len(selected_scans)==0:
    selected_scans.append(" ")
    scan_flag = True
    
if len(selected_joins)==0:
    selected_joins.append(" ")
    join_flag = True
        
to_perm = [selected_scans] + [selected_joins] + [selected_ha] + [selected_ma] + [selected_es]
print(to_perm)
p = list(itertools.product(*to_perm))
print(" ")
print(p)
permutation = []

if scan_flag==True:
    selected_scans=[]
if join_flag==True:
    selected_joins=[]

for perm in p:
    if len(selected_joins)!=0 and len(selected_scans)!=0:
        current_perm = { "enable_bitmapscan": False,
                            "enable_hashagg": False,
                            "enable_hashjoin": False,
                            "enable_indexscan" : False,
                            "enable_indexonlyscan" : False,
                            "enable_material": False,
                            "enable_mergejoin": False,
                            "enable_nestloop": False,
                            "enable_seqscan": False,
                            "enable_sort": False,
                            "enable_tidscan": False
                             }
    elif len(selected_joins)==0:
        current_perm = { "enable_bitmapscan": False,
                            "enable_hashagg": False,
                            "enable_hashjoin": True,
                            "enable_indexscan" : False,
                            "enable_indexonlyscan" : False,
                            "enable_material": False,
                            "enable_mergejoin": True,
                            "enable_nestloop": True,
                            "enable_seqscan": False,
                            "enable_sort": False,
                            "enable_tidscan": False
                                }
    
    elif len(selected_scans)==0:
        current_perm = { "enable_bitmapscan": True,
                            "enable_hashagg": False,
                            "enable_hashjoin": False,
                            "enable_indexscan" : True,
                            "enable_indexonlyscan" : True,
                            "enable_material": False,
                            "enable_mergejoin": False,
                            "enable_nestloop": False,
                            "enable_seqscan": True,
                            "enable_sort": False,
                            "enable_tidscan": True
                             }

    for item in perm:
        arg = PARAM_DICT.get(item, False)
        if arg:
            current_perm[arg] = True
    permutation.append(current_perm)
    
print(permutation)

