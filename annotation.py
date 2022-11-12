class Annotator:

    def __init__(self):
        self.iCount = 0
        self.stepCount = 0

    def wrapper(self, qep):
        final = self.annotate(qep[0][0][0]['Plan'], True)[1]
        final = final[:-3]
        final += " to get the final result."
        print(final)
        return final 

    def annotate(self, query, first = False):
        
        joinTables = []

        result = ""

        if "Plans" in query:
            for plan in query["Plans"]:
                temp = self.annotate(plan)
                joinTables.append(temp[0])
                result += temp[1]


        self.stepCount += 1
        result += "Step {}: ".format(self.stepCount)


        if query["Node Type"] == 'Seq Scan':
            table = query["Relation Name"]
            name = query["Alias"]
            msg = "Perform sequential scan on table {} as {}".format(table, name)
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            msg += ". \n"
            return table, result + msg


        elif query["Node Type"] == 'Index-Only Scan':
            table = query["Relation Name"]
            name = query["Alias"]
            msg = "Perform index scan on table {} as {} using index on {}".format(table, name, query["Index Name"])
            if "Index Cond" in query:
                msg += " where {}".format(query["Index Cond"])
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            msg += ". \n"
            return table, result + msg


        elif query["Node Type"] == 'Index Scan':
            table = query["Relation Name"]
            name = query["Alias"]
            msg = "Perform index scan on table {} as {} using index on {}".format(table, name, query["Index Name"])
            if "Index Cond" in query:
                msg += " where {}".format(query["Index Cond"])
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            msg += ". \n"
            return table, result + msg



        elif query["Node Type"] == 'Foreign Scan':
            table = query["Relation Name"]
            name = query["Alias"]
            msg = "Perform foreign scan on table {} from schema {} as {}. \n".format(table, query["Schema"], name)
            return table, result + msg


        elif query["Node Type"] == 'CTE Scan':
            table = query["CTE Name"]
            name = query["Alias"]
            msg = "Perform CTE scan on table {} as {}".format(table, name)
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            msg += ". \n"
            return table, result + msg



        
        elif query["Node Type"] == 'Function Scan':
            table = query["Schema"]
            name = query["alias"]
            msg = "Perform function {} on schema {} and return the results as {}".format(query["Function Name"], table, name)
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            msg += ". \n"
            return table, result + msg

        
        elif query["Node Type"] == 'Subquery Scan':
            msg = "The subquery results from the previous operation is read"
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            msg += ". \n"
            return joinTables[0], result + msg

        elif query["Node Type"] == 'Nested Loop':
            self.iCount += 1
            msg = "Perform a nested loop join on tables {} and {}".format(joinTables[0], joinTables[1])
            if "Join Filter" in query:
                msg += " under the condition {}".format(joinTables[0], joinTables[1], query["Join Filter"])
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg

        
        elif query["Node Type"] == 'TID Scan':
            table = query["Relation"]
            name = query["Alias"]
            msg = "Perform a Tuple ID scan on table {} as {}. \n".format(table ,name)
            return table, result + msg

        


        
        elif query["Node Type"] == 'Hash Join':
            self.iCount += 1
            msg = "Perform a hash join on tables {} and {}".format(joinTables[0], joinTables[1])
            if "Hash Cond" in query:
                msg += " under the condition {}".format(query["Hash Cond"])
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg


        elif query["Node Type"] == 'Merge Join':
            self.iCount += 1
            msg = "Perform a merge join on tables {} and {}".format(joinTables[0], joinTables[1])
            if "Merge Cond" in query:
                msg += " under the condition {}".format(query["Merge Cond"])
            if "Filter" in query:
                msg += " with filter {}".format(query["Filter"])
            msg += ". \n"
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg

        
        elif query["Node Type"] == 'Aggregate':
            self.iCount += 1
            msg = "Perform aggregate on table {}".format(joinTables[0])
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg

        

        
        elif query["Node Type"] == 'Gather':
            self.iCount += 1
            msg = ("Perform gather on table {}".format(joinTables[0]))
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg


        elif query["Node Type"] == 'Append':
            self.iCount += 1
            msg = "Append the results from table {} to table {}".format(joinTables[0], joinTables[1]) 
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg


        
        elif query["Node Type"] == 'Gather Merge':
            msg = "The results of the previous operation are gathered and merged. \n"
            return joinTables[0], result + msg

        
        elif query["Node Type"] == 'GroupAggregate':
            self.iCount += 1
            msg = "Perform a group aggregate on table {}".format(joinTables[0])
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg

        elif query["Node Type"] == 'HashAggregate':
            self.iCount += 1
            msg = "Perform a hash aggregate on table {}".format(joinTables[0])
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg

        
        elif query["Node Type"] == 'Hash':
            msg = "Perform hashing on table {}. \n".format(joinTables[0])
            return joinTables[0], result + msg





        elif query["Node Type"] == 'Incremental Sort':
            msg = "An incremetal sort is performed on table {} with sort key {}. \n".format(joinTables[0], query["Sort Key"])
            return joinTables[0], result + msg


        elif query["Node Type"] == 'Limit':
            msg = "The specified number of rows is selected from table {}. \n".format(joinTables[0])
            return joinTables[0], result + msg


        elif query["Node Type"] == 'Materialize':
            msg = "Materialize table {}. \n".format(joinTables[0])
            return joinTables[0], result + msg


        elif query["Node Type"] == 'ModifyTable':
            table = query["Relation Name"]
            msg = "Table {} is modified. \n ".format(table)
            return table, result + msg

        elif query["Node Type"] == 'MergeAppend':
            self.iCount += 1
            msg = "Results from table {} are appended to table {}".format(joinTables[0], joinTables[1])
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg





        elif query["Node Type"] == 'SetOp':
            self.iCount += 1
            msg = "A set operation is performed on table {}".format(joinTables[0])
            if not first:
                msg += " to get intermediate table T{}. \n".format(self.iCount)
            else: msg += ". \n"
            return "T" + str(self.iCount), result + msg


        elif query["Node Type"] == 'Sort':
            msg = "Perform a sort on table {} with sort key {}. \n".format(joinTables[0], query["Sort Key"])
            return joinTables[0], result + msg


        elif query["Node Type"] == 'Unique':
            table = query["Subplan Name"] if "Subplan Name" in query else joinTables[0]
            msg = "Duplicates are removed from table {}. \n".format(table)
            return table, result + msg


        else:
            msg = "Perform {}. \n".format(query["Node Type"])
            return joinTables[0], result + msg
