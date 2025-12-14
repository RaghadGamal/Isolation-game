def game(mode):
    # نعمل البورد الفاضية
    board = create_board()  
    # مكان البداية بتاع Player A
    posA = (0, 0)  
    # مكان البداية بتاع Player B
    posB = (SIZE-1, SIZE-1)
    # نبدأ بـ Player A
    turn = "A"
    # لوب اللعبة الرئيسية
    while True:
        # نطبع شكل البورد الحالي
        print_board(board, posA, posB)
        # نحدد الدور الحالي مين
        if turn == "A":
            current_pos = posA        # مكان اللاعب الحالي
            other_pos = posB          # مكان اللاعب التاني
            player_name = "Player A"  # اسم اللاعب
        else:
            current_pos = posB
            other_pos = posA
            player_name = "Player B"

        # ------- نختار طريقة اللعب ------
        if mode == 1:  # Player vs Player
            # الاتنين بني آدمين
            new_pos = human_move(player_name, current_pos, board, other_pos)
        elif mode == 2:  # Player vs AI
            if turn == "A":
                # Player A بني آدم
                new_pos = human_move("Player A", posA, board, posB)
            else:
                # دور الـ AI
                print("AI thinking...")
                time.sleep(0.5)  # وقفة صغيرة عشان الشكل
                new_pos = ai_move(posB, board, posA, "B")

        elif mode == 3:  # AI vs AI
            # الاتنين AI
            print(f"{player_name} (AI) thinking...")
            time.sleep(0.4)
            new_pos = ai_move(current_pos, board, other_pos, turn)
        # --------------------------------
        # لو مفيش أي حركة متاحة
        if new_pos is None:
            print(f"{player_name} has NO moves!")
            
            # اللاعب التاني هو اللي كسب
            winner = "B" if turn == "A" else "A"
            print(f"🏆 Player {winner} WINS!")
            break

        # نقفل المكان القديم (نحطه بلوك)
        r, c = current_pos
        board[r][c] = BLOCK

        # نحرك اللاعب ونغير الدور
        if turn == "A":
            posA = new_pos   # نحدث مكان Player A
            turn = "B"       # ندي الدور لـ Player B
        else:
            posB = new_pos   # نحدث مكان Player B
            turn = "A"       # نرجع الدور لـ Player A
