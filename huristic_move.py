def heuristic_move(board, posA, posB, turn):
    """ دي دالة بتختار أحسن حركة بشكل heuristic: تبعد عن الخصم، تزود حركتك، وتقلل حركة الخصم """
    current_pos = posA if turn == "A" else posB  # بشوف مين دوره دلوقتي وأجيب مكانه
    other_pos = posB if turn == "A" else posA  # وبجيب مكان الخصم
    moves = get_moves(current_pos, board, other_pos)  # بجيب كل الحركات اللي ممكن تتعمل من المكان الحالي
    if not moves:  # لو مفيش أي حركة متاحة
        return None  # يبقى خلاص مفيش حركة

    best_move = None  # هنا هخزن أحسن حركة لقيتها
    best_score = -9999  # ببدأ بسكور قليل جدًا عشان أي حاجة تبقى أحسن منه

    for move in moves:  # بلف على كل حركة ممكنة
        mr, mc = move  # بفك الحركة لصف وعمود

        # بعمل محاكاة للحركة
        temp_board = [row[:] for row in board]  # نسخة جديدة من البورد عشان ما أعدلش في الأصلية
        temp_board[current_pos[0]][current_pos[1]] = BLOCK  # المكان اللي كنت فيه بيتقفل
        temp_posA = move if turn == "A" else posA  # لو اللاعب A هو اللي لعب، مكانه يتغير
        temp_posB = move if turn == "B" else posB  # لو اللاعب B هو اللي لعب، مكانه يتغير
        temp_other_pos = temp_posB if turn == "A" else temp_posA  # مكان الخصم بعد الحركة
        temp_current_pos = temp_posA if turn == "A" else temp_posB  # مكان اللاعب الحالي بعد الحركة

        # 1) أبعد عن الخصم
        dist = abs(mr - temp_other_pos[0]) + abs(mc - temp_other_pos[1])  # المسافة المانهاتن بين الاتنين

        # 2) زود حركتك (عدد الحركات اللي تقدر تعملها بعد الحركة دي)
        own_mobility = len(get_moves(temp_current_pos, temp_board, temp_other_pos))

        # 3) قلل حركة الخصم (عدد الحركات اللي الخصم يقدر يعملها بعد الحركة دي)
        opp_mobility = len(get_moves(temp_other_pos, temp_board, temp_current_pos))

        # السكور النهائي: كل ما تبعد أكتر + تزود حركتك + تقلل حركة الخصم
        score = (dist * 1.0) + (own_mobility * 1.5) - (opp_mobility * 2.0)

        if score > best_score:  # لو السكور ده أحسن من اللي قبله
            best_score = score  # أحدث السكور
            best_move = move  # وأخزن الحركة دي كأحسن حركة

    return best_move  # في الآخر أرجع الحركة اللي طلعت أحسن واحدة
