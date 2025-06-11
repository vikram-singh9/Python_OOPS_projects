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

    def view_all_mission(self):
        print('=== All Missions ===')
        if not self.missions:
            print('No missions available.')
        else:
            for mission in self.missions:
                mission.show_info()

    def filter_by_status(self, status):
                
        print(f"\n🔍 Missions with status '{status}':")
        found = False

        for mission in self.missions:
            if mission.status.lower() == status.lower():
                mission.show_info()
                found = True

        if not found:
            print(f'No missions found with status: {status}')


mission1 = Mission('Mars Rover', 'NASA', 2020, 'Completed')
mission2 = Mission('Lunar Gateway', 'ESA', 2021, 'In Progress')
mission3 = Mission('James Webb Telescope', 'NASA', 2022, 'Completed')


mission_tracker = MissionTracker()
mission_tracker.add_mission(mission1)
mission_tracker.add_mission(mission2)
mission_tracker.add_mission(mission3)


mission_tracker.filter_by_status('Completed')

mission_tracker.view_all_mission()
        


        
        