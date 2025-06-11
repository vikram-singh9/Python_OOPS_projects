class Mission:
    def __init__(self, name, agency, year, status):
        self.name = name
        self.agency = agency
        self.year = year
        self.status = status
    def show_info(self):
        print(f'Mission Name: {self.name}, Agency: {self.agency}, Year: {self.year}, Status: {self.status}')


class MissionTracker:
    def __init__(self):
        self.missions = []


    def add_mission(self, mission):
        self.missions.append(mission)
        print(f'mission {mission.name} has been added.')

    def view_mission(self):
        
        
        