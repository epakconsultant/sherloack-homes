# Importing
import time;
import threading;
from functools import partial
import random;
import threading
import time;
import winsound, sys
#array 
SuspicousPeople = {

    "Tom":  [],
    "Robert":    [],
    "Morven":     [],
    "Thomos":    [],
    "John":      [],
    "chinchow":   [],
    "Moris":   [],
    "Danniel":   [],

                    };


InnocentPeople = [

    "Nim",
    "Mughal",
    "Rosset",
    "Moha",
    "Vicky",
    "Samuel",

                    ];
#pick the random one
def ChooseRandomInnocent():
    return random.choice(InnocentPeople);

ChosenMurderer = random.choice(list(SuspicousPeople.keys()));
# Rooms
# All the rooms in the game, with items.
Rooms = {};

Rooms["HomeRoom2"] = {

    "Pen":   "There are a few pens on the floor.",
    "Ruler": "There is a ruler shaped like a knife.",
    "Blood": "There is some blood on a book.",
    
                        };

Rooms["HomeRoom3"] = {

    "Gun":    "There is a gun on the table.",
    "Laptop": "There is a laptop, with a tad of blood.",

                        };

Rooms["HomeRoom4"] = {

    "Case": "There is a pencil case on the chair.",
    "Bottle": "There is a bottle which is neary full.",

                        };

Rooms["HomeRoom5"] = {

    "Glasses": "There are some broken glasses in the corner.",
    "Flashlight": "There seems to be a flash-light on the table.",
    "Photo": "There is a photo covered with something.",
    
                        };

RoomInteractionwithmurder = {};

# HomeRoom2
RoomInteractionwithmurder["HomeRoom2"] = {};

RoomInteractionwithmurder["HomeRoom2"]["Pen"] = {

    "Analyse":     "These pens are owned by " + ChosenMurderer + ".",
    "Take":        None,
    "Use":         "The ink is red... The ink is not ink, it is blood.",
    "Fingerprint": "The freshest fingerprints belong to " + ChosenMurderer + ".",
    
                                };
#iteraction
RoomInteractionwithmurder["HomeRoom2"]["Ruler"] = {

    "Analyse":     "This ruler belongs to " + ChooseRandomInnocent() + ". It has been carved into a knife-like shape.",
    "Take":        None,
    "Use":         "You have made yourself get a small cut; with more force, this could be deadly.",
    "Fingerprint": "The freshest fingerprints belong to " + ChosenMurderer + ".",

                                    };

RoomInteractionwithmurder["HomeRoom2"]["Blood"] = {

    "Analyse": "This blood is fresh - around 5-10 minutes old.",
    "Taste":   "It is very warm and very sweet. Interesting...",

                                    };

# ------------------------------------------------------------------------------------------------------- #

# HomeRoom3
RoomInteractionwithmurder["HomeRoom3"] = {};
        
RoomInteractionwithmurder["HomeRoom3"]["Gun"] = {
    
    "Analyse":     "This gun looks illegal and unlicensed.",
    "Take":        None,
    "Use":         None,
    "Fingerprint": "The fingerprints belong to " + ChosenMurderer + ".",

                                };
    
RoomInteractionwithmurder["HomeRoom3"]["Laptop"] = {

    "Analyse": "This laptop belongs to " + ChooseRandomInnocent() + ". It has been running for the past hour.",
    "Use":     None,

                                    };


# HomeRoom4
RoomInteractionwithmurder["HomeRoom4"] = {};

RoomInteractionwithmurder["HomeRoom4"]["Case"] = {

    "Analyse": "This pencil case belongs to " + ChooseRandomInnocent() + ". Inside it is a pocket knife, with blood.",
    "Take":    None,

                                    };

RoomInteractionwithmurder["HomeRoom4"]["Bottle"] = {

    "Analyse": "This bottle belongs to " + ChosenMurderer + ". Not too much of its contents has been drank.",
    "Drink": "That was refreshing...",

                                    };


# HomeRoom5
RoomInteractionwithmurder["HomeRoom5"] = {};
RoomInteractionwithmurder["HomeRoom5"]["Glasses"] = {

    "Analyse": "These glasses belong to " + ChooseRandomInnocent() + ". They have been cracked by something.",
    "Take":    None,
                                    };
RoomInteractionwithmurder["HomeRoom5"]["Flashlight"] = {

    "Analyse": "This flashlight looks like it belongs to a surgeon.",
    "Use": "It doesn't work properly. The light keeps flickering...",
    "Fingerprint": "The fingerprints belong to " + ChooseRandomInnocent() + ".",

                                    };
RoomInteractionwithmurder["HomeRoom5"]["Photo"] = {

    "Analyse": "This is a photo of " + ChooseRandomInnocent() + ". Their face has been covered by blood.",
    "Take": None,

                                    };
#use for clear lines
#--------------------------------------------------------------------------------------------------------->
def Clear():
	print(" ");
#loop
def LoopList(List, Dictionary):
    if not Dictionary:
        for Item in List:
            print(Item);
    else:
        for Item, Item2 in List.items():
            print(Item + ": " + Item2);
                           
#helping
def DisplayHelp():
    
    HelpMessages = {

        "Innocent": "Shows a list of all innocent people.->",
        "Suspicous": "Shows a list of currently suspicous people.->",
        "Rooms": "Shows a list of all rooms.->",
        "Restart": "Restarts the current game.->",
        "Guilty PERSON NAME": "You find someone to be guilty. If right, then you win the game. If wrong, game over. This only works like: 'guilty ExampleName' not like: 'I think ExampleName is guilty.'.",
        "Backpack": "See what's in your backpack (things you have taken).",
        
                    };

    Clear();

    print("****************");
    print("Displaying help.");
    print("****************");
    
    Clear();
    
    print("Note: Enter the keywords below with your text to easily use them!");
    print("      Also, these keywords only work in INTERACTION MODE.");
    
    Clear();
    
    LoopList(HelpMessages, True);

#for sound
def PlaySound(SoundName):
    winsound.PlaySound('%s.wav' % SoundName, winsound.SND_ASYNC)
    
# Start Game Messages.
# Display The messages for the first time being opened.
StartGameMessages = [
    "Brought to you by Your name ",
    "The murder took place in the town of Baskerville which is a small town in the middleof nowhere in Scotland.  ",
    "There is a hound on the loose and the hound has been used to kill the men of the Baskerville estate for years. ",
    "The Baskerville family has been cursed with every year for being klled by the beast",
    "Use 'help' command during interaction mode / console window to get a list of commands.",
    "The commands are Innocent,Suspicous, Rooms, Restart, guilty, Take, Analyse, Use, Spotify and backpack (name of person)",
    "There will be a 1 second wait for every checkpoint.",
    "Note:----************INTERACTION MODE means is whenever the game asks you to input something.********************",
    ];


Clear();
print("Sherlock holmes and Dr. Watson");
print("******************************");

# Loop through the starting messages and printing them.
for WelcomeMessage in StartGameMessages:
    time.sleep(1);
    Clear();
    print(WelcomeMessage);

# ------------------------------------------------------------------------------------------------------- #

# Room Interaction functions setting.

def Take(ItemName, Room):
    Rooms[Room].pop(ItemName, None);
    print("The " + ItemName + " has been taken.");
    Backpack[ItemName] = Room;
    InteractWithRoomUser(Room, "Placeholder2");

#HomeRoom2

RoomInteractionwithmurder["HomeRoom2"]["Pen"]["Take"] = partial(Take, "Pen", "HomeRoom2");

RoomInteractionwithmurder["HomeRoom2"]["Ruler"]["Take"] = partial(Take, "Ruler", "HomeRoom2");

#HomeRoom3

def GunUse():
    PlaySound("GunShot");
    print("There are no bullets. But the sound of shooting still plays..................");
    InteractWithItem("HomeRoom3", "Gun");

RoomInteractionwithmurder["HomeRoom3"]["Gun"]["Take"] = partial(Take, "Gun", "HomeRoom3")
RoomInteractionwithmurder["HomeRoom3"]["Gun"]["Use"] = GunUse;
#laptopn
def LaptopUse(Placeholder1=None, Placeholder2=None):
    Clear();
    print("****************");
    print("Using The Laptop");
    print("****************");

    Clear();

    print("To return, say 'return' or 'HomeRoom3'.");

    Clear();
    
    TabsOpen = {

        "Google":  "A search for: 'Dealing with threat emails. and may show the whos is suspected'.",
        "Outlook": "The latest email states: 'Watch out - I'm coming for you.'.",
        "Police":  "An advice page for reporting threats.",
        "eBay":    "Self defence weapons are being listed.",
        "Spotify": "Currently playing - OMI Cheerleader------------------",
            
                };

    LoopList(TabsOpen, False);

    Clear();

    Interaction = raw_input("What would you like to interact with? ");

    Clear();
#master
    def FunctionToRunmaster(Item1, Item2):
        print(Item2);
        if Item1 == "Spotify":
            PlaySound("Cheerleader");

        LaptopUse("Placeholder1", "Placeholder2");
    
    InteractionalLoop(Interaction, TabsOpen, LaptopUse, None, None, "HomeRoom3", InteractWithRoomUser, "HomeRoom3", None, FunctionToRunmaster);
                      
RoomInteractionwithmurder["HomeRoom3"]["Laptop"]["Use"] = LaptopUse;

# HomeRoom4

RoomInteractionwithmurder["HomeRoom4"]["Case"]["Take"] = partial(Take, "Case", "HomeRoom4");

# HomeRoom5

RoomInteractionwithmurder["HomeRoom5"]["Glasses"]["Take"] = partial(Take, "Glasses", "HomeRoom5");

RoomInteractionwithmurder["HomeRoom5"]["Photo"]["Take"]  = partial(Take, "Photo", "HomeRoom5");

# Start
# Starts a new game.
def Start():
    Clear();

    print("*******************");
    print("Starting A New Game");
    print("*******************");

    Clear();

    print("There's a wild murderer loose! We need your help to stop him.");
    print("As Sherlock holmes and Dr. Watson, it's up to you to find out who this murderer is!");
    print("Your job: Gather evidence/clues and find out who this murderer really is.");

    Clear();

    # Defining a global variable to store the users's name.
    global UserName
    UserName = raw_input("So Sherlock holmes and Dr. Watson, my name is? ");

    global Backpack
    Backpack = {};

    Clear();

    print("Welcome, " + UserName + ". For now, we'll leave you to it.");

    # Starting the game off in the Baskerville.
    Hall("Placeholder1", "Placeholder2");

# Hall
# The command for being in the Baskerville.
def Hall(Placeholder1, Placeholder2):
    Clear();

    print("****************");
    print("In The Home of Baskerville Town");
    print("**************");

    Clear();

    print("The rooms you can go to are:");

    Clear();

    # Loop through the string keys (RoomNames).
    LoopList(Rooms, False);

    Clear();

    # Getting the players input.
    Interaction = raw_input("Where would you like to go (rooms)" + UserName + "? ");

    def FunctionToRunmaster(Item1, Item2):
        InteractWithRoomUser(Item1, "Placeholder2");

    InteractionalLoop(Interaction, Rooms, Hall, None, None, "Hall", Hall, None, None, FunctionToRunmaster);

HelpCommands = {};
#table loop
def LoopTable(List):
    Clear();

    print("****************");
    print("Displaying List");
    print("***************");

    Clear();

    LoopList(List, False);

HelpCommands["Innocent"] = partial(LoopTable, InnocentPeople);

HelpCommands["Suspicous"] = partial(LoopTable, SuspicousPeople);

HelpCommands["Rooms"] = partial(LoopTable, Rooms);

HelpCommands["Restart"] = Start;
#guilty
def GuiltyF(PersonName, Placeholder2):
    Clear();
    print("********************************************************");
    print("User declares Guilty on behalf of sherlock and Dr.Watson");
    print("********************************************************");

    Clear();

    if PersonName in SuspicousPeople:

        Interaction = raw_input("Are you sure that '" + PersonName + "' is guilty? ");

        Clear();

        Answers = {}
        Answers["Yes"] = "Yes";
        Answers["No"] = "No";

        def FunctionToRunmaster(Item1, Item2):
            if Item1 == "Yes":
                print("Alright, " + UserName + ". We'll carry on.");

                Clear();

                print("We are now executing " + PersonName + ". Hopefully you are right.");
    
                Clear();
                time.sleep(1);

                # That person was guilty!
                if ChosenMurderer == PersonName:
                    print("Congratulations! Dr Watsopn and sherlock  successully stopped the murderer!");
                    PlaySound("Win");

                # That person is not guilty!
                else:
                    print("Game Over! Unfortunetly " + PersonName + " is not the murderer.ohhhh Poor souls (you and " + PersonName + "'s).");
                    PlaySound("GameOver");

                Start();
                
            else:
                print("Alright, " + UserName + ". Make sure to find out soon...................!");

                Clear();
    
        InteractionalLoop(Interaction, Answers, GuiltyF, PersonName, None, "Guilty", GuiltyF, PersonName, None, FunctionToRunmaster);
        
    else:
        print(PersonName + " is not a suspicous person.");

HelpCommands["Guilty"] = GuiltyF;
#back pack for sherloack homes
def BackpackF(Placeholder1, Placehodler2):
    Clear();

    print("****************");
    print("Showing Backpack");
    print("****************");

    Clear();

    print("To return, say 'return' or 'hall'.");
    
    Clear();

    if len(Backpack) == 0:
        print("There are no items in your backpack.");
        return;

    LoopList(Backpack, False);

    Clear();

    Interaction = raw_input("What would you like to interact with? ");

    Clear();

    def FunctionToRunmaster(Item1, Item2):        
        Clear();

       
        Item = RoomInteractionwithmurder[Item2][Item1];
        print("*********************");
        print("Interacting With Item");
        print("*********************");

        Clear();

        print("To return, say 'return' or '" + Item2 + "'.");
        
        Clear();

        print("You can interact with: ");

        Clear();

        for ItemName in Item:
            if ItemName != "Take":
                print(ItemName);
                
        Clear();

        Interaction = raw_input(UserName + ", what would you like to interact with? ");

        Clear();

        def FunctionToRunmaster(Item1, Item2):
            if type(Item2) is str:
                print(Item2);
            else:
                Item2();
                    
        InteractionalLoop(Interaction, Item, FunctionToRunmaster, Item2, ItemName, Item2, InteractWithRoomUser, Item2, None, FunctionToRunmaster);

    InteractionalLoop(Interaction, Backpack, BackpackF, None, None, "Hall", Hall, None, None, FunctionToRunmaster);

HelpCommands["Backpack"] = BackpackF;

#interaction
def InteractionalLoop(Interaction, Dictionary, Function=None, FuncArg1=None, FuncArg2=None, ReturnSelection=None, ReturnFunction=None, ReturnArg1=None, ReturnArg2=None, FunctionToRunmaster=None):
        Clear();            

              
        if Function == None:
            def Function(Placeholder1, Placeholder2):
                return;
            
        elif FuncArg1 == None:
            FuncArg1, FuncArg2 = "Placeholder1", "Placeholder2";

        elif FuncArg2 == None:
            Func2 = "Placeholder";

       
        if ReturnFunction == None:
            def ReturnFunction(Placeholder1, Placeholder2):
                return;
            
        elif ReturnArg1 == None:
            ReturnArg1, ReturnArg2 = "Placeholder1", "Placeholder2";

        elif ReturnArg2 == None:
            ReturnArg2 = "Placeholder2";
        
      
        LoweredInteraction = Interaction.lower();
        
      
        for Item1, Item2 in Dictionary.items():
            # Item1 has been found in the interaction.
            if LoweredInteraction.find(Item1.lower()) != -1:
                FunctionToRunmaster(Item1, Item2);

                time.sleep(1);
                Function(FuncArg1, FuncArg2);
                return Item1, Item2;

           
            elif LoweredInteraction.find("help") != -1:
                DisplayHelp();

                time.sleep(1);
                Function(FuncArg1, FuncArg2);
                return "help";

           
            elif LoweredInteraction.find("return") != -1 or LoweredInteraction.find(ReturnSelection.lower()) != -1:
                ReturnFunction(ReturnArg1, ReturnArg2);

                time.sleep(1);
                Function(FuncArg1, FuncArg2);
                return "return"

            # Searching through HelpCommands.
            else:
                for HelpName, HelpAction in HelpCommands.items():
                    if LoweredInteraction.find(HelpName.lower()) != -1:
                        if HelpName.lower() == "guilty":
                            HelpAction((Interaction[7:]).strip(), "Placeholder2");

                        elif HelpName.lower() == "backpack":
                            HelpAction("Placeholder1", "Placeholder");
                            
                        else:
                            HelpAction();

                        time.sleep(1);
                        Function(FuncArg1, FuncArg2);
                        return HelpName, HelpAction;
                                    
        # Couldn't understand.
        print("System Could not understand, " + UserName + ".");
        print("Please try again.............................");
        
        Function(FuncArg1, FuncArg2);
        return False;


def InteractWithItem(RoomName, ItemName):
    Clear();

    
    Item = RoomInteractionwithmurder[RoomName][ItemName];

    print("*********************");
    print("Interacting With Item");
    print("*********************");

    Clear();

    print("To return, say 'return' or '" + RoomName + "'.");

    Clear();

    print("You can interact with: ");

    Clear();

    LoopList(Item, False);

    Clear();

    Interaction = raw_input(UserName + ", what would you like to interact with? ");

    Clear();

    def FunctionToRunmaster(Item1, Item2):
        if type(Item2) is str:
            print(Item2);
        else:
            Item2();
                
    InteractionalLoop(Interaction, Item, InteractWithItem, RoomName, ItemName, RoomName, InteractWithRoomUser, RoomName, None, FunctionToRunmaster);


def InteractWithRoomUser(RoomName, Placeholder):
    Clear();

  
    Room = Rooms[RoomName];
    print("**********************");
    print("Yor are In " + RoomName);
    print("**********************");

    Clear();

    print("To return, say 'return' or 'hall'.");

    Clear();

    print("The items within this room are:");

    Clear();

   
    LoopList(Room, False);

    Clear();

    Interaction = raw_input("What would you like to interact with, " + UserName + "? ");

    def FunctionToRunmaster(Item1, Item2):
        InteractWithItem(RoomName, Item1);

    InteractionalLoop(Interaction, Room, InteractWithRoomUser, RoomName, None, "Hall", Hall, None, None, FunctionToRunmaster);



# Starting the game.
Start();






