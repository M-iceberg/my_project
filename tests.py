def main():
    print("==========Testing character model===========")
    test_chacter=character.Character()

    print("==========Standard Input Test===============")
    test_character.change_position(2,3)
    assert test_character.update_position(x,y)==(2,3)

    print("==========Zero Input test===============")
    test_character.change_position(0,0)
    assert test_character.update_position(x,y)=(0,0)

    print("==========Negative Input test==========")
    test_charcter.change_position(-2,-3)
    assert test_character.update_position(x,y)=(-2,-3)

    print("==========speed input test============")
    test_character.change_speed(10,10)
    assert test_character.speed_update==20

    print("============negative speed test========")
    test_character.change_speed(10,-10)
    assert test_character.speed_update==-0

    print("=============zero speed test=============")
    test_character.change_speed(10,0)
    assert test_character.speed_update==10

    print("==============Testing music model===========")
    test_music=music.Music()

    print("============Standard input test===============")
    test_music.change_volume(3)
    assert test_music.update_volume==10

    print("===========negative input test===============")
    test_music.change_volume(-3)
    assert test_music.update_volume==4

    print("==========zero input test==============")
    test_music.change_volume(0)
    assert test_music.update_volume==7

    print("==========screen test=================")
    screen_test=screen.Screen()

    print("==========standard input test========")
    screen_test.give_position(7,7)
    assert screen.test.update_screenpos=(7,7)

    print("=========zero input test===========")
    screen_test.give_position(0,0)
    assert screen.test.update_screenpos(0,0)

    print("======== negative input test========")
    screen_test.given_position(-2,-2)
    assert screen_test.update_screenpos(-2,-2)

    print("=========testing monster model========")
    test_monster=monster.Monster()

    print("==========monster position test==========")
    test_monster.changeposition(2,3)
    assert test_monster.getposition(2,3)

    print("===========monster position test=========")
    test_monster.changeposition(0,0)
    assert test_monster.getposition(0,0)

    print("==========monster speed test==========")
    test_speed=test_monster.faster()

    print("=========test standard monster speed=========")
    test_monster.faster(10,10)
    assert test_monster.get_speed=10

    print("=======test negative monster speed=======")
    test_monster.faster(-10,10)
    assert test_monster.get_speed=-10
    
main()
    
    
    
                                 
          

    

