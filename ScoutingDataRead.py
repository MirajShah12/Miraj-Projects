# set up the excel
import pandas as pd
import tbapy
import customtkinter
import scipy.stats as st 
import math

tba = tbapy.TBA('s7V5ltnoGZHvMdX89SRUVH32V7RxvP5zfKxQHMD5grd7bzz0qiScu0weFXDwYaKB')


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("1250x400")
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
pick_list_button.place(x=1100, y= 20)


pages = [frame,page1, page2]

#Statbotics knows
events = '2024dal'
#CSV File
df = pd.read_csv("scoutingData.csv")


#Creating the list of teams for buttons
theteams = tba.event_teams(events, keys=True)
team_numbers = [int(team_name[3:]) for team_name in theteams]
cteam_numbers = sorted(team_numbers)

#Do Math part
def averagPoints(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Points'].sum()
    return (pts/len(teaminstances))
def averagSpeakerTele(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Speaker tele'].sum()
    return (pts/len(teaminstances))
def averagAmpTele(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Amp tele'].sum()
    return (pts/len(teaminstances))
def averagAmpAuton(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Amp Auton'].sum()
    return (pts/len(teaminstances))
def averagSpeakerAuton(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['Speaker Auton'].sum()
    return (pts/len(teaminstances))
def doesZone(teamed): #Function does Works
    teaminstances = df[(df['team'] == teamed)]
    pts = teaminstances['left zone'].sum()
    if pts > .8:
        return True
    else:
        return False
def getMax(teamed):
    teaminstances = df[(df['team'] == teamed)]
    max = teaminstances['Speaker tele'].max()
    return max
def getMin(teamed):
    teaminstances = df[(df['team'] == teamed)]
    min = teaminstances['Speaker tele'].min()
    return min
def getMaxAmp(teamed):
    teaminstances = df[(df['team'] == teamed)]
    max = teaminstances['Amp tele'].max()
    return max
def getMinAmp(teamed):
    teaminstances = df[(df['team'] == teamed)]
    min = teaminstances['Amp tele'].min()
    return min
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


def pickList1(teamed):
    global pick_score
    global pick_scores
    pick_scores = {}

    if (averagSpeakerTele(teamed) > averagAmpTele(teamed)):
        speakerAutoWeight = 6
        ampAutoWeight = 1
        speakerTeleWeight = averagSpeakerTele(teamed) - averagAmpTele(teamed)
        ampTeleWeight = averagAmpTele(teamed) * 2
    if (averagSpeakerTele(teamed) <= averagAmpTele(teamed)):
        speakerAutoWeight = 6
        ampAutoWeight = 1
        speakerTeleWeight = averagSpeakerTele(teamed) * 2
        ampTeleWeight = averagAmpTele(teamed) -averagSpeakerTele(teamed) + 1
    for team in team_numbers:
        # Calculate the pick score using the weighted sum of criteria
        pick_score = (averagSpeakerAuton(team) * speakerAutoWeight +
                      averagAmpAuton(team) * ampAutoWeight +
                      averagSpeakerTele(team) * speakerTeleWeight +
                      averagAmpTele(team) * ampTeleWeight)
        pick_scores[team] = pick_score

    sorted_teams = sorted(team_numbers, key=lambda team: pick_scores[team], reverse=True)
    
    # Return a list of tuples containing team number and pick score, sorted by pick score
    sorted_teams_with_pick_scores = [(team, pick_scores[team]) for team in sorted_teams]
    return sorted_teams_with_pick_scores
def pickList2(teamed, team2):
    global pick_score
    global pick_scores
    pick_scores = {}

    if (averagSpeakerTele(teamed) + averagSpeakerTele(team2) > averagAmpTele(teamed) + averagAmpTele(team2)):
        speakerAutoWeight = 3
        ampAutoWeight = 1
        speakerTeleWeight = (averagSpeakerTele(teamed) + averagSpeakerTele(team2)) - averagAmpTele(teamed) + averagAmpTele(team2)
        ampTeleWeight = (averagAmpTele(teamed) + averagAmpTele(team2)) * 2
    if (averagSpeakerTele(teamed) + averagSpeakerTele(team2) <= averagAmpTele(teamed) + averagAmpTele(team2)):
        speakerAutoWeight = 3
        ampAutoWeight = 1
        speakerTeleWeight = (averagSpeakerTele(teamed) + averagSpeakerTele(team2)) * 2
        ampTeleWeight = (averagAmpTele(teamed) + averagAmpTele(team2) - averagSpeakerTele(teamed) + averagSpeakerTele(team2))  + 1 
    for team in team_numbers:
        # Calculate the pick score using the weighted sum of criteria
        pick_score = (averagSpeakerAuton(team) * speakerAutoWeight +
                      averagAmpAuton(team) * ampAutoWeight +
                      averagSpeakerTele(team) * speakerTeleWeight +
                      averagAmpTele(team) * ampTeleWeight)
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
        top_teams = pickList2(4522, 1690)
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



lb1=None
lb2=None
lb3=None
lb4=None
lb5=None
lb6=None
lb7=None
lb8=None
lb9=None
lb10=None
lb11=None
lb12=None

def giveMath(teamed):
    global lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9, lb10,lb11, lb12
    # Destroy the labels if they exist
    if lb1 is not None:
        lb1.destroy()
    if lb2 is not None:
        lb2.destroy()
    if lb3 is not None:
        lb3.destroy()
    if lb4 is not None:
        lb4.destroy()
    if lb5 is not None:
        lb5.destroy()
    if lb6 is not None:
        lb6.destroy() 
    if lb7 is not None:
        lb7.destroy()  
    if lb8 is not None:
        lb8.destroy()  
    if lb9 is not None:
        lb9.destroy()
    if lb10 is not None:
        lb10.destroy()
    if lb11 is not None:
        lb11.destroy()  
    if lb12 is not None:
        lb12.destroy()       
    switch_page(page1)

    # Create and pack the label on page 1
    lb1 = customtkinter.CTkLabel(page1, text=f"Average Points: {round(averagPoints(teamed), 2)}",font=('Bold', 20))
    lb1.pack()
    lb1.place(x=50,y=25)

    lb2 = customtkinter.CTkLabel(page1, text=f"Average Amp Auton: {round(averagAmpAuton(teamed), 2)}",font=('Bold', 20))
    lb2.pack()
    lb2.place(x=50,y=50)
    
    lb3 = customtkinter.CTkLabel(page1, text=f"Average Speaker Auton: {round(averagSpeakerAuton(teamed), 2)}",font=('Bold', 20))
    lb3.pack()
    lb3.place(x=50,y=75)
    
    if doesZone(teamed):
        lb4 = customtkinter.CTkLabel(page1, text="This team does leave zone",font=('Bold', 20))
        lb4.pack()
        lb4.place(x=50,y=100)
    else:
        lb4 = customtkinter.CTkLabel(page1, text="They don't leave zone normally",font=('Bold', 20))
        lb4.pack()
        lb4.place(x=50,y=100)
        
    lb5 = customtkinter.CTkLabel(page1, text=f"Average Amp Tele: {round(averagAmpTele(teamed), 2)}",font=('Bold', 20))
    lb5.pack()
    lb5.place(x=50,y=125)
    
    lb6 = customtkinter.CTkLabel(page1, text=f"Average Speaker Tele: {round(averagSpeakerTele(teamed), 2)}", font=('Bold', 20))
    lb6.pack()
    lb6.place(x=50,y=150)

    lb7 = customtkinter.CTkLabel(page1, text=f"Max Speaker Score: {round(getMax(teamed), 2)}", font=('Bold', 20))
    lb7.pack()
    lb7.place(x=50,y=175)

    lb8 = customtkinter.CTkLabel(page1, text=f"Min Speaker Score: {round(getMin(teamed), 2)}", font=('Bold', 20))
    lb8.pack()
    lb8.place(x=50,y=200)
    
    lb9 = customtkinter.CTkLabel(page1, text=f"Max Amp Score: {round(getMaxAmp(teamed), 2)}", font=('Bold', 20))
    lb9.pack()
    lb9.place(x=50,y=225)

    lb10 = customtkinter.CTkLabel(page1, text=f"Max Amp Score: {round(getMinAmp(teamed), 2)}", font=('Bold', 20))
    lb10.pack()
    lb10.place(x=50,y=250)

    lb11 =customtkinter.CTkLabel(page1, text=f"StandardDEviations: {(stdvs(teamed))}", font=('Bold', 20))
    lb11.pack()
    lb11.place(x=50,y=275)

    lb12 =customtkinter.CTkLabel(page1, text=f"We are 95% confident that the values are in between: {(confidenceIntervals(teamed))}", font=('Bold', 20))
    lb12.pack()
    lb12.place(x=50,y=300)

#Pick List Label


# Create and configure 49 custom buttons
buttons =[]

def buttonMaker(n):
    counter=0
    for j in range(int((n/7))):
        for i in range(7):
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
buttonMaker(75)

root.mainloop()
