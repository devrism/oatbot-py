# Manager for the ActivityGroup class. 
class ActivityGroupManager:
    # This is automatically instantiated on boot.
    def __init__(self):
        self.groupList = [] # List of ActivityGroup objects.

    # Returns the group if a group with that name exists.
    # Otherwise returns None.
    def isGroupNameInGroupList(self, groupName):
        for group in self.groupList:
            if group.groupName == groupName:
                return group
        return None

    # Returns error message if group name already exists in the group 
    # list or if the group name is invalid.
    # Returns success message if group creation is successful
    def createGroup(self, groupName, groupLeader):
        if groupName == "":
            return "Error: Group name cannot be empty. Try again using `/group [groupName]`, without brackets!"
        else:
            newGroup = self.isGroupNameInGroupList(groupName)
            if newGroup is not None:
                return "Error: A group with that name already exists! Please delete the pre-existing group using `/group delete [groupName]` or choose a different group name."
            else:
                newGroupActivity = ActivityGroup(groupName, groupLeader)
                self.groupList = self.groupList.append(newGroupActivity)
                return "🎉 Successfully created group: " + groupName + ". Tell all your friends to join using `/group join [groupName]`, without brackets!"

    # Returns a message containing:
    # A ping for every member of the group
    # The group start message.
    def startGroup(self, groupName): #TODO
        response = ""
        return response

    def getGroupMembers(self, groupName):
        groupMembers = self.groupList[groupName].viewMembers()
        response = groupMembers #TODO format this response to include a group member list that indicates the group leader
        return response

    #TODO create utility func to check if user is a group leader or admin

    
    def deleteGroup(self, groupName, deleter):
        # If deleter is not the leader of the group or is not an admin, return an error.
        removedGroup = self.isGroupNameInGroupList(groupName)
        if removedGroup is not None and (removedGroup.groupLeader == deleter or deleter.roles == adminRole ): #TODO this last part -- how to get admin role?
            self.groupList = self.groupList.remove(removedGroup)
            return "Successfully deleted group: " + groupName + "."
        else:
            return "Error: Could not find group or you do not have the proper permissions to delete the group; only admins and the group leader are able to delete a group. Check who is the group leader using `/group members [groupName]`, without brackets."

class ActivityGroup:
    # The group leader is assigned to the user that creates 
    # the group and automatically added to the members list.
    def __init__(self, groupName, groupLeader):
        self.groupName = groupName
        self.groupLeader = groupLeader
        self.members = [groupLeader]

    # Add a member to the group.
    def addMember(self, newMember):
        self.members = self.members.append(newMember)

    # Remove a member from the group.
    def removeMember(self, member):
        self.members = self.members.remove(member)

    # Return the list of group members.
    def viewMembers(self):
        return self.members