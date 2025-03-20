# set up the excel
import pandas as pd
import tbapy
import customtkinter


tba = tbapy.TBA('s7V5ltnoGZHvMdX89SRUVH32V7RxvP5zfKxQHMD5grd7bzz0qiScu0weFXDwYaKB')


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("1500x600")
root.title("2869 Data Analysis App")


back_button = None
def create_back_button(page):
    global back_button
    back_button = customtkinter.CTkButton(page, text="Go Back", command=lambda: switch_page(frame))
    back_button.pack()

def switch_page(page):
    global back_button
    # Hide all frames
    for frame in pages:
        frame.pack_forget()
    # Pack the selected page
    page.pack(fill="both", expand=True)
    # Repack the back button only on page1
    if page == page1 or page == page2:
        back_button.pack()

frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

page1 = customtkinter.CTkFrame(root)
page1.pack(fill="both", expand=True)

page2 = customtkinter.CTkFrame(root)
page2.pack(fill="both", expand=True)

back_button = customtkinter.CTkButton(page1, text= "Go Back", command = lambda:switch_page(frame))
back_button.pack()

back_button2 = customtkinter.CTkButton(page2, text= "Go Back", command = lambda:switch_page(frame))
back_button2.pack()

pick_list_button = customtkinter.CTkButton(frame, text= "Pick List", command = lambda:switch_page(page2))
pick_list_button.pack()
pick_list_button.place(x=1300, y= 20)


pages = [frame,page1, page2]

#Statbotics knows
events = '2025nyli2'
#CSV File
df = pd.read_csv("scoutingData.csv")


#Creating the list of teams for buttons
#theteams = tba.event_teams(events, keys=True)
#team_numbers = [int(team_name[3:]) for team_name in theteams]
#cteam_numbers = sorted(team_numbers)
team_numbers = [
    28, 263, 271, 287, 329, 353, 358, 496, 514, 527,
    533, 545, 564, 569, 601, 806, 810, 870, 871, 884,
    1468, 1546, 1554, 1601, 1803, 2027, 2161, 2347, 2487,
    2869, 2872, 2875, 3137, 3624, 3950, 4458, 4567, 5016,
    5736, 6024, 6423, 6636, 6806, 8267, 9016, 9646, 9692,
    10621
]
cteam_numbers = sorted(team_numbers)
#Do Math part

def avgAL1(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['A_L1'].sum()
    return (pts/len(teaminstances))
def avgAL2(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['A_L2'].sum()
    return (pts/len(teaminstances))
def avgAL3(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['A_L3'].sum()
    return (pts/len(teaminstances))
def avgAL4(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['A_L4'].sum()
    return (pts/len(teaminstances))
def avgAPScore(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Pscore_A'].sum()
    return (pts/len(teaminstances))
def avgPNet(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Nscore'].sum()
    return (pts/len(teaminstances))

def avgTL1(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['T_L1'].sum()
    return (pts/len(teaminstances))
def avgTL2(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['T_L2'].sum()
    return (pts/len(teaminstances))
def avgTL3(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['T_L3'].sum()
    return (pts/len(teaminstances))
def avgTL4(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['T_L4'].sum()
    return (pts/len(teaminstances))
def avgTPScore(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Pscore_t'].sum()
    return (pts/len(teaminstances))
def avgTNet(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Nscore_t'].sum()
    return (pts/len(teaminstances))
def doesZone(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Starting'].sum()
    if pts > .8:
        return True
    else:
        return False

def avgClimbTime(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Climb_time'].sum()
    return (pts/len(teaminstances))

def pickUpS(teamed):
    teaminstances = df[(df['team'] == teamed)]
    s_count = (teaminstances == 's').sum().sum()
    return s_count  
def pickUpF(teamed):
    teaminstances = df[(df['team'] == teamed)]
    s_count = (teaminstances == 'f').sum().sum()
    return s_count  
def pickUpb(teamed):
    teaminstances = df[(df['team'] == teamed)]
    s_count = (teaminstances == 'b').sum().sum()
    return s_count  

def climbD(teamed):
    teaminstances = df[(df['team'] == teamed)]
    s_count = (teaminstances == 'bd').sum().sum()
    return s_count  
def climbS(teamed):
    teaminstances = df[(df['team'] == teamed)]
    s_count = (teaminstances == 'bs').sum().sum()
    return s_count  
def climbF(teamed):
    teaminstances = df[(df['team'] == teamed)]
    s_count = (teaminstances == 'ba').sum().sum()
    return s_count  
def climbP(teamed):
    teaminstances = df[(df['team'] == teamed)]
    s_count = (teaminstances == 'bp').sum().sum()
    return s_count  

def diedCount(teamed):
    teaminstances = df[(df['team'] == teamed)]
    count = teaminstances['Died'].sum()
    return count

def maxAL1(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['A_L1'].max()

def maxAL2(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['A_L2'].max()

def maxAL3(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['A_L3'].max()

def maxAL4(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['A_L4'].max()

def maxAPScore(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['Pscore_A'].max()

def maxPNet(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['Nscore'].max()

def maxTL1(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['T_L1'].max()

def maxTL2(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['T_L2'].max()

def maxTL3(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['T_L3'].max()

def maxTL4(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['T_L4'].max()

def maxTPScore(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['Pscore_t'].max()

def maxTNet(teamed):
    teaminstances = df[(df['team'] == teamed)]
    return teaminstances['Nscore_t'].max()

'''
def stdvs(teamed):
    global teaminstances, points, speakerAuto, ampAuto, speakerTele, ampTele
    teaminstances = df[(df['team'] == teamed)]
    points= st.tstd(teaminstances['Points'])
    speakerAuto= st.tstd(teaminstances['Speaker Auton'])
    ampAuto= st.tstd(teaminstances['Amp Auton'])
    speakerTele= st.tstd(teaminstances['Speaker tele'])
    ampTele = st.tstd(teaminstances['Amp tele'])
    return points, speakerAuto, ampAuto, speakerTele, ampTele
def confidenceIntervals(teamed):
    num = math.sqrt(len(df[(df['team'] == teamed)])-1)
    minVal= round((averagPoints(teamed) - (2.262) * (stdvs(teamed)[0]/num)), 2)
    maxVal= round((averagPoints(teamed) + (2.262) * (stdvs(teamed)[0]/num)),2)
    return minVal, maxVal
'''

def pickList1(teamed):
    global pick_score
    global pick_scores
    pick_scores = {}

    # Define weights based on your requirements
    L4AutoWeight = 10  # Highest weight for Auto L4
    L3AutoWeight = 8   # High weight for Auto L3
    L4TeleWeight = 6   # Weight for Teleop L4
    L3TeleWeight = 5   # Weight for Teleop L3
    L2AutoWeight = 4   # Weight for Auto L2
    L1AutoWeight = 3   # Weight for Auto L1
    L2TeleWeight = 2   # Weight for Teleop L2
    L1TeleWeight = 1   # Weight for Teleop L1
    DeepClimbWeight = 7  # Weight for deep climb
    ClimbTimeWeight = 0.5  # Multiplier for climb time (faster climbs are worth more)
    NetWeight = 12  # Highest weight for net score
    AlgaeWeight = 5  # Weight for algae

    for team in team_numbers:
        # Calculate the pick score using the weighted sum of criteria
        pick_score = (
            avgAL4(team) * L4AutoWeight +
            avgAL3(team) * L3AutoWeight +
            avgTL4(team) * L4TeleWeight +
            avgTL3(team) * L3TeleWeight +
            avgAL2(team) * L2AutoWeight +
            avgAL1(team) * L1AutoWeight +
            avgTL2(team) * L2TeleWeight +
            avgTL1(team) * L1TeleWeight +
            climbD(team) * DeepClimbWeight * (1 / (avgClimbTime(team) + 0.1) * ClimbTimeWeight +  # Faster climbs are worth more
            avgPNet(team) * NetWeight +  # Net score has the highest weight
            avgTNet(team) * AlgaeWeight  # Algae score has some weight
        ))
        pick_scores[team] = pick_score

    sorted_teams = sorted(team_numbers, key=lambda team: pick_scores[team], reverse=True)
    
    # Return a list of tuples containing team number and pick score, sorted by pick score
    sorted_teams_with_pick_scores = [(team, pick_scores[team]) for team in sorted_teams]
    return sorted_teams_with_pick_scores

def pickList2(teamed, team2):
    global pick_score
    global pick_scores
    pick_scores = {}

    # Define weights based on your requirements
    L4AutoWeight = 10  # Highest weight for Auto L4
    L3AutoWeight = 8   # High weight for Auto L3
    L4TeleWeight = 6   # Weight for Teleop L4
    L3TeleWeight = 5   # Weight for Teleop L3
    L2AutoWeight = 4   # Weight for Auto L2
    L1AutoWeight = 3   # Weight for Auto L1
    L2TeleWeight = 2   # Weight for Teleop L2
    L1TeleWeight = 1   # Weight for Teleop L1
    DeepClimbWeight = 7  # Weight for deep climb
    ClimbTimeWeight = 0.5  # Multiplier for climb time (faster climbs are worth more)
    NetWeight = 12  # Highest weight for net score
    AlgaeWeight = 5  # Weight for algae

    for team in team_numbers:
        # Calculate the pick score using the weighted sum of criteria
        pick_score = (
            avgAL4(team) * L4AutoWeight +
            avgAL3(team) * L3AutoWeight +
            avgTL4(team) * L4TeleWeight +
            avgTL3(team) * L3TeleWeight +
            avgAL2(team) * L2AutoWeight +
            avgAL1(team) * L1AutoWeight +
            avgTL2(team) * L2TeleWeight +
            avgTL1(team) * L1TeleWeight +
            climbD(team) * DeepClimbWeight * (1 / (avgClimbTime(team) + 0.1)) * ClimbTimeWeight +  # Faster climbs are worth more
            avgPNet(team) * NetWeight +  # Net score has the highest weight
            avgTNet(team) * AlgaeWeight  # Algae score has some weight
        )
        pick_scores[team] = pick_score

    sorted_teams = sorted(team_numbers, key=lambda team: pick_scores[team], reverse=True)
    
    # Return a list of tuples containing team number and pick score, sorted by pick score
    sorted_teams_with_pick_scores = [(team, pick_scores[team]) for team in sorted_teams]
    return sorted_teams_with_pick_scores

def display_pick_list(kind):
    # Get the top teams with their pick scores
    if kind == 1:
        top_teams = pickList1(2869)
        # Create a string to display in the label
        label_text = "Top Teams with Highest First Pick Scores:\n\n"
        for i, (team, pick_score) in enumerate(top_teams, 1):
            label_text += f"{i}. Team {team}: Pick Score {pick_score}\n"
        
        # Create and configure the label
        lb13 = customtkinter.CTkLabel(page2, text=label_text, font=('Bold', 20))
        lb13.pack()
        lb13.place(x=50, y=100)
    elif kind == 2:
        top_teams = pickList2(2869, 1468)
        # Create a string to display in the label
        label_text = "Top Teams with Highest Second Pick Scores:\n\n"
        for i, (team, pick_score) in enumerate(top_teams, 1):
            label_text += f"{i}. Team {team}: Pick Score {pick_score}\n"
        
        # Create and configure the label
        lb13 = customtkinter.CTkLabel(page2, text=label_text, font=('Bold', 20))
        lb13.pack()
        lb13.place(x=450, y=100)        
display_pick_list(1)
display_pick_list(2)

# Initialize a list to store all labels
lbs = [None] * 50  # 26 labels (lb1 to lb26)

def giveMath(teamed):
    global lbs
    
    # Destroy the labels if they exist
    for i in range(len(lbs)):
        if lbs[i] is not None:
            lbs[i].destroy()
            lbs[i] = None  # Reset the label to None after destroying
    
    switch_page(page1)

    # Create and pack the label on page 1

    lb2 = customtkinter.CTkLabel(page1, text=f"Average L1 Auton: {round(avgAL1(teamed), 2)}",font=('Bold', 20))
    lb2.pack()
    lb2.place(x=50,y=50)
    
    lb3 = customtkinter.CTkLabel(page1, text=f"Average L2 Auton: {round(avgAL2(teamed), 2)}",font=('Bold', 20))
    lb3.pack()
    lb3.place(x=50,y=75)
    
    lb6 = customtkinter.CTkLabel(page1, text=f"Average L3 Auton: {round(avgAL3(teamed), 2)}", font=('Bold', 20))
    lb6.pack()
    lb6.place(x=50,y=100)

    lb7 = customtkinter.CTkLabel(page1, text=f"Average L4 Auton: {round(avgAL4(teamed), 2)}", font=('Bold', 20))
    lb7.pack()
    lb7.place(x=50,y=125)

    lb8 = customtkinter.CTkLabel(page1, text=f"Average Processor Auton: {round(avgAPScore(teamed), 2)}", font=('Bold', 20))
    lb8.pack()
    lb8.place(x=50,y=150)
    
    lb9 = customtkinter.CTkLabel(page1, text=f"Average Net Score Auton: {round(avgTNet(teamed), 2)}", font=('Bold', 20))
    lb9.pack()
    lb9.place(x=50,y=175)

    if doesZone(teamed):
        lb4 = customtkinter.CTkLabel(page1, text="This team does leave zone",font=('Bold', 20))
        lb4.pack()
        lb4.place(x=50,y=200)
    else:
        lb4 = customtkinter.CTkLabel(page1, text="They don't leave zone normally",font=('Bold', 20))
        lb4.pack()
        lb4.place(x=50,y=200)


    lb10 = customtkinter.CTkLabel(page1, text=f"Average L1 Teleop: {round(avgTL1(teamed), 2)}", font=('Bold', 20))
    lb10.pack()
    lb10.place(x=50,y=225)

    lb11 =customtkinter.CTkLabel(page1, text=f"Average L2 Teleop: {(avgTL2(teamed))}", font=('Bold', 20))
    lb11.pack()
    lb11.place(x=50,y=250)

    lb12 =customtkinter.CTkLabel(page1, text=f"Average L3 Teleop: {(avgTL3(teamed))}", font=('Bold', 20))
    lb12.pack()
    lb12.place(x=50,y=275)

    lb1 =customtkinter.CTkLabel(page1, text=f"Average L4 Teleop: {(avgTL4(teamed))}", font=('Bold', 20))
    lb1.pack()
    lb1.place(x=50,y=300)

    lb5 =customtkinter.CTkLabel(page1, text=f"Processor Score Teleop: {(avgTPScore(teamed))}", font=('Bold', 20))
    lb5.pack()
    lb5.place(x=50,y=325)

    lb13 =customtkinter.CTkLabel(page1, text=f"Average Net Score: {(avgTNet(teamed))}", font=('Bold', 20))
    lb13.pack()
    lb13.place(x=50,y=350)

    lb23 = customtkinter.CTkLabel(page1, text=f"Max Auto L1: {maxAL1(teamed)}", font=('Bold', 20))
    lb23.pack()
    lb23.place(x=500, y=50)

    lb24 = customtkinter.CTkLabel(page1, text=f"Max Auto L2: {maxAL2(teamed)}", font=('Bold', 20))
    lb24.pack()
    lb24.place(x=500, y=75)

    lb25 = customtkinter.CTkLabel(page1, text=f"Max Auto L3: {maxAL3(teamed)}", font=('Bold', 20))
    lb25.pack()
    lb25.place(x=500, y=100)

    lb26 = customtkinter.CTkLabel(page1, text=f"Max Auto L4: {maxAL4(teamed)}", font=('Bold', 20))
    lb26.pack()
    lb26.place(x=500, y=125)

    lb27 = customtkinter.CTkLabel(page1, text=f"Max Auto PScore: {maxAPScore(teamed)}", font=('Bold', 20))
    lb27.pack()
    lb27.place(x=500, y=150)

    lb28 = customtkinter.CTkLabel(page1, text=f"Max Auto Net: {maxPNet(teamed)}", font=('Bold', 20))
    lb28.pack()
    lb28.place(x=500, y=175)

    lb29 = customtkinter.CTkLabel(page1, text=f"Max Teleop L1: {maxTL1(teamed)}", font=('Bold', 20))
    lb29.pack()
    lb29.place(x=500, y=200)

    lb30 = customtkinter.CTkLabel(page1, text=f"Max Teleop L2: {maxTL2(teamed)}", font=('Bold', 20))
    lb30.pack()
    lb30.place(x=500, y=225)

    lb31 = customtkinter.CTkLabel(page1, text=f"Max Teleop L3: {maxTL3(teamed)}", font=('Bold', 20))
    lb31.pack()
    lb31.place(x=500, y=250)

    lb32 = customtkinter.CTkLabel(page1, text=f"Max Teleop L4: {maxTL4(teamed)}", font=('Bold', 20))
    lb32.pack()
    lb32.place(x=500, y=275)

    lb33 = customtkinter.CTkLabel(page1, text=f"Max Teleop PScore: {maxTPScore(teamed)}", font=('Bold', 20))
    lb33.pack()
    lb33.place(x=500, y=300)

    lb34 = customtkinter.CTkLabel(page1, text=f"Max Teleop Net: {maxTNet(teamed)}", font=('Bold', 20))
    lb34.pack()
    lb34.place(x=500, y=325)

    lb14 =customtkinter.CTkLabel(page1, text=f"Station Pickup Count: {(pickUpS(teamed))}", font=('Bold', 20))
    lb14.pack()
    lb14.place(x=1000,y=50)

    lb15 =customtkinter.CTkLabel(page1, text=f"Floor Pickup Count: {(pickUpF(teamed))}", font=('Bold', 20))
    lb15.pack()
    lb15.place(x=1000,y=75)

    lb16 =customtkinter.CTkLabel(page1, text=f"Both Pickup Count: {(pickUpb(teamed))}", font=('Bold', 20))
    lb16.pack()
    lb16.place(x=1000,y=100)

    lb17 =customtkinter.CTkLabel(page1, text=f"Deep Climb Count: {(climbD(teamed))}", font=('Bold', 20))
    lb17.pack()
    lb17.place(x=1000,y=125)

    lb18 =customtkinter.CTkLabel(page1, text=f"Shallow Climb Count: {(climbS(teamed))}", font=('Bold', 20))
    lb18.pack()
    lb18.place(x=1000,y=150)

    lb19 =customtkinter.CTkLabel(page1, text=f"Failed Climb And Park Count: {(climbF(teamed))}", font=('Bold', 20))
    lb19.pack()
    lb19.place(x=1000,y=175) 

    lb20 =customtkinter.CTkLabel(page1, text=f"Park Count: {(climbP(teamed))}", font=('Bold', 20))
    lb20.pack()
    lb20.place(x=1000,y=200) 

    lb21 =customtkinter.CTkLabel(page1, text=f"Average Climb Time: {(avgClimbTime(teamed))}", font=('Bold', 20))
    lb21.pack()
    lb21.place(x=1000,y=225) 

    lb22 =customtkinter.CTkLabel(page1, text=f"Times Died: {(diedCount(teamed))}", font=('Bold', 20))
    lb22.pack()
    lb22.place(x=1000,y=250) 

#Pick List Label


# Create and configure 49 custom buttons
buttons =[]

def buttonMaker(n):
    counter=0
    for j in range(int((n/7))):
        for i in range(8):
            # Calculate the button's position based on i and j
            x_position = 20 + i * 150  # Adjust as needed
            y_position = 20 + j * 50  # Adjust as needed
            # Create a custom button
            button = customtkinter.CTkButton(
                master=frame,
                text=cteam_numbers[counter],  # Adjust the button label
                command=lambda team=cteam_numbers[counter]: giveMath(team) # Adjust the command function
            )
            # Pack or place the button based on your layout preference
            button.place(x=x_position,y=y_position) 

            # Store the button in the list
            buttons.append(button)

            if counter + 1 < 49:
                counter+=1
            else:
                break
buttonMaker(48)

root.mainloop()
