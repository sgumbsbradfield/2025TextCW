from ortools.sat.python import cp_model

class Pupil:
    def __init__(self, id, name, status, tutor_group, previous_roommates, preferences):
        self.id = id
        self.name = name
        self.status = status  # 'boarder' or 'day'
        self.tutor_group = tutor_group
        self.previous_roommates = previous_roommates  # list of pupil ids
        self.preferences = preferences  # list of pupil ids

class Room:
    def __init__(self, id, name, capacity, num_boarding_beds, num_day_desks):
        self.id = id
        self.name = name
        self.capacity = capacity  # total capacity
        self.num_boarding_beds = num_boarding_beds
        self.num_day_desks = num_day_desks

    def can_accommodate(self, pupil_status):
        if pupil_status == 'boarder':
            return self.num_boarding_beds > 0
        elif pupil_status == 'day':
            return self.num_day_desks > 0 or self.num_boarding_beds > 0
        else:
            return False

# Sample data for pupils and rooms
pupils = [
    Pupil(1, 'Acacia', 'day', 'K',[15,23], [18, 67, 45]),
    Pupil(2, 'Addie', 'day', 'K',[9,30,46], [22, 50, 24]),
    Pupil(3, 'Alexa', 'boarder', 'J',[40,59,64,65], [24, 27, 27]),
    Pupil(4, 'Amber', 'boarder', 'I',[12,54], [62, 5, 64]),
    Pupil(5, 'Arielle', 'boarder', 'M',[49], [27, 4, 12]),
    Pupil(6, 'Ava F', 'boarder', 'J',[14,39], [46, 41, 8]),
    Pupil(7, 'Ava G', 'boarder', 'I',[33,52,55], [10, 22, 9]),
    Pupil(8, 'Betsy', 'boarder', 'K',[37,41], [6, 46, 30]),
    Pupil(9, 'Betty', 'boarder', 'J',[2,30,46], [51, 31, 10]),
    Pupil(10, 'Cecily', 'boarder', 'M',[62], [9, 7, 51]),
    Pupil(11, 'Charlie', 'boarder', 'M',[11,56], [36, 21, 28]),
    Pupil(12, 'Charlotte', 'boarder', 'J',[4,54], [16, 64, 5]),
    Pupil(13, 'Cleo', 'boarder', 'K',[25], [50, 21, 5]),
    Pupil(14, 'Coco', 'boarder', 'I',[6,39], [62, 46, 9]),
    Pupil(15, 'Connie', 'day', 'J',[1,23], [41, 68, 51]),
    Pupil(16, 'Dorothy', 'boarder', 'I',[22], [5, 12, 10]),
    Pupil(17, 'Eliza P', 'boarder', 'I',[43,63], [19, 25, 26]),
    Pupil(18, 'Eliza W', 'boarder', 'I',[35], [19, 53, 43]),
    Pupil(19, 'Emily D', 'boarder', 'K',[27], [18, 16, 54]),
    Pupil(20, 'Emily RW', 'boarder', 'K',[47], [68, 24, 10]),
    Pupil(21, 'Emily W', 'boarder', 'K',[24,34], [36, 11, 38]),
    Pupil(22, 'Flora', 'boarder', 'M',[16], [24, 68, 62]),
    Pupil(23, 'Florence L', 'boarder', 'I',[1,15], [4, 58, 31]),
    Pupil(24, 'Florence MN', 'boarder', 'I',[21,34], [29, 22, 62]),
    Pupil(25, 'Georgia', 'boarder', 'J',[13], [31, 58, 37]),
    Pupil(26, 'Georgie', 'boarder', 'J',[36,38], [31, 41, 46]),
    Pupil(27, 'Grace', 'boarder', 'M',[19], [24, 3, 51]),
    Pupil(28, 'Harriet', 'boarder', 'K',[50], [4, 18, None]),
    Pupil(29, 'Hattie', 'day', 'J',[31,44], [22, 24, 2]),
    Pupil(30, 'Holly', 'boarder', 'I',[2,9,46], [31, 6, 26]),
    Pupil(31, 'India', 'boarder', 'K', [29,44],[9, 26, 41]),
    Pupil(32, 'Iona F', 'boarder', 'I',[58], [53, 67, 25]),
    Pupil(33, 'Iona M', 'day', 'M', [7,52,55],[42, 1, 35]),
    Pupil(34, 'Irem', 'day', 'M', [21,24],[50, 15, 40]),
    Pupil(35, 'Isabella', 'boarder', 'K',[18], [52, 1, 57]),
    Pupil(36, 'Isla', 'day', 'I',[26,38], [11, 12, 21]),
    Pupil(37, 'Izzie W', 'boarder', 'J',[8,41], [46, 68, 24]),
    Pupil(38, 'Izzy S', 'boarder', 'M',[26,36], [21, 53, 28]),
    Pupil(39, 'Katie', 'day', 'K',[6,14], [52, 32, 1]),
    Pupil(40, 'Kitty', 'boarder', 'K',[3,59,64,65], [24, 50, 34]),
    Pupil(41, 'Lily', 'boarder', 'I',[8,37], [46, 31, 26]),
    Pupil(42, 'Louisa', 'day', 'I',[45,60,66], [67, 33, 18]),
    Pupil(43, 'Lucy', 'boarder', 'J',[17,63], [53, 18, 67]),
    Pupil(44, 'Maria', 'boarder', 'M', [29,31],[49, 12, 10]),
    Pupil(45, 'Matilda', 'boarder', 'M',[42,60,66], [52, 1, 21]),
    Pupil(46, 'Megan', 'boarder', 'M',[2,9,30], [6, 8, 41]),
    Pupil(47, 'Millie', 'boarder', 'I',[20], [37, 55, 31]),
    Pupil(48, 'Mirabelle', 'day', 'I', [53,67],[31, None, None]),
    Pupil(49, 'Olivia', 'boarder', 'I', [5],[54, 64, 59]),
    Pupil(50, 'Ophelia', 'boarder', 'J',[28], [13, 20, 2]),
    Pupil(51, 'Orla', 'boarder', 'I',[57], [62, 9, 10]),
    Pupil(52, 'Penelope', 'day', 'K', [7,33,55],[45, 57, 65]),
    Pupil(53, 'Phoebe', 'boarder', 'K', [48,67],[43, 18, 17]),
    Pupil(54, 'Poppy HH', 'boarder', 'M', [4,12],[16, 59, 5]),
    Pupil(55, 'Poppy M', 'boarder', 'J',[7,33,52], [47, 46, 10]),
    Pupil(56, 'Poppy O', 'boarder', 'I',[11], [6, 29, 8]),
    Pupil(57, 'Riya', 'boarder', 'M',[51], [1, 52, 35]),
    Pupil(58, 'Rose', 'boarder', 'K',[32], [62, 23, 4]),
    Pupil(59, 'Savannah', 'boarder', 'I',[3,40,64,65], [54, 55, 62]),
    Pupil(60, 'Scarlet M', 'boarder', 'I',[42,45,66], [34, 66, 50]),
    Pupil(61, 'Scarlett R', 'boarder', 'K', [68],[46, 23, 59]),
    Pupil(62, 'Sophie', 'boarder', 'J',[10], [51, 22, 31]),
    Pupil(63, 'Stella', 'boarder', 'M',[17,43], [52, 44, 28]),
    Pupil(64, 'Tabitha', 'boarder', 'M',[3,40,59,65], [4, 17, 18]),
    Pupil(65, 'Tilda', 'boarder', 'J', [3,40,59,64],[67, 17, 53]),
    Pupil(66, 'Viva', 'boarder', 'J',[42,45,60], [12, 36, 4]),
    Pupil(67, 'Willa', 'boarder', 'M', [48,53],[17, 43, 18]),
    Pupil(68, 'Xanthe', 'boarder', 'I',[61], [22, 31, 10]),
]

rooms = [
    Room(128, 'Room 128',5, 5, 0),
    Room(127, 'Room 127',3,  3, 0),
    Room(126, 'Room 126',3, 2, 1),
    Room(125, 'Room 125',3, 2, 1),
    Room(124, 'Room 124',3, 3, 0),
    Room(123, 'Room 123',2, 2, 0),
    Room(122, 'Room 122',3, 3, 0),
    Room(121, 'Room 121',2, 2, 0),
    Room(120, 'Room 120',3, 2, 1),
    Room(119, 'Room 119',3, 2, 1),
    Room(118, 'Room 118',3, 3, 0),
    Room(117, 'Room 118a',2, 2, 0),
    Room(228, 'Room 228',4, 4, 0),
    Room(227, 'Room 227',4, 2, 2),
    Room(226, 'Room 226',3, 2, 1),
    Room(225, 'Room 225',2, 2, 0),
    Room(224, 'Room 224',3, 2, 1),
    Room(223, 'Room 223',2, 2, 0),
    Room(222, 'Room 222',3, 2, 1),
    Room(221, 'Room 221',2, 2, 0),
    Room(220, 'Room 220',2, 2, 0),
    Room(219, 'Room 219',2, 2, 0),
    Room(218, 'Room 218',2, 2, 0),
    Room(217, 'Room 217',2, 2, 0),
    Room(216, 'Room 216',2, 2, 0),
    Room(215, 'Room 215',4, 4, 0),
]

def assign_pupils_to_rooms(pupils, rooms):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    pupil_vars = {}
    for pupil in pupils:
        # Determine possible rooms for the pupil based on their status
        possible_rooms = []
        for room in rooms:
            if room.can_accommodate(pupil.status):
                possible_rooms.append(room.id)
        if not possible_rooms:
            print(f"No rooms available for pupil {pupil.name} ({pupil.status})")
            return None
        pupil_vars[pupil.id] = model.NewIntVarFromDomain(cp_model.Domain.FromValues(possible_rooms), f'Room_{pupil.id}')

    # Constraints
    # Previous roommates constraint
    '''for pupil in pupils:
        for prev_roommate_id in pupil.previous_roommates:
            if prev_roommate_id in pupil_vars:
                model.Add(pupil_vars[pupil.id] != pupil_vars[prev_roommate_id])'''

    # Tutor group constraint
    tutor_groups = {}
    for pupil in pupils:
        tutor_groups.setdefault(pupil.tutor_group, []).append(pupil.id)
    for group in tutor_groups.values():
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                model.Add(pupil_vars[group[i]] != pupil_vars[group[j]])

    # Room capacity constraints and boarding/day space constraints
    for room in rooms:
        occupants = []
        boarding_pupils = []
        day_pupils = []
        for pupil in pupils:
            if room.can_accommodate(pupil.status):
                # Create Boolean variable indicating whether the pupil is assigned to this room
                assigned = model.NewBoolVar(f'Assigned_{pupil.id}_to_{room.id}')
                model.Add(pupil_vars[pupil.id] == room.id).OnlyEnforceIf(assigned)
                model.Add(pupil_vars[pupil.id] != room.id).OnlyEnforceIf(assigned.Not())
                occupants.append(assigned)
                if pupil.status == 'boarder':
                    boarding_pupils.append(assigned)
                else:
                    day_pupils.append(assigned)
        # Room capacity constraint
        model.Add(sum(occupants) <= room.capacity)
        # Boarding beds constraint
        model.Add(sum(boarding_pupils) <= room.num_boarding_beds)
        # Day desks constraint
        if room.num_day_desks > 0:
            model.Add(sum(day_pupils) <= room.num_day_desks)
        else:
            # If no day desks, day pupils can use boarding beds
            pass  # Day pupils can use boarding beds

        # Compute number of boarders and day pupils in the room
        num_boarders = model.NewIntVar(0, room.capacity, f'num_boarders_in_room_{room.id}')
        num_day_pupils = model.NewIntVar(0, room.capacity, f'num_day_pupils_in_room_{room.id}')
        model.Add(num_boarders == sum(boarding_pupils))
        model.Add(num_day_pupils == sum(day_pupils))

        # Define Boolean variables
        day_pupils_in_room = model.NewBoolVar(f'day_pupils_in_room_{room.id}')
        model.Add(num_day_pupils >= 1).OnlyEnforceIf(day_pupils_in_room)
        model.Add(num_day_pupils == 0).OnlyEnforceIf(day_pupils_in_room.Not())

        # One or two boarders in room
        one_boarder_in_room = model.NewBoolVar(f'one_boarder_in_room_{room.id}')
        model.Add(num_boarders == 1).OnlyEnforceIf(one_boarder_in_room)
        model.Add(num_boarders != 1).OnlyEnforceIf(one_boarder_in_room.Not())

        two_boarders_in_room = model.NewBoolVar(f'two_boarders_in_room_{room.id}')
        model.Add(num_boarders == 2).OnlyEnforceIf(two_boarders_in_room)
        model.Add(num_boarders != 2).OnlyEnforceIf(two_boarders_in_room.Not())

        one_or_two_boarders_in_room = model.NewBoolVar(f'one_or_two_boarders_in_room_{room.id}')
        model.AddMaxEquality(one_or_two_boarders_in_room, [one_boarder_in_room, two_boarders_in_room])

        # Add constraint to prevent invalid combinations
        # If there are day pupils in the room, number of boarders cannot be 1 or 2
        model.Add(day_pupils_in_room + one_or_two_boarders_in_room <= 1)

    # Preference constraints
    preference_satisfaction = []
    for pupil in pupils:
        if pupil.preferences:
            # For each preference, create a variable indicating if the pupil is in the same room as the preferred pupil
            pref_vars = []
            for pref_id in pupil.preferences:
                if pref_id in pupil_vars:
                    same_room = model.NewBoolVar(f'Pref_{pupil.id}_{pref_id}')
                    model.Add(pupil_vars[pupil.id] == pupil_vars[pref_id]).OnlyEnforceIf(same_room)
                    model.Add(pupil_vars[pupil.id] != pupil_vars[pref_id]).OnlyEnforceIf(same_room.Not())
                    pref_vars.append(same_room)
            if pref_vars:
                # At least one preference satisfied
                pref_satisfied = model.NewBoolVar(f'PrefSat_{pupil.id}')
                model.AddMaxEquality(pref_satisfied, pref_vars)
                preference_satisfaction.append(pref_satisfied)
        else:
            # No preferences, consider as satisfied
            pass  # Do not add anything to preference_satisfaction

    # Objective: Maximize preference satisfaction
    model.Maximize(sum(preference_satisfaction))

    # Solve the model
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        assignments = {}
        for room in rooms:
            assignments[room.id] = []
        for pupil in pupils:
            room_id = solver.Value(pupil_vars[pupil.id])
            assignments[room_id].append(pupil)
        # Output the assignments
        for room in rooms:
            print(f"Room {room.name}:")
            for pupil in assignments[room.id]:
                print(f"  {pupil.name} ({pupil.status}, Tutor Group {pupil.tutor_group})")
            print()
        # Print the number of preferences satisfied
        total_prefs_satisfied = 0
        for pref_var in preference_satisfaction:
            total_prefs_satisfied += solver.Value(pref_var)
        print(f"Total preferences satisfied: {int(total_prefs_satisfied)} out of {len(preference_satisfaction)}")
    else:
        print("No feasible solution found.")

# Run the assignment function
assign_pupils_to_rooms(pupils, rooms)
