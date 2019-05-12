def backgroundExist(state, available_betting_point_address):
    state_string = ''.join(str(i) for i in state)
    background_exist = True
    best_point_address = [-1,-1]
    best_column = 0
    if state_string == '':
        best_column = 3
    elif state_string == "31":
        best_column = 4
    elif state_string == "32":
        best_column = 6
    elif state_string == "33":
        best_column = 2
    elif state_string == "34":
        best_column = 3
    elif state_string == "35":
        best_column = 3
    elif state_string == "36":
        best_column = 2
    elif state_string == "37":
        best_column = 3
    elif state_string == "3141":
        best_column = 5
    elif state_string == "3142":
        best_column = 2
    elif state_string == "3143":
        best_column = 5
    elif state_string == "3144":
        best_column = 5
    elif state_string == "3145":
        best_column = 5
    elif state_string == "3146":
        best_column = 2
    elif state_string == "3147":
        best_column = 5
    elif state_string == "3261":
        best_column = 3
    elif state_string == "3262":
        best_column = 6
    elif state_string == "3263":
        best_column = 3
    elif state_string == "3264":
        best_column = 6
    elif state_string == "3265":
        best_column = 3
    elif state_string == "3266":
        best_column = 6
    elif state_string == "3267":
        best_column = 2
    elif state_string == "3321":
        best_column = 3
    elif state_string == "3322":
        best_column = 4
    elif state_string == "3323":
        best_column = 4
    elif state_string == "3324":
        best_column = 4
    elif state_string == "3325":
        best_column = 3
    elif state_string == "3326":
        best_column = 4
    elif state_string == "3327":
        best_column = 4
    elif state_string == "3431":
        best_column = 3
    elif state_string == "3432":
        best_column = 3
    elif state_string == "3433":
        best_column = 4
    elif state_string == "3434":
        best_column = 3
    elif state_string == "3435":
        best_column = 3
    elif state_string == "3436":
        best_column = 3
    elif state_string == "3437":
        best_column = 3
    elif state_string == "3531":
        best_column = 3
    elif state_string == "3532":
        best_column = 3
    elif state_string == "3533":
        best_column = 5
    elif state_string == "3534":
        best_column = 3
    elif state_string == "3535":
        best_column = 3
    elif state_string == "3536":
        best_column = 3
    elif state_string == "3537":
        best_column = 3
    elif state_string == "3621":
        best_column = 2
    elif state_string == "3622":
        best_column = 4
    elif state_string == "3623":
        best_column = 4
    elif state_string == "3624":
        best_column = 4
    elif state_string == "3625":
        best_column = 2
    elif state_string == "3626":
        best_column = 4
    elif state_string == "3627":
        best_column = 4
    elif state_string == "3731":
        best_column = 3
    elif state_string == "3732":
        best_column = 3
    elif state_string == "3733":
        best_column = 4
    elif state_string == "3734":
        best_column = 3
    elif state_string == "3735":
        best_column = 3
    elif state_string == "3736":
        best_column = 4
    elif state_string == "3737":
        best_column = 3
    elif state_string == "314221":
        best_column = 1
    elif state_string == "314222":
        best_column = 4
    elif state_string == "314223":
        best_column = 2
    elif state_string == "314224":
        best_column = 4
    elif state_string == "314225":
        best_column = 4
    elif state_string == "314226":
        best_column = 2
    elif state_string == "314227":
        best_column = 4
    elif state_string == "314551":
        best_column = 3
    elif state_string == "314552":
        best_column = 2
    elif state_string == "314553":
        best_column = 5
    elif state_string == "314554":
        best_column = 4
    elif state_string == "314555":
        best_column = 3
    elif state_string == "314556":
        best_column = 3
    elif state_string == "314557":
        best_column = 3
    elif state_string == "314621":
        best_column = 5
    elif state_string == "314622":
        best_column = 5
    elif state_string == "314623":
        best_column = 5
    elif state_string == "314624":
        best_column = 5
    elif state_string == "314625":
        best_column = 2
    elif state_string == "314626":
        best_column = 5
    elif state_string == "314627":
        best_column = 5
    elif state_string == "326131":
        best_column = 3
    elif state_string == "326132":
        best_column = 3
    elif state_string == "326133":
        best_column = 2
    elif state_string == "326134":
        best_column = 3
    elif state_string == "326135":
        best_column = 6
    elif state_string == "326136":
        best_column = 3
    elif state_string == "326137":
        best_column = 3
    elif state_string == "326261":
        best_column = 5
    elif state_string == "326262":
        best_column = 2
    elif state_string == "326263":
        best_column = 3
    elif state_string == "326264":
        best_column = 4
    elif state_string == "326265":
        best_column = 6
    elif state_string == "326266":
        best_column = 5
    elif state_string == "326267":
        best_column = 5
    elif state_string == "326331":
        best_column = 3
    elif state_string == "326332":
        best_column = 6
    elif state_string == "326333":
        best_column = 5
    elif state_string == "326334":
        best_column = 6
    elif state_string == "326335":
        best_column = 5
    elif state_string == "326336":
        best_column = 5
    elif state_string == "326337":
        best_column = 2
    elif state_string == "326461":
        best_column = 4
    elif state_string == "326462":
        best_column = 4
    elif state_string == "326463":
        best_column = 3
    elif state_string == "326464":
        best_column = 4
    elif state_string == "326465":
        best_column = 3
    elif state_string == "326466":
        best_column = 4
    elif state_string == "326467":
        best_column = 2
    elif state_string == "326531":
        best_column = 6
    elif state_string == "326532":
        best_column = 3
    elif state_string == "326533":
        best_column = 5
    elif state_string == "326534":
        best_column = 3
    elif state_string == "326535":
        best_column = 3
    elif state_string == "326536":
        best_column = 2
    elif state_string == "326537":
        best_column = 6
    elif state_string == "326661":
        best_column = 2
    elif state_string == "326662":
        best_column = 5
    elif state_string == "326663":
        best_column = 3
    elif state_string == "326664":
        best_column = 4
    elif state_string == "326665":
        best_column = 3
    elif state_string == "326666":
        best_column = 4
    elif state_string == "326667":
        best_column = 2
    elif state_string == "326721":
        best_column = 3
    elif state_string == "326722":
        best_column = 5
    elif state_string == "326723":
        best_column = 3
    elif state_string == "326724":
        best_column = 6
    elif state_string == "326725":
        best_column = 5
    elif state_string == "326726":
        best_column = 3
    elif state_string == "326727":
        best_column = 2
    elif state_string == "332131":
        best_column = 3
    elif state_string == "332132":
        best_column = 5
    elif state_string == "332133":
        best_column = 4
    elif state_string == "332134":
        best_column = 4
    elif state_string == "332135":
        best_column = 2
    elif state_string == "332136":
        best_column = 4
    elif state_string == "332137":
        best_column = 4
    elif state_string == "332441":
        best_column = 4
    elif state_string == "332442":
        best_column = 4
    elif state_string == "332443":
        best_column = 3
    elif state_string == "332444":
        best_column = 4
    elif state_string == "332445":
        best_column = 3
    elif state_string == "332446":
        best_column = 3
    elif state_string == "332447":
        best_column = 4
    elif state_string == "332531":
        best_column = 2
    elif state_string == "332532":
        best_column = 4
    elif state_string == "332533":
        best_column = 4
    elif state_string == "332534":
        best_column = 2
    elif state_string == "332535":
        best_column = 4
    elif state_string == "332536":
        best_column = 4
    elif state_string == "332537":
        best_column = 4
    elif state_string == "343131":
        best_column = 3
    elif state_string == "343132":
        best_column = 3
    elif state_string == "343133":
        best_column = 4
    elif state_string == "343134":
        best_column = 3
    elif state_string == "343135":
        best_column = 3
    elif state_string == "343136":
        best_column = 3
    elif state_string == "343137":
        best_column = 3
    elif state_string == "343231":
        best_column = 3
    elif state_string == "343232":
        best_column = 3
    elif state_string == "343233":
        best_column = 1
    elif state_string == "343234":
        best_column = 3
    elif state_string == "343235":
        best_column = 3
    elif state_string == "343236":
        best_column = 3
    elif state_string == "343237":
        best_column = 3
    elif state_string == "343341":
        best_column = 4
    elif state_string == "343342":
        best_column = 4
    elif state_string == "343343":
        best_column = 4
    elif state_string == "343344":
        best_column = 4
    elif state_string == "343345":
        best_column = 4
    elif state_string == "343346":
        best_column = 4
    elif state_string == "343347":
        best_column = 4
    elif state_string == "343431":
        best_column = 3
    elif state_string == "343432":
        best_column = 3
    elif state_string == "343433":
        best_column = 4
    elif state_string == "343434":
        best_column = 3
    elif state_string == "343435":
        best_column = 3
    elif state_string == "343436":
        best_column = 3
    elif state_string == "343437":
        best_column = 3
    elif state_string == "343531":
        best_column = 3
    elif state_string == "343532":
        best_column = 3
    elif state_string == "343533":
        best_column = 1
    elif state_string == "343534":
        best_column = 3
    elif state_string == "343535":
        best_column = 3
    elif state_string == "343536":
        best_column = 3
    elif state_string == "343537":
        best_column = 3
    elif state_string == "343631":
        best_column = 3
    elif state_string == "343632":
        best_column = 3
    elif state_string == "343633":
        best_column = 6
    elif state_string == "343634":
        best_column = 3
    elif state_string == "343635":
        best_column = 3
    elif state_string == "343636":
        best_column = 3
    elif state_string == "343637":
        best_column = 3
    elif state_string == "343731":
        best_column = 3
    elif state_string == "343732":
        best_column = 3
    elif state_string == "343733":
        best_column = 2
    elif state_string == "343734":
        best_column = 3
    elif state_string == "343735":
        best_column = 3
    elif state_string == "343736":
        best_column = 3
    elif state_string == "343737":
        best_column = 3
    elif state_string == "353131":
        best_column = 3
    elif state_string == "353132":
        best_column = 3
    elif state_string == "353133":
        best_column = 4
    elif state_string == "353134":
        best_column = 3
    elif state_string == "353135":
        best_column = 3
    elif state_string == "353136":
        best_column = 3
    elif state_string == "353137":
        best_column = 3
    elif state_string == "353231":
        best_column = 3
    elif state_string == "353232":
        best_column = 3
    elif state_string == "353233":
        best_column = 6
    elif state_string == "353234":
        best_column = 3
    elif state_string == "353235":
        best_column = 3
    elif state_string == "353236":
        best_column = 3
    elif state_string == "353237":
        best_column = 3
    elif state_string == "353351":
        best_column = 3
    elif state_string == "353352":
        best_column = 2
    elif state_string == "353353":
        best_column = 1
    elif state_string == "353354":
        best_column = 3
    elif state_string == "353355":
        best_column = 2
    elif state_string == "353356":
        best_column = 7
    elif state_string == "353357":
        best_column = 6
    elif state_string == "353431":
        best_column = 3
    elif state_string == "353432":
        best_column = 3
    elif state_string == "353433":
        best_column = 1
    elif state_string == "353434":
        best_column = 3
    elif state_string == "353435":
        best_column = 3
    elif state_string == "353436":
        best_column = 3
    elif state_string == "353437":
        best_column = 3
    elif state_string == "353531":
        best_column = 3
    elif state_string == "353532":
        best_column = 3
    elif state_string == "353533":
        best_column = 5
    elif state_string == "353534":
        best_column = 3
    elif state_string == "353535":
        best_column = 3
    elif state_string == "353536":
        best_column = 3
    elif state_string == "353537":
        best_column = 3
    elif state_string == "353631":
        best_column = 3
    elif state_string == "353632":
        best_column = 3
    elif state_string == "353633":
        best_column = 4
    elif state_string == "353634":
        best_column = 3
    elif state_string == "353635":
        best_column = 3
    elif state_string == "353636":
        best_column = 3
    elif state_string == "353637":
        best_column = 3
    elif state_string == "353731":
        best_column = 3
    elif state_string == "353732":
        best_column = 3
    elif state_string == "353733":
        best_column = 4
    elif state_string == "353734":
        best_column = 3
    elif state_string == "353735":
        best_column = 3
    elif state_string == "353736":
        best_column = 3
    elif state_string == "353737":
        best_column = 3
    elif state_string == "362121":
        best_column = 2
    elif state_string == "362122":
        best_column = 3
    elif state_string == "362123":
        best_column = 2
    elif state_string == "362124":
        best_column = 2
    elif state_string == "362125":
        best_column = 2
    elif state_string == "362126":
        best_column = 2
    elif state_string == "362127":
        best_column = 2
    elif state_string == "362441":
        best_column = 4
    elif state_string == "362442":
        best_column = 4
    elif state_string == "362443":
        best_column = 3
    elif state_string == "362444":
        best_column = 4
    elif state_string == "362445":
        best_column = 7
    elif state_string == "362446":
        best_column = 2
    elif state_string == "362447":
        best_column = 5
    elif state_string == "362521":
        best_column = 2
    elif state_string == "362522":
        best_column = 3
    elif state_string == "362523":
        best_column = 2
    elif state_string == "362524":
        best_column = 7
    elif state_string == "362525":
        best_column = 2
    elif state_string == "362526":
        best_column = 2
    elif state_string == "362527":
        best_column = 4
    elif state_string == "373131":
        best_column = 3
    elif state_string == "373132":
        best_column = 2
    elif state_string == "373133":
        best_column = 3
    elif state_string == "373134":
        best_column = 3
    elif state_string == "373135":
        best_column = 3
    elif state_string == "373136":
        best_column = 3
    elif state_string == "373137":
        best_column = 3
    elif state_string == "373231":
        best_column = 3
    elif state_string == "373232":
        best_column = 3
    elif state_string == "373233":
        best_column = 2
    elif state_string == "373234":
        best_column = 3
    elif state_string == "373235":
        best_column = 3
    elif state_string == "373236":
        best_column = 3
    elif state_string == "373237":
        best_column = 3
    elif state_string == "373341":
        best_column = 5
    elif state_string == "373342":
        best_column = 4
    elif state_string == "373343":
        best_column = 2
    elif state_string == "373344":
        best_column = 2
    elif state_string == "373345":
        best_column = 4
    elif state_string == "373346":
        best_column = 2
    elif state_string == "373347":
        best_column = 2
    elif state_string == "373431":
        best_column = 3
    elif state_string == "373432":
        best_column = 3
    elif state_string == "373433":
        best_column = 2
    elif state_string == "373434":
        best_column = 3
    elif state_string == "373435":
        best_column = 3
    elif state_string == "373436":
        best_column = 3
    elif state_string == "373437":
        best_column = 3
    elif state_string == "373531":
        best_column = 3
    elif state_string == "373532":
        best_column = 3
    elif state_string == "373533":
        best_column = 4
    elif state_string == "373534":
        best_column = 3
    elif state_string == "373535":
        best_column = 3
    elif state_string == "373536":
        best_column = 3
    elif state_string == "373537":
        best_column = 3
    elif state_string == "373641":
        best_column = 3
    elif state_string == "373642":
        best_column = 4
    elif state_string == "373643":
        best_column = 2
    elif state_string == "373644":
        best_column = 2
    elif state_string == "373645":
        best_column = 3
    elif state_string == "373646":
        best_column = 2
    elif state_string == "373647":
        best_column = 2
    elif state_string == "373731":
        best_column = 3
    elif state_string == "373732":
        best_column = 3
    elif state_string == "373733":
        best_column = 4
    elif state_string == "373734":
        best_column = 3
    elif state_string == "373735":
        best_column = 3
    elif state_string == "373736":
        best_column = 3
    elif state_string == "373737":
        best_column = 3

    elif state_string == "1":
        best_column = 4
    elif state_string == "2":
        best_column = 3
    elif state_string == "3":
        best_column = 4
    elif state_string == "4":
        best_column = 4
    elif state_string == "5":
        best_column = 4
    elif state_string == "6":
        best_column = 5
    elif state_string == "7":
        best_column = 4
    elif state_string == "141":
        best_column = 4
    elif state_string == "142":
        best_column = 4
    elif state_string == "143":
        best_column = 4
    elif state_string == "144":
        best_column = 4
    elif state_string == "145":
        best_column = 4
    elif state_string == "146":
        best_column = 4
    elif state_string == "147":
        best_column = 3
    elif state_string == "231":
        best_column = 3
    elif state_string == "232":
        best_column = 2
    elif state_string == "233":
        best_column = 3
    elif state_string == "234":
        best_column = 4
    elif state_string == "235":
        best_column = 3
    elif state_string == "236":
        best_column = 3
    elif state_string == "237":
        best_column = 3
    elif state_string == "341":
        best_column = 4
    elif state_string == "342":
        best_column = 4
    elif state_string == "343":
        best_column = 3
    elif state_string == "344":
        best_column = 4
    elif state_string == "345":
        best_column = 4
    elif state_string == "346":
        best_column = 4
    elif state_string == "347":
        best_column = 4
    elif state_string == "541":
        best_column = 4
    elif state_string == "542":
        best_column = 4
    elif state_string == "543":
        best_column = 4
    elif state_string == "544":
        best_column = 4
    elif state_string == "545":
        best_column = 5
    elif state_string == "546":
        best_column = 4
    elif state_string == "547":
        best_column = 4
    elif state_string == "651":
        best_column = 5
    elif state_string == "652":
        best_column = 5
    elif state_string == "653":
        best_column = 5
    elif state_string == "654":
        best_column = 4
    elif state_string == "655":
        best_column = 5
    elif state_string == "656":
        best_column = 6
    elif state_string == "657":
        best_column = 5
    elif state_string == "741":
        best_column = 5
    elif state_string == "742":
        best_column = 4
    elif state_string == "743":
        best_column = 4
    elif state_string == "744":
        best_column = 4
    elif state_string == "745":
        best_column = 4
    elif state_string == "746":
        best_column = 4
    elif state_string == "747":
        best_column = 4
    elif state_string == "14141":
        best_column = 1
    elif state_string == "14142":
        best_column = 4
    elif state_string == "14143":
        best_column = 4
    elif state_string == "14144":
        best_column = 5
    elif state_string == "14145":
        best_column = 4
    elif state_string == "14146":
        best_column = 4
    elif state_string == "14147":
        best_column = 4
    elif state_string == "14241":
        best_column = 4
    elif state_string == "14242":
        best_column = 4
    elif state_string == "14243":
        best_column = 4
    elif state_string == "14244":
        best_column = 2
    elif state_string == "14245":
        best_column = 4
    elif state_string == "14246":
        best_column = 4
    elif state_string == "14247":
        best_column = 4
    elif state_string == "14341":
        best_column = 4
    elif state_string == "14342":
        best_column = 4
    elif state_string == "14343":
        best_column = 4
    elif state_string == "14344":
        best_column = 3
    elif state_string == "14345":
        best_column = 4
    elif state_string == "14346":
        best_column = 4
    elif state_string == "14347":
        best_column = 4
    elif state_string == "14441":
        best_column = 4
    elif state_string == "14442":
        best_column = 4
    elif state_string == "14443":
        best_column = 3
    elif state_string == "14444":
        best_column = 6
    elif state_string == "14445":
        best_column = 4
    elif state_string == "14446":
        best_column = 4
    elif state_string == "14447":
        best_column = 4
    elif state_string == "14541":
        best_column = 4
    elif state_string == "14542":
        best_column = 4
    elif state_string == "14543":
        best_column = 4
    elif state_string == "14544":
        best_column = 5
    elif state_string == "14545":
        best_column = 4
    elif state_string == "14546":
        best_column = 4
    elif state_string == "14547":
        best_column = 4
    elif state_string == "14641":
        best_column = 5
    elif state_string == "14642":
        best_column = 4
    elif state_string == "14643":
        best_column = 4
    elif state_string == "14644":
        best_column = 4
    elif state_string == "14645":
        best_column = 4
    elif state_string == "14646":
        best_column = 4
    elif state_string == "14647":
        best_column = 4
    elif state_string == "14731":
        best_column = 5
    elif state_string == "14732":
        best_column = 4
    elif state_string == "14733":
        best_column = 5
    elif state_string == "14734":
        best_column = 5
    elif state_string == "14735":
        best_column = 3
    elif state_string == "14736":
        best_column = 4
    elif state_string == "14737":
        best_column = 5
    elif state_string == "23131":
        best_column = 3
    elif state_string == "23132":
        best_column = 3
    elif state_string == "23133":
        best_column = 3
    elif state_string == "23134":
        best_column = 3
    elif state_string == "23135":
        best_column = 3
    elif state_string == "23136":
        best_column = 3
    elif state_string == "23137":
        best_column = 3
    elif state_string == "23221":
        best_column = 3
    elif state_string == "23222":
        best_column = 3
    elif state_string == "23223":
        best_column = 3
    elif state_string == "23224":
        best_column = 4
    elif state_string == "23225":
        best_column = 3
    elif state_string == "23226":
        best_column = 6
    elif state_string == "23227":
        best_column = 4
    elif state_string == "23331":
        best_column = 3
    elif state_string == "23332":
        best_column = 3
    elif state_string == "23333":
        best_column = 2
    elif state_string == "23334":
        best_column = 4
    elif state_string == "23335":
        best_column = 3
    elif state_string == "23336":
        best_column = 3
    elif state_string == "23337":
        best_column = 3
    elif state_string == "23441":
        best_column = 4
    elif state_string == "23442":
        best_column = 4
    elif state_string == "23443":
        best_column = 4
    elif state_string == "23444":
        best_column = 3
    elif state_string == "23445":
        best_column = 4
    elif state_string == "23446":
        best_column = 4
    elif state_string == "23447":
        best_column = 4
    elif state_string == "23531":
        best_column = 3
    elif state_string == "23532":
        best_column = 3
    elif state_string == "23533":
        best_column = 5
    elif state_string == "23534":
        best_column = 4
    elif state_string == "23535":
        best_column = 5
    elif state_string == "23536":
        best_column = 5
    elif state_string == "23537":
        best_column = 5
    elif state_string == "23631":
        best_column = 3
    elif state_string == "23632":
        best_column = 3
    elif state_string == "23633":
        best_column = 3
    elif state_string == "23634":
        best_column = 4
    elif state_string == "23635":
        best_column = 3
    elif state_string == "23636":
        best_column = 6
    elif state_string == "23637":
        best_column = 4
    elif state_string == "23731":
        best_column = 3
    elif state_string == "23732":
        best_column = 3
    elif state_string == "23733":
        best_column = 3
    elif state_string == "23734":
        best_column = 4
    elif state_string == "23735":
        best_column = 5
    elif state_string == "23736":
        best_column = 4
    elif state_string == "23737":
        best_column = 3
    elif state_string == "34141":
        best_column = 4
    elif state_string == "34142":
        best_column = 4
    elif state_string == "34143":
        best_column = 4
    elif state_string == "34144":
        best_column = 3
    elif state_string == "34145":
        best_column = 4
    elif state_string == "34146":
        best_column = 4
    elif state_string == "34147":
        best_column = 4
    elif state_string == "34241":
        best_column = 4
    elif state_string == "34242":
        best_column = 4
    elif state_string == "34243":
        best_column = 4
    elif state_string == "34244":
        best_column = 4
    elif state_string == "34245":
        best_column = 4
    elif state_string == "34246":
        best_column = 4
    elif state_string == "34247":
        best_column = 4
    elif state_string == "34331":
        best_column = 4
    elif state_string == "34332":
        best_column = 4
    elif state_string == "34333":
        best_column = 4
    elif state_string == "34334":
        best_column = 4
    elif state_string == "34335":
        best_column = 4
    elif state_string == "34336":
        best_column = 4
    elif state_string == "34337":
        best_column = 4
    elif state_string == "34441":
        best_column = 3
    elif state_string == "34442":
        best_column = 4
    elif state_string == "34443":
        best_column = 4
    elif state_string == "34444":
        best_column = 3
    elif state_string == "34445":
        best_column = 4
    elif state_string == "34446":
        best_column = 4
    elif state_string == "34447":
        best_column = 4
    elif state_string == "34541":
        best_column = 4
    elif state_string == "34542":
        best_column = 4
    elif state_string == "34543":
        best_column = 4
    elif state_string == "34544":
        best_column = 4
    elif state_string == "34545":
        best_column = 4
    elif state_string == "34546":
        best_column = 4
    elif state_string == "34547":
        best_column = 4
    elif state_string == "34641":
        best_column = 4
    elif state_string == "34642":
        best_column = 4
    elif state_string == "34643":
        best_column = 4
    elif state_string == "34644":
        best_column = 4
    elif state_string == "34645":
        best_column = 4
    elif state_string == "34646":
        best_column = 4
    elif state_string == "34647":
        best_column = 4
    elif state_string == "34741":
        best_column = 4
    elif state_string == "34742":
        best_column = 4
    elif state_string == "34743":
        best_column = 4
    elif state_string == "34744":
        best_column = 3
    elif state_string == "34745":
        best_column = 4
    elif state_string == "34746":
        best_column = 4
    elif state_string == "34747":
        best_column = 4
    elif state_string == "54141":
        best_column = 4
    elif state_string == "54142":
        best_column = 4
    elif state_string == "54143":
        best_column = 4
    elif state_string == "54144":
        best_column = 5
    elif state_string == "54145":
        best_column = 4
    elif state_string == "54146":
        best_column = 4
    elif state_string == "54147":
        best_column = 4
    elif state_string == "54241":
        best_column = 4
    elif state_string == "54242":
        best_column = 4
    elif state_string == "54243":
        best_column = 4
    elif state_string == "54244":
        best_column = 4
    elif state_string == "54245":
        best_column = 4
    elif state_string == "54246":
        best_column = 4
    elif state_string == "54247":
        best_column = 4
    elif state_string == "54341":
        best_column = 4
    elif state_string == "54342":
        best_column = 4
    elif state_string == "54343":
        best_column = 4
    elif state_string == "54344":
        best_column = 3
    elif state_string == "54345":
        best_column = 4
    elif state_string == "54346":
        best_column = 4
    elif state_string == "54347":
        best_column = 4
    elif state_string == "54441":
        best_column = 4
    elif state_string == "54442":
        best_column = 4
    elif state_string == "54443":
        best_column = 4
    elif state_string == "54444":
        best_column = 5
    elif state_string == "54445":
        best_column = 4
    elif state_string == "54446":
        best_column = 4
    elif state_string == "54447":
        best_column = 4
    elif state_string == "54551":
        best_column = 4
    elif state_string == "54552":
        best_column = 4
    elif state_string == "54553":
        best_column = 4
    elif state_string == "54554":
        best_column = 4
    elif state_string == "54555":
        best_column = 4
    elif state_string == "54556":
        best_column = 4
    elif state_string == "54557":
        best_column = 4
    elif state_string == "54641":
        best_column = 4
    elif state_string == "54642":
        best_column = 4
    elif state_string == "54643":
        best_column = 4
    elif state_string == "54644":
        best_column = 4
    elif state_string == "54645":
        best_column = 4
    elif state_string == "54646":
        best_column = 4
    elif state_string == "54647":
        best_column = 4
    elif state_string == "54741":
        best_column = 4
    elif state_string == "54742":
        best_column = 4
    elif state_string == "54743":
        best_column = 4
    elif state_string == "54744":
        best_column = 5
    elif state_string == "54745":
        best_column = 4
    elif state_string == "54746":
        best_column = 4
    elif state_string == "54747":
        best_column = 4
    elif state_string == "65151":
        best_column = 5
    elif state_string == "65152":
        best_column = 5
    elif state_string == "65153":
        best_column = 5
    elif state_string == "65154":
        best_column = 4
    elif state_string == "65155":
        best_column = 5
    elif state_string == "65156":
        best_column = 5
    elif state_string == "65157":
        best_column = 5
    elif state_string == "65251":
        best_column = 5
    elif state_string == "65252":
        best_column = 6
    elif state_string == "65253":
        best_column = 5
    elif state_string == "65254":
        best_column = 4
    elif state_string == "65255":
        best_column = 5
    elif state_string == "65256":
        best_column = 5
    elif state_string == "65257":
        best_column = 5
    elif state_string == "65351":
        best_column = 5
    elif state_string == "65352":
        best_column = 5
    elif state_string == "65353":
        best_column = 3
    elif state_string == "65354":
        best_column = 4
    elif state_string == "65355":
        best_column = 3
    elif state_string == "65356":
        best_column = 5
    elif state_string == "65357":
        best_column = 5
    elif state_string == "65441":
        best_column = 4
    elif state_string == "65442":
        best_column = 4
    elif state_string == "65443":
        best_column = 4
    elif state_string == "65444":
        best_column = 5
    elif state_string == "65445":
        best_column = 4
    elif state_string == "65446":
        best_column = 4
    elif state_string == "65447":
        best_column = 4
    elif state_string == "65551":
        best_column = 5
    elif state_string == "65552":
        best_column = 4
    elif state_string == "65553":
        best_column = 5
    elif state_string == "65554":
        best_column = 4
    elif state_string == "65555":
        best_column = 6
    elif state_string == "65556":
        best_column = 5
    elif state_string == "65557":
        best_column = 5
    elif state_string == "65661":
        best_column = 4
    elif state_string == "65662":
        best_column = 5
    elif state_string == "65663":
        best_column = 5
    elif state_string == "65664":
        best_column = 4
    elif state_string == "65665":
        best_column = 5
    elif state_string == "65666":
        best_column = 5
    elif state_string == "65667":
        best_column = 5
    elif state_string == "65751":
        best_column = 5
    elif state_string == "65752":
        best_column = 5
    elif state_string == "65753":
        best_column = 5
    elif state_string == "65754":
        best_column = 5
    elif state_string == "65755":
        best_column = 5
    elif state_string == "65756":
        best_column = 5
    elif state_string == "65757":
        best_column = 5
    elif state_string == "74151":
        best_column = 3
    elif state_string == "74152":
        best_column = 4
    elif state_string == "74153":
        best_column = 5
    elif state_string == "74154":
        best_column = 3
    elif state_string == "74155":
        best_column = 3
    elif state_string == "74156":
        best_column = 4
    elif state_string == "74157":
        best_column = 3
    elif state_string == "74241":
        best_column = 4
    elif state_string == "74242":
        best_column = 4
    elif state_string == "74243":
        best_column = 4
    elif state_string == "74244":
        best_column = 4
    elif state_string == "74245":
        best_column = 4
    elif state_string == "74246":
        best_column = 4
    elif state_string == "74247":
        best_column = 3
    elif state_string == "74341":
        best_column = 4
    elif state_string == "74342":
        best_column = 4
    elif state_string == "74343":
        best_column = 4
    elif state_string == "74344":
        best_column = 3
    elif state_string == "74345":
        best_column = 4
    elif state_string == "74346":
        best_column = 4
    elif state_string == "74347":
        best_column = 4
    elif state_string == "74441":
        best_column = 4
    elif state_string == "74442":
        best_column = 4
    elif state_string == "74443":
        best_column = 4
    elif state_string == "74444":
        best_column = 2
    elif state_string == "74445":
        best_column = 5
    elif state_string == "74446":
        best_column = 4
    elif state_string == "74447":
        best_column = 4
    elif state_string == "74541":
        best_column = 4
    elif state_string == "74542":
        best_column = 4
    elif state_string == "74543":
        best_column = 4
    elif state_string == "74544":
        best_column = 5
    elif state_string == "74545":
        best_column = 4
    elif state_string == "74546":
        best_column = 4
    elif state_string == "74547":
        best_column = 4
    elif state_string == "74641":
        best_column = 4
    elif state_string == "74642":
        best_column = 4
    elif state_string == "74643":
        best_column = 4
    elif state_string == "74644":
        best_column = 6
    elif state_string == "74645":
        best_column = 4
    elif state_string == "74646":
        best_column = 4
    elif state_string == "74647":
        best_column = 4
    elif state_string == "74741":
        best_column = 4
    elif state_string == "74742":
        best_column = 3
    elif state_string == "74743":
        best_column = 3
    elif state_string == "74744":
        best_column = 3
    elif state_string == "74745":
        best_column = 3
    elif state_string == "74746":
        best_column = 3
    elif state_string == "74747":
        best_column = 7
    elif state_string == "1414111":
        best_column = 5
    elif state_string == "1414112":
        best_column = 4
    elif state_string == "1414113":
        best_column = 4
    elif state_string == "1414114":
        best_column = 5
    elif state_string == "1414115":
        best_column = 4
    elif state_string == "1414116":
        best_column = 4
    elif state_string == "1414117":
        best_column = 5
    elif state_string == "1414241":
        best_column = 4
    elif state_string == "1414242":
        best_column = 4
    elif state_string == "1414243":
        best_column = 4
    elif state_string == "1414244":
        best_column = 5
    elif state_string == "1414245":
        best_column = 4
    elif state_string == "1414246":
        best_column = 4
    elif state_string == "1414247":
        best_column = 4
    elif state_string == "1414341":
        best_column = 4
    elif state_string == "1414342":
        best_column = 4
    elif state_string == "1414343":
        best_column = 4
    elif state_string == "1414344":
        best_column = 4
    elif state_string == "1414345":
        best_column = 4
    elif state_string == "1414346":
        best_column = 4
    elif state_string == "1414347":
        best_column = 4
    elif state_string == "1414451":
        best_column = 1
    elif state_string == "1414452":
        best_column = 6
    elif state_string == "1414453":
        best_column = 5
    elif state_string == "1414454":
        best_column = 6
    elif state_string == "1414455":
        best_column = 6
    elif state_string == "1414456":
        best_column = 5
    elif state_string == "1414457":
        best_column = 3
    elif state_string == "1414541":
        best_column = 4
    elif state_string == "1414542":
        best_column = 4
    elif state_string == "1414543":
        best_column = 4
    elif state_string == "1414544":
        best_column = 5
    elif state_string == "1414545":
        best_column = 4
    elif state_string == "1414546":
        best_column = 4
    elif state_string == "1414547":
        best_column = 4
    elif state_string == "1414641":
        best_column = 4
    elif state_string == "1414642":
        best_column = 4
    elif state_string == "1414643":
        best_column = 4
    elif state_string == "1414644":
        best_column = 5
    elif state_string == "1414645":
        best_column = 4
    elif state_string == "1414646":
        best_column = 4
    elif state_string == "1414647":
        best_column = 4
    elif state_string == "1414741":
        best_column = 4
    elif state_string == "1414742":
        best_column = 4
    elif state_string == "1414743":
        best_column = 4
    elif state_string == "1414744":
        best_column = 5
    elif state_string == "1414745":
        best_column = 4
    elif state_string == "1414746":
        best_column = 4
    elif state_string == "1414747":
        best_column = 4
    elif state_string == "1424141":
        best_column = 4
    elif state_string == "1424142":
        best_column = 4
    elif state_string == "1424143":
        best_column = 4
    elif state_string == "1424144":
        best_column = 5
    elif state_string == "1424145":
        best_column = 4
    elif state_string == "1424146":
        best_column = 4
    elif state_string == "1424147":
        best_column = 4
    elif state_string == "1424241":
        best_column = 4
    elif state_string == "1424242":
        best_column = 4
    elif state_string == "1424243":
        best_column = 4
    elif state_string == "1424244":
        best_column = 5
    elif state_string == "1424245":
        best_column = 4
    elif state_string == "1424246":
        best_column = 4
    elif state_string == "1424247":
        best_column = 4
    elif state_string == "1424341":
        best_column = 4
    elif state_string == "1424342":
        best_column = 4
    elif state_string == "1424343":
        best_column = 4
    elif state_string == "1424344":
        best_column = 5
    elif state_string == "1424345":
        best_column = 4
    elif state_string == "1424346":
        best_column = 4
    elif state_string == "1424347":
        best_column = 4
    elif state_string == "1424421":
        best_column = 4
    elif state_string == "1424422":
        best_column = 5
    elif state_string == "1424423":
        best_column = 3
    elif state_string == "1424424":
        best_column = 2
    elif state_string == "1424425":
        best_column = 5
    elif state_string == "1424426":
        best_column = 4
    elif state_string == "1424427":
        best_column = 7
    elif state_string == "1424541":
        best_column = 4
    elif state_string == "1424542":
        best_column = 4
    elif state_string == "1424543":
        best_column = 4
    elif state_string == "1424544":
        best_column = 5
    elif state_string == "1424545":
        best_column = 4
    elif state_string == "1424546":
        best_column = 4
    elif state_string == "1424547":
        best_column = 4
    elif state_string == "1424641":
        best_column = 4
    elif state_string == "1424642":
        best_column = 4
    elif state_string == "1424643":
        best_column = 4
    elif state_string == "1424644":
        best_column = 5
    elif state_string == "1424645":
        best_column = 4
    elif state_string == "1424646":
        best_column = 4
    elif state_string == "1424647":
        best_column = 4
    elif state_string == "1424741":
        best_column = 4
    elif state_string == "1424742":
        best_column = 4
    elif state_string == "1424743":
        best_column = 4
    elif state_string == "1424744":
        best_column = 5
    elif state_string == "1424745":
        best_column = 4
    elif state_string == "1424746":
        best_column = 4
    elif state_string == "1424747":
        best_column = 4
    elif state_string == "1434141":
        best_column = 4
    elif state_string == "1434142":
        best_column = 4
    elif state_string == "1434143":
        best_column = 4
    elif state_string == "1434144":
        best_column = 5
    elif state_string == "1434145":
        best_column = 4
    elif state_string == "1434146":
        best_column = 4
    elif state_string == "1434147":
        best_column = 4
    elif state_string == "1434241":
        best_column = 4
    elif state_string == "1434242":
        best_column = 4
    elif state_string == "1434243":
        best_column = 4
    elif state_string == "1434244":
        best_column = 5
    elif state_string == "1434245":
        best_column = 4
    elif state_string == "1434246":
        best_column = 4
    elif state_string == "1434247":
        best_column = 4
    elif state_string == "1434341":
        best_column = 4
    elif state_string == "1434342":
        best_column = 4
    elif state_string == "1434343":
        best_column = 4
    elif state_string == "1434344":
        best_column = 3
    elif state_string == "1434345":
        best_column = 4
    elif state_string == "1434346":
        best_column = 4
    elif state_string == "1434347":
        best_column = 4
    elif state_string == "1434431":
        best_column = 3
    elif state_string == "1434432":
        best_column = 4
    elif state_string == "1434433":
        best_column = 1
    elif state_string == "1434434":
        best_column = 1
    elif state_string == "1434435":
        best_column = 5
    elif state_string == "1434436":
        best_column = 4
    elif state_string == "1434437":
        best_column = 3
    elif state_string == "1434541":
        best_column = 4
    elif state_string == "1434542":
        best_column = 4
    elif state_string == "1434543":
        best_column = 4
    elif state_string == "1434544":
        best_column = 5
    elif state_string == "1434545":
        best_column = 4
    elif state_string == "1434546":
        best_column = 4
    elif state_string == "1434547":
        best_column = 4
    elif state_string == "1434641":
        best_column = 4
    elif state_string == "1434642":
        best_column = 4
    elif state_string == "1434643":
        best_column = 4
    elif state_string == "1434644":
        best_column = 6
    elif state_string == "1434645":
        best_column = 4
    elif state_string == "1434646":
        best_column = 4
    elif state_string == "1434647":
        best_column = 4
    elif state_string == "1434741":
        best_column = 4
    elif state_string == "1434742":
        best_column = 4
    elif state_string == "1434743":
        best_column = 4
    elif state_string == "1434744":
        best_column = 3
    elif state_string == "1434745":
        best_column = 4
    elif state_string == "1434746":
        best_column = 4
    elif state_string == "1434747":
        best_column = 4
    elif state_string == "1444141":
        best_column = 1
    elif state_string == "1444142":
        best_column = 4
    elif state_string == "1444143":
        best_column = 4
    elif state_string == "1444144":
        best_column = 5
    elif state_string == "1444145":
        best_column = 4
    elif state_string == "1444146":
        best_column = 4
    elif state_string == "1444147":
        best_column = 4
    elif state_string == "1444241":
        best_column = 4
    elif state_string == "1444242":
        best_column = 4
    elif state_string == "1444243":
        best_column = 4
    elif state_string == "1444244":
        best_column = 5
    elif state_string == "1444245":
        best_column = 4
    elif state_string == "1444246":
        best_column = 4
    elif state_string == "1444247":
        best_column = 4
    elif state_string == "1444331":
        best_column = 4
    elif state_string == "1444332":
        best_column = 4
    elif state_string == "1444333":
        best_column = 4
    elif state_string == "1444334":
        best_column = 3
    elif state_string == "1444335":
        best_column = 3
    elif state_string == "1444336":
        best_column = 3
    elif state_string == "1444337":
        best_column = 4
    elif state_string == "1444461":
        best_column = 5
    elif state_string == "1444462":
        best_column = 5
    elif state_string == "1444463":
        best_column = 5
    elif state_string == "1444464":
        best_column = 5
    elif state_string == "1444465":
        best_column = 5
    elif state_string == "1444466":
        best_column = 5
    elif state_string == "1444467":
        best_column = 5
    elif state_string == "1444541":
        best_column = 4
    elif state_string == "1444542":
        best_column = 4
    elif state_string == "1444543":
        best_column = 4
    elif state_string == "1444544":
        best_column = 5
    elif state_string == "1444545":
        best_column = 4
    elif state_string == "1444546":
        best_column = 4
    elif state_string == "1444547":
        best_column = 4
    elif state_string == "1444641":
        best_column = 4
    elif state_string == "1444642":
        best_column = 4
    elif state_string == "1444643":
        best_column = 4
    elif state_string == "1444644":
        best_column = 5
    elif state_string == "1444645":
        best_column = 4
    elif state_string == "1444646":
        best_column = 4
    elif state_string == "1444647":
        best_column = 4
    elif state_string == "1444741":
        best_column = 4
    elif state_string == "1444742":
        best_column = 4
    elif state_string == "1444743":
        best_column = 4
    elif state_string == "1444744":
        best_column = 5
    elif state_string == "1444745":
        best_column = 4
    elif state_string == "1444746":
        best_column = 4
    elif state_string == "1444747":
        best_column = 4
    elif state_string == "1454141":
        best_column = 4
    elif state_string == "1454142":
        best_column = 4
    elif state_string == "1454143":
        best_column = 4
    elif state_string == "1454144":
        best_column = 5
    elif state_string == "1454145":
        best_column = 4
    elif state_string == "1454146":
        best_column = 4
    elif state_string == "1454147":
        best_column = 4
    elif state_string == "1454241":
        best_column = 4
    elif state_string == "1454242":
        best_column = 4
    elif state_string == "1454243":
        best_column = 4
    elif state_string == "1454244":
        best_column = 5
    elif state_string == "1454245":
        best_column = 4
    elif state_string == "1454246":
        best_column = 4
    elif state_string == "1454247":
        best_column = 4
    elif state_string == "1454341":
        best_column = 4
    elif state_string == "1454342":
        best_column = 4
    elif state_string == "1454343":
        best_column = 4
    elif state_string == "1454344":
        best_column = 5
    elif state_string == "1454345":
        best_column = 4
    elif state_string == "1454346":
        best_column = 4
    elif state_string == "1454347":
        best_column = 4
    elif state_string == "1454451":
        best_column = 4
    elif state_string == "1454452":
        best_column = 4
    elif state_string == "1454453":
        best_column = 4
    elif state_string == "1454454":
        best_column = 5
    elif state_string == "1454455":
        best_column = 4
    elif state_string == "1454456":
        best_column = 6
    elif state_string == "1454457":
        best_column = 7
    elif state_string == "1454541":
        best_column = 4
    elif state_string == "1454542":
        best_column = 4
    elif state_string == "1454543":
        best_column = 4
    elif state_string == "1454544":
        best_column = 5
    elif state_string == "1454545":
        best_column = 4
    elif state_string == "1454546":
        best_column = 4
    elif state_string == "1454547":
        best_column = 4
    elif state_string == "1454641":
        best_column = 4
    elif state_string == "1454642":
        best_column = 4
    elif state_string == "1454643":
        best_column = 4
    elif state_string == "1454644":
        best_column = 5
    elif state_string == "1454645":
        best_column = 4
    elif state_string == "1454646":
        best_column = 4
    elif state_string == "1454647":
        best_column = 4
    elif state_string == "1454741":
        best_column = 4
    elif state_string == "1454742":
        best_column = 4
    elif state_string == "1454743":
        best_column = 4
    elif state_string == "1454744":
        best_column = 5
    elif state_string == "1454745":
        best_column = 4
    elif state_string == "1454746":
        best_column = 4
    elif state_string == "1454747":
        best_column = 4
    elif state_string == "1464151":
        best_column = 1
    elif state_string == "1464152":
        best_column = 4
    elif state_string == "1464153":
        best_column = 5
    elif state_string == "1464154":
        best_column = 5
    elif state_string == "1464155":
        best_column = 4
    elif state_string == "1464156":
        best_column = 3
    elif state_string == "1464157":
        best_column = 4
    elif state_string == "1464241":
        best_column = 4
    elif state_string == "1464242":
        best_column = 4
    elif state_string == "1464243":
        best_column = 4
    elif state_string == "1464244":
        best_column = 5
    elif state_string == "1464245":
        best_column = 4
    elif state_string == "1464246":
        best_column = 4
    elif state_string == "1464247":
        best_column = 4
    elif state_string == "1464341":
        best_column = 4
    elif state_string == "1464342":
        best_column = 4
    elif state_string == "1464343":
        best_column = 4
    elif state_string == "1464344":
        best_column = 6
    elif state_string == "1464345":
        best_column = 4
    elif state_string == "1464346":
        best_column = 4
    elif state_string == "1464347":
        best_column = 4
    elif state_string == "1464441":
        best_column = 4
    elif state_string == "1464442":
        best_column = 4
    elif state_string == "1464443":
        best_column = 4
    elif state_string == "1464444":
        best_column = 6
    elif state_string == "1464445":
        best_column = 4
    elif state_string == "1464446":
        best_column = 4
    elif state_string == "1464447":
        best_column = 4
    elif state_string == "1464541":
        best_column = 4
    elif state_string == "1464542":
        best_column = 4
    elif state_string == "1464543":
        best_column = 4
    elif state_string == "1464544":
        best_column = 5
    elif state_string == "1464545":
        best_column = 4
    elif state_string == "1464546":
        best_column = 4
    elif state_string == "1464547":
        best_column = 4
    elif state_string == "1464641":
        best_column = 4
    elif state_string == "1464642":
        best_column = 4
    elif state_string == "1464643":
        best_column = 4
    elif state_string == "1464644":
        best_column = 3
    elif state_string == "1464645":
        best_column = 4
    elif state_string == "1464646":
        best_column = 4
    elif state_string == "1464647":
        best_column = 4
    elif state_string == "1464741":
        best_column = 4
    elif state_string == "1464742":
        best_column = 4
    elif state_string == "1464743":
        best_column = 4
    elif state_string == "1464744":
        best_column = 3
    elif state_string == "1464745":
        best_column = 4
    elif state_string == "1464746":
        best_column = 4
    elif state_string == "1464747":
        best_column = 4
    elif state_string == "1473151":
        best_column = 2
    elif state_string == "1473152":
        best_column = 6
    elif state_string == "1473153":
        best_column = 2
    elif state_string == "1473154":
        best_column = 2
    elif state_string == "1473155":
        best_column = 2
    elif state_string == "1473156":
        best_column = 2
    elif state_string == "1473157":
        best_column = 2
    elif state_string == "1473241":
        best_column = 4
    elif state_string == "1473242":
        best_column = 4
    elif state_string == "1473243":
        best_column = 4
    elif state_string == "1473244":
        best_column = 3
    elif state_string == "1473245":
        best_column = 4
    elif state_string == "1473246":
        best_column = 4
    elif state_string == "1473247":
        best_column = 4
    elif state_string == "1473351":
        best_column = 6
    elif state_string == "1473352":
        best_column = 6
    elif state_string == "1473353":
        best_column = 6
    elif state_string == "1473354":
        best_column = 6
    elif state_string == "1473355":
        best_column = 6
    elif state_string == "1473356":
        best_column = 2
    elif state_string == "1473357":
        best_column = 6
    elif state_string == "1473451":
        best_column = 6
    elif state_string == "1473452":
        best_column = 6
    elif state_string == "1473453":
        best_column = 6
    elif state_string == "1473454":
        best_column = 6
    elif state_string == "1473455":
        best_column = 6
    elif state_string == "1473456":
        best_column = 2
    elif state_string == "1473457":
        best_column = 6
    elif state_string == "1473531":
        best_column = 3
    elif state_string == "1473532":
        best_column = 3
    elif state_string == "1473533":
        best_column = 4
    elif state_string == "1473534":
        best_column = 3
    elif state_string == "1473535":
        best_column = 5
    elif state_string == "1473536":
        best_column = 3
    elif state_string == "1473537":
        best_column = 3
    elif state_string == "1473641":
        best_column = 4
    elif state_string == "1473642":
        best_column = 4
    elif state_string == "1473643":
        best_column = 4
    elif state_string == "1473644":
        best_column = 3
    elif state_string == "1473645":
        best_column = 4
    elif state_string == "1473646":
        best_column = 4
    elif state_string == "1473647":
        best_column = 4
    elif state_string == "1473751":
        best_column = 6
    elif state_string == "1473752":
        best_column = 6
    elif state_string == "1473753":
        best_column = 6
    elif state_string == "1473754":
        best_column = 6
    elif state_string == "1473755":
        best_column = 6
    elif state_string == "1473756":
        best_column = 2
    elif state_string == "1473757":
        best_column = 6
    elif state_string == "2313133":
        best_column = 5
    elif state_string == "2313233":
        best_column = 5
    elif state_string == "2313331":
        best_column = 4
    elif state_string == "2313332":
        best_column = 2
    elif state_string == "2313333":
        best_column = 6
    elif state_string == "2313334":
        best_column = 4
    elif state_string == "2313335":
        best_column = 5
    elif state_string == "2313336":
        best_column = 5
    elif state_string == "2313337":
        best_column = 4
    elif state_string == "2313433":
        best_column = 4
    elif state_string == "2313533":
        best_column = 5
    elif state_string == "2313633":
        best_column = 2
    elif state_string == "2313733":
        best_column = 5
    elif state_string == "2322131":
        best_column = 3
    elif state_string == "2322132":
        best_column = 3
    elif state_string == "2322133":
        best_column = 3
    elif state_string == "2322134":
        best_column = 4
    elif state_string == "2322135":
        best_column = 3
    elif state_string == "2322136":
        best_column = 3
    elif state_string == "2322137":
        best_column = 3
    elif state_string == "2322231":
        best_column = 4
    elif state_string == "2322232":
        best_column = 4
    elif state_string == "2322233":
        best_column = 4
    elif state_string == "2322234":
        best_column = 4
    elif state_string == "2322235":
        best_column = 3
    elif state_string == "2322236":
        best_column = 3
    elif state_string == "2322237":
        best_column = 4
    elif state_string == "2322331":
        best_column = 2
    elif state_string == "2322332":
        best_column = 4
    elif state_string == "2322333":
        best_column = 3
    elif state_string == "2322334":
        best_column = 4
    elif state_string == "2322335":
        best_column = 3
    elif state_string == "2322336":
        best_column = 4
    elif state_string == "2322337":
        best_column = 4
    elif state_string == "2322441":
        best_column = 2
    elif state_string == "2322442":
        best_column = 4
    elif state_string == "2322443":
        best_column = 4
    elif state_string == "2322444":
        best_column = 4
    elif state_string == "2322445":
        best_column = 4
    elif state_string == "2322446":
        best_column = 4
    elif state_string == "2322447":
        best_column = 4
    elif state_string == "2322531":
        best_column = 3
    elif state_string == "2322532":
        best_column = 3
    elif state_string == "2322533":
        best_column = 5
    elif state_string == "2322534":
        best_column = 5
    elif state_string == "2322535":
        best_column = 3
    elif state_string == "2322536":
        best_column = 3
    elif state_string == "2322537":
        best_column = 3
    elif state_string == "2322661":
        best_column = 3
    elif state_string == "2322662":
        best_column = 3
    elif state_string == "2322663":
        best_column = 6
    elif state_string == "2322664":
        best_column = 4
    elif state_string == "2322665":
        best_column = 6
    elif state_string == "2322666":
        best_column = 3
    elif state_string == "2322667":
        best_column = 4
    elif state_string == "2322741":
        best_column = 4
    elif state_string == "2322742":
        best_column = 4
    elif state_string == "2322743":
        best_column = 4
    elif state_string == "2322744":
        best_column = 3
    elif state_string == "2322745":
        best_column = 3
    elif state_string == "2322746":
        best_column = 4
    elif state_string == "2322747":
        best_column = 4
    elif state_string == "2333131":
        best_column = 4
    elif state_string == "2333132":
        best_column = 4
    elif state_string == "2333133":
        best_column = 4
    elif state_string == "2333134":
        best_column = 4
    elif state_string == "2333135":
        best_column = 5
    elif state_string == "2333136":
        best_column = 6
    elif state_string == "2333137":
        best_column = 4
    elif state_string == "2333231":
        best_column = 4
    elif state_string == "2333232":
        best_column = 2
    elif state_string == "2333233":
        best_column = 4
    elif state_string == "2333234":
        best_column = 4
    elif state_string == "2333235":
        best_column = 5
    elif state_string == "2333236":
        best_column = 6
    elif state_string == "2333237":
        best_column = 4
    elif state_string == "2333321":
        best_column = 2
    elif state_string == "2333322":
        best_column = 4
    elif state_string == "2333323":
        best_column = 2
    elif state_string == "2333324":
        best_column = 4
    elif state_string == "2333325":
        best_column = 5
    elif state_string == "2333326":
        best_column = 6
    elif state_string == "2333327":
        best_column = 4
    elif state_string == "2333441":
        best_column = 4
    elif state_string == "2333442":
        best_column = 4
    elif state_string == "2333443":
        best_column = 4
    elif state_string == "2333444":
        best_column = 4
    elif state_string == "2333445":
        best_column = 4
    elif state_string == "2333446":
        best_column = 4
    elif state_string == "2333447":
        best_column = 4
    elif state_string == "2333531":
        best_column = 5
    elif state_string == "2333532":
        best_column = 5
    elif state_string == "2333533":
        best_column = 5
    elif state_string == "2333534":
        best_column = 4
    elif state_string == "2333535":
        best_column = 4
    elif state_string == "2333536":
        best_column = 4
    elif state_string == "2333537":
        best_column = 5
    elif state_string == "2333631":
        best_column = 3
    elif state_string == "2333632":
        best_column = 6
    elif state_string == "2333633":
        best_column = 4
    elif state_string == "2333634":
        best_column = 4
    elif state_string == "2333635":
        best_column = 4
    elif state_string == "2333636":
        best_column = 4
    elif state_string == "2333637":
        best_column = 4
    elif state_string == "2333731":
        best_column = 4
    elif state_string == "2333732":
        best_column = 4
    elif state_string == "2333733":
        best_column = 4
    elif state_string == "2333734":
        best_column = 6
    elif state_string == "2333735":
        best_column = 5
    elif state_string == "2333736":
        best_column = 4
    elif state_string == "2333737":
        best_column = 4
    elif state_string == "2344141":
        best_column = 4
    elif state_string == "2344142":
        best_column = 4
    elif state_string == "2344143":
        best_column = 4
    elif state_string == "2344144":
        best_column = 2
    elif state_string == "2344145":
        best_column = 4
    elif state_string == "2344146":
        best_column = 4
    elif state_string == "2344147":
        best_column = 4
    elif state_string == "2344241":
        best_column = 4
    elif state_string == "2344242":
        best_column = 2
    elif state_string == "2344243":
        best_column = 4
    elif state_string == "2344244":
        best_column = 1
    elif state_string == "2344245":
        best_column = 4
    elif state_string == "2344246":
        best_column = 4
    elif state_string == "2344247":
        best_column = 4
    elif state_string == "2344341":
        best_column = 4
    elif state_string == "2344342":
        best_column = 4
    elif state_string == "2344343":
        best_column = 4
    elif state_string == "2344344":
        best_column = 3
    elif state_string == "2344345":
        best_column = 4
    elif state_string == "2344346":
        best_column = 4
    elif state_string == "2344347":
        best_column = 4
    elif state_string == "2344431":
        best_column = 4
    elif state_string == "2344432":
        best_column = 3
    elif state_string == "2344433":
        best_column = 2
    elif state_string == "2344434":
        best_column = 3
    elif state_string == "2344435":
        best_column = 2
    elif state_string == "2344436":
        best_column = 2
    elif state_string == "2344437":
        best_column = 2
    elif state_string == "2344541":
        best_column = 4
    elif state_string == "2344542":
        best_column = 4
    elif state_string == "2344543":
        best_column = 4
    elif state_string == "2344544":
        best_column = 3
    elif state_string == "2344545":
        best_column = 4
    elif state_string == "2344546":
        best_column = 7
    elif state_string == "2344547":
        best_column = 6
    elif state_string == "2344641":
        best_column = 4
    elif state_string == "2344642":
        best_column = 4
    elif state_string == "2344643":
        best_column = 4
    elif state_string == "2344644":
        best_column = 5
    elif state_string == "2344645":
        best_column = 7
    elif state_string == "2344646":
        best_column = 4
    elif state_string == "2344647":
        best_column = 5
    elif state_string == "2344741":
        best_column = 4
    elif state_string == "2344742":
        best_column = 4
    elif state_string == "2344743":
        best_column = 4
    elif state_string == "2344744":
        best_column = 6
    elif state_string == "2344745":
        best_column = 6
    elif state_string == "2344746":
        best_column = 5
    elif state_string == "2344747":
        best_column = 5
    elif state_string == "2353131":
        best_column = 3
    elif state_string == "2353132":
        best_column = 3
    elif state_string == "2353133":
        best_column = 5
    elif state_string == "2353134":
        best_column = 3
    elif state_string == "2353135":
        best_column = 3
    elif state_string == "2353136":
        best_column = 3
    elif state_string == "2353137":
        best_column = 3
    elif state_string == "2353231":
        best_column = 3
    elif state_string == "2353232":
        best_column = 3
    elif state_string == "2353233":
        best_column = 5
    elif state_string == "2353234":
        best_column = 3
    elif state_string == "2353235":
        best_column = 3
    elif state_string == "2353236":
        best_column = 3
    elif state_string == "2353237":
        best_column = 3
    elif state_string == "2353351":
        best_column = 5
    elif state_string == "2353352":
        best_column = 2
    elif state_string == "2353353":
        best_column = 2
    elif state_string == "2353354":
        best_column = 4
    elif state_string == "2353355":
        best_column = 6
    elif state_string == "2353356":
        best_column = 7
    elif state_string == "2353357":
        best_column = 6
    elif state_string == "2353441":
        best_column = 2
    elif state_string == "2353442":
        best_column = 4
    elif state_string == "2353443":
        best_column = 2
    elif state_string == "2353444":
        best_column = 2
    elif state_string == "2353445":
        best_column = 5
    elif state_string == "2353446":
        best_column = 7
    elif state_string == "2353447":
        best_column = 6
    elif state_string == "2353551":
        best_column = 3
    elif state_string == "2353552":
        best_column = 2
    elif state_string == "2353553":
        best_column = 3
    elif state_string == "2353554":
        best_column = 4
    elif state_string == "2353555":
        best_column = 3
    elif state_string == "2353556":
        best_column = 7
    elif state_string == "2353557":
        best_column = 3
    elif state_string == "2353651":
        best_column = 4
    elif state_string == "2353652":
        best_column = 3
    elif state_string == "2353653":
        best_column = 7
    elif state_string == "2353654":
        best_column = 7
    elif state_string == "2353655":
        best_column = 3
    elif state_string == "2353656":
        best_column = 3
    elif state_string == "2353657":
        best_column = 4
    elif state_string == "2353751":
        best_column = 4
    elif state_string == "2353752":
        best_column = 3
    elif state_string == "2353753":
        best_column = 6
    elif state_string == "2353754":
        best_column = 6
    elif state_string == "2353755":
        best_column = 6
    elif state_string == "2353756":
        best_column = 4
    elif state_string == "2353757":
        best_column = 4
    elif state_string == "2363131":
        best_column = 3
    elif state_string == "2363132":
        best_column = 3
    elif state_string == "2363133":
        best_column = 2
    elif state_string == "2363134":
        best_column = 3
    elif state_string == "2363135":
        best_column = 3
    elif state_string == "2363136":
        best_column = 3
    elif state_string == "2363137":
        best_column = 3
    elif state_string == "2363231":
        best_column = 3
    elif state_string == "2363232":
        best_column = 3
    elif state_string == "2363233":
        best_column = 2
    elif state_string == "2363234":
        best_column = 3
    elif state_string == "2363235":
        best_column = 3
    elif state_string == "2363236":
        best_column = 3
    elif state_string == "2363237":
        best_column = 3
    elif state_string == "2363331":
        best_column = 2
    elif state_string == "2363332":
        best_column = 2
    elif state_string == "2363333":
        best_column = 2
    elif state_string == "2363334":
        best_column = 4
    elif state_string == "2363335":
        best_column = 7
    elif state_string == "2363336":
        best_column = 6
    elif state_string == "2363337":
        best_column = 5
    elif state_string == "2363441":
        best_column = 3
    elif state_string == "2363442":
        best_column = 4
    elif state_string == "2363443":
        best_column = 4
    elif state_string == "2363444":
        best_column = 2
    elif state_string == "2363445":
        best_column = 7
    elif state_string == "2363446":
        best_column = 3
    elif state_string == "2363447":
        best_column = 5
    elif state_string == "2363531":
        best_column = 3
    elif state_string == "2363532":
        best_column = 3
    elif state_string == "2363533":
        best_column = 5
    elif state_string == "2363534":
        best_column = 3
    elif state_string == "2363535":
        best_column = 3
    elif state_string == "2363536":
        best_column = 3
    elif state_string == "2363537":
        best_column = 3
    elif state_string == "2363661":
        best_column = 3
    elif state_string == "2363662":
        best_column = 3
    elif state_string == "2363663":
        best_column = 3
    elif state_string == "2363664":
        best_column = 4
    elif state_string == "2363665":
        best_column = 3
    elif state_string == "2363666":
        best_column = 3
    elif state_string == "2363667":
        best_column = 4
    elif state_string == "2363741":
        best_column = 4
    elif state_string == "2363742":
        best_column = 3
    elif state_string == "2363743":
        best_column = 4
    elif state_string == "2363744":
        best_column = 4
    elif state_string == "2363745":
        best_column = 4
    elif state_string == "2363746":
        best_column = 3
    elif state_string == "2363747":
        best_column = 3
    elif state_string == "2373131":
        best_column = 3
    elif state_string == "2373132":
        best_column = 3
    elif state_string == "2373133":
        best_column = 5
    elif state_string == "2373134":
        best_column = 3
    elif state_string == "2373135":
        best_column = 3
    elif state_string == "2373136":
        best_column = 3
    elif state_string == "2373137":
        best_column = 3
    elif state_string == "2373231":
        best_column = 3
    elif state_string == "2373232":
        best_column = 3
    elif state_string == "2373233":
        best_column = 2
    elif state_string == "2373234":
        best_column = 3
    elif state_string == "2373235":
        best_column = 3
    elif state_string == "2373236":
        best_column = 3
    elif state_string == "2373237":
        best_column = 3
    elif state_string == "2373331":
        best_column = 4
    elif state_string == "2373332":
        best_column = 2
    elif state_string == "2373333":
        best_column = 2
    elif state_string == "2373334":
        best_column = 4
    elif state_string == "2373335":
        best_column = 6
    elif state_string == "2373336":
        best_column = 5
    elif state_string == "2373337":
        best_column = 4
    elif state_string == "2373441":
        best_column = 3
    elif state_string == "2373442":
        best_column = 3
    elif state_string == "2373443":
        best_column = 2
    elif state_string == "2373444":
        best_column = 2
    elif state_string == "2373445":
        best_column = 6
    elif state_string == "2373446":
        best_column = 5
    elif state_string == "2373447":
        best_column = 3
    elif state_string == "2373551":
        best_column = 4
    elif state_string == "2373552":
        best_column = 3
    elif state_string == "2373553":
        best_column = 6
    elif state_string == "2373554":
        best_column = 6
    elif state_string == "2373555":
        best_column = 3
    elif state_string == "2373556":
        best_column = 4
    elif state_string == "2373557":
        best_column = 3
    elif state_string == "2373641":
        best_column = 4
    elif state_string == "2373642":
        best_column = 3
    elif state_string == "2373643":
        best_column = 4
    elif state_string == "2373644":
        best_column = 4
    elif state_string == "2373645":
        best_column = 4
    elif state_string == "2373646":
        best_column = 3
    elif state_string == "2373647":
        best_column = 3
    elif state_string == "2373731":
        best_column = 3
    elif state_string == "2373732":
        best_column = 3
    elif state_string == "2373733":
        best_column = 5
    elif state_string == "2373734":
        best_column = 3
    elif state_string == "2373735":
        best_column = 3
    elif state_string == "2373736":
        best_column = 3
    elif state_string == "2373737":
        best_column = 3
    elif state_string == "3414141":
        best_column = 4
    elif state_string == "3414142":
        best_column = 4
    elif state_string == "3414143":
        best_column = 4
    elif state_string == "3414144":
        best_column = 5
    elif state_string == "3414145":
        best_column = 4
    elif state_string == "3414146":
        best_column = 4
    elif state_string == "3414147":
        best_column = 4
    elif state_string == "3414241":
        best_column = 4
    elif state_string == "3414242":
        best_column = 4
    elif state_string == "3414243":
        best_column = 4
    elif state_string == "3414244":
        best_column = 5
    elif state_string == "3414245":
        best_column = 4
    elif state_string == "3414246":
        best_column = 4
    elif state_string == "3414247":
        best_column = 4
    elif state_string == "3414341":
        best_column = 4
    elif state_string == "3414342":
        best_column = 4
    elif state_string == "3414343":
        best_column = 4
    elif state_string == "3414344":
        best_column = 3
    elif state_string == "3414345":
        best_column = 4
    elif state_string == "3414346":
        best_column = 4
    elif state_string == "3414347":
        best_column = 4
    elif state_string == "3414431":
        best_column = 3
    elif state_string == "3414432":
        best_column = 3
    elif state_string == "3414433":
        best_column = 1
    elif state_string == "3414434":
        best_column = 1
    elif state_string == "3414435":
        best_column = 5
    elif state_string == "3414436":
        best_column = 6
    elif state_string == "3414437":
        best_column = 3
    elif state_string == "3414541":
        best_column = 4
    elif state_string == "3414542":
        best_column = 4
    elif state_string == "3414543":
        best_column = 4
    elif state_string == "3414544":
        best_column = 5
    elif state_string == "3414545":
        best_column = 4
    elif state_string == "3414546":
        best_column = 4
    elif state_string == "3414547":
        best_column = 4
    elif state_string == "3414641":
        best_column = 4
    elif state_string == "3414642":
        best_column = 4
    elif state_string == "3414643":
        best_column = 4
    elif state_string == "3414644":
        best_column = 6
    elif state_string == "3414645":
        best_column = 4
    elif state_string == "3414646":
        best_column = 4
    elif state_string == "3414647":
        best_column = 4
    elif state_string == "3414741":
        best_column = 4
    elif state_string == "3414742":
        best_column = 4
    elif state_string == "3414743":
        best_column = 4
    elif state_string == "3414744":
        best_column = 3
    elif state_string == "3414745":
        best_column = 4
    elif state_string == "3414746":
        best_column = 4
    elif state_string == "3414747":
        best_column = 4
    elif state_string == "3424141":
        best_column = 4
    elif state_string == "3424142":
        best_column = 4
    elif state_string == "3424143":
        best_column = 4
    elif state_string == "3424144":
        best_column = 5
    elif state_string == "3424145":
        best_column = 4
    elif state_string == "3424146":
        best_column = 4
    elif state_string == "3424147":
        best_column = 4
    elif state_string == "3424241":
        best_column = 4
    elif state_string == "3424242":
        best_column = 4
    elif state_string == "3424243":
        best_column = 4
    elif state_string == "3424244":
        best_column = 2
    elif state_string == "3424245":
        best_column = 4
    elif state_string == "3424246":
        best_column = 4
    elif state_string == "3424247":
        best_column = 4
    elif state_string == "3424341":
        best_column = 4
    elif state_string == "3424342":
        best_column = 4
    elif state_string == "3424343":
        best_column = 4
    elif state_string == "3424344":
        best_column = 3
    elif state_string == "3424345":
        best_column = 4
    elif state_string == "3424346":
        best_column = 4
    elif state_string == "3424347":
        best_column = 4
    elif state_string == "3424441":
        best_column = 3
    elif state_string == "3424442":
        best_column = 2
    elif state_string == "3424443":
        best_column = 3
    elif state_string == "3424444":
        best_column = 3
    elif state_string == "3424445":
        best_column = 3
    elif state_string == "3424446":
        best_column = 3
    elif state_string == "3424447":
        best_column = 3
    elif state_string == "3424541":
        best_column = 4
    elif state_string == "3424542":
        best_column = 4
    elif state_string == "3424543":
        best_column = 4
    elif state_string == "3424544":
        best_column = 5
    elif state_string == "3424545":
        best_column = 4
    elif state_string == "3424546":
        best_column = 4
    elif state_string == "3424547":
        best_column = 4
    elif state_string == "3424641":
        best_column = 4
    elif state_string == "3424642":
        best_column = 4
    elif state_string == "3424643":
        best_column = 4
    elif state_string == "3424644":
        best_column = 3
    elif state_string == "3424645":
        best_column = 4
    elif state_string == "3424646":
        best_column = 4
    elif state_string == "3424647":
        best_column = 4
    elif state_string == "3424741":
        best_column = 4
    elif state_string == "3424742":
        best_column = 4
    elif state_string == "3424743":
        best_column = 4
    elif state_string == "3424744":
        best_column = 3
    elif state_string == "3424745":
        best_column = 4
    elif state_string == "3424746":
        best_column = 4
    elif state_string == "3424747":
        best_column = 4
    elif state_string == "3433141":
        best_column = 4
    elif state_string == "3433142":
        best_column = 4
    elif state_string == "3433143":
        best_column = 4
    elif state_string == "3433144":
        best_column = 3
    elif state_string == "3433145":
        best_column = 4
    elif state_string == "3433146":
        best_column = 4
    elif state_string == "3433147":
        best_column = 4
    elif state_string == "3433241":
        best_column = 4
    elif state_string == "3433242":
        best_column = 4
    elif state_string == "3433243":
        best_column = 4
    elif state_string == "3433244":
        best_column = 4
    elif state_string == "3433245":
        best_column = 4
    elif state_string == "3433246":
        best_column = 4
    elif state_string == "3433247":
        best_column = 4
    elif state_string == "3433341":
        best_column = 4
    elif state_string == "3433342":
        best_column = 4
    elif state_string == "3433343":
        best_column = 4
    elif state_string == "3433344":
        best_column = 4
    elif state_string == "3433345":
        best_column = 4
    elif state_string == "3433346":
        best_column = 4
    elif state_string == "3433347":
        best_column = 4
    elif state_string == "3433441":
        best_column = 3
    elif state_string == "3433442":
        best_column = 4
    elif state_string == "3433443":
        best_column = 4
    elif state_string == "3433444":
        best_column = 4
    elif state_string == "3433445":
        best_column = 4
    elif state_string == "3433446":
        best_column = 4
    elif state_string == "3433447":
        best_column = 4
    elif state_string == "3433541":
        best_column = 4
    elif state_string == "3433542":
        best_column = 4
    elif state_string == "3433543":
        best_column = 4
    elif state_string == "3433544":
        best_column = 4
    elif state_string == "3433545":
        best_column = 4
    elif state_string == "3433546":
        best_column = 4
    elif state_string == "3433547":
        best_column = 4
    elif state_string == "3433641":
        best_column = 4
    elif state_string == "3433642":
        best_column = 4
    elif state_string == "3433643":
        best_column = 4
    elif state_string == "3433644":
        best_column = 4
    elif state_string == "3433645":
        best_column = 4
    elif state_string == "3433646":
        best_column = 4
    elif state_string == "3433647":
        best_column = 4
    elif state_string == "3433741":
        best_column = 4
    elif state_string == "3433742":
        best_column = 4
    elif state_string == "3433743":
        best_column = 4
    elif state_string == "3433744":
        best_column = 4
    elif state_string == "3433745":
        best_column = 4
    elif state_string == "3433746":
        best_column = 4
    elif state_string == "3433747":
        best_column = 4
    elif state_string == "3444131":
        best_column = 4
    elif state_string == "3444132":
        best_column = 4
    elif state_string == "3444133":
        best_column = 4
    elif state_string == "3444134":
        best_column = 3
    elif state_string == "3444135":
        best_column = 3
    elif state_string == "3444136":
        best_column = 3
    elif state_string == "3444137":
        best_column = 4
    elif state_string == "3444241":
        best_column = 4
    elif state_string == "3444242":
        best_column = 4
    elif state_string == "3444243":
        best_column = 4
    elif state_string == "3444244":
        best_column = 3
    elif state_string == "3444245":
        best_column = 4
    elif state_string == "3444246":
        best_column = 4
    elif state_string == "3444247":
        best_column = 4
    elif state_string == "3444341":
        best_column = 4
    elif state_string == "3444342":
        best_column = 4
    elif state_string == "3444343":
        best_column = 3
    elif state_string == "3444344":
        best_column = 1
    elif state_string == "3444345":
        best_column = 5
    elif state_string == "3444346":
        best_column = 3
    elif state_string == "3444347":
        best_column = 4
    elif state_string == "3444431":
        best_column = 3
    elif state_string == "3444432":
        best_column = 4
    elif state_string == "3444433":
        best_column = 4
    elif state_string == "3444434":
        best_column = 3
    elif state_string == "3444435":
        best_column = 3
    elif state_string == "3444436":
        best_column = 3
    elif state_string == "3444437":
        best_column = 3
    elif state_string == "3444541":
        best_column = 4
    elif state_string == "3444542":
        best_column = 4
    elif state_string == "3444543":
        best_column = 4
    elif state_string == "3444544":
        best_column = 3
    elif state_string == "3444545":
        best_column = 4
    elif state_string == "3444546":
        best_column = 4
    elif state_string == "3444547":
        best_column = 4
    elif state_string == "3444641":
        best_column = 4
    elif state_string == "3444642":
        best_column = 4
    elif state_string == "3444643":
        best_column = 3
    elif state_string == "3444644":
        best_column = 3
    elif state_string == "3444645":
        best_column = 3
    elif state_string == "3444646":
        best_column = 3
    elif state_string == "3444647":
        best_column = 3
    elif state_string == "3444741":
        best_column = 4
    elif state_string == "3444742":
        best_column = 4
    elif state_string == "3444743":
        best_column = 4
    elif state_string == "3444744":
        best_column = 3
    elif state_string == "3444745":
        best_column = 5
    elif state_string == "3444746":
        best_column = 4
    elif state_string == "3444747":
        best_column = 4
    elif state_string == "3454141":
        best_column = 4
    elif state_string == "3454142":
        best_column = 4
    elif state_string == "3454143":
        best_column = 4
    elif state_string == "3454144":
        best_column = 5
    elif state_string == "3454145":
        best_column = 4
    elif state_string == "3454146":
        best_column = 4
    elif state_string == "3454147":
        best_column = 4
    elif state_string == "3454241":
        best_column = 4
    elif state_string == "3454242":
        best_column = 4
    elif state_string == "3454243":
        best_column = 4
    elif state_string == "3454244":
        best_column = 5
    elif state_string == "3454245":
        best_column = 4
    elif state_string == "3454246":
        best_column = 4
    elif state_string == "3454247":
        best_column = 4
    elif state_string == "3454341":
        best_column = 4
    elif state_string == "3454342":
        best_column = 4
    elif state_string == "3454343":
        best_column = 4
    elif state_string == "3454344":
        best_column = 3
    elif state_string == "3454345":
        best_column = 4
    elif state_string == "3454346":
        best_column = 4
    elif state_string == "3454347":
        best_column = 4
    elif state_string == "3454441":
        best_column = 3
    elif state_string == "3454442":
        best_column = 3
    elif state_string == "3454443":
        best_column = 3
    elif state_string == "3454444":
        best_column = 3
    elif state_string == "3454445":
        best_column = 5
    elif state_string == "3454446":
        best_column = 5
    elif state_string == "3454447":
        best_column = 3
    elif state_string == "3454541":
        best_column = 4
    elif state_string == "3454542":
        best_column = 4
    elif state_string == "3454543":
        best_column = 4
    elif state_string == "3454544":
        best_column = 5
    elif state_string == "3454545":
        best_column = 4
    elif state_string == "3454546":
        best_column = 4
    elif state_string == "3454547":
        best_column = 4
    elif state_string == "3454641":
        best_column = 4
    elif state_string == "3454642":
        best_column = 4
    elif state_string == "3454643":
        best_column = 4
    elif state_string == "3454644":
        best_column = 3
    elif state_string == "3454645":
        best_column = 4
    elif state_string == "3454646":
        best_column = 4
    elif state_string == "3454647":
        best_column = 4
    elif state_string == "3454741":
        best_column = 4
    elif state_string == "3454742":
        best_column = 4
    elif state_string == "3454743":
        best_column = 4
    elif state_string == "3454744":
        best_column = 3
    elif state_string == "3454745":
        best_column = 4
    elif state_string == "3454746":
        best_column = 4
    elif state_string == "3454747":
        best_column = 4
    elif state_string == "3464141":
        best_column = 4
    elif state_string == "3464142":
        best_column = 4
    elif state_string == "3464143":
        best_column = 4
    elif state_string == "3464144":
        best_column = 6
    elif state_string == "3464145":
        best_column = 5
    elif state_string == "3464146":
        best_column = 6
    elif state_string == "3464147":
        best_column = 7
    elif state_string == "3464241":
        best_column = 4
    elif state_string == "3464242":
        best_column = 4
    elif state_string == "3464243":
        best_column = 4
    elif state_string == "3464244":
        best_column = 3
    elif state_string == "3464245":
        best_column = 4
    elif state_string == "3464246":
        best_column = 4
    elif state_string == "3464247":
        best_column = 4
    elif state_string == "3464341":
        best_column = 4
    elif state_string == "3464342":
        best_column = 4
    elif state_string == "3464343":
        best_column = 4
    elif state_string == "3464344":
        best_column = 3
    elif state_string == "3464345":
        best_column = 4
    elif state_string == "3464346":
        best_column = 4
    elif state_string == "3464347":
        best_column = 4
    elif state_string == "3464441":
        best_column = 3
    elif state_string == "3464442":
        best_column = 3
    elif state_string == "3464443":
        best_column = 3
    elif state_string == "3464444":
        best_column = 3
    elif state_string == "3464445":
        best_column = 5
    elif state_string == "3464446":
        best_column = 6
    elif state_string == "3464447":
        best_column = 3
    elif state_string == "3464541":
        best_column = 4
    elif state_string == "3464542":
        best_column = 4
    elif state_string == "3464543":
        best_column = 4
    elif state_string == "3464544":
        best_column = 3
    elif state_string == "3464545":
        best_column = 4
    elif state_string == "3464546":
        best_column = 4
    elif state_string == "3464547":
        best_column = 4
    elif state_string == "3464641":
        best_column = 4
    elif state_string == "3464642":
        best_column = 4
    elif state_string == "3464643":
        best_column = 4
    elif state_string == "3464644":
        best_column = 6
    elif state_string == "3464645":
        best_column = 4
    elif state_string == "3464646":
        best_column = 4
    elif state_string == "3464647":
        best_column = 4
    elif state_string == "3464741":
        best_column = 4
    elif state_string == "3464742":
        best_column = 4
    elif state_string == "3464743":
        best_column = 4
    elif state_string == "3464744":
        best_column = 3
    elif state_string == "3464745":
        best_column = 4
    elif state_string == "3464746":
        best_column = 4
    elif state_string == "3464747":
        best_column = 4
    elif state_string == "3474141":
        best_column = 4
    elif state_string == "3474142":
        best_column = 4
    elif state_string == "3474143":
        best_column = 4
    elif state_string == "3474144":
        best_column = 3
    elif state_string == "3474145":
        best_column = 4
    elif state_string == "3474146":
        best_column = 4
    elif state_string == "3474147":
        best_column = 4
    elif state_string == "3474241":
        best_column = 4
    elif state_string == "3474242":
        best_column = 4
    elif state_string == "3474243":
        best_column = 4
    elif state_string == "3474244":
        best_column = 3
    elif state_string == "3474245":
        best_column = 4
    elif state_string == "3474246":
        best_column = 4
    elif state_string == "3474247":
        best_column = 4
    elif state_string == "3474341":
        best_column = 4
    elif state_string == "3474342":
        best_column = 4
    elif state_string == "3474343":
        best_column = 4
    elif state_string == "3474344":
        best_column = 3
    elif state_string == "3474345":
        best_column = 4
    elif state_string == "3474346":
        best_column = 4
    elif state_string == "3474347":
        best_column = 4
    elif state_string == "3474431":
        best_column = 3
    elif state_string == "3474432":
        best_column = 3
    elif state_string == "3474433":
        best_column = 3
    elif state_string == "3474434":
        best_column = 4
    elif state_string == "3474435":
        best_column = 5
    elif state_string == "3474436":
        best_column = 6
    elif state_string == "3474437":
        best_column = 4
    elif state_string == "3474541":
        best_column = 4
    elif state_string == "3474542":
        best_column = 4
    elif state_string == "3474543":
        best_column = 4
    elif state_string == "3474544":
        best_column = 3
    elif state_string == "3474545":
        best_column = 4
    elif state_string == "3474546":
        best_column = 4
    elif state_string == "3474547":
        best_column = 4
    elif state_string == "3474641":
        best_column = 4
    elif state_string == "3474642":
        best_column = 4
    elif state_string == "3474643":
        best_column = 4
    elif state_string == "3474644":
        best_column = 3
    elif state_string == "3474645":
        best_column = 4
    elif state_string == "3474646":
        best_column = 4
    elif state_string == "3474647":
        best_column = 4
    elif state_string == "3474741":
        best_column = 4
    elif state_string == "3474742":
        best_column = 4
    elif state_string == "3474743":
        best_column = 4
    elif state_string == "3474744":
        best_column = 3
    elif state_string == "3474745":
        best_column = 4
    elif state_string == "3474746":
        best_column = 4
    elif state_string == "3474747":
        best_column = 4
    elif state_string == "5414141":
        best_column = 4
    elif state_string == "5414142":
        best_column = 4
    elif state_string == "5414143":
        best_column = 4
    elif state_string == "5414144":
        best_column = 5
    elif state_string == "5414145":
        best_column = 4
    elif state_string == "5414146":
        best_column = 4
    elif state_string == "5414147":
        best_column = 4
    elif state_string == "5414241":
        best_column = 4
    elif state_string == "5414242":
        best_column = 4
    elif state_string == "5414243":
        best_column = 4
    elif state_string == "5414244":
        best_column = 5
    elif state_string == "5414245":
        best_column = 4
    elif state_string == "5414246":
        best_column = 4
    elif state_string == "5414247":
        best_column = 4
    elif state_string == "5414341":
        best_column = 4
    elif state_string == "5414342":
        best_column = 4
    elif state_string == "5414343":
        best_column = 4
    elif state_string == "5414344":
        best_column = 5
    elif state_string == "5414345":
        best_column = 4
    elif state_string == "5414346":
        best_column = 4
    elif state_string == "5414347":
        best_column = 4
    elif state_string == "5414451":
        best_column = 5
    elif state_string == "5414452":
        best_column = 4
    elif state_string == "5414453":
        best_column = 3
    elif state_string == "5414454":
        best_column = 5
    elif state_string == "5414455":
        best_column = 4
    elif state_string == "5414456":
        best_column = 5
    elif state_string == "5414457":
        best_column = 5
    elif state_string == "5414541":
        best_column = 4
    elif state_string == "5414542":
        best_column = 4
    elif state_string == "5414543":
        best_column = 4
    elif state_string == "5414544":
        best_column = 5
    elif state_string == "5414545":
        best_column = 4
    elif state_string == "5414546":
        best_column = 4
    elif state_string == "5414547":
        best_column = 4
    elif state_string == "5414641":
        best_column = 4
    elif state_string == "5414642":
        best_column = 4
    elif state_string == "5414643":
        best_column = 4
    elif state_string == "5414644":
        best_column = 5
    elif state_string == "5414645":
        best_column = 4
    elif state_string == "5414646":
        best_column = 4
    elif state_string == "5414647":
        best_column = 4
    elif state_string == "5414741":
        best_column = 4
    elif state_string == "5414742":
        best_column = 4
    elif state_string == "5414743":
        best_column = 4
    elif state_string == "5414744":
        best_column = 5
    elif state_string == "5414745":
        best_column = 4
    elif state_string == "5414746":
        best_column = 4
    elif state_string == "5414747":
        best_column = 4
    elif state_string == "5424141":
        best_column = 4
    elif state_string == "5424142":
        best_column = 4
    elif state_string == "5424143":
        best_column = 4
    elif state_string == "5424144":
        best_column = 5
    elif state_string == "5424145":
        best_column = 4
    elif state_string == "5424146":
        best_column = 4
    elif state_string == "5424147":
        best_column = 4
    elif state_string == "5424241":
        best_column = 4
    elif state_string == "5424242":
        best_column = 4
    elif state_string == "5424243":
        best_column = 4
    elif state_string == "5424244":
        best_column = 2
    elif state_string == "5424245":
        best_column = 4
    elif state_string == "5424246":
        best_column = 4
    elif state_string == "5424247":
        best_column = 4
    elif state_string == "5424341":
        best_column = 4
    elif state_string == "5424342":
        best_column = 4
    elif state_string == "5424343":
        best_column = 4
    elif state_string == "5424344":
        best_column = 5
    elif state_string == "5424345":
        best_column = 4
    elif state_string == "5424346":
        best_column = 4
    elif state_string == "5424347":
        best_column = 4
    elif state_string == "5424441":
        best_column = 5
    elif state_string == "5424442":
        best_column = 2
    elif state_string == "5424443":
        best_column = 3
    elif state_string == "5424444":
        best_column = 5
    elif state_string == "5424445":
        best_column = 5
    elif state_string == "5424446":
        best_column = 5
    elif state_string == "5424447":
        best_column = 5
    elif state_string == "5424541":
        best_column = 4
    elif state_string == "5424542":
        best_column = 4
    elif state_string == "5424543":
        best_column = 4
    elif state_string == "5424544":
        best_column = 5
    elif state_string == "5424545":
        best_column = 4
    elif state_string == "5424546":
        best_column = 4
    elif state_string == "5424547":
        best_column = 4
    elif state_string == "5424641":
        best_column = 4
    elif state_string == "5424642":
        best_column = 4
    elif state_string == "5424643":
        best_column = 4
    elif state_string == "5424644":
        best_column = 5
    elif state_string == "5424645":
        best_column = 4
    elif state_string == "5424646":
        best_column = 4
    elif state_string == "5424647":
        best_column = 4
    elif state_string == "5424741":
        best_column = 4
    elif state_string == "5424742":
        best_column = 4
    elif state_string == "5424743":
        best_column = 4
    elif state_string == "5424744":
        best_column = 2
    elif state_string == "5424745":
        best_column = 4
    elif state_string == "5424746":
        best_column = 4
    elif state_string == "5424747":
        best_column = 4
    elif state_string == "5434141":
        best_column = 4
    elif state_string == "5434142":
        best_column = 4
    elif state_string == "5434143":
        best_column = 4
    elif state_string == "5434144":
        best_column = 5
    elif state_string == "5434145":
        best_column = 4
    elif state_string == "5434146":
        best_column = 4
    elif state_string == "5434147":
        best_column = 4
    elif state_string == "5434241":
        best_column = 4
    elif state_string == "5434242":
        best_column = 4
    elif state_string == "5434243":
        best_column = 4
    elif state_string == "5434244":
        best_column = 5
    elif state_string == "5434245":
        best_column = 4
    elif state_string == "5434246":
        best_column = 4
    elif state_string == "5434247":
        best_column = 4
    elif state_string == "5434341":
        best_column = 4
    elif state_string == "5434342":
        best_column = 4
    elif state_string == "5434343":
        best_column = 4
    elif state_string == "5434344":
        best_column = 3
    elif state_string == "5434345":
        best_column = 4
    elif state_string == "5434346":
        best_column = 4
    elif state_string == "5434347":
        best_column = 4
    elif state_string == "5434431":
        best_column = 4
    elif state_string == "5434432":
        best_column = 4
    elif state_string == "5434433":
        best_column = 4
    elif state_string == "5434434":
        best_column = 5
    elif state_string == "5434435":
        best_column = 4
    elif state_string == "5434436":
        best_column = 4
    elif state_string == "5434437":
        best_column = 4
    elif state_string == "5434541":
        best_column = 4
    elif state_string == "5434542":
        best_column = 4
    elif state_string == "5434543":
        best_column = 4
    elif state_string == "5434544":
        best_column = 5
    elif state_string == "5434545":
        best_column = 4
    elif state_string == "5434546":
        best_column = 4
    elif state_string == "5434547":
        best_column = 4
    elif state_string == "5434641":
        best_column = 4
    elif state_string == "5434642":
        best_column = 4
    elif state_string == "5434643":
        best_column = 4
    elif state_string == "5434644":
        best_column = 3
    elif state_string == "5434645":
        best_column = 4
    elif state_string == "5434646":
        best_column = 4
    elif state_string == "5434647":
        best_column = 4
    elif state_string == "5434741":
        best_column = 4
    elif state_string == "5434742":
        best_column = 4
    elif state_string == "5434743":
        best_column = 4
    elif state_string == "5434744":
        best_column = 5
    elif state_string == "5434745":
        best_column = 4
    elif state_string == "5434746":
        best_column = 4
    elif state_string == "5434747":
        best_column = 4
    elif state_string == "5444141":
        best_column = 4
    elif state_string == "5444142":
        best_column = 4
    elif state_string == "5444143":
        best_column = 4
    elif state_string == "5444144":
        best_column = 5
    elif state_string == "5444145":
        best_column = 4
    elif state_string == "5444146":
        best_column = 4
    elif state_string == "5444147":
        best_column = 4
    elif state_string == "5444241":
        best_column = 4
    elif state_string == "5444242":
        best_column = 4
    elif state_string == "5444243":
        best_column = 4
    elif state_string == "5444244":
        best_column = 5
    elif state_string == "5444245":
        best_column = 5
    elif state_string == "5444246":
        best_column = 4
    elif state_string == "5444247":
        best_column = 5
    elif state_string == "5444341":
        best_column = 4
    elif state_string == "5444342":
        best_column = 4
    elif state_string == "5444343":
        best_column = 4
    elif state_string == "5444344":
        best_column = 3
    elif state_string == "5444345":
        best_column = 4
    elif state_string == "5444346":
        best_column = 5
    elif state_string == "5444347":
        best_column = 5
    elif state_string == "5444451":
        best_column = 6
    elif state_string == "5444452":
        best_column = 5
    elif state_string == "5444453":
        best_column = 5
    elif state_string == "5444454":
        best_column = 5
    elif state_string == "5444455":
        best_column = 4
    elif state_string == "5444456":
        best_column = 5
    elif state_string == "5444457":
        best_column = 5
    elif state_string == "5444541":
        best_column = 4
    elif state_string == "5444542":
        best_column = 5
    elif state_string == "5444543":
        best_column = 3
    elif state_string == "5444544":
        best_column = 7
    elif state_string == "5444545":
        best_column = 5
    elif state_string == "5444546":
        best_column = 4
    elif state_string == "5444547":
        best_column = 3
    elif state_string == "5444641":
        best_column = 5
    elif state_string == "5444642":
        best_column = 3
    elif state_string == "5444643":
        best_column = 5
    elif state_string == "5444644":
        best_column = 5
    elif state_string == "5444645":
        best_column = 4
    elif state_string == "5444646":
        best_column = 4
    elif state_string == "5444647":
        best_column = 5
    elif state_string == "5444741":
        best_column = 5
    elif state_string == "5444742":
        best_column = 5
    elif state_string == "5444743":
        best_column = 5
    elif state_string == "5444744":
        best_column = 5
    elif state_string == "5444745":
        best_column = 4
    elif state_string == "5444746":
        best_column = 5
    elif state_string == "5444747":
        best_column = 5
    elif state_string == "5455141":
        best_column = 4
    elif state_string == "5455142":
        best_column = 4
    elif state_string == "5455143":
        best_column = 4
    elif state_string == "5455144":
        best_column = 4
    elif state_string == "5455145":
        best_column = 4
    elif state_string == "5455146":
        best_column = 4
    elif state_string == "5455147":
        best_column = 4
    elif state_string == "5455241":
        best_column = 4
    elif state_string == "5455242":
        best_column = 4
    elif state_string == "5455243":
        best_column = 4
    elif state_string == "5455244":
        best_column = 4
    elif state_string == "5455245":
        best_column = 4
    elif state_string == "5455246":
        best_column = 4
    elif state_string == "5455247":
        best_column = 4
    elif state_string == "5455341":
        best_column = 4
    elif state_string == "5455342":
        best_column = 4
    elif state_string == "5455343":
        best_column = 4
    elif state_string == "5455344":
        best_column = 4
    elif state_string == "5455345":
        best_column = 4
    elif state_string == "5455346":
        best_column = 4
    elif state_string == "5455347":
        best_column = 4
    elif state_string == "5455441":
        best_column = 4
    elif state_string == "5455442":
        best_column = 4
    elif state_string == "5455443":
        best_column = 4
    elif state_string == "5455444":
        best_column = 4
    elif state_string == "5455445":
        best_column = 4
    elif state_string == "5455446":
        best_column = 4
    elif state_string == "5455447":
        best_column = 5
    elif state_string == "5455541":
        best_column = 4
    elif state_string == "5455542":
        best_column = 4
    elif state_string == "5455543":
        best_column = 4
    elif state_string == "5455544":
        best_column = 4
    elif state_string == "5455545":
        best_column = 4
    elif state_string == "5455546":
        best_column = 4
    elif state_string == "5455547":
        best_column = 4
    elif state_string == "5455641":
        best_column = 4
    elif state_string == "5455642":
        best_column = 4
    elif state_string == "5455643":
        best_column = 4
    elif state_string == "5455644":
        best_column = 4
    elif state_string == "5455645":
        best_column = 4
    elif state_string == "5455646":
        best_column = 4
    elif state_string == "5455647":
        best_column = 4
    elif state_string == "5455741":
        best_column = 4
    elif state_string == "5455742":
        best_column = 4
    elif state_string == "5455743":
        best_column = 4
    elif state_string == "5455744":
        best_column = 4
    elif state_string == "5455745":
        best_column = 4
    elif state_string == "5455746":
        best_column = 4
    elif state_string == "5455747":
        best_column = 4
    elif state_string == "5464141":
        best_column = 4
    elif state_string == "5464142":
        best_column = 4
    elif state_string == "5464143":
        best_column = 4
    elif state_string == "5464144":
        best_column = 5
    elif state_string == "5464145":
        best_column = 4
    elif state_string == "5464146":
        best_column = 4
    elif state_string == "5464147":
        best_column = 4
    elif state_string == "5464241":
        best_column = 4
    elif state_string == "5464242":
        best_column = 4
    elif state_string == "5464243":
        best_column = 4
    elif state_string == "5464244":
        best_column = 5
    elif state_string == "5464245":
        best_column = 4
    elif state_string == "5464246":
        best_column = 4
    elif state_string == "5464247":
        best_column = 4
    elif state_string == "5464341":
        best_column = 4
    elif state_string == "5464342":
        best_column = 4
    elif state_string == "5464343":
        best_column = 4
    elif state_string == "5464344":
        best_column = 3
    elif state_string == "5464345":
        best_column = 4
    elif state_string == "5464346":
        best_column = 4
    elif state_string == "5464347":
        best_column = 4
    elif state_string == "5464441":
        best_column = 5
    elif state_string == "5464442":
        best_column = 5
    elif state_string == "5464443":
        best_column = 5
    elif state_string == "5464444":
        best_column = 5
    elif state_string == "5464445":
        best_column = 6
    elif state_string == "5464446":
        best_column = 5
    elif state_string == "5464447":
        best_column = 6
    elif state_string == "5464541":
        best_column = 4
    elif state_string == "5464542":
        best_column = 4
    elif state_string == "5464543":
        best_column = 4
    elif state_string == "5464544":
        best_column = 5
    elif state_string == "5464545":
        best_column = 4
    elif state_string == "5464546":
        best_column = 4
    elif state_string == "5464547":
        best_column = 4
    elif state_string == "5464641":
        best_column = 4
    elif state_string == "5464642":
        best_column = 4
    elif state_string == "5464643":
        best_column = 4
    elif state_string == "5464644":
        best_column = 6
    elif state_string == "5464645":
        best_column = 4
    elif state_string == "5464646":
        best_column = 4
    elif state_string == "5464647":
        best_column = 4
    elif state_string == "5464741":
        best_column = 4
    elif state_string == "5464742":
        best_column = 4
    elif state_string == "5464743":
        best_column = 4
    elif state_string == "5464744":
        best_column = 3
    elif state_string == "5464745":
        best_column = 4
    elif state_string == "5464746":
        best_column = 4
    elif state_string == "5464747":
        best_column = 4
    elif state_string == "5474141":
        best_column = 4
    elif state_string == "5474142":
        best_column = 4
    elif state_string == "5474143":
        best_column = 4
    elif state_string == "5474144":
        best_column = 5
    elif state_string == "5474145":
        best_column = 4
    elif state_string == "5474146":
        best_column = 4
    elif state_string == "5474147":
        best_column = 4
    elif state_string == "5474241":
        best_column = 4
    elif state_string == "5474242":
        best_column = 4
    elif state_string == "5474243":
        best_column = 4
    elif state_string == "5474244":
        best_column = 2
    elif state_string == "5474245":
        best_column = 4
    elif state_string == "5474246":
        best_column = 4
    elif state_string == "5474247":
        best_column = 4
    elif state_string == "5474341":
        best_column = 4
    elif state_string == "5474342":
        best_column = 4
    elif state_string == "5474343":
        best_column = 4
    elif state_string == "5474344":
        best_column = 3
    elif state_string == "5474345":
        best_column = 4
    elif state_string == "5474346":
        best_column = 4
    elif state_string == "5474347":
        best_column = 4
    elif state_string == "5474451":
        best_column = 5
    elif state_string == "5474452":
        best_column = 4
    elif state_string == "5474453":
        best_column = 3
    elif state_string == "5474454":
        best_column = 7
    elif state_string == "5474455":
        best_column = 7
    elif state_string == "5474456":
        best_column = 5
    elif state_string == "5474457":
        best_column = 5
    elif state_string == "5474541":
        best_column = 4
    elif state_string == "5474542":
        best_column = 4
    elif state_string == "5474543":
        best_column = 4
    elif state_string == "5474544":
        best_column = 5
    elif state_string == "5474545":
        best_column = 4
    elif state_string == "5474546":
        best_column = 4
    elif state_string == "5474547":
        best_column = 4
    elif state_string == "5474641":
        best_column = 4
    elif state_string == "5474642":
        best_column = 4
    elif state_string == "5474643":
        best_column = 4
    elif state_string == "5474644":
        best_column = 5
    elif state_string == "5474645":
        best_column = 4
    elif state_string == "5474646":
        best_column = 4
    elif state_string == "5474647":
        best_column = 4
    elif state_string == "5474741":
        best_column = 4
    elif state_string == "5474742":
        best_column = 4
    elif state_string == "5474743":
        best_column = 4
    elif state_string == "5474744":
        best_column = 3
    elif state_string == "5474745":
        best_column = 4
    elif state_string == "5474746":
        best_column = 4
    elif state_string == "5474747":
        best_column = 4
    elif state_string == "6515151":
        best_column = 5
    elif state_string == "6515152":
        best_column = 5
    elif state_string == "6515153":
        best_column = 5
    elif state_string == "6515154":
        best_column = 5
    elif state_string == "6515155":
        best_column = 3
    elif state_string == "6515156":
        best_column = 5
    elif state_string == "6515157":
        best_column = 5
    elif state_string == "6515251":
        best_column = 5
    elif state_string == "6515252":
        best_column = 5
    elif state_string == "6515253":
        best_column = 5
    elif state_string == "6515254":
        best_column = 5
    elif state_string == "6515255":
        best_column = 4
    elif state_string == "6515256":
        best_column = 5
    elif state_string == "6515257":
        best_column = 5
    elif state_string == "6515351":
        best_column = 5
    elif state_string == "6515352":
        best_column = 5
    elif state_string == "6515353":
        best_column = 5
    elif state_string == "6515354":
        best_column = 5
    elif state_string == "6515355":
        best_column = 3
    elif state_string == "6515356":
        best_column = 5
    elif state_string == "6515357":
        best_column = 5
    elif state_string == "6515441":
        best_column = 5
    elif state_string == "6515442":
        best_column = 3
    elif state_string == "6515443":
        best_column = 2
    elif state_string == "6515444":
        best_column = 6
    elif state_string == "6515445":
        best_column = 6
    elif state_string == "6515446":
        best_column = 5
    elif state_string == "6515447":
        best_column = 5
    elif state_string == "6515551":
        best_column = 4
    elif state_string == "6515552":
        best_column = 3
    elif state_string == "6515553":
        best_column = 2
    elif state_string == "6515554":
        best_column = 4
    elif state_string == "6515555":
        best_column = 6
    elif state_string == "6515556":
        best_column = 6
    elif state_string == "6515557":
        best_column = 4
    elif state_string == "6515651":
        best_column = 5
    elif state_string == "6515652":
        best_column = 5
    elif state_string == "6515653":
        best_column = 5
    elif state_string == "6515654":
        best_column = 5
    elif state_string == "6515655":
        best_column = 2
    elif state_string == "6515656":
        best_column = 5
    elif state_string == "6515657":
        best_column = 5
    elif state_string == "6515751":
        best_column = 5
    elif state_string == "6515752":
        best_column = 5
    elif state_string == "6515753":
        best_column = 5
    elif state_string == "6515754":
        best_column = 5
    elif state_string == "6515755":
        best_column = 3
    elif state_string == "6515756":
        best_column = 5
    elif state_string == "6515757":
        best_column = 5
    elif state_string == "6525151":
        best_column = 5
    elif state_string == "6525152":
        best_column = 5
    elif state_string == "6525153":
        best_column = 5
    elif state_string == "6525154":
        best_column = 5
    elif state_string == "6525155":
        best_column = 4
    elif state_string == "6525156":
        best_column = 5
    elif state_string == "6525157":
        best_column = 5
    elif state_string == "6525261":
        best_column = 3
    elif state_string == "6525262":
        best_column = 2
    elif state_string == "6525263":
        best_column = 4
    elif state_string == "6525264":
        best_column = 5
    elif state_string == "6525265":
        best_column = 5
    elif state_string == "6525266":
        best_column = 5
    elif state_string == "6525267":
        best_column = 5
    elif state_string == "6525351":
        best_column = 5
    elif state_string == "6525352":
        best_column = 5
    elif state_string == "6525353":
        best_column = 5
    elif state_string == "6525354":
        best_column = 5
    elif state_string == "6525355":
        best_column = 3
    elif state_string == "6525356":
        best_column = 5
    elif state_string == "6525357":
        best_column = 5
    elif state_string == "6525441":
        best_column = 3
    elif state_string == "6525442":
        best_column = 5
    elif state_string == "6525443":
        best_column = 1
    elif state_string == "6525444":
        best_column = 6
    elif state_string == "6525445":
        best_column = 6
    elif state_string == "6525446":
        best_column = 4
    elif state_string == "6525447":
        best_column = 5
    elif state_string == "6525551":
        best_column = 3
    elif state_string == "6525552":
        best_column = 2
    elif state_string == "6525553":
        best_column = 1
    elif state_string == "6525554":
        best_column = 4
    elif state_string == "6525555":
        best_column = 6
    elif state_string == "6525556":
        best_column = 6
    elif state_string == "6525557":
        best_column = 3
    elif state_string == "6525651":
        best_column = 5
    elif state_string == "6525652":
        best_column = 5
    elif state_string == "6525653":
        best_column = 5
    elif state_string == "6525654":
        best_column = 5
    elif state_string == "6525655":
        best_column = 6
    elif state_string == "6525656":
        best_column = 5
    elif state_string == "6525657":
        best_column = 5
    elif state_string == "6525751":
        best_column = 5
    elif state_string == "6525752":
        best_column = 5
    elif state_string == "6525753":
        best_column = 5
    elif state_string == "6525754":
        best_column = 5
    elif state_string == "6525755":
        best_column = 6
    elif state_string == "6525756":
        best_column = 5
    elif state_string == "6525757":
        best_column = 5
    elif state_string == "6535151":
        best_column = 5
    elif state_string == "6535152":
        best_column = 5
    elif state_string == "6535153":
        best_column = 5
    elif state_string == "6535154":
        best_column = 5
    elif state_string == "6535155":
        best_column = 3
    elif state_string == "6535156":
        best_column = 5
    elif state_string == "6535157":
        best_column = 5
    elif state_string == "6535251":
        best_column = 5
    elif state_string == "6535252":
        best_column = 5
    elif state_string == "6535253":
        best_column = 5
    elif state_string == "6535254":
        best_column = 5
    elif state_string == "6535255":
        best_column = 3
    elif state_string == "6535256":
        best_column = 5
    elif state_string == "6535257":
        best_column = 5
    elif state_string == "6535331":
        best_column = 5
    elif state_string == "6535332":
        best_column = 1
    elif state_string == "6535333":
        best_column = 5
    elif state_string == "6535334":
        best_column = 4
    elif state_string == "6535335":
        best_column = 5
    elif state_string == "6535336":
        best_column = 6
    elif state_string == "6535337":
        best_column = 5
    elif state_string == "6535441":
        best_column = 2
    elif state_string == "6535442":
        best_column = 1
    elif state_string == "6535443":
        best_column = 3
    elif state_string == "6535444":
        best_column = 6
    elif state_string == "6535445":
        best_column = 6
    elif state_string == "6535446":
        best_column = 5
    elif state_string == "6535447":
        best_column = 6
    elif state_string == "6535531":
        best_column = 2
    elif state_string == "6535532":
        best_column = 1
    elif state_string == "6535533":
        best_column = 2
    elif state_string == "6535534":
        best_column = 4
    elif state_string == "6535535":
        best_column = 6
    elif state_string == "6535536":
        best_column = 6
    elif state_string == "6535537":
        best_column = 6
    elif state_string == "6535651":
        best_column = 5
    elif state_string == "6535652":
        best_column = 5
    elif state_string == "6535653":
        best_column = 5
    elif state_string == "6535654":
        best_column = 5
    elif state_string == "6535655":
        best_column = 3
    elif state_string == "6535656":
        best_column = 5
    elif state_string == "6535657":
        best_column = 5
    elif state_string == "6535751":
        best_column = 5
    elif state_string == "6535752":
        best_column = 5
    elif state_string == "6535753":
        best_column = 5
    elif state_string == "6535754":
        best_column = 5
    elif state_string == "6535755":
        best_column = 3
    elif state_string == "6535756":
        best_column = 5
    elif state_string == "6535757":
        best_column = 5
    elif state_string == "6544141":
        best_column = 4
    elif state_string == "6544142":
        best_column = 3
    elif state_string == "6544143":
        best_column = 2
    elif state_string == "6544144":
        best_column = 2
    elif state_string == "6544145":
        best_column = 4
    elif state_string == "6544146":
        best_column = 4
    elif state_string == "6544147":
        best_column = 4
    elif state_string == "6544241":
        best_column = 3
    elif state_string == "6544242":
        best_column = 4
    elif state_string == "6544243":
        best_column = 1
    elif state_string == "6544244":
        best_column = 3
    elif state_string == "6544245":
        best_column = 4
    elif state_string == "6544246":
        best_column = 4
    elif state_string == "6544247":
        best_column = 4
    elif state_string == "6544341":
        best_column = 2
    elif state_string == "6544342":
        best_column = 1
    elif state_string == "6544343":
        best_column = 4
    elif state_string == "6544344":
        best_column = 5
    elif state_string == "6544345":
        best_column = 5
    elif state_string == "6544346":
        best_column = 5
    elif state_string == "6544347":
        best_column = 4
    elif state_string == "6544451":
        best_column = 6
    elif state_string == "6544452":
        best_column = 6
    elif state_string == "6544453":
        best_column = 6
    elif state_string == "6544454":
        best_column = 5
    elif state_string == "6544455":
        best_column = 6
    elif state_string == "6544456":
        best_column = 5
    elif state_string == "6544457":
        best_column = 4
    elif state_string == "6544541":
        best_column = 4
    elif state_string == "6544542":
        best_column = 4
    elif state_string == "6544543":
        best_column = 4
    elif state_string == "6544544":
        best_column = 5
    elif state_string == "6544545":
        best_column = 4
    elif state_string == "6544546":
        best_column = 4
    elif state_string == "6544547":
        best_column = 4
    elif state_string == "6544641":
        best_column = 4
    elif state_string == "6544642":
        best_column = 4
    elif state_string == "6544643":
        best_column = 4
    elif state_string == "6544644":
        best_column = 7
    elif state_string == "6544645":
        best_column = 4
    elif state_string == "6544646":
        best_column = 6
    elif state_string == "6544647":
        best_column = 4
    elif state_string == "6544741":
        best_column = 4
    elif state_string == "6544742":
        best_column = 4
    elif state_string == "6544743":
        best_column = 4
    elif state_string == "6544744":
        best_column = 6
    elif state_string == "6544745":
        best_column = 4
    elif state_string == "6544746":
        best_column = 4
    elif state_string == "6544747":
        best_column = 4
    elif state_string == "6555151":
        best_column = 4
    elif state_string == "6555152":
        best_column = 4
    elif state_string == "6555153":
        best_column = 3
    elif state_string == "6555154":
        best_column = 2
    elif state_string == "6555155":
        best_column = 4
    elif state_string == "6555156":
        best_column = 4
    elif state_string == "6555157":
        best_column = 4
    elif state_string == "6555241":
        best_column = 2
    elif state_string == "6555242":
        best_column = 5
    elif state_string == "6555243":
        best_column = 3
    elif state_string == "6555244":
        best_column = 5
    elif state_string == "6555245":
        best_column = 4
    elif state_string == "6555246":
        best_column = 4
    elif state_string == "6555247":
        best_column = 4
    elif state_string == "6555351":
        best_column = 3
    elif state_string == "6555352":
        best_column = 4
    elif state_string == "6555353":
        best_column = 4
    elif state_string == "6555354":
        best_column = 4
    elif state_string == "6555355":
        best_column = 3
    elif state_string == "6555356":
        best_column = 3
    elif state_string == "6555357":
        best_column = 3
    elif state_string == "6555441":
        best_column = 4
    elif state_string == "6555442":
        best_column = 4
    elif state_string == "6555443":
        best_column = 4
    elif state_string == "6555444":
        best_column = 4
    elif state_string == "6555445":
        best_column = 4
    elif state_string == "6555446":
        best_column = 4
    elif state_string == "6555447":
        best_column = 4
    elif state_string == "6555561":
        best_column = 4
    elif state_string == "6555562":
        best_column = 4
    elif state_string == "6555563":
        best_column = 3
    elif state_string == "6555564":
        best_column = 4
    elif state_string == "6555565":
        best_column = 4
    elif state_string == "6555566":
        best_column = 4
    elif state_string == "6555567":
        best_column = 6
    elif state_string == "6555651":
        best_column = 4
    elif state_string == "6555652":
        best_column = 2
    elif state_string == "6555653":
        best_column = 3
    elif state_string == "6555654":
        best_column = 4
    elif state_string == "6555655":
        best_column = 4
    elif state_string == "6555656":
        best_column = 6
    elif state_string == "6555657":
        best_column = 4
    elif state_string == "6555751":
        best_column = 4
    elif state_string == "6555752":
        best_column = 2
    elif state_string == "6555753":
        best_column = 3
    elif state_string == "6555754":
        best_column = 4
    elif state_string == "6555755":
        best_column = 4
    elif state_string == "6555756":
        best_column = 4
    elif state_string == "6555757":
        best_column = 4
    elif state_string == "6566141":
        best_column = 4
    elif state_string == "6566142":
        best_column = 2
    elif state_string == "6566143":
        best_column = 4
    elif state_string == "6566144":
        best_column = 6
    elif state_string == "6566145":
        best_column = 5
    elif state_string == "6566146":
        best_column = 5
    elif state_string == "6566147":
        best_column = 4
    elif state_string == "6566251":
        best_column = 5
    elif state_string == "6566252":
        best_column = 5
    elif state_string == "6566253":
        best_column = 5
    elif state_string == "6566254":
        best_column = 5
    elif state_string == "6566255":
        best_column = 5
    elif state_string == "6566256":
        best_column = 5
    elif state_string == "6566257":
        best_column = 5
    elif state_string == "6566351":
        best_column = 5
    elif state_string == "6566352":
        best_column = 5
    elif state_string == "6566353":
        best_column = 3
    elif state_string == "6566354":
        best_column = 4
    elif state_string == "6566355":
        best_column = 5
    elif state_string == "6566356":
        best_column = 5
    elif state_string == "6566357":
        best_column = 5
    elif state_string == "6566441":
        best_column = 4
    elif state_string == "6566442":
        best_column = 4
    elif state_string == "6566443":
        best_column = 4
    elif state_string == "6566444":
        best_column = 4
    elif state_string == "6566445":
        best_column = 4
    elif state_string == "6566446":
        best_column = 4
    elif state_string == "6566447":
        best_column = 6
    elif state_string == "6566551":
        best_column = 4
    elif state_string == "6566552":
        best_column = 4
    elif state_string == "6566553":
        best_column = 5
    elif state_string == "6566554":
        best_column = 4
    elif state_string == "6566555":
        best_column = 5
    elif state_string == "6566556":
        best_column = 4
    elif state_string == "6566557":
        best_column = 7
    elif state_string == "6566651":
        best_column = 4
    elif state_string == "6566652":
        best_column = 5
    elif state_string == "6566653":
        best_column = 5
    elif state_string == "6566654":
        best_column = 4
    elif state_string == "6566655":
        best_column = 5
    elif state_string == "6566656":
        best_column = 4
    elif state_string == "6566657":
        best_column = 4
    elif state_string == "6566751":
        best_column = 5
    elif state_string == "6566752":
        best_column = 5
    elif state_string == "6566753":
        best_column = 5
    elif state_string == "6566754":
        best_column = 5
    elif state_string == "6566755":
        best_column = 5
    elif state_string == "6566756":
        best_column = 5
    elif state_string == "6566757":
        best_column = 5
    elif state_string == "6575151":
        best_column = 5
    elif state_string == "6575152":
        best_column = 5
    elif state_string == "6575153":
        best_column = 5
    elif state_string == "6575154":
        best_column = 5
    elif state_string == "6575155":
        best_column = 3
    elif state_string == "6575156":
        best_column = 5
    elif state_string == "6575157":
        best_column = 5
    elif state_string == "6575251":
        best_column = 5
    elif state_string == "6575252":
        best_column = 5
    elif state_string == "6575253":
        best_column = 5
    elif state_string == "6575254":
        best_column = 5
    elif state_string == "6575255":
        best_column = 6
    elif state_string == "6575256":
        best_column = 5
    elif state_string == "6575257":
        best_column = 5
    elif state_string == "6575351":
        best_column = 5
    elif state_string == "6575352":
        best_column = 5
    elif state_string == "6575353":
        best_column = 5
    elif state_string == "6575354":
        best_column = 5
    elif state_string == "6575355":
        best_column = 3
    elif state_string == "6575356":
        best_column = 5
    elif state_string == "6575357":
        best_column = 5
    elif state_string == "6575451":
        best_column = 5
    elif state_string == "6575452":
        best_column = 5
    elif state_string == "6575453":
        best_column = 5
    elif state_string == "6575454":
        best_column = 5
    elif state_string == "6575455":
        best_column = 4
    elif state_string == "6575456":
        best_column = 5
    elif state_string == "6575457":
        best_column = 5
    elif state_string == "6575551":
        best_column = 4
    elif state_string == "6575552":
        best_column = 3
    elif state_string == "6575553":
        best_column = 3
    elif state_string == "6575554":
        best_column = 4
    elif state_string == "6575555":
        best_column = 6
    elif state_string == "6575556":
        best_column = 6
    elif state_string == "6575557":
        best_column = 4
    elif state_string == "6575651":
        best_column = 5
    elif state_string == "6575652":
        best_column = 5
    elif state_string == "6575653":
        best_column = 5
    elif state_string == "6575654":
        best_column = 5
    elif state_string == "6575655":
        best_column = 2
    elif state_string == "6575656":
        best_column = 5
    elif state_string == "6575657":
        best_column = 5
    elif state_string == "6575751":
        best_column = 5
    elif state_string == "6575752":
        best_column = 5
    elif state_string == "6575753":
        best_column = 5
    elif state_string == "6575754":
        best_column = 5
    elif state_string == "6575755":
        best_column = 3
    elif state_string == "6575756":
        best_column = 5
    elif state_string == "6575757":
        best_column = 5
    elif state_string == "7415131":
        best_column = 1
    elif state_string == "7415132":
        best_column = 4
    elif state_string == "7415133":
        best_column = 4
    elif state_string == "7415134":
        best_column = 3
    elif state_string == "7415135":
        best_column = 3
    elif state_string == "7415136":
        best_column = 4
    elif state_string == "7415137":
        best_column = 3
    elif state_string == "7415241":
        best_column = 4
    elif state_string == "7415242":
        best_column = 4
    elif state_string == "7415243":
        best_column = 4
    elif state_string == "7415244":
        best_column = 5
    elif state_string == "7415245":
        best_column = 4
    elif state_string == "7415246":
        best_column = 4
    elif state_string == "7415247":
        best_column = 4
    elif state_string == "7415351":
        best_column = 4
    elif state_string == "7415352":
        best_column = 4
    elif state_string == "7415353":
        best_column = 3
    elif state_string == "7415354":
        best_column = 5
    elif state_string == "7415355":
        best_column = 4
    elif state_string == "7415356":
        best_column = 4
    elif state_string == "7415357":
        best_column = 4
    elif state_string == "7415431":
        best_column = 3
    elif state_string == "7415432":
        best_column = 4
    elif state_string == "7415433":
        best_column = 4
    elif state_string == "7415434":
        best_column = 3
    elif state_string == "7415435":
        best_column = 3
    elif state_string == "7415436":
        best_column = 4
    elif state_string == "7415437":
        best_column = 3
    elif state_string == "7415531":
        best_column = 6
    elif state_string == "7415532":
        best_column = 6
    elif state_string == "7415533":
        best_column = 6
    elif state_string == "7415534":
        best_column = 6
    elif state_string == "7415535":
        best_column = 6
    elif state_string == "7415536":
        best_column = 2
    elif state_string == "7415537":
        best_column = 6
    elif state_string == "7415641":
        best_column = 4
    elif state_string == "7415642":
        best_column = 4
    elif state_string == "7415643":
        best_column = 4
    elif state_string == "7415644":
        best_column = 5
    elif state_string == "7415645":
        best_column = 4
    elif state_string == "7415646":
        best_column = 4
    elif state_string == "7415647":
        best_column = 4
    elif state_string == "7415731":
        best_column = 2
    elif state_string == "7415732":
        best_column = 6
    elif state_string == "7415733":
        best_column = 6
    elif state_string == "7415734":
        best_column = 6
    elif state_string == "7415735":
        best_column = 6
    elif state_string == "7415736":
        best_column = 2
    elif state_string == "7415737":
        best_column = 6
    elif state_string == "7424141":
        best_column = 4
    elif state_string == "7424142":
        best_column = 4
    elif state_string == "7424143":
        best_column = 4
    elif state_string == "7424144":
        best_column = 5
    elif state_string == "7424145":
        best_column = 4
    elif state_string == "7424146":
        best_column = 4
    elif state_string == "7424147":
        best_column = 4
    elif state_string == "7424241":
        best_column = 4
    elif state_string == "7424242":
        best_column = 4
    elif state_string == "7424243":
        best_column = 4
    elif state_string == "7424244":
        best_column = 5
    elif state_string == "7424245":
        best_column = 4
    elif state_string == "7424246":
        best_column = 4
    elif state_string == "7424247":
        best_column = 4
    elif state_string == "7424341":
        best_column = 4
    elif state_string == "7424342":
        best_column = 4
    elif state_string == "7424343":
        best_column = 4
    elif state_string == "7424344":
        best_column = 3
    elif state_string == "7424345":
        best_column = 4
    elif state_string == "7424346":
        best_column = 4
    elif state_string == "7424347":
        best_column = 4
    elif state_string == "7424441":
        best_column = 4
    elif state_string == "7424442":
        best_column = 2
    elif state_string == "7424443":
        best_column = 3
    elif state_string == "7424444":
        best_column = 2
    elif state_string == "7424445":
        best_column = 5
    elif state_string == "7424446":
        best_column = 6
    elif state_string == "7424447":
        best_column = 2
    elif state_string == "7424541":
        best_column = 4
    elif state_string == "7424542":
        best_column = 4
    elif state_string == "7424543":
        best_column = 4
    elif state_string == "7424544":
        best_column = 2
    elif state_string == "7424545":
        best_column = 4
    elif state_string == "7424546":
        best_column = 4
    elif state_string == "7424547":
        best_column = 4
    elif state_string == "7424641":
        best_column = 4
    elif state_string == "7424642":
        best_column = 4
    elif state_string == "7424643":
        best_column = 4
    elif state_string == "7424644":
        best_column = 5
    elif state_string == "7424645":
        best_column = 4
    elif state_string == "7424646":
        best_column = 4
    elif state_string == "7424647":
        best_column = 4
    elif state_string == "7424731":
        best_column = 4
    elif state_string == "7424732":
        best_column = 5
    elif state_string == "7424733":
        best_column = 4
    elif state_string == "7424734":
        best_column = 3
    elif state_string == "7424735":
        best_column = 3
    elif state_string == "7424736":
        best_column = 3
    elif state_string == "7424737":
        best_column = 7
    elif state_string == "7434141":
        best_column = 4
    elif state_string == "7434142":
        best_column = 4
    elif state_string == "7434143":
        best_column = 4
    elif state_string == "7434144":
        best_column = 3
    elif state_string == "7434145":
        best_column = 4
    elif state_string == "7434146":
        best_column = 4
    elif state_string == "7434147":
        best_column = 4
    elif state_string == "7434241":
        best_column = 4
    elif state_string == "7434242":
        best_column = 4
    elif state_string == "7434243":
        best_column = 4
    elif state_string == "7434244":
        best_column = 3
    elif state_string == "7434245":
        best_column = 4
    elif state_string == "7434246":
        best_column = 4
    elif state_string == "7434247":
        best_column = 4
    elif state_string == "7434341":
        best_column = 4
    elif state_string == "7434342":
        best_column = 4
    elif state_string == "7434343":
        best_column = 4
    elif state_string == "7434344":
        best_column = 3
    elif state_string == "7434345":
        best_column = 4
    elif state_string == "7434346":
        best_column = 4
    elif state_string == "7434347":
        best_column = 4
    elif state_string == "7434431":
        best_column = 3
    elif state_string == "7434432":
        best_column = 3
    elif state_string == "7434433":
        best_column = 3
    elif state_string == "7434434":
        best_column = 3
    elif state_string == "7434435":
        best_column = 5
    elif state_string == "7434436":
        best_column = 6
    elif state_string == "7434437":
        best_column = 7
    elif state_string == "7434541":
        best_column = 4
    elif state_string == "7434542":
        best_column = 4
    elif state_string == "7434543":
        best_column = 4
    elif state_string == "7434544":
        best_column = 3
    elif state_string == "7434545":
        best_column = 4
    elif state_string == "7434546":
        best_column = 4
    elif state_string == "7434547":
        best_column = 4
    elif state_string == "7434641":
        best_column = 4
    elif state_string == "7434642":
        best_column = 4
    elif state_string == "7434643":
        best_column = 4
    elif state_string == "7434644":
        best_column = 3
    elif state_string == "7434645":
        best_column = 4
    elif state_string == "7434646":
        best_column = 4
    elif state_string == "7434647":
        best_column = 4
    elif state_string == "7434741":
        best_column = 4
    elif state_string == "7434742":
        best_column = 4
    elif state_string == "7434743":
        best_column = 4
    elif state_string == "7434744":
        best_column = 3
    elif state_string == "7434745":
        best_column = 4
    elif state_string == "7434746":
        best_column = 4
    elif state_string == "7434747":
        best_column = 4
    elif state_string == "7444141":
        best_column = 3
    elif state_string == "7444142":
        best_column = 3
    elif state_string == "7444143":
        best_column = 3
    elif state_string == "7444144":
        best_column = 3
    elif state_string == "7444145":
        best_column = 5
    elif state_string == "7444146":
        best_column = 3
    elif state_string == "7444147":
        best_column = 5
    elif state_string == "7444241":
        best_column = 4
    elif state_string == "7444242":
        best_column = 4
    elif state_string == "7444243":
        best_column = 4
    elif state_string == "7444244":
        best_column = 4
    elif state_string == "7444245":
        best_column = 4
    elif state_string == "7444246":
        best_column = 4
    elif state_string == "7444247":
        best_column = 4
    elif state_string == "7444341":
        best_column = 4
    elif state_string == "7444342":
        best_column = 4
    elif state_string == "7444343":
        best_column = 4
    elif state_string == "7444344":
        best_column = 3
    elif state_string == "7444345":
        best_column = 5
    elif state_string == "7444346":
        best_column = 5
    elif state_string == "7444347":
        best_column = 5
    elif state_string == "7444421":
        best_column = 3
    elif state_string == "7444422":
        best_column = 3
    elif state_string == "7444423":
        best_column = 3
    elif state_string == "7444424":
        best_column = 3
    elif state_string == "7444425":
        best_column = 3
    elif state_string == "7444426":
        best_column = 3
    elif state_string == "7444427":
        best_column = 3
    elif state_string == "7444551":
        best_column = 4
    elif state_string == "7444552":
        best_column = 5
    elif state_string == "7444553":
        best_column = 5
    elif state_string == "7444554":
        best_column = 5
    elif state_string == "7444555":
        best_column = 4
    elif state_string == "7444556":
        best_column = 4
    elif state_string == "7444557":
        best_column = 4
    elif state_string == "7444641":
        best_column = 4
    elif state_string == "7444642":
        best_column = 4
    elif state_string == "7444643":
        best_column = 4
    elif state_string == "7444644":
        best_column = 3
    elif state_string == "7444645":
        best_column = 4
    elif state_string == "7444646":
        best_column = 4
    elif state_string == "7444647":
        best_column = 4
    elif state_string == "7444741":
        best_column = 5
    elif state_string == "7444742":
        best_column = 5
    elif state_string == "7444743":
        best_column = 5
    elif state_string == "7444744":
        best_column = 3
    elif state_string == "7444745":
        best_column = 5
    elif state_string == "7444746":
        best_column = 5
    elif state_string == "7444747":
        best_column = 7

    else:
        background_exist = False
    best_point_address[1] = best_column
    for x in available_betting_point_address:
        if best_column == x[1]:
            best_point_address[0] = x[0]
    return background_exist, best_point_address