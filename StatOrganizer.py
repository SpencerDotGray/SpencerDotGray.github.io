
class StatOrganizer:

    def get_refined_list(stats, desiredVal):

        if stats is None:
            return []

        returnList = []

        for key in stats.keys():

            if str(stats[key]) == str(desiredVal):
                returnList.append(key)
        
        return returnList