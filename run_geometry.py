print("""
████──███──████──█───██─███──███──████──██─██
█─────█────█──█──██─███─█─────█───█──█───███
█─██──███──█──█──█─█─██─███───█───████────█
█──█──█────█──█──█───██─█─────█───█─█─────█
████──███──████──█───██─███───█───█─█─────█
──────────────────────────────────────────█
""")
print("https://github.com/Sandrototo/simple_geometry")
menu = input("""
1 - English;
2 - Russian;
Enter value: """)
if menu == "2":
    import geometry_ru
elif menu == "1":
    import geometry_en