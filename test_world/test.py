def test_func(a, b):
    BXE.ui.text_box("test {0} {1}".format(a, b))
    temp = BXE.audio.play_sfx("beep-221.wav")
    BXE.database.put("test", "teststring")
    print(BXE.database.get("test"))
    BXE.database.remove("test")
    BXE.database.put("test2", "teststring")
