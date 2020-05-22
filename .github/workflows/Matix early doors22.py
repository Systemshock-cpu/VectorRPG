import anki_vector
from anki_vector.util import degrees, Angle, Pose ,distance_mm
import random
import time

##GAME DATA vector spawn point
sectorx = 5
sectory = 5
sdisnmid=""
sdisnlong=""
sdisnmax=""
sdiss=""
dead = False

##GAME DATA



with anki_vector.Robot() as robot:
    robot.world.disconnect_cube()
    robot.behavior.drive_off_charger()
    
    print(" disconnecting from any connected cube…")
    robot.world.disconnect_cube()

    time.sleep(2)
    connected_cube = robot.world.connected_light_cube
    robot.behavior.say_text("Turning my cube in to !! a joystick ! to move in  the game")
    connectionResult = robot.world.connect_cube()
    time.sleep(1)
    robot.behavior.say_text("red is north , blue is east ,yellow is move south and green is west ")
    
    if robot.world.connected_light_cube:
            cube = robot.world.connected_light_cube

            cube.set_light_corners(anki_vector.lights.red_light,
                                   anki_vector.lights.blue_light,
                                   anki_vector.lights.yellow_light,
                                   anki_vector.lights.green_light)



    ##GAME DATA simple map

    space_grid = [
        
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,4,0],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [4,0,0,0,1,6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [5,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [6,0,0,0,1,7,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [8,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [11,0,0,0,5,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [21,0,0,0,5,0,0,0,0,1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [31,0,0,0,5,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [37,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]


##LOCATION center
    for x in range(0, 500):
        
        if (space_grid[sectorx][sectory]) == 0:
            sdis=" empty space"
            ##add random here  of drivable floor to  make this  more  convatioal


        if (space_grid[sectorx][sectory]) == 1:
            sdis="  I am touching ,a metal wall  "


            
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx][sectory]) == 2:
            sdis=" I am touching a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx][sectory]) == 3:
            sdis="I am touching a Plane looking wall "
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx][sectory]) == 4:
            sdis="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx][sectory]) == 5:
            sdis=" there a  wood clad wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx][sectory]) == 6:
            sdis="  I am in  a pit of lava thanks,thank so  fucking much  I am burning to death  thank you so so much "
            

        if (space_grid[sectorx][sectory]) == 7:
            sdis=" there a large lid  covering a pit !  "

            robot.say_text("Ok there Large leaver in the box you thinking  what am thinking  fist bump! to do it")
            ang = robot.pose_angle_rad + 0.01
            robot.behavior.set_head_angle(degrees(45))
            robot.behavior.set_lift_height(1.0)
            while robot.pose_angle_rad < ang:
                print(ang)
                print(robot.pose_angle_rad)
                time.sleep(0.01)

                        
            robot.say_text("A  large cover lowering slowley on to the lava pit from the roof nice ! win! Team US !")
            robot.behavior.turn_in_place(degrees(180))





            
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx][sectory]) == 8:
            sdis=" there a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx][sectory]) == 9:
            sdis="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx][sectory]) == 10:
            sdis="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx][sectory]) == 11:
            sdis=" there open doorway"
        ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx][sectory]) == 12:
            sdis="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioalconvatioal
            
        else:
            robot.behavior.say_text(" here I am")
            
        print(space_grid[sectorx][sectory])

        
        robot.behavior.say_text(sdis)


    ##LOCATION north
        if (space_grid[sectorx -1][sectory]) == 0:
           sdisn=" 2 m of space"
        if (space_grid[sectorx -2][sectory]) <= 1:
           sdisnmid=" another 5 m of space"
        if (space_grid[sectorx -3][sectory]) <= 1:
               sdisnlong=" It a big space total up to 10 m"
        if (space_grid[sectorx -4][sectory]) <= 1:
            sdisnmax=" I can see nothing more 20 m ,hay I do my but veiw is limted from down here "
            
        
       
        if (space_grid[sectorx -1][sectory]) == 1:
            sdisn="  It 1 meter to a metal wall  "
        if (space_grid[sectorx -2][sectory]) >= 1:
           sdisnmid="then a metal wall "
        if (space_grid[sectorx -3][sectory]) >= 1:
            sdisnlong=" in the distance a metal wall"  


            
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx -1][sectory]) == 2:
            sdisn=" It 1 meter to  a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx-1][sectory]) == 3:
            sdisn="I am touching a Plane looking wall "
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx -1][sectory]) == 4:
            sdisn="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx-1][sectory]) == 5:
            sdisn=" there a  wood clad wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx-1][sectory]) == 6:
            sdisn=" a firey pit od lava , a pit of death,  lovely thanks !"
            ##add random here  of drivable floor to  make this  more  if (space_grid[sectorx][sectory]) == 0:
            sdis=" empty space"

        if (space_grid[sectorx-1][sectory]) == 7:
            sdisn="  is a metal wall but it look there a box on it "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx-1][sectory]) == 8:
            sdisn=" there a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx-1][sectory]) == 9:
            sdisn="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx-1][sectory]) == 10:
            
           sdisn ="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx-1][sectory]) == 11:
            sdisn=" there open doorway"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx-1][sectory]) == 12:
            sdisn="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioalconvatioal



    ##LOCATION east
        if (space_grid[sectorx ][sectory+1]) == 0:
           sdisn=" 2 m of space"
        if (space_grid[sectorx ][sectory]+2) <= 1:
           sdisnmid=" another 5 m of space"
        if (space_grid[sectorx ][sectory]+3) <= 1:
               sdisnlong=" It a big space total up to 10 m"
        if (space_grid[sectorx ][sectory]+4) <= 1:
            sdisnmax=" I can see nothing more 20 m ,hay I do my but veiw is limted from down here "


        if (space_grid[sectorx ][sectory]+1) == 1:
            sdise="  It 1 meter to a metal wall here it's "
            
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx ][sectory]+1) == 2:
            sdise=" It 1 meter to  a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx][sectory]+1) == 3:
            sdise="I am touching a Plane looking wall "
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory]+1) == 4:
            sdise="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx ][sectory]+1) == 5:
            sdise=" there a  wood clad wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory]+1) == 6:
            sdise="  fire  riseing  from a lava pit"
            ##add random here  of drivable floor to  make this  more  if (space_grid[sectorx][sectory]) == 0:
            sdie=" empty space"

        if (space_grid[sectorx ][sectory]+1) == 7:
            sdise=" is a metal wall but it look there a box on it  "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx ][sectory]+1) == 8:
            sdise=" there a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory]+1) == 9:
            sdise="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory]+1) == 10:
            
           sdise ="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx ][sectory]+1) == 11:
            sdiss=" there open doorway"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory]+1) == 12:
            sdise="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioalconvatioal

    ##LOCATION west
        if (space_grid[sectorx ][sectory-1]) == 0:
            sdisw=" empty space"
            ##the clever bit liner o sight


        if (space_grid[sectorx ][sectory -1]) == 1:
            sdisw="  It 1 meter to a metal wall here "



        if (space_grid[sectorx ][sectory -1]) == 2:
            sdisw=" It 1 meter to  a wood wall"
                  

        if (space_grid[sectorx ][sectory -1]) == 3:
            sdisw="I am touching a Plane looking wall "
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory -1]) == 4:
            sdiss="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx ][sectory -1]) == 5:
            sdiss=" there a  wood clad wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory -1]) == 6:
            sdisw="  Is that  lava  dam that hot"
            ##add random here  of drivable floor to  make this  more  if (space_grid[sectorx][sectory]) == 0:
           

        if (space_grid[sectorx ][sectory -1]) == 7:
            sdisw=" is a metal wall but it look there a box on it  "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx ][sectory -1]) == 8:
            sdisw=" there a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory]) == 9:
            sdisw="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory]) == 10:
            
           sdisw ="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx ][sectory -1]) == 11:
            sdisw=" there open doorway"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx ][sectory -1])== 12:
            sdisw="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioalconvatioal

            ##LOCATION south
        if (space_grid[sectorx ][sectory -1]) == 0:
            sdiss=" empty space"
            ##the clever bit liner o sight


        if (space_grid[sectorx +1][sectory]) == 1:
            sdiss="  It 1 meter to a metal wall here "
            
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx +1][sectory]) == 2:
            sdiss=" It 1 meter to  a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory]) == 3:
            sdiss="I am touching a Plane looking wall "
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory]) == 4:
            sdiss="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx-1][sectory]) == 5:
            sdiss=" there a  wood clad wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory]) == 6:
            sdiss="  What  Pycho game wrigter  put me in a game with lava pits"
            ##add random here  of drivable floor to  make this  more  if (space_grid[sectorx][sectory]) == 0:
            sdis=" empty space"

        if (space_grid[sectorx +1][sectory]) == 7:
            sdiss=" is a metal wall but it look there a box on it  "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx +1][sectory]) == 8:
            sdiss=" there a wood wall"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory]) == 9:
            sdiss="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory]) == 10:
            
           sdiss ="  I am touching a metal wall here "
            ##add random here  of drivable floor to  make this  more  convatioal
            
        if (space_grid[sectorx +1][sectory]) == 11:
            sdiss=" there open doorway"
            ##add random here  of drivable floor to  make this  more  convatioal

        if (space_grid[sectorx +1][sectory])== 12:
            sdiss="  there wall here"
            ##add random here  of drivable floor to  make this  more  convatioalconvatioal   


    ##    Vector shows off, this is the fun bit  he turn and say what direction he looking.

        
        robot.behavior.say_text(" I am faceing north now") 


        robot.behavior.say_text(" In frount of me north i can see " +(sdisn) +(sdisnmid) +(sdisnlong) )
        robot.behavior.turn_in_place(degrees(90))
        robot.behavior.say_text(" east i can see " +(sdise) )
        robot.behavior.turn_in_place(degrees(90))
        robot.behavior.say_text(" Behind me south i can see " +(sdiss) )
        robot.behavior.turn_in_place(degrees(90))
        robot.behavior.say_text(" west i can see " +(sdisw) )
        robot.behavior.turn_in_place(degrees(90))

        robot.behavior.say_text(" OK what next !")
        time.sleep(1)
       

        if (robot.world.connected_light_cube.up_axis) == 1: 
            up_axis=6
            robot.behavior.say_text(" ok I  move  north")
            sectory = (sectory - 1)
            
        if (robot.world.connected_light_cube.up_axis) == 2:
            sectory = (sectory + 1)
            robot.behavior.say_text("I move south")
            up_axis=6
            
        if (robot.world.connected_light_cube.up_axis) == 3:
            sectorx = (sectorx + 1)
            robot.behavior.say_text("I move east")
            up_axis=6

        if (robot.world.connected_light_cube.up_axis) == 4:
            sectorx = (sectorx - 1)
            robot.behavior.say_text("I move west")
            up_axis == 6
       
        

       
        up_axis=0

##        def cubejoy():
##
##            print("connect to a cube...")
##            connectionResult = robot.world.connect_cube()
##
##            robot.behavior.say_text("3 sec to input")
##            for _ in range(30):
##                connected_cube = robot.world.connected_light_cube
##                if connected_cube:
##                    print(f'up_axis: {connected_cube.up_axis}')
##                    
##
##                if (robot.world.connected_light_cube.up_axis) == 1:
##                  robot.behavior.say_text("I  move  north")
##                  sectory == ( sectory -1)
##                 
##                  up_axis=6
##               
##                  
##                if (robot.world.connected_light_cube.up_axis) == 2:
##                    robot.behavior.say_text("I move south")
##                    up_axis=6
##                    sectory = sectory +1
##                    
##                if (robot.world.connected_light_cube.up_axis) == 3:
##                  robot.behavior.say_text("I move east")
##                  up_axis=6
##                  sectorx = sectorx+1
##                  
##
##                if (robot.world.connected_light_cube.up_axis) == 4:
##                  robot.behavior.say_text("I move west")
##                  up_axis=6
##                  sectorx = sectorx+1
##                    
##                else:
##                  time.sleep(0.5)
##                  
##
##        cubejoy()
##        time.sleep(1)
##        robot.behavior.say_text("your 3 seconds and")
        
    
   



    
