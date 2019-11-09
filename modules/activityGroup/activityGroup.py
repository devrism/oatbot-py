# Manager for the ActivityGroup class. 
class ActivityGroupManager:
    # This is automatically instantiated on boot.
    def __init__(self):
        self.groupList = [] # List of ActivityGroup objects.
        self.groupMaximum = 10
        self.groupNameMaximum = 250 # character limit for a group name

    def findGroup(self, name):
        """ Finds an ActivityGroup with the given name, if it exists.
        Args: 
            name (str): Name of the group to be created.
            groupLeader (Message.author.id): ID of the user that created the group.
        Returns:
            Returns the ActivityGroup if a group with that name exists. Otherwise returns None.
        """
        if self.groupList and name:
            for group in self.groupList:
                if group.groupName == name:
                    return group
        return None

    def parseGroupCommand(self, message):


    # utility function to check if user is a group leader or admin
    # Takes in a Group and Member object, returns True or False
    def isGroupAdmin(self, group, member):
        isAdmin = False
        if group.groupLeader == member:
            isAdmin = True
        for role in member.roles:
            if role.id == '283838280766849025':
                isAdmin = True
                break
        return isAdmin

    def createGroup(self, groupName, groupLeader):
        """ Returns error message if group name already exists in the group list or if the group name is invalid.
        Args: 
            groupName (str): Name of the group to be created.
            groupLeader (Message.author.id): ID of the user that created the group.
        Returns:
            str: Returns a success message if the group creation is successful.
        """
        print("activityGroups in list: " + str(len(self.groupList)) + "groupList status: " + str(self.groupList)) #TODO delete

        # Group name cannot be more than 300 characters
        if len(groupName) > self.groupNameMaximum:
            return "Error: Group name cannot be longer than " + str(self.groupNameMaximum) " characters. Use a shorter name and try again."
        # Group number cannot exceed 100
        elif len(self.groupList) >= self.groupMaximum:
            return "Error: Number of groups cannot exceed " + str(self.groupMaximum) + ". Please delete some groups and try again."
        elif groupName == "":
            return "Error: Group name cannot be empty. Try again using `/group [groupName]`, without brackets!"

        else:
            # Do not create a group if one with the same name already exists.
            newGroup = self.findGroup(groupName) 
            if newGroup:
                return "Error: A group with that name already exists! Please delete the pre-existing group using `/group delete [groupName]` or choose a different group name."
            else:
                self.groupList.append(ActivityGroup(groupName, groupLeader))
                return "🎉 Successfully created group: " + groupName + ". Tell all your friends to join using `/group join [groupName]`, without brackets!"

    # Returns a message containing:
    # A ping for every member of the group
    # The group start message.
    def launchGroup(self, groupName, groupLeader): #TODO
        response = "🎉 Party time! A group called " + groupName + "! In the groupList: " #TODO list out the members of the group and ping them
        return response

    # Adds a given user to the specified group.
    # @param groupNick: String representing the name of the group to be added to
    # @param newMember: String representing the id of the user to be added to the group.
    # needs to be formatted like this: <@!123456789>
    def addMemberToGroup(self, groupNick, newMember):
        group = self.findGroup(groupNick)
        if group:
            group.addMember(newMember)
            return "Added to group: " + group.groupName + "."
        return "Could not find group."

    def getGroupMembers(self, groupName):
        groupMembers = self.groupList[groupName].viewMembers()
        response = "TODO this is a list of group members" #groupMembers #TODO format this response to include a group member list that indicates the group leader
        return response
    
    # groupName: string representing the group nickname
    # deleter: a discord.Member object
    def deleteGroup(self, groupName, deleter):
        # If deleter is not the leader of the group or is not an admin, return an error.
        removedGroup = self.findGroup(groupName)
        isAdmin = self.isGroupAdmin(removedGroup, deleter)
        if removedGroup and (removedGroup.groupLeader == deleter or isAdmin == True): 
            self.groupList.remove(removedGroup)
            print("activityGroups in list: " + str(len(self.groupList)) + "groupList status: " + str(self.groupList)) 
            return "Successfully deleted group: " + groupName + "."
        else:
            return "Error: Could not find group or you do not have the proper permissions to delete the group; only admins and the group leader are able to delete a group. Check who is the group leader using `/group members [groupName]`, without brackets."


class ActivityGroup:
    # The group leader is assigned to the user that creates 
    # the group and automatically added to the members list.
    def __init__(self, groupName, groupLeader, description = ''):
        self.groupName = groupName
        self.groupLeader = groupLeader
        self.members = [groupLeader]
        self.description = description

    # Add a member to the group.
    def addMember(self, newMember):
        self.members = self.members.append(newMember)

    # Remove a member from the group.
    def removeMember(self, member):
        self.members = self.members.remove(member)

    # Return the list of group members.
    def viewMembers(self):
        return self.members

    # Print group details.
    def printGroup(self):
        #TODO
        return